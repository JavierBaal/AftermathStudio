# Aftermath Studio — contexto para Claude

Proyecto de Fran Barbero: motor agnóstico de simulación de escenarios multiagente con IA.

- Idioma de trabajo: español de España.
- Antes de proponer cambios de diseño, lee `docs/01-briefing.md` y `docs/02-esquema-escenario.md`.
- El esquema del escenario es la pieza central: cualquier cambio en `esquema/plantilla-escenario.yaml` debe reflejarse en `docs/02-esquema-escenario.md` y en los escenarios de `escenarios/`.
- Principios que no se negocian: rondas sincronizadas con estado del mundo compartido, cada afirmación con mecanismo, roles aislados, supuestos explícitos.
- Nada de usar credenciales de suscripción de Claude fuera de las apps oficiales: modo ligero vía MCP dentro de Claude, modo intensivo con API key del usuario.
- Pruebas con DeepSeek solo con escenarios ficticios o anonimizados.
