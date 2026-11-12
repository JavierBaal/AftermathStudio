---
name: aftermath-simular
description: Ejecuta un escenario de Aftermath Studio desde su YAML: rondas sincronizadas, agentes como subagentes aislados, árbitro por tramo, biblia en archivos e informe final.
---

# Aftermath Studio — ejecutar una simulación (modo ligero)

Esta skill ejecuta un escenario descrito con el esquema de Aftermath Studio (`esquema/plantilla-escenario.yaml`, versión 0.1) dentro de Claude. Tú eres el **orquestador**: no interpretas a ningún agente ni al árbitro. Cada agente y el árbitro se ejecutan como **subagentes independientes**, cada uno con su propio contexto, para que no se contaminen entre sí.

Úsala cuando Fran pida "lanzar", "ejecutar" o "simular" un escenario de Aftermath Studio, o te pase un `escenario.yaml`.

## Principios que no se negocian

1. **Rondas sincronizadas.** Todos los agentes activos pronostican el mismo tramo; el árbitro lo consolida; el tramo siguiente parte de ese estado del mundo.
2. **Roles aislados.** Un subagente por agente y por tramo. Nunca pases a un agente el `conocimiento_privado` de otro. No reescribas ni resumas con tu voz lo que dicen los agentes: pasa sus afirmaciones tal cual.
3. **Mecanismo en cada afirmación.** Lo exige el contrato de salida; el árbitro deja fuera del canon lo que no lo tenga.
4. **Supuestos explícitos.** Los supuestos del escenario son hechos del mundo para todos los agentes.
5. **Uso exploratorio.** El informe describe un futuro plausible, no una predicción. Dilo en el informe.

## Paso 0 — Cargar y validar el escenario

1. Localiza el archivo: la ruta que te den, un adjunto, o `escenarios/<id>/escenario.yaml` en el repositorio `JavierBaal/AftermathStudio`.
2. Léelo y comprueba, con un script si hace falta:
   - `version_esquema` es "0.1".
   - Existen `meta`, `evento`, `cronologia`, `agentes`, `arbitro`, `interaccion`, `ejecucion`, `resultados`.
   - Los `id` de agentes y tramos son únicos.
   - Si existen `ejecucion.agentes` o `ejecucion.tramos`, todos sus ids existen. Son el subconjunto activo; si no existen, se usan todos, en el orden del archivo.
3. Si hay supuestos con `fuente: configurador`, enuméralos: están sin confirmar.
4. Esta versión ejecuta **una repetición**. Si `ejecucion.repeticiones` es mayor que 1, avisa de que se ejecutará una sola. Las `variables` no se aplican salvo que Fran fije un valor para cada una; si lo hace, añádelas como supuestos de esta ejecución.
5. Antes de lanzar, resume en pocas líneas: título, agentes activos, tramos activos y coste aproximado en llamadas: `agentes activos × tramos activos` intervenciones + `tramos activos` consolidaciones del árbitro. Pide confirmación una vez: es una tarea cara de repetir.

## Paso 1 — Crear la biblia de la ejecución

Crea esta carpeta (dentro del repositorio si está clonado; si no, en el directorio de trabajo):

```
simulaciones/<meta.id>/<AAAA-MM-DD-HHMM>/
  escenario.yaml            copia exacta del escenario ejecutado
  intervenciones/<tramo>/<agente>.yaml
  estado/<tramo>.yaml       estado del mundo de cada tramo (el canon)
  memoria/<agente>.md       lo que cada agente ha dicho y lo que ya es canon
  registro.md               una línea por paso: qué se lanzó, cuándo, incidencias
  informe.md                informe final
```

## Paso 2 — Bucle por tramo

Para cada tramo activo, en orden:

### 2a. Lanzar a los agentes en paralelo

Lanza **un subagente por agente activo, todos en el mismo mensaje**, con la plantilla de la sección "Plantilla del agente". Cada uno recibe solo:

- su propia ficha (rol, perfil, objetivos, su conocimiento privado, herramientas);
- el evento, los supuestos y lo que queda fuera de alcance;
- el tramo actual y el anterior;
- el estado del mundo del tramo anterior (en el primer tramo: "el suceso acaba de ocurrir");
- si `interaccion.visibilidad` es `estado_e_intervenciones`: las afirmaciones de **todos** los agentes en el tramo anterior (texto, mecanismo e id), sin su conocimiento privado;
- su propia memoria (`memoria/<agente>.md`).

Si el agente tiene `busqueda_web` en `herramientas`, indícale que busque datos. Si el escenario fija `modelo` o `temperatura` y el entorno no lo permite, anótalo en el registro y sigue.

### 2b. Guardar y comprobar las intervenciones

- Guarda cada respuesta en `intervenciones/<tramo>/<agente>.yaml`.
- Asigna a cada afirmación el id `<agente>/<tramo>/<n>` (n desde 1) y añádelo al archivo.
- Comprueba el contrato: cada afirmación tiene `texto`, `mecanismo` y `confianza`; no supera `interaccion.max_afirmaciones_por_tramo`. Si falla, pide una corrección al mismo subagente una sola vez; si vuelve a fallar, guarda lo válido y anótalo en el registro.

### 2c. Consolidar con el árbitro

Lanza un subagente árbitro con la sección "Plantilla del árbitro". Guarda su respuesta en `estado/<tramo>.yaml`. Comprueba que cada hecho establecido cita al menos un id real en `origen` y que las métricas son las de `resultados.metricas`.

### 2d. Actualizar la memoria de cada agente

Añade a `memoria/<agente>.md` un bloque por tramo con sus afirmaciones (id y texto) y cuáles entraron en el canon.

### 2e. Informar a Fran

Una sola línea por tramo: tramo cerrado, el hecho más relevante y las métricas. Nada más.

## Paso 3 — Informe final

Escríbelo tú, a partir de los archivos de la biblia (no de memoria):

- Sigue las secciones de `resultados.informe.secciones` y la extensión indicada.
- Abre con un párrafo que diga qué se simuló, con qué supuestos y que es un ejercicio exploratorio.
- Cada afirmación relevante cita su origen entre corchetes, por ejemplo `[medios/h2/3]`.
- Incluye una tabla con la evolución de las métricas por tramo.
- Destaca los efectos cruzados entre áreas y lo que propuso el disruptor que entró en el canon.
- Si la ejecución fue reducida, dilo y nombra los agentes y tramos que faltaron.

Guárdalo en `informe.md` y entrégalo a Fran como documento. Si el repositorio está clonado, propón hacer commit de la carpeta de la simulación.

## Plantilla del agente

```
Eres un agente de una simulación de escenarios de Aftermath Studio. Interpretas un único papel y nadie más.

## Tu papel
Nombre: {nombre o id}
Rol: {rol}
Perfil: {perfil}
Objetivos: {objetivos}
Lo que solo tú sabes: {conocimiento_privado, o "nada especial"}

## El mundo
Suceso: {evento.premisa}
Momento cero: {evento.momento_cero}. Alcance: {evento.alcance}.
Supuestos (son hechos del mundo; no los discutas ni los expliques):
{lista de supuestos}
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
- Construye sobre los hechos establecidos; no los repitas. Puedes discrepar de otro agente: indícalo en reacciona_a con su id y explica por qué en el mecanismo.
- Evita la narrativa previsible (pánico, caída de mercados, adaptación, nueva normalidad) salvo que tengas un mecanismo concreto.
{solo si tipo es a_pie: "Hablas desde tu vida cotidiana, en primera persona y sin jerga técnica. El mecanismo es por qué te pasa a ti o a la gente de tu entorno."}
{solo si tipo es disruptor: "Tu trabajo es proponer al menos un efecto que nadie ha previsto y que la narrativa dominante del tramo anterior ignora. Tiene que ser plausible y llevar mecanismo."}

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

## Tramo que consolidas
{etiqueta} ({desde_evento} desde el suceso)
Estado del mundo anterior: {estado anterior completo, o "Primer tramo."}
Intervenciones de este tramo (todas, con sus ids):
{todas las intervenciones}

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.
5. Puntúa las métricas: {lista de resultados.metricas con tipo y opciones; las de escala, de 1 a 5}.

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
  metricas:
    {id_metrica}: valor
```

## Lo que esta versión todavía no hace

- Más de una repetición y la estadística entre ejecuciones (llega con el motor MCP).
- Los modos de seguimiento: entrevistar a un agente, zoom temático y rama contrafactual (siguiente paso de la hoja de ruta). La biblia ya guarda lo necesario para ellos.
