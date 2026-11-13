# Registro de la ejecución

Escenario: vision-ultravioleta v5 (esquema 0.2) · tercera ejecución · prueba reducida (7 agentes: economista, político, medios, oftalmóloga, adolescente, agitador y disruptor; tramos h1, h2, h3, h5) · modo ligero · 1 repetición
Cambios respecto a 2026-11-12-1800: incentivos y restricciones en todos los agentes, agente actor 'agitador', tipo de evidencia por afirmación, regla de cifras sin fuente, evaluador separado del árbitro y métricas con niveles descritos.
Modelos: orquestador, agentes, árbitro y evaluador con claude-opus-5-5 (subagentes del entorno, heredan el modelo del orquestador); parámetros por defecto del entorno; sin temperatura configurable.
Aislamiento: cada subagente lee solo su ficha en _prompts/<tramo>/<rol>.md y escribe su salida en la biblia.

- 2026-11-12 21:26 · h1: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
- 2026-11-12 21:28 · h1: intervenciones comprobadas
- 2026-11-12 21:28 · h1: ficha del árbitro preparada
- 2026-11-12 21:29 · h1: estado consolidado; 10 hechos, 5 descartadas
- 2026-11-12 21:29 · h1: ficha del evaluador preparada
- 2026-11-12 21:30 · h1: métricas evaluadas {'alarma_social': 3, 'confianza_institucional': 3, 'respuesta_gobiernos': 'comunicacion', 'impacto_economico': 2, 'adaptacion': 1}
- 2026-11-12 21:30 · h2: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
- 2026-11-13 09:05 · h2: los 7 subagentes se cortaron por el límite de uso de 5 horas de la cuenta (12/11 ~21:45) antes de escribir; se relanzan con las mismas fichas
- 2026-11-13 09:07 · h2: intervenciones comprobadas
- 2026-11-13 09:07 · h2: ficha del árbitro preparada
- 2026-11-13 09:09 · h2: estado consolidado; 10 hechos, 11 descartadas
- 2026-11-13 09:09 · h2: ficha del evaluador preparada
- 2026-11-13 09:09 · h2: métricas evaluadas {'alarma_social': 3, 'confianza_institucional': 3, 'respuesta_gobiernos': 'comunicacion', 'impacto_economico': 2, 'adaptacion': 2}
- 2026-11-13 09:09 · h3: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
