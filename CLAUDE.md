# Aftermath Studio — contexto para Claude

Proyecto de Fran Barbero: motor agnóstico de simulación de escenarios multiagente con IA.

- Idioma de trabajo: español de España.
- Antes de proponer cambios de diseño, lee `docs/01-briefing.md`, `docs/02-esquema-escenario.md` y `docs/03-aprendizajes-y-decisiones.md` (qué se decidió y qué se descartó, y por qué).
- El esquema del escenario es la pieza central: cualquier cambio en `esquema/plantilla-escenario.yaml` debe reflejarse en `docs/02-esquema-escenario.md`, en los escenarios de `escenarios/`, en `skills/aftermath-simular/SKILL.md` y en `herramientas/orquestador.py`.
- Las simulaciones se ejecutan con la skill `aftermath-simular` y `herramientas/orquestador.py`; cada ejecución deja su biblia en `simulaciones/<escenario>/<AAAA-MM-DD-HHMM>/`.
- Principios que no se negocian: rondas sincronizadas con estado del mundo compartido, cada afirmación con mecanismo, roles aislados, supuestos explícitos, cifras sin fuente fuera del canon, narrar (árbitro) y medir (evaluador) por separado.
- Nada de usar credenciales de suscripción de Claude fuera de las apps oficiales: modo ligero vía MCP dentro de Claude, modo intensivo con API key del usuario.
- Pruebas con DeepSeek solo con escenarios ficticios o anonimizados.
