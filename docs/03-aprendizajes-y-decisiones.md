# Aftermath Studio — Aprendizajes de las primeras pruebas y decisiones

12 de noviembre de 2026 · Fran Barbero

Este documento recoge lo aprendido en las dos primeras ejecuciones del escenario ultravioleta, el análisis de dos revisiones externas del proyecto y las decisiones que salen de ambas. Los cambios marcados como "ahora" se aplicaron en el esquema v0.2.

## 1. Qué mostraron las dos ejecuciones

Detalle completo en [`simulaciones/vision-ultravioleta/comparativa-1422-1800.md`](../simulaciones/vision-ultravioleta/comparativa-1422-1800.md).

| | A · 2026-11-12-1422 (árbitro permisivo) | B · 2026-11-12-1800 (árbitro estricto) |
| --- | --- | --- |
| Afirmaciones de los agentes | 119 | 118 |
| Entran en el canon | 118 (99 %) | 88 (75 %) |
| Hechos en el canon por tramo | 23–27 | 10 |
| Descartadas por el árbitro | 1 | 30 |
| Referencias entre agentes | 39 | 50 |
| Métricas en la hora 5 | alarma 3 · comunicación · económico 2 · adaptación 3 | idénticas |
| Coste aproximado | 3,3 M tokens de subagentes | similar |

Conclusiones:

1. **La exigencia de mecanismo funciona.** Las afirmaciones son concretas y verificables y evitan la narrativa previsible.
2. **Se repite la física y se ramifica la sociedad.** Lo que depende del ojo y la luz aparece igual en las dos ejecuciones; lo que depende de decisiones humanas sigue caminos distintos. A fue una historia geográfica y de consumo; B, una historia política y de confianza. Hay ramificación real.
3. **El árbitro permisivo no filtra.** Con un máximo de 10 hechos por tramo y criterios de descarte, el canon es legible y los agentes se citan más entre sí. Se queda.
4. **Sesgo hacia la calma.** En ninguna de las dos ejecuciones hay emergencia en ningún país. Como persiste con los dos árbitros, el sesgo está en los agentes: ninguno gana nada con que la crisis escale.
5. **Las métricas no distinguen ramas.** Dos historias muy distintas terminan con métricas idénticas. El árbitro las puntúa de pasada, sin criterios por nivel.
6. **Aislamiento por instrucción.** Cada subagente lee su ficha de un archivo con la orden de no abrir otros; no hay aislamiento técnico.

## 2. Revisiones externas

Se pidió a otro asistente de IA un análisis sin complacencia del briefing y del esquema, sin decirle quién era el autor. Las dos revisiones fueron útiles y coincidían en lo esencial: la separación entre el configurador y el motor y el esquema declarativo son las decisiones clave del proyecto. Su sesgo común: resolver cada problema añadiendo infraestructura (motor determinista, base vectorial, grafo causal), algo que no corresponde a esta fase ni a un fundador en solitario. Ninguna de las dos tenía acceso a los resultados de las ejecuciones, ni entró en la cuestión de quién paga y por qué.

### Propuestas y decisión

| Propuesta | Decisión | Motivo |
| --- | --- | --- |
| Separar el árbitro (qué ocurre) del evaluador de métricas | **Ahora** | Ataca las métricas planas: un evaluador aparte, con criterios por nivel, puntúa con atención y de forma comparable |
| Incentivos de los agentes | **Ahora** (`incentivos`) | Causa probable del sesgo hacia la calma: nadie gana con que escale |
| Restricciones de los agentes | **Ahora** (`restricciones`) | Más realismo sin coste |
| Actores con intereses, no solo expertos que opinan | **Ahora** (tipo `actor`) | Un agente que actúa en el mundo, guiado por sus incentivos |
| Registrar proveedor, modelo, versión y parámetros en cada ejecución | **Ahora** | La semilla no garantiza reproducibilidad |
| `fuente: externa` en los supuestos, con referencia | **Ahora** | Distinguir hipótesis del usuario, decisiones del configurador y hechos documentados |
| Nivel de evidencia en cada afirmación | **Ahora**, simplificado (`dato`, `inferencia`, `especulacion`) | Base para que el árbitro no admita cifras inventadas |
| Que los agentes no conviertan cifras inventadas en hechos | **Ahora**: regla del árbitro | Una cifra sin fuente no entra en el canon como hecho |
| Análisis de sensibilidad y robustez | **Ahora como método** | La comparativa A/B ya lo es; el informe separará lo que se repite entre ejecuciones de lo que aparece en una sola |
| Métricas diseñadas para distinguir configuraciones | **Ahora** | Nuevas métricas con descripción de cada nivel |
| Visibilidad selectiva por rol | **Después**, con el primer vertical de negocio | Imprescindible en negociaciones y crisis corporativas; en escenarios de mundo público aporta poco |
| Relaciones y recursos de los agentes | **Después**, con la visibilidad selectiva | Van juntos |
| Versionado formal del canon | **Después**, con las ramas contrafactuales | Cada rama apuntará al tramo del canon del que nace |
| JSON Schema de validación | **Después**, con el motor MCP | En la skill, el script de validación cumple esa función |
| Debate formal entre agentes antes del árbitro | **Después**, como experimento | Duplica el coste por tramo; probar solo si la ramificación cae |
| Ejecución adaptativa (modelos pequeños para tareas simples, no llamar agentes que no aportan) | **Después**, con el modo intensivo | Tiene sentido cuando se paga por token |
| Variables continuas | **No** | Un modelo de lenguaje no distingue en la práctica entre 37 y 41; los niveles discretos descritos funcionan mejor |
| Intervalos y distribuciones de incertidumbre | **No** | Excesivo; basta con confianza y tipo de evidencia |
| Motor determinista y modelo causal cuantitativo | **No en el motor genérico** | Solo tendría sentido dentro de un vertical concreto con datos reales |
| Memoria con base relacional, vectorial y grafo | **No por ahora** | Con la escala actual, los archivos bastan; el motor MCP usará SQLite con registro de eventos |

## 3. Cambios aplicados en el esquema v0.2

- `version_esquema: "0.2"`.
- `evento.supuestos[].fuente` admite `externa`, con un campo `referencia` opcional.
- `agentes[].tipo` admite `actor`: no analiza desde fuera, actúa en el mundo según sus incentivos.
- `agentes[].incentivos` y `agentes[].restricciones`, opcionales.
- Cada afirmación lleva `evidencia: dato | inferencia | especulacion`.
- El árbitro ya no puntúa métricas. Regla fija: una cifra sin fuente no entra en el canon como hecho.
- Nuevo paso de **evaluador** por tramo: puntúa cada métrica con su justificación y los hechos que la apoyan, en `metricas/<tramo>.yaml`.
- `resultados.metricas[].niveles`: descripción de cada valor de la escala o de cada opción categórica.
- El registro de la ejecución anota proveedor, modelo y parámetros.

En el escenario ultravioleta (versión 5):

- Todos los agentes activos tienen `incentivos` y `restricciones`.
- Nuevo agente `agitador`, de tipo `actor`: creador de contenido que gana audiencia con el miedo y la desconfianza.
- Métricas rediseñadas con niveles: alarma social, confianza institucional, respuesta de los gobiernos (con una opción nueva, `medidas_sectoriales`), impacto económico y adaptación.

## 4. Tercera ejecución con el esquema v0.2 (13/11/2026)

Detalle en [`simulaciones/vision-ultravioleta/comparativa-tres-ejecuciones.md`](../simulaciones/vision-ultravioleta/comparativa-tres-ejecuciones.md) y en el informe de `2026-11-12-2126`.

- **El agitador funciona.** Coloca 13 de 20 afirmaciones y marca el rumbo: la historia pasa a ser la del daño causado por la conducta (lámparas UV-C, retinopatía, abandono del protector), explotado como prueba de que "algo nos han hecho". Aparece la primera tensión institucional real: un recuento oficial frente a uno sin verificar.
- **La respuesta de los gobiernos se mueve por primera vez**, de comunicación a medidas sectoriales.
- **La alarma y la confianza siguen planas** (3 durante cinco horas). Causa identificada en el propio motor: la regla del evaluador "ante la duda entre dos niveles, el inferior" empuja hacia la calma.
- **Tres ramas distintas sobre un núcleo físico estable:** la ramificación es robusta.
- **Coste:** unos 4,1 millones de tokens de subagentes; la ejecución agotó el límite de uso de 5 horas de la cuenta y se reanudó al día siguiente. El modo ligero solo sirve para pruebas reducidas.

## 5. Pendientes

- ~~Evaluador: sustituir la regla "ante la duda, el inferior" por "el nivel más cercano, justificado", y añadir métricas de dinámica.~~ Aplicado el 13/11/2026 (ver sección 6).
- ~~Cuarta ejecución con el escenario v6 para comprobar si las métricas captan ya la tensión.~~ Hecha el 13/11/2026 (ver sección 7).
- Volver a evaluar el canon de la tercera ejecución con la regla nueva (4 llamadas) para separar el efecto de la regla del de la historia.
- Tramos más largos (día 1, día 3, semana 1) para ver si la alarma escala; requiere el modo intensivo.
- Probar la variable `explicacion_publica: conspirativa` o mezclar modelos.
- Modos de seguimiento (entrevista, zoom y rama).
- Motor MCP y modo intensivo.

## 6. Cambios aplicados tras la tercera ejecución (13/11/2026)

- **Regla del evaluador.** Antes: "si el mundo está entre dos niveles, elige el inferior". Ahora: "elige el más cercano según los hechos, no el inferior ni el superior por prudencia, y di qué falta para alcanzar el siguiente". Motivo: la regla anterior empujaba de forma sistemática hacia la calma; en la tercera ejecución la alarma quedó en 3 estando, según el propio evaluador, "entre 3 y 4". Aplicado en `herramientas/orquestador.py` y en la skill.
- **Métrica `relatos_en_competencia`** (escala de 1 a 5, con niveles descritos). Mide el grado de enfrentamiento entre relatos sobre lo que está pasando: de un relato compartido (1) a una fractura en la que grupos amplios viven en relatos incompatibles (5). Motivo: en la tercera ejecución lo que de verdad cambió fue la competencia entre el recuento oficial y el del agitador, y ninguna métrica lo registraba. Se añade al escenario ultravioleta, que pasa a la versión 6, y se recomienda para cualquier escenario de crisis.

## 7. Cuarta ejecución con el escenario v6 (13/11/2026)

Detalle en [`simulaciones/vision-ultravioleta/comparativa-cuatro-ejecuciones.md`](../simulaciones/vision-ultravioleta/comparativa-cuatro-ejecuciones.md) y en el informe de `2026-11-13-1404`.

- **Las métricas de tensión se mueven por primera vez.** Relatos en competencia sube de 3 a 4 en la hora 5 (cifras incompatibles de heridos: hospitales y Gobierno atribuyen las quemaduras de córnea a las lámparas; el agitador y la prensa de clics, al fenómeno). La confianza institucional pasa de 2 a 3 y el impacto económico está en 3 desde la primera hora. La respuesta de los gobiernos vuelve a llegar a medidas sectoriales (alerta de Consumo sobre lámparas UV).
- **La alarma social sigue en 3**, con una justificación coherente con sus niveles: cambios de conducta visibles, sin acaparamiento, colapso ni protestas. Probablemente es el nivel correcto en cinco horas.
- **Cuarta rama social distinta:** lo que la piel escondía. Los moratones antiguos se ven y llegan consultas a protección de menores y a las líneas de violencia de género; tres ministerios aclaran que una marca vista solo en UV no es prueba. También aparece la inversión de autoridad por edad. El núcleo físico se mantiene.
- **Más interacción:** 82 referencias entre agentes (39, 50 y 64 en las anteriores). El agitador coloca 15 de 20 afirmaciones.
- **Cautela:** entre C y D cambian a la vez la regla y la historia; para aislar el efecto de la regla falta volver a evaluar el canon de C.
