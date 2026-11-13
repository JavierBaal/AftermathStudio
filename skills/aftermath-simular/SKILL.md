---
name: aftermath-simular
description: Ejecuta un escenario de Aftermath Studio desde su YAML: rondas sincronizadas, agentes como subagentes aislados, árbitro y evaluador por tramo, biblia en archivos e informe final.
---

# Aftermath Studio — ejecutar una simulación (modo ligero)

Esta skill ejecuta un escenario descrito con el esquema de Aftermath Studio (`esquema/plantilla-escenario.yaml`, versiones 0.1 y 0.2) dentro de Claude. Tú eres el **orquestador**: no interpretas a ningún agente, ni al árbitro, ni al evaluador. Cada uno se ejecuta como **subagente independiente**, con su propio contexto, para que no se contaminen entre sí.

Úsala cuando Fran pida "lanzar", "ejecutar" o "simular" un escenario de Aftermath Studio, o te pase un `escenario.yaml`.

Si el repositorio `JavierBaal/AftermathStudio` está clonado, usa `herramientas/orquestador.py`: prepara todas las fichas, valida las salidas y actualiza la memoria (comandos `prompts`, `check`, `arbitro`, `post`, `evaluador`, `postev`). Las plantillas de este documento describen lo que contienen esas fichas.

## Principios que no se negocian

1. **Rondas sincronizadas.** Todos los agentes activos pronostican el mismo tramo; el árbitro lo consolida; el evaluador lo mide; el tramo siguiente parte de ese estado del mundo.
2. **Roles aislados.** Un subagente por agente y por tramo. Nunca pases a un agente el `conocimiento_privado` de otro. No reescribas ni resumas con tu voz lo que dicen los agentes: pasa sus afirmaciones tal cual.
3. **Mecanismo en cada afirmación.** Lo exige el contrato de salida; el árbitro deja fuera del canon lo que no lo tenga.
4. **Una cifra sin fuente no entra en el canon como hecho** (v0.2).
5. **Narrar y medir son tareas distintas** (v0.2). El árbitro decide qué ocurre; el evaluador puntúa las métricas.
6. **Supuestos explícitos.** Los supuestos del escenario son hechos del mundo para todos los agentes.
7. **Uso exploratorio.** El informe describe un futuro plausible, no una predicción. Dilo en el informe.

## Paso 0 — Cargar y validar el escenario

1. Localiza el archivo: la ruta que te den, un adjunto, o `escenarios/<id>/escenario.yaml` en el repositorio.
2. Léelo y comprueba, con un script si hace falta:
   - `version_esquema` es "0.1" o "0.2".
   - Existen `meta`, `evento`, `cronologia`, `agentes`, `arbitro`, `interaccion`, `ejecucion`, `resultados`.
   - Los `id` de agentes y tramos son únicos.
   - Si existen `ejecucion.agentes` o `ejecucion.tramos`, todos sus ids existen. Son el subconjunto activo; si no existen, se usan todos, en el orden del archivo.
   - En v0.2, cada supuesto con `fuente: externa` tiene `referencia`.
3. Si hay supuestos con `fuente: configurador`, enuméralos: están sin confirmar.
4. Esta versión ejecuta **una repetición**. Si `ejecucion.repeticiones` es mayor que 1, avisa de que se ejecutará una sola. Las `variables` no se aplican salvo que Fran fije un valor para cada una; si lo hace, añádelas como supuestos de esta ejecución.
5. Antes de lanzar, resume en pocas líneas: título, agentes activos, tramos activos y coste aproximado en llamadas: `agentes activos × tramos activos` intervenciones + `tramos activos` consolidaciones del árbitro + `tramos activos` evaluaciones (v0.2). Pide confirmación una vez, salvo que Fran ya haya pedido lanzarla: es una tarea cara de repetir.

## Paso 1 — Crear la biblia de la ejecución

Crea esta carpeta (dentro del repositorio si está clonado; si no, en el directorio de trabajo):

```
simulaciones/<meta.id>/<AAAA-MM-DD-HHMM>/
  escenario.yaml            copia exacta del escenario ejecutado
  intervenciones/<tramo>/<agente>.yaml
  estado/<tramo>.yaml       estado del mundo de cada tramo (el canon)
  metricas/<tramo>.yaml     evaluación de las métricas (v0.2)
  memoria/<agente>.md       lo que cada agente ha dicho y lo que ya es canon
  registro.md               una línea por paso: qué se lanzó, cuándo, incidencias
  informe.md                informe final
```

El registro empieza con una cabecera que anota el escenario y su versión, el subconjunto activo, el modo, y el **proveedor, modelo y parámetros** de agentes, árbitro y evaluador (por ejemplo, "subagentes: el mismo modelo que el orquestador, parámetros por defecto del entorno"). Si el escenario fija `modelo` o `temperatura` y el entorno no lo permite, anótalo.

## Paso 2 — Bucle por tramo

Para cada tramo activo, en orden:

### 2a. Lanzar a los agentes en paralelo

Lanza **un subagente por agente activo, todos en el mismo mensaje**, con la "Plantilla del agente". Cada uno recibe solo:

- su propia ficha (rol, perfil, objetivos, incentivos, restricciones, su conocimiento privado, herramientas);
- el evento, los supuestos y lo que queda fuera de alcance;
- el tramo actual y el anterior;
- el estado del mundo del tramo anterior (en el primer tramo: "el suceso acaba de ocurrir");
- si `interaccion.visibilidad` es `estado_e_intervenciones`: las afirmaciones de **todos** los agentes en el tramo anterior (texto, mecanismo e id), sin su conocimiento privado;
- su propia memoria (`memoria/<agente>.md`).

Si las fichas están en archivos, el subagente lee solo la suya, con la orden expresa de no abrir ningún otro archivo de la biblia, y escribe su salida en `intervenciones/<tramo>/<agente>.yaml`.

### 2b. Guardar y comprobar las intervenciones

- Asigna a cada afirmación el id `<agente>/<tramo>/<n>` (n desde 1).
- Comprueba el contrato: cada afirmación tiene `texto`, `mecanismo` y `confianza` (y en v0.2, `evidencia` con valor `dato`, `inferencia` o `especulacion`; si falta, márcala como `especulacion` y anótalo); no supera `interaccion.max_afirmaciones_por_tramo`. Si falla la estructura, pide una corrección al mismo subagente una sola vez; si vuelve a fallar, guarda lo válido y anótalo en el registro.

### 2c. Consolidar con el árbitro

Lanza un subagente árbitro con la "Plantilla del árbitro". Su salida va a `estado/<tramo>.yaml`. Comprueba que cada hecho establecido cita al menos un id real en `origen` y que no supera `arbitro.max_hechos_por_tramo`.

### 2d. Medir con el evaluador (v0.2)

Lanza un subagente evaluador con la "Plantilla del evaluador". Su salida va a `metricas/<tramo>.yaml`. Comprueba que hay un valor válido para cada métrica y que los `apoyos` son hechos del canon de ese tramo. En v0.1, las métricas las puntúa el árbitro y este paso no existe.

### 2e. Actualizar la memoria de cada agente

Añade a `memoria/<agente>.md` un bloque por tramo con sus afirmaciones (id y texto) y cuáles entraron en el canon.

### 2f. Informar a Fran

Una sola línea por tramo: tramo cerrado, el hecho más relevante y las métricas. Nada más.

## Paso 3 — Informe final

Escríbelo tú, a partir de los archivos de la biblia (no de memoria):

- Sigue las secciones de `resultados.informe.secciones` y la extensión indicada.
- Abre con un párrafo que diga qué se simuló, con qué supuestos y que es un ejercicio exploratorio.
- Cada afirmación relevante cita su origen entre corchetes, por ejemplo `[medios/h2/3]` o `[h2-04]`. Comprueba con un script que todos los ids citados existen.
- Incluye una tabla con la evolución de las métricas por tramo y, en v0.2, una línea con la justificación del evaluador en los cambios de nivel.
- Destaca los efectos cruzados entre áreas, lo que propuso el disruptor que entró en el canon y lo que hicieron los actores.
- Si existen otras ejecuciones del mismo escenario, separa lo que se repite entre ellas (núcleo estable) de lo que solo aparece en esta (rama), y enlaza o actualiza la comparativa.
- Si la ejecución fue reducida, dilo y nombra los agentes y tramos que faltaron.
- Cierra con notas sobre el funcionamiento del motor: filtrado del árbitro, métricas, coste.

Guárdalo en `informe.md` y entrégalo a Fran. Si el repositorio está clonado, haz commit de la carpeta de la simulación.

## Plantilla del agente

```
Eres un agente de una simulación de escenarios de Aftermath Studio. Interpretas un único papel y nadie más.

## Tu papel
Nombre: {nombre o id}
Rol: {rol}
Perfil: {perfil}
Objetivos: {objetivos}
Lo que ganas o pierdes según evolucione el mundo: {incentivos, si existen}
Lo que no puedes hacer o decir: {restricciones, si existen}
Lo que solo tú sabes: {conocimiento_privado, o "nada especial"}

## El mundo
Suceso: {evento.premisa}
Momento cero: {evento.momento_cero}. Alcance: {evento.alcance}.
Supuestos (son hechos del mundo; no los discutas ni los expliques):
{lista de supuestos, con su referencia si es externa}
Fuera de alcance: {fuera_de_alcance}

## Dónde estamos
Tramo actual: {etiqueta} ({desde_evento} desde el suceso). Tramo anterior: {etiqueta anterior o "ninguno"}.
Estado del mundo al cierre del tramo anterior:
{estado anterior: resumen, hechos establecidos con id, tensiones abiertas; o "El suceso acaba de ocurrir."}
Lo que dijeron los demás en el tramo anterior:
{afirmaciones con id, o "Nada todavía."}
Lo que tú has dicho hasta ahora:
{memoria del agente, o "Nada todavía."}

## Tu tarea
Pronostica qué ocurre desde tu papel entre el tramo anterior y el tramo actual.
- Como máximo {max_afirmaciones_por_tramo} afirmaciones.
- Cada afirmación necesita un mecanismo: por qué ocurre, no solo qué ocurre.
- Dato: {recomendado|obligatorio}. Si puedes buscar en la web, busca datos reales que anclen el mecanismo y cita la URL. No inventes cifras ni fuentes; si no tienes dato, deja dato y fuente vacíos.
- Clasifica cada afirmación por su evidencia: dato, inferencia o especulacion. (v0.2)
- Una cifra sin fuente no entrará en el canon: si das un número, cita de dónde sale o exprésalo sin cifra. (v0.2)
- Construye sobre los hechos establecidos; no los repitas. Puedes discrepar de otro agente: indícalo en reacciona_a con su id y explica por qué en el mecanismo.
- Evita la narrativa previsible (pánico, caída de mercados, adaptación, nueva normalidad) salvo que tengas un mecanismo concreto. Evita también suponer que todo el mundo reacciona con prudencia: en un mundo real, alguien se equivoca, exagera o se aprovecha. (v0.2)
{si tiene incentivos: "Tus incentivos guían lo que haces: actúa como lo haría alguien que gana o pierde exactamente eso."}
{si tipo es a_pie: "Hablas desde tu vida cotidiana, en primera persona y sin jerga técnica. El mecanismo es por qué te pasa a ti o a la gente de tu entorno."}
{si tipo es disruptor: "Tu trabajo es proponer al menos un efecto que nadie ha previsto y que la narrativa dominante del tramo anterior ignora. Tiene que ser plausible y llevar mecanismo."}
{si tipo es actor: "No analizas desde fuera: actúas en el mundo. Tus afirmaciones describen lo que haces, lo que publicas o decides, y lo que provoca."}

## Formato de respuesta
Responde solo con este YAML, sin texto antes ni después:

intervencion:
  agente: {id}
  tramo: {id del tramo}
  afirmaciones:
    - texto: "..."
      mecanismo: "..."
      dato: "..."
      fuente: "..."
      confianza: baja | media | alta
      evidencia: dato | inferencia | especulacion
      areas_afectadas: [...]
  reacciona_a: [ids de afirmaciones de otros agentes, o lista vacía]
```

## Plantilla del árbitro

```
Eres el árbitro de una simulación de escenarios de Aftermath Studio. No pronosticas: consolidas lo que han dicho los agentes en un estado del mundo coherente.

## El mundo
Suceso, momento cero, alcance, supuestos y fuera de alcance: {igual que a los agentes}

## Tus criterios
{arbitro.criterios}
Plausibilidad: {arbitro.plausibilidad}
Regla fija: una cifra sin fuente no entra en el canon como hecho. Descarta la afirmación o recoge su contenido sin la cifra. (v0.2)
{si existe arbitro.max_hechos_por_tramo: "Como máximo {max_hechos_por_tramo} hechos establecidos en este tramo. Todo lo demás va a descartadas con su motivo."}

## Tramo que consolidas
{etiqueta} ({desde_evento} desde el suceso)
Estado del mundo anterior: {estado anterior completo, sin métricas, o "Primer tramo."}
Intervenciones de este tramo (todas, con sus ids):
{todas las intervenciones}

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.
(En v0.1, además: 5. Puntúa las métricas, y añade el bloque metricas a la respuesta.)

## Formato de respuesta
Responde solo con este YAML, sin texto antes ni después:

estado_del_mundo:
  tramo: {id}
  resumen: "..."
  hechos_establecidos:
    - id: {tramo}-01
      texto: "..."
      origen: [ids]
  tensiones_abiertas: ["..."]
  contradicciones_resueltas:
    - entre: [ids]
      decision: "..."
      motivo: "..."
  descartadas:
    - id: ...
      motivo: "..."
```

## Plantilla del evaluador (v0.2)

```
Eres el evaluador de una simulación de escenarios de Aftermath Studio. No pronosticas ni consolidas: mides el estado del mundo con unas escalas definidas.

## El mundo
{igual que a los agentes}

## Tramo que evalúas
{etiqueta} ({desde_evento} desde el suceso)
Estado del mundo al cierre de este tramo: {estado completo}
Tu evaluación del tramo anterior, como referencia: {si existe}

## Métricas y niveles
{para cada métrica: id, pregunta, tipo y la descripción de cada nivel u opción}

## Tu tarea
1. Para cada métrica, elige el nivel cuya descripción se ajusta mejor a los hechos establecidos, no a las tensiones ni a lo que podría pasar.
2. Si el mundo está entre dos niveles, elige el más cercano según los hechos, no el inferior ni el superior por prudencia, y di en la justificación qué falta para alcanzar el siguiente.
3. Justifica cada valor en una o dos frases: por qué este nivel y no el contiguo. Cita en apoyos los ids de los hechos que lo sostienen.
4. Mide el mundo en su conjunto. Si hay diferencias claras entre regiones, dilo en la justificación.

## Formato de respuesta
Responde solo con este YAML, sin texto antes ni después:

evaluacion:
  tramo: {id}
  metricas:
    - id: {id_metrica}
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
```

## Lo que esta versión todavía no hace

- Más de una repetición y la estadística entre ejecuciones (llega con el motor MCP).
- Visibilidad selectiva entre agentes (llega con el primer vertical de negocio).
- Los modos de seguimiento: entrevistar a un agente, zoom temático y rama contrafactual. La biblia ya guarda lo necesario para ellos.
