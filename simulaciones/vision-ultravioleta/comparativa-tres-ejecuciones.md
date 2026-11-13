# Comparativa de las tres primeras ejecuciones

Escenario `vision-ultravioleta` · prueba reducida (horas 1, 2, 3 y 5) · 12 y 13 de noviembre de 2026

- **A** — `2026-11-12-1422` · escenario v3 · esquema 0.1 · árbitro permisivo · 6 agentes
- **B** — `2026-11-12-1800` · escenario v4 · esquema 0.1 · árbitro estricto · 6 agentes
- **C** — `2026-11-12-2126` · escenario v5 · esquema 0.2 · árbitro estricto · 7 agentes (entra el agitador), incentivos y restricciones, evidencia, evaluador separado

La comparación detallada de A y B está en [`comparativa-1422-1800.md`](comparativa-1422-1800.md).

## Conclusión

1. **El núcleo físico se mantiene en las tres.** Cámaras que no captan el fenómeno, gafas que lo apagan, crema solar visible, el parabrisas que protege y las ventanillas que no, la queratitis diferida, el recreo dentro, los mercados que no se hunden. Es el resultado más sólido hasta ahora.
2. **Cada ejecución toma una rama social distinta.** A: geografía y consumo. B: secreto y confianza. C: daño causado por la conducta, explotado por un actor interesado.
3. **El agitador cambia la historia, pero no las métricas de alarma.** En C hay por primera vez una tensión institucional real (dos recuentos de daños que compiten) y la respuesta de los gobiernos sube a medidas sectoriales. Pero la alarma social y la confianza siguen en 3 durante cinco horas, igual que en A y B.
4. **El sesgo hacia la calma tiene ahora una causa identificada en el propio motor:** la regla del evaluador "ante la duda, el nivel inferior". En C la alarma de la hora 5 quedó en 3 estando "entre 3 y 4".

## Los números

| | A | B | C |
| --- | --- | --- | --- |
| Agentes | 6 | 6 | 7 |
| Afirmaciones | 119 | 118 | 138 |
| Entran en el canon | 118 (99 %) | 88 (75 %) | 88 (64 %) |
| Descartadas por el árbitro | 1 | 30 | 50 |
| Con fuente buscada | 52 | 56 | 59 |
| Referencias entre agentes | 39 | 50 | 64 |
| Disruptor en el canon | 19 de 19 | 14 de 19 | 12 de 18 |
| Agitador en el canon | — | — | 13 de 20 |
| Alarma social, hora 5 | 3 | 3 | 3 |
| Confianza institucional, hora 5 | — | — | 3 |
| Respuesta de los gobiernos, hora 5 | comunicación | comunicación | **medidas sectoriales** |
| Impacto económico, hora 5 | 2 | 2 | 2 |
| Adaptación, hora 5 | 3 | 3 | 2 |
| Tokens de subagentes (aprox.) | 3,3 M | 3,3 M | 4,1 M |

Las métricas de A y B las puntuó el árbitro sin niveles descritos; las de C, el evaluador con niveles. La adaptación no es comparable entre A/B y C: el evaluador de C exige que las pautas estén adoptadas, no solo publicadas.

## Núcleo estable (en las tres)

- Las cámaras no captan los colores nuevos; se viralizan testimonios y reacciones.
- Las gafas de sol y las lentes con filtro atenúan o apagan el fenómeno; los usuarios de gafas graduadas lo notan.
- La crema solar y el daño solar de la piel se vuelven visibles.
- El parabrisas laminado protege; las ventanillas laterales no.
- La queratitis por mirar al sol o a lámparas llega con horas de retraso; los oftalmólogos se adelantan.
- Los colegios meten el recreo dentro sin cerrar; las instrucciones llegan tarde y desiguales.
- Los adolescentes rechazan las gafas y adoptan alguna conducta de riesgo para ver mejor el color.
- Los mercados no se hunden: movimientos en óptica, gafas y cosmética solar.
- Ningún gobierno declara la emergencia en cinco horas.

## Ramas (solo en una)

| A · geografía y consumo | B · secreto y confianza | C · daño por conducta |
| --- | --- | --- |
| Brecha norte-sur en Europa y escepticismo nórdico | Evaluaciones secretas de defensa | Lámparas germicidas UV-C vendidas para "ver el color" |
| El índice UV oficial refuerza a los escépticos | Sesiones a puerta cerrada en Madrid y Washington | Retinopatía solar sospechada en adolescentes |
| Turismo nórdico a Canarias | Operados con filtro organizados y mezclados con la conspiración | Registro de "síntomas tardíos" y recuento del agitador |
| Parada de inspecciones aeronáuticas | El cristal de las ventanas no protege; lámina anti-UV | Tinción con fluoresceína como prueba objetiva |
| Estigma sobre vitíligo y melasma | Rumor asiático de que "ya se ha ido" | Abandono preventivo del protector en el Cono Sur |
| Restauraciones descubiertas en la segunda mano | Primer mensaje sanitario común de la UE | Reacciones fototóxicas por fármacos comunes |
| | | Comida fluorescente en la despensa |
| | | Fin de la invisibilidad del marcado forense |
| | | Órdenes sectoriales de Trabajo y Consumo; notificación a Safety Gate |

Hay temas que aparecen en dos ejecuciones y no figuran como rama: los billetes rechazados (A y C), el conflicto laboral por el deslumbramiento (B y C) y la luz LED que apaga el fenómeno en interiores (A y C).

## Qué aprendemos para el motor

1. **Los incentivos y los actores funcionan.** El agitador es el agente con más influencia en el rumbo de C y genera la primera dinámica institucional de competencia por el relato. Se queda.
2. **Las métricas siguen sin captar la tensión.** Dos cambios posibles: quitar la regla "ante la duda, el inferior" y pedir al evaluador que elija el nivel más cercano con su justificación; y añadir métricas de dinámica, como el grado de polarización o la existencia de relatos en competencia, que en C es lo que de verdad cambió.
3. **La ramificación es robusta.** Tres ejecuciones, tres ramas sociales distintas sobre el mismo núcleo físico. El motor produce futuros alternativos, no la misma historia repetida.
4. **El modo ligero tiene un techo claro.** C agotó el límite de 5 horas de la cuenta a mitad de ejecución. Para más de una ejecución seguida o para tramos largos hace falta el modo intensivo con API propia.
