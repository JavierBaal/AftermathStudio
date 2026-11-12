# Aftermath Studio — Briefing inicial

11 de noviembre de 2026 · Fran Barbero

Documento vivo (versión editable con diagrama): https://claude.ai/artifact/Cvp5vXqY3DoVUCAbsNCusS

## Qué es Aftermath Studio

Aftermath Studio es un motor agnóstico de simulación de escenarios con agentes de IA: varios agentes con roles distintos simulan un suceso, el sistema consolida lo que ocurre y el usuario puede seguir explorando ese mundo después.

Empieza como un experimento con escenarios especulativos y está pensado para servir de base a usos profesionales de prospectiva y simulación.

**Origen.** Es una idea que Fran intentó construir con los primeros modelos de GPT-3 y no funcionó: contexto corto, sin búsquedas, sin herramientas y poca coherencia en textos largos.

**Por qué ahora.** Esos cuatro límites están resueltos. Hoy hay contexto largo, búsqueda web, subagentes con contexto propio y modelos capaces de sostener una cronología de un año sin contradecirse.

## El experimento inicial

El primer caso de prueba es un escenario especulativo: **¿qué ocurriría si mañana martes, a las 10:00 en punto, todos los seres humanos desarrollaran la capacidad de ver el espectro ultravioleta?**

Un consejo de expertos analiza el suceso desde su área, con acceso a búsquedas para anclar sus pronósticos en datos:

- Expertos: economista, sociólogo, psicólogo, psiquiatra, político y otras áreas clave de la sociedad.
- Agentes de a pie: personas corrientes de perfiles distintos (por ejemplo, un agricultor, una adolescente, una persona mayor) que aportan los efectos que los expertos no ven.
- Disruptor: un agente cuyo trabajo es proponer lo que nadie ha previsto.
- Árbitro: consolida el estado del mundo en cada tramo y redacta el informe final.

La cronología avanza por tramos: hora 1, hora 2, hora 3, hora 5, primera semana, segunda semana, primer mes, 2 meses, 6 meses y 1 año después del evento.

El resultado es un informe final que explica qué le ocurre a la sociedad en ese escenario.

## Principios de diseño de la simulación

La regla central: los agentes no escriben en silos. Una cronología completa por experto, juntada al final, son ensayos paralelos; los efectos interesantes son los cruzados entre áreas.

1. **Rondas sincronizadas.** Todos los agentes pronostican el mismo tramo (hora 1). El árbitro consolida un estado del mundo de ese tramo y resuelve contradicciones. El siguiente tramo parte de ese estado compartido.
2. **Mecanismos y datos, no clichés.** Cada afirmación necesita un mecanismo (por qué ocurre) y, cuando se pueda, un dato buscado. Sin esto, los modelos caen en la narrativa esperada: pánico, caída de mercados, adaptación, nueva normalidad.
3. **Disruptor.** Un agente dedicado a romper la narrativa previsible.
4. **Agentes de a pie.** La vista de la calle completa la vista de los expertos.
5. **Roles aislados.** Cada agente se ejecuta con su propio contexto (subagente), para que no se contaminen entre sí ni converjan.
6. **Repetición y futuros ramificados.** Ejecutar el mismo escenario varias veces, con variaciones, produce futuros alternativos en lugar de uno solo. El uso es comparativo y exploratorio: comparar estrategias y descubrir escenarios, no dar probabilidades exactas.

## Exploración posterior: un mundo persistente

Tras el informe, la simulación no se archiva: el usuario sigue explorando el mismo mundo.

**La biblia del escenario.** La simulación principal deja un canon: el estado del mundo en cada tramo, los hechos establecidos y lo que sabe cada agente. Toda exploración posterior parte de ese canon. Si lo contradice, es una rama y se marca como tal.

Tres modos de seguimiento:

- **Entrevistar a un agente.** Conversar con el psicólogo o el economista, que conservan la memoria de la simulación.
- **Zoom temático.** Una pregunta sobre una dimensión concreta lanza una sub-simulación y recluta especialistas nuevos. Ejemplo: para la nutrición, un nutricionista, un agricultor, la industria alimentaria, un chef y marketing de producto.
- **Rama contrafactual.** Bifurcar la línea temporal desde un punto ("¿y si los gobiernos hubieran declarado la emergencia en la hora 3?") y compararla con la original.

Ejemplos de zoom en el escenario ultravioleta:

- **Relaciones interpersonales.** En ultravioleta, las manchas y el daño solar de la piel se vuelven visibles, y la crema solar se ve oscura. Afecta a cánones de belleza, atracción, cosmética y autoimagen.
- **Nutrición.** Las señales visuales de frescura, madurez y apetito cambian, y la industria tendría que rediseñar envases, iluminación y presentación.

## Arquitectura

La pieza que hace el motor agnóstico es un **esquema de escenario declarativo**: un formato estándar que describe cualquier simulación. El configurador solo tiene que rellenarlo, y el motor solo tiene que ejecutarlo.

Flujo (el diagrama está en la versión viva del documento):

1. **Usuario** → describe el escenario.
2. **Configurador (Claude)** → entrevista, propone supuestos y genera el **esquema del escenario** (agentes, tramos, variables).
3. **Motor de simulación** (modo ligero: subagentes en Claude · modo intensivo: API del usuario), en bucle por tramos:
   - **Agentes en ronda** (expertos, a pie, disruptor; subagentes aislados) → **Árbitro** (consolida el tramo, resuelve contradicciones) → **Estado del mundo** (hechos del tramo N, punto de partida del N+1) → siguiente tramo.
4. El motor guarda todo en la **biblia del escenario** (canon de hechos por tramo, memoria de cada agente).
5. **Análisis e informe (Claude)** → agrega y redacta el informe; estadísticas si hay tandas.
6. **Seguimiento** (entrevistar, zoom, rama; siempre desde el canon) → relanza el motor cuando hace falta.

Claude se encarga de configurar y analizar; el motor ejecuta.

## Ejecución híbrida y modelos

Claude es el asistente principal; la inferencia masiva la pagan los usuarios con su propia API.

| Modo | Cuándo | Cómo funciona | Coste para Aftermath |
| --- | --- | --- | --- |
| Ligero | Una simulación o pocas decenas | Dentro de Claude, con la suscripción del usuario: conector MCP (mismo patrón que Four Hands Studio) y roles como subagentes | Cero |
| Intensivo | Cientos de ejecuciones | Claude lanza la tanda; el motor MCP llama en segundo plano a la API que configura el usuario y devuelve estadísticas agregadas | Cero |

**Proveedores.** Cada usuario configura el suyo según rigor y privacidad: modelo local (Ollama, LM Studio), OpenRouter o DeepSeek directo. Los tres son compatibles con el formato de API de OpenAI: URL base, API key y modelo.

**Decisión para las pruebas:** API de DeepSeek directa, solo con escenarios ficticios o anonimizados.

**Detalles previstos en el motor:**

- Modelo asignable por agente y por árbitro, para ganar diversidad.
- Registro de tokens y coste por ejecución, con estimación antes de lanzar una tanda.
- Cola con paralelismo configurable y reintentos ante límites del proveedor.
- Cada resultado guarda la versión del escenario y los modelos usados.

**Normas de Anthropic.** No se permite que una app propia ofrezca el inicio de sesión de Claude.ai ni use las credenciales de suscripción de sus usuarios. Sí se permite un conector MCP o plugin usado dentro de las apps oficiales con la cuenta del propio usuario, y el uso con la API key del usuario. Los planes Max, Ultra y Team incluyen créditos mensuales de API desde octubre de 2026. Fuentes: [Legal and compliance – Claude Code](https://code.claude.com/docs/en/legal-and-compliance) · [Agent SDK con tu plan – Claude Help Center](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)

## Riesgos conocidos

| Riesgo | En qué consiste | Mitigación |
| --- | --- | --- |
| Calibración | Que el 62 % de las ejecuciones dé un resultado no significa que su probabilidad real sea del 62 % | Uso comparativo y exploratorio; backtesting si algún día se venden predicciones |
| Homogeneidad | Agentes del mismo modelo convergen y dan poca varianza | Perfiles muy marcados, temperatura, variación de parámetros y mezcla de modelos |
| Cliché plausible | Narrativas genéricas y previsibles | Exigir mecanismo y dato por afirmación; agente disruptor |
| Contaminación de roles | En un solo contexto, cada rol ve lo que saben los demás | Subagentes aislados |
| Coste | Cientos de miles de tokens por ejecución multiagente | Modelos baratos para los roles; API del usuario en modo intensivo |
| Privacidad | DeepSeek procesa datos en China; inaceptable para clientes europeos con datos confidenciales | Proveedor elegido por el usuario; local o modelos alojados en la UE |
| Calidad del escenario | Un escenario mal planteado da resultados creíbles pero inútiles | Configurador exigente que muestra sus supuestos |

## Usos de negocio potenciales

El motor es agnóstico, pero la salida al mercado debe ser por un caso concreto: nadie compra "simular cualquier cosa".

- **Prospectiva estratégica (scenario planning).** Disciplina establecida en empresas, aseguradoras y administraciones: "qué pasa si se aprueba esta ley", "si el petróleo sube un 40 %".
- **Comunicación de crisis.** Comparar cómo reaccionan prensa, redes, empleados y regulador ante distintas versiones de un comunicado.
- **Ejercicios de incidentes (tabletop).** Ciberataques o caídas con roles de dirección, IT, legal y comunicación. DORA y NIS2 obligan a probar la respuesta a incidentes.
- **Negociaciones con varias partes.** Convenios colectivos, compras grandes, reparto de sociedades.
- **Licitaciones públicas.** Competidores y mesa de contratación simulados; las adjudicaciones públicas permiten algo de validación.
- **Estrategia competitiva (wargaming).** Movimientos propios y respuestas de competidores.
- **Contenido.** Una serie pública "¿Qué pasaría si...?" para probar el motor y construir audiencia.
- **Worldbuilding** para escritores de ciencia ficción.

Descartado por ahora: el simulador de juicios, demasiado complejo para un fundador en solitario por la validación y el riesgo regulatorio.

## Nombre y marca

Nombre elegido: **Aftermath Studio**. "Aftermath" significa "las consecuencias", que es exactamente lo que simula; "Studio" crea familia con Four Hands Studio.

- **Descartado: Sandtable.** Dos empresas con ese nombre ya operan en simulación con IA: una startup de defensa estadounidense de wargaming con contratos del Ejército y otra que simula comportamiento humano con poblaciones virtuales.
- **Sin choque en la categoría.** Los "Aftermath" existentes son de videojuegos, medios y música (incluido el sello Aftermath Entertainment), no de simulación ni IA.
- **Pega:** la palabra está muy transitada en buscadores. Usar siempre el nombre completo con descriptor: "Aftermath Studio — simulación de escenarios con IA".
- **Pendiente:** comprobar dominios (aftermath.studio, aftermathstudio.ai, aftermathstudio.com) y marca en la EUIPO, clases 9 y 42.

Fuentes: [Tectonic – Sandtable](https://www.tectonicdefense.com/?p=24023) · [Crunchbase – Sandtable](https://www.crunchbase.com/organization/sandtable)

## Hoja de ruta y próximos pasos

1. **Esquema del escenario.** Definir el formato declarativo: agentes, roles, información privada, tramos de la cronología, reglas de interacción, variables y definición de resultados. Es la pieza que hace todo agnóstico.
2. **Prototipo como skill.** Escenario ultravioleta con rondas sincronizadas, subagentes aislados, árbitro y biblia del escenario guardada en archivo. Sin código: valida si los resultados son útiles.
3. **Modos de seguimiento en la skill.** Entrevistar, zoom temático y rama contrafactual.
4. **Motor MCP.** Cuando la skill se quede corta: estado persistente, estadísticas fiables, relanzar variantes y modo intensivo con API del usuario (DeepSeek en pruebas).
5. **Primer vertical.** Elegir un caso de negocio concreto sobre el mismo motor.

- [ ] Comprobar dominios y marca de Aftermath Studio
- [ ] Redactar el esquema del escenario
- [ ] Montar la skill del escenario ultravioleta
