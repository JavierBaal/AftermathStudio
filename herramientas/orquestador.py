"""Orquestador auxiliar de Aftermath Studio para el modo ligero (esquema v0.1 y v0.2).

Prepara las fichas de agentes, árbitro y evaluador a partir de la biblia de una ejecución,
valida las salidas y actualiza la memoria de los agentes. No llama a ningún modelo:
los subagentes los lanza Claude, que lee cada ficha y escribe la salida en la biblia.

Uso:
    python3 herramientas/orquestador.py <biblia> <comando> <tramo>

Comandos, en orden por tramo:
    prompts    fichas de los agentes activos en _prompts/<tramo>/<agente>.md
    check      valida intervenciones/<tramo>/*.yaml y asigna ids agente/tramo/n
    arbitro    ficha del árbitro en _prompts/<tramo>/arbitro.md
    post       valida estado/<tramo>.yaml y actualiza memoria/<agente>.md
    evaluador  ficha del evaluador en _prompts/<tramo>/evaluador.md (solo v0.2)
    postev     valida metricas/<tramo>.yaml (solo v0.2)

La biblia debe contener una copia de escenario.yaml.
"""
import sys, os, yaml, datetime

B, CMD, T = sys.argv[1], sys.argv[2], sys.argv[3]
E = yaml.safe_load(open(f"{B}/escenario.yaml", encoding="utf-8"))
V2 = str(E.get("version_esquema")) >= "0.2"
AG = {a["id"]: a for a in E["agentes"]}
ALL_T = [x["id"] for x in E["cronologia"]["tramos"]]
TR = [t for t in E["cronologia"]["tramos"] if t["id"] in E["ejecucion"].get("tramos", ALL_T)]
ACT = E["ejecucion"].get("agentes", list(AG))
idx = [t["id"] for t in TR].index(T)
cur = TR[idx]; prev = TR[idx - 1] if idx else None
INT = E["interaccion"]
MAX = INT["max_afirmaciones_por_tramo"]
DATO = INT["exigencias"]["dato"]
EVIDENCIAS = ("dato", "inferencia", "especulacion")
METS = E["resultados"]["metricas"]


def log(msg):
    with open(f"{B}/registro.md", "a", encoding="utf-8") as f:
        f.write(f"- {datetime.datetime.now():%Y-%m-%d %H:%M} · {msg}\n")


def dump(obj, path):
    yaml.safe_dump(obj, open(path, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False, width=1000)


def mundo():
    ev = E["evento"]
    s = f"Suceso: {ev['premisa']}\nMomento cero: {ev['momento_cero']}. Alcance: {ev['alcance']}.\n"
    s += "Supuestos (son hechos del mundo; no los discutas ni los expliques):\n"
    s += "".join(f"- {x['texto']}" + (f" (fuente: {x['referencia']})" if x.get("referencia") else "") + "\n" for x in ev["supuestos"])
    s += "Fuera de alcance: " + "; ".join(ev["fuera_de_alcance"]) + "\n"
    return s


def estado(tid):
    return yaml.safe_load(open(f"{B}/estado/{tid}.yaml", encoding="utf-8"))["estado_del_mundo"]


def estado_txt(tid, completo=False):
    st = estado(tid)
    if completo:
        st = {k: v for k, v in st.items() if k != "metricas"}
        return yaml.safe_dump({"estado_del_mundo": st}, allow_unicode=True, sort_keys=False, width=1000)
    s = f"Resumen: {st['resumen']}\nHechos establecidos:\n"
    s += "".join(f"- [{h['id']}] {h['texto']}\n" for h in st.get("hechos_establecidos") or [])
    s += "Tensiones abiertas:\n" + "".join(f"- {x}\n" for x in st.get("tensiones_abiertas") or [])
    return s


def interv(tid):
    out = []
    for a in ACT:
        p = f"{B}/intervenciones/{tid}/{a}.yaml"
        if os.path.exists(p):
            out.append(yaml.safe_load(open(p, encoding="utf-8"))["intervencion"])
    return out


def interv_txt(tid):
    s = ""
    for iv in interv(tid):
        for af in iv["afirmaciones"]:
            s += f"- [{af['id']}] {af['texto']} — Mecanismo: {af['mecanismo']}\n"
    return s or "Nada todavía.\n"


def memoria(a):
    p = f"{B}/memoria/{a}.md"
    return open(p, encoding="utf-8").read() if os.path.exists(p) else "Nada todavía.\n"


def lista(xs):
    return "; ".join(xs or [])


if CMD == "prompts":
    os.makedirs(f"{B}/_prompts/{T}", exist_ok=True)
    os.makedirs(f"{B}/intervenciones/{T}", exist_ok=True)
    for a in ACT:
        g = AG[a]
        p = "Eres un agente de una simulación de escenarios de Aftermath Studio. Interpretas un único papel y nadie más.\n\n"
        p += f"## Tu papel\nNombre: {g.get('nombre', a)}\nRol: {g['rol']}\nPerfil: {g['perfil']}\nObjetivos: {lista(g['objetivos'])}\n"
        if g.get("incentivos"):
            p += f"Lo que ganas o pierdes según evolucione el mundo: {lista(g['incentivos'])}\n"
        if g.get("restricciones"):
            p += f"Lo que no puedes hacer o decir: {lista(g['restricciones'])}\n"
        p += "Lo que solo tú sabes: " + (lista(g.get("conocimiento_privado")) or "nada especial") + "\n\n"
        p += "## El mundo\n" + mundo() + "\n## Dónde estamos\n"
        p += f"Tramo actual: {cur['etiqueta']} ({cur['desde_evento']} desde el suceso). Tramo anterior: {prev['etiqueta'] if prev else 'ninguno'}.\n"
        p += "Estado del mundo al cierre del tramo anterior:\n" + (estado_txt(prev["id"]) if prev else "El suceso acaba de ocurrir.\n")
        if INT["visibilidad"] == "estado_e_intervenciones":
            p += "Lo que dijeron los demás en el tramo anterior:\n" + (interv_txt(prev["id"]) if prev else "Nada todavía.\n")
        p += "Lo que tú has dicho hasta ahora:\n" + memoria(a) + "\n"
        p += f"## Tu tarea\nPronostica qué ocurre desde tu papel entre el tramo anterior y el tramo actual ({cur['etiqueta']}).\n"
        p += f"- Como máximo {MAX} afirmaciones.\n- Cada afirmación necesita un mecanismo: por qué ocurre, no solo qué ocurre.\n"
        if "busqueda_web" in (g.get("herramientas") or []):
            p += f"- Dato: {DATO}. Busca en la web datos reales que anclen el mecanismo y cita la URL. No inventes cifras ni fuentes; si no tienes dato, deja dato y fuente vacíos.\n"
        else:
            p += "- No necesitas buscar datos: deja dato y fuente vacíos.\n"
        if V2:
            p += "- Clasifica cada afirmación por su evidencia: dato (apoyada en un dato con fuente), inferencia (se deduce de hechos establecidos o datos) o especulacion (plausible, sin apoyo directo).\n"
            p += "- Una cifra sin fuente no entrará en el canon: si das un número, cita de dónde sale o exprésalo sin cifra.\n"
        p += "- Construye sobre los hechos establecidos; no los repitas. Puedes discrepar de otro agente: indícalo en reacciona_a con su id y explica por qué en el mecanismo.\n"
        p += "- Evita la narrativa previsible (pánico, caída de mercados, adaptación, nueva normalidad) salvo que tengas un mecanismo concreto. Evita también suponer que todo el mundo reacciona con prudencia: en un mundo real, alguien se equivoca, exagera o se aprovecha.\n" if V2 else "- Evita la narrativa previsible (pánico, caída de mercados, adaptación, nueva normalidad) salvo que tengas un mecanismo concreto.\n"
        if g.get("incentivos"):
            p += "- Tus incentivos guían lo que haces: actúa como lo haría alguien que gana o pierde exactamente eso.\n"
        if g["tipo"] == "a_pie":
            p += "- Hablas desde tu vida cotidiana, en primera persona y sin jerga técnica. El mecanismo es por qué te pasa a ti o a la gente de tu entorno.\n"
        if g["tipo"] == "disruptor":
            p += "- Tu trabajo es proponer al menos un efecto que nadie ha previsto y que la narrativa dominante del tramo anterior ignora. Tiene que ser plausible y llevar mecanismo.\n"
        if g["tipo"] == "actor":
            p += "- No analizas desde fuera: actúas en el mundo. Tus afirmaciones describen lo que haces, lo que publicas o decides, y lo que provoca, en tercera persona y con tu nombre de rol.\n"
        ev_line = "      evidencia: dato | inferencia | especulacion\n" if V2 else ""
        p += f"\n## Formato de respuesta\nSolo este YAML (comillas dobles en los textos):\n\nintervencion:\n  agente: {a}\n  tramo: {T}\n  afirmaciones:\n    - texto: \"...\"\n      mecanismo: \"...\"\n      dato: \"...\"\n      fuente: \"...\"\n      confianza: baja | media | alta\n{ev_line}      areas_afectadas: [...]\n  reacciona_a: [ids de afirmaciones de otros agentes, o lista vacía]\n"
        open(f"{B}/_prompts/{T}/{a}.md", "w", encoding="utf-8").write(p)
    log(f"{T}: fichas preparadas para {', '.join(ACT)}")
    print("ok", len(ACT), "fichas")

elif CMD == "check":
    bad = []
    for a in ACT:
        p = f"{B}/intervenciones/{T}/{a}.yaml"
        try:
            iv = yaml.safe_load(open(p, encoding="utf-8"))["intervencion"]
            afs = iv["afirmaciones"]
            if len(afs) > MAX:
                log(f"{T}/{a}: {len(afs)} afirmaciones, se recortan a {MAX}"); afs = afs[:MAX]
            ok = []
            for af in afs:
                if not all(af.get(k) for k in ("texto", "mecanismo", "confianza")):
                    log(f"{T}/{a}: afirmación sin campos obligatorios, descartada"); continue
                if V2 and af.get("evidencia") not in EVIDENCIAS:
                    log(f"{T}/{a}: evidencia ausente o no válida ({af.get('evidencia')}); se marca como especulacion")
                    af["evidencia"] = "especulacion"
                ok.append(af)
            for n, af in enumerate(ok, 1):
                af["id"] = f"{a}/{T}/{n}"
            iv["afirmaciones"] = ok; iv["agente"] = a; iv["tramo"] = T
            iv["reacciona_a"] = iv.get("reacciona_a") or []
            dump({"intervencion": iv}, p)
            print(a, len(ok), "afirmaciones")
        except Exception as ex:
            bad.append(a); print("ERROR", a, ex)
    log(f"{T}: intervenciones comprobadas" + (f"; con error: {bad}" if bad else ""))

elif CMD == "arbitro":
    ar = E["arbitro"]
    p = "Eres el árbitro de una simulación de escenarios de Aftermath Studio. No pronosticas: consolidas lo que han dicho los agentes en un estado del mundo coherente.\n\n"
    p += "## El mundo\n" + mundo() + "\n## Tus criterios\n" + "".join(f"- {c}\n" for c in ar["criterios"])
    p += f"Plausibilidad: {ar['plausibilidad']}\n"
    if V2:
        p += "Regla fija: una cifra sin fuente no entra en el canon como hecho. Descarta la afirmación o recoge su contenido sin la cifra.\n"
    if ar.get("max_hechos_por_tramo"):
        p += f"Como máximo {ar['max_hechos_por_tramo']} hechos establecidos en este tramo. Todo lo demás va a descartadas con su motivo.\n"
    p += f"\n## Tramo que consolidas\n{cur['etiqueta']} ({cur['desde_evento']} desde el suceso)\n"
    p += "Estado del mundo anterior:\n" + (estado_txt(prev["id"], True) if prev else "Primer tramo.\n")
    p += "\nIntervenciones de este tramo (todas, con sus ids):\n"
    p += yaml.safe_dump(interv(T), allow_unicode=True, sort_keys=False, width=1000)
    p += "\n## Tu tarea\n1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.\n"
    p += "2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.\n"
    p += "3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.\n"
    p += "4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.\n"
    if V2:
        fmt_m = ""
    else:
        p += "5. Puntúa las métricas:\n" + "".join(f"- {m['id']}: {m['pregunta']} ({m['tipo']}" + (f"; opciones: {', '.join(m['opciones'])}" if m.get("opciones") else "; de 1 a 5") + ")\n" for m in METS)
        fmt_m = "  metricas:\n" + "".join(f"    {m['id']}: valor\n" for m in METS)
    p += f"\n## Formato de respuesta\nSolo este YAML (comillas dobles en los textos):\n\nestado_del_mundo:\n  tramo: {T}\n  resumen: \"...\"\n  hechos_establecidos:\n    - id: {T}-01\n      texto: \"...\"\n      origen: [ids]\n  tensiones_abiertas: [\"...\"]\n  contradicciones_resueltas:\n    - entre: [ids]\n      decision: \"...\"\n      motivo: \"...\"\n  descartadas:\n    - id: ...\n      motivo: \"...\"\n" + fmt_m
    open(f"{B}/_prompts/{T}/arbitro.md", "w", encoding="utf-8").write(p)
    log(f"{T}: ficha del árbitro preparada")
    print("ok", f"{B}/_prompts/{T}/arbitro.md", len(p), "caracteres")

elif CMD == "post":
    st = estado(T)
    ids = {af["id"] for iv in interv(T) for af in iv["afirmaciones"]}
    prev_h = {h["id"] for h in estado(prev["id"]).get("hechos_establecidos") or []} if prev else set()
    probs = [h["id"] for h in st.get("hechos_establecidos") or [] if not h.get("origen") or not all(x in ids or x in prev_h for x in h["origen"])]
    mx = E["arbitro"].get("max_hechos_por_tramo")
    if mx and len(st.get("hechos_establecidos") or []) > mx:
        probs.append(f"supera {mx} hechos")
    if not V2 and set(st.get("metricas", {})) != {m["id"] for m in METS}:
        probs.append("metricas")
    canon = {x for h in st.get("hechos_establecidos") or [] for x in (h.get("origen") or [])}
    os.makedirs(f"{B}/memoria", exist_ok=True)
    for iv in interv(T):
        with open(f"{B}/memoria/{iv['agente']}.md", "a", encoding="utf-8") as f:
            f.write(f"\n### {cur['etiqueta']}\n")
            for af in iv["afirmaciones"]:
                f.write(f"- [{af['id']}] {af['texto']}" + (" (entró en el canon)" if af["id"] in canon else " (no entró en el canon)") + "\n")
    n = len(st.get("hechos_establecidos") or []); d = len(st.get("descartadas") or [])
    log(f"{T}: estado consolidado; {n} hechos, {d} descartadas" + (f"; métricas {st.get('metricas')}" if not V2 else "") + (f"; revisar: {probs}" if probs else ""))
    print("hechos", n, "| descartadas", d, "| problemas", probs)
    print("resumen:", st["resumen"])

elif CMD == "evaluador":
    os.makedirs(f"{B}/metricas", exist_ok=True)
    p = "Eres el evaluador de una simulación de escenarios de Aftermath Studio. No pronosticas ni consolidas: mides el estado del mundo con unas escalas definidas.\n\n"
    p += "## El mundo\n" + mundo() + "\n"
    p += f"## Tramo que evalúas\n{cur['etiqueta']} ({cur['desde_evento']} desde el suceso)\n"
    p += "Estado del mundo al cierre de este tramo:\n" + estado_txt(T, True) + "\n"
    if prev and os.path.exists(f"{B}/metricas/{prev['id']}.yaml"):
        p += "Tu evaluación del tramo anterior, como referencia:\n" + open(f"{B}/metricas/{prev['id']}.yaml", encoding="utf-8").read() + "\n"
    p += "## Métricas y niveles\n"
    for m in METS:
        p += f"\n### {m['id']}: {m['pregunta']} ({m['tipo']})\n"
        if m.get("niveles"):
            p += "".join(f"- {k}: {v}\n" for k, v in m["niveles"].items())
        elif m.get("opciones"):
            p += "Opciones: " + ", ".join(m["opciones"]) + "\n"
        else:
            p += "Escala de 1 a 5.\n"
    p += "\n## Tu tarea\n1. Para cada métrica, elige el nivel cuya descripción se ajusta mejor a los hechos establecidos, no a las tensiones ni a lo que podría pasar.\n"
    p += "2. Si el mundo está entre dos niveles, elige el más cercano según los hechos, no el inferior ni el superior por prudencia, y di en la justificación qué falta para alcanzar el siguiente.\n"
    p += "3. Justifica cada valor en una o dos frases: por qué este nivel y no el contiguo. Cita en apoyos los ids de los hechos que lo sostienen.\n"
    p += "4. Mide el mundo en su conjunto. Si hay diferencias claras entre regiones, dilo en la justificación.\n"
    p += f"\n## Formato de respuesta\nSolo este YAML (comillas dobles en los textos):\n\nevaluacion:\n  tramo: {T}\n  metricas:\n" + "".join(f"    - id: {m['id']}\n      valor: ...\n      justificacion: \"...\"\n      apoyos: [ids de hechos]\n" for m in METS)
    open(f"{B}/_prompts/{T}/evaluador.md", "w", encoding="utf-8").write(p)
    log(f"{T}: ficha del evaluador preparada")
    print("ok", f"{B}/_prompts/{T}/evaluador.md", len(p), "caracteres")

elif CMD == "postev":
    ev = yaml.safe_load(open(f"{B}/metricas/{T}.yaml", encoding="utf-8"))["evaluacion"]
    hechos = {h["id"] for h in estado(T).get("hechos_establecidos") or []}
    probs = []
    got = {m["id"]: m for m in ev["metricas"]}
    for m in METS:
        g = got.get(m["id"])
        if not g:
            probs.append(f"falta {m['id']}"); continue
        validos = [str(k) for k in m["niveles"]] if m.get("niveles") else (m.get("opciones") or [str(i) for i in range(1, 6)])
        if str(g.get("valor")) not in validos:
            probs.append(f"{m['id']}: valor {g.get('valor')} no válido")
        if any(x not in hechos for x in g.get("apoyos") or []):
            probs.append(f"{m['id']}: apoyos que no son hechos de este tramo")
    vals = {m["id"]: got[m["id"]]["valor"] for m in METS if m["id"] in got}
    log(f"{T}: métricas evaluadas {vals}" + (f"; revisar: {probs}" if probs else ""))
    print("metricas", vals, "| problemas", probs)

else:
    sys.exit(f"Comando desconocido: {CMD}")
