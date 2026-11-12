# Aftermath Studio — Esquema del escenario v0.1

12 de noviembre de 2026 · Fran Barbero

Documento vivo: https://claude.ai/artifact/DetSZyD3cQea6c3j9XhYrc

El esquema es un archivo YAML que describe una simulación completa: el configurador lo genera entrevistando al usuario, el motor lo ejecuta sin saber nada del tema y la biblia del escenario guarda todo lo que produce.

- Plantilla completa: [`esquema/plantilla-escenario.yaml`](../esquema/plantilla-escenario.yaml)
- Ejemplo real: [`escenarios/vision-ultravioleta/escenario.yaml`](../escenarios/vision-ultravioleta/escenario.yaml)

## Los bloques del esquema

Diez bloques cubren cualquier simulación. Los cuatro primeros describen el mundo; los seis siguientes, cómo se ejecuta y qué se obtiene.

| Bloque | Qué describe | Quién lo usa |
| --- | --- | --- |
| `meta` | Identidad: título, tipo (especulativo o negocio), idioma, versión | Todos |
| `evento` | La premisa, el momento cero, el alcance y los supuestos que se dan por fijos | Configurador, agentes, árbitro |
| `cronologia` | Los tramos en los que avanza la simulación | Motor |
| `agentes` | Cada rol: tipo, perfil, objetivos, conocimiento privado, herramientas y modelo | Motor, agentes |
| `arbitro` | Cómo consolida cada tramo, resuelve contradicciones y cuántos hechos admite como máximo por tramo | Árbitro |
| `interaccion` | Qué ve cada agente de los demás y qué exige cada afirmación | Motor, agentes |
| `variables` | Lo que cambia entre repeticiones para obtener futuros distintos | Motor |
| `ejecucion` | Repeticiones, semilla, modo (ligero o intensivo), proveedor por defecto y, opcionalmente, un subconjunto de agentes y tramos para pruebas | Motor |
| `resultados` | Métricas que el árbitro puntúa y estructura del informe | Árbitro, análisis |
| `seguimiento` | Qué se guarda en la biblia y qué modos de exploración se permiten | Motor, Claude |

Dos reglas del formato:

- **Todo supuesto es explícito.** Lo que el usuario no dijo y el configurador decidió queda marcado con `fuente: configurador`, para que el usuario lo vea y lo corrija.
- **El motor no interpreta el tema.** Solo lee bloques, lanza agentes y guarda salidas. Todo el conocimiento del escenario está en el archivo.

## Contratos de salida

Agentes y árbitro responden siempre con la misma estructura. Así el motor puede guardar, comparar y contar sin entender el contenido.

**Intervención de un agente en un tramo.** Cada afirmación lleva su mecanismo, su dato si lo hay y su grado de confianza:

```yaml
intervencion:
  agente: economista
  tramo: h1
  afirmaciones:
    - texto: "Las bolsas suspenden la cotización en las primeras horas"
      mecanismo: "Los reguladores activan los cortacircuitos ante caídas bruscas por incertidumbre"
      dato: "Descripción del mecanismo de suspensión del mercado en cuestión"
      fuente: "URL consultada"        # vacío si no hay dato buscado
      confianza: media               # baja | media | alta
      areas_afectadas: [finanzas, politica]
  reacciona_a: [politico/h1/2]       # afirmaciones de otros agentes que tiene en cuenta
```

**Estado del mundo al cerrar un tramo.** Lo redacta el árbitro y es el punto de partida del tramo siguiente:

```yaml
estado_del_mundo:
  tramo: h1
  resumen: "Tres o cuatro frases que cualquier agente pueda leer"
  hechos_establecidos:               # canon: lo que ya no se puede contradecir
    - id: h1-01
      texto: "..."
      origen: [psicologo/h1/1, sociologo/h1/3]
  tensiones_abiertas: ["..."]        # lo que el siguiente tramo debe resolver
  contradicciones_resueltas:
    - entre: [economista/h1/2, politico/h1/1]
      decision: "..."
      motivo: "..."
  descartadas:                       # afirmaciones que no entran en el canon
    - id: medios/h1/4
      motivo: "Sin mecanismo plausible"
  metricas:                          # las definidas en el bloque resultados
    alarma_social: 4
```

Los identificadores del tipo `agente/tramo/número` permiten rastrear cualquier hecho del informe hasta la intervención que lo originó.

## Decisiones abiertas

Las cinco decisiones previas a la skill quedaron cerradas el 12/11/2026:

- [x] **Supuestos del ultravioleta.** Cerrado el 12/11/2026: se mantienen s2 (UV-A como colores nuevos) y s4 (causa y permanencia desconocidas); s3 pasa a incluir deslumbramiento y fatiga visual los primeros días, sin daño permanente.
- [x] **Visibilidad entre agentes.** Cerrado: `estado_e_intervenciones`. Cada agente ve el estado del mundo y lo que dijeron los demás; más efectos cruzados a cambio de más contexto y algo más de riesgo de convergencia.
- [x] **Número de agentes.** Cerrado: la primera prueba usa 6 agentes (economista, político, medios, oftalmóloga, adolescente y disruptor) y los 4 primeros tramos, mediante `ejecucion.agentes` y `ejecucion.tramos`. Son 24 intervenciones y 4 consolidaciones, frente a 110 y 10 de la simulación completa.
- [x] **Formato del archivo.** Cerrado: YAML para que lo lean personas; el JSON Schema de validación llega con el motor MCP.
- [x] **Métricas.** Cerrado: se empieza con las cuatro propuestas (alarma social, respuesta de los gobiernos, impacto económico y adaptación); se revisan tras la primera prueba.
