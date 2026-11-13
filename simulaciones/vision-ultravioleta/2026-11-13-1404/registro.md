# Registro de la ejecución

Escenario: vision-ultravioleta v6 (esquema 0.2) · cuarta ejecución · prueba reducida (7 agentes: economista, político, medios, oftalmóloga, adolescente, agitador y disruptor; tramos h1, h2, h3, h5) · modo ligero · 1 repetición
Cambios respecto a 2026-11-12-2126: el evaluador elige el nivel más cercano en lugar del inferior; nueva métrica relatos_en_competencia.
Modelos: orquestador, agentes, árbitro y evaluador con claude-opus-5-5 (subagentes del entorno, heredan el modelo del orquestador); parámetros por defecto del entorno; sin temperatura configurable.
Aislamiento: cada subagente lee solo su ficha en _prompts/<tramo>/<rol>.md y escribe su salida en la biblia.

- 2026-11-13 14:04 · h1: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
- 2026-11-13 14:06 · h1: intervenciones comprobadas
- 2026-11-13 14:06 · h1: ficha del árbitro preparada
- 2026-11-13 14:07 · h1: estado consolidado; 10 hechos, 5 descartadas
- 2026-11-13 14:07 · h1: ficha del evaluador preparada
- 2026-11-13 14:07 · h1: métricas evaluadas {'alarma_social': 3, 'confianza_institucional': 2, 'relatos_en_competencia': 3, 'respuesta_gobiernos': 'comunicacion', 'impacto_economico': 3, 'adaptacion': 2}
- 2026-11-13 14:07 · h2: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
- 2026-11-13 14:10 · h2: intervenciones comprobadas
- 2026-11-13 14:10 · h2: ficha del árbitro preparada
- 2026-11-13 14:11 · h2: estado consolidado; 10 hechos, 8 descartadas
- 2026-11-13 14:11 · h2: ficha del evaluador preparada
- 2026-11-13 14:12 · h2: métricas evaluadas {'alarma_social': 3, 'confianza_institucional': 3, 'relatos_en_competencia': 3, 'respuesta_gobiernos': 'comunicacion', 'impacto_economico': 3, 'adaptacion': 3}
- 2026-11-13 14:12 · h3: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
- 2026-11-13 14:15 · h3: intervenciones comprobadas
- 2026-11-13 14:15 · h3: ficha del árbitro preparada
- 2026-11-13 14:17 · h3: estado consolidado; 10 hechos, 14 descartadas
- 2026-11-13 14:17 · h3: ficha del evaluador preparada
- 2026-11-13 14:17 · h3: métricas evaluadas {'alarma_social': 3, 'confianza_institucional': 3, 'relatos_en_competencia': 3, 'respuesta_gobiernos': 'comunicacion', 'impacto_economico': 3, 'adaptacion': 3}
- 2026-11-13 14:17 · h5: fichas preparadas para economista, politico, medios, oftalmologa, adolescente, agitador, disruptor
