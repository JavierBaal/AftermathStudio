# Comparativa de las dos primeras ejecuciones

Escenario `vision-ultravioleta` · prueba reducida (6 agentes, horas 1, 2, 3 y 5) · 12 de noviembre de 2026

- **Ejecución A** — `2026-11-12-1422` · escenario v3 · árbitro permisivo
- **Ejecución B** — `2026-11-12-1800` · escenario v4 · árbitro estricto (máximo 10 hechos por tramo, criterios de descarte)

Agentes, fichas y tramos idénticos. Las dos diferencias son el árbitro y el azar propio de cada ejecución.

## Conclusión

**Se repite la física y se ramifica la sociedad.** Lo que depende de cómo funciona el ojo y la luz aparece en las dos ejecuciones casi igual. Lo que depende de decisiones humanas (qué hacen los gobiernos, de qué sospecha la gente, qué sector se ve afectado) sigue caminos distintos. Es la señal que buscábamos: no hay una sola historia repetida, hay futuros ramificados sobre un núcleo estable.

**Pero las métricas son idénticas en las dos**, y en ninguna hay emergencia en ningún sitio. Ese sesgo hacia la calma, el "cliché inverso", no depende del árbitro: está en los agentes.

## Los números

| | A (permisivo) | B (estricto) |
| --- | --- | --- |
| Afirmaciones de los agentes | 119 | 118 |
| Entran en el canon | 118 (99 %) | 88 (75 %) |
| Hechos en el canon por tramo | 23–27 | 10 |
| Descartadas por el árbitro | 1 | 30 |
| Afirmaciones con fuente buscada | 52 | 56 |
| Referencias a otros agentes (`reacciona_a`) | 39 | 50 |
| Afirmaciones del disruptor en el canon | 19 de 19 | 14 de 19 |
| Métricas en la hora 5 | alarma 3 · comunicación · económico 2 · adaptación 3 | alarma 3 · comunicación · económico 2 · adaptación 3 |

El árbitro estricto filtra de verdad: el canon es menos de la mitad y casi uno de cada cuatro afirmaciones se queda fuera. Los hechos que entran son más largos porque combinan varias afirmaciones. Además, en B los agentes se citan más entre sí, probablemente porque un canon más corto deja más claro de qué hay que hablar.

## El núcleo estable (aparece en las dos)

- Las cámaras no captan el fenómeno, y eso alimenta los bulos y la disputa por las imágenes de falso color.
- Las gafas y lentillas con filtro UV lo apagan.
- La crema solar se ve como manchas oscuras, y se vuelven visibles las manchas y el daño solar de la piel.
- La edad cambia lo que se ve, por el cristalino; los operados de cataratas con lente con filtro ven menos y algunos piden cambiarla.
- La sombra protege poco porque el ultravioleta llega desde todo el cielo.
- Las fuentes artificiales de UV-A (matainsectos, lámparas de uñas, cabinas de bronceado) se vuelven visibles y molestas.
- El amanecer en Estados Unidos es un momento clave para creer o no.
- Los adolescentes rechazan las gafas; aparece un mercado de gafas que no protegen.
- Los colegios pasan el recreo a interiores.
- Los oftalmólogos se adelantan a los casos de queratitis, que tardan horas en dar síntomas.
- Los gobiernos comunican sin declarar emergencia y los mercados no se hunden.

## Las ramas (solo en una)

| Solo en A | Solo en B |
| --- | --- |
| Brecha norte-sur dentro de Europa y escepticismo nórdico | Evaluaciones secretas de defensa y teoría de la ocultación |
| El índice UV oficial refuerza a los escépticos | Sesiones a puerta cerrada en Madrid y Washington |
| Turismo nórdico de última hora a Canarias y el Mediterráneo | El agravio de los operados con filtro se organiza, se mezcla con la conspiración y Sanidad advierte contra el turismo quirúrgico |
| Billetes auténticos rechazados en los mercados | El cristal de las ventanas no protege y se dispara la lámina anti-UV |
| Parada de las inspecciones aeronáuticas, EASA y la FAA | Comité de Seguridad Sanitaria y primer mensaje común de la UE |
| Luz negra en colchones y hoteles como prueba | Rumor asiático de que "ya se ha ido" |
| Restauraciones no declaradas en la segunda mano | Conflicto laboral por los trabajadores al aire libre |
| Estigma sobre vitíligo y melasma | |

La diferencia de fondo: A es una historia **geográfica y de consumo** (dónde se ve, qué se compra, qué se rechaza), y B es una historia **política y de confianza** (quién sabía qué, quién queda fuera de la sala).

## Qué aprendemos para el motor

1. **El árbitro estricto se queda.** Un canon de 10 hechos por tramo es legible y obliga a priorizar sin perder los efectos cruzados.
2. **Hay ramificación real.** Con una sola variable cambiada salen dos futuros distintos y coherentes. Hace falta una tercera ejecución con el mismo árbitro para separar cuánto se debe al árbitro y cuánto al azar.
3. **El sesgo hacia la calma persiste.** Las dos ejecuciones terminan con métricas idénticas y ningún gobierno en emergencia. Se puede atacar con las variables del escenario (`explicacion_publica: conspirativa`, `permanencia_percibida`), con agentes de perfil más extremo, por ejemplo un gobierno autoritario o un movimiento religioso, o mezclando modelos distintos.
4. **Las métricas no sirven en ventanas cortas.** Son idénticas en dos historias muy diferentes. Hay que replantearlas: puntuar por región, o medir cosas que sí distinguen ramas, como el grado de confianza en las instituciones.
5. **Coste similar.** Unos 3,3 millones de tokens de subagentes por ejecución en las dos.
