# Aftermath Studio

**Simulación de escenarios con IA.**

Aftermath Studio es un motor agnóstico de simulación de escenarios con agentes de IA: varios agentes con roles distintos simulan un suceso por tramos de tiempo, un árbitro consolida lo que ocurre y el usuario puede seguir explorando ese mundo después (entrevistar a un agente, hacer zoom en un tema o abrir una rama contrafactual).

Estado: **prototipo**. La skill `aftermath-simular` ejecuta un escenario dentro de Claude con subagentes aislados. Dos ejecuciones de prueba del escenario ultravioleta completadas; esquema en v0.2. Aún sin repeticiones automáticas ni modos de seguimiento.

## Estructura del repositorio

```
docs/
  01-briefing.md              Concepto, arquitectura, riesgos, negocio y hoja de ruta
  02-esquema-escenario.md     El formato declarativo que describe cualquier simulación
  03-aprendizajes-y-decisiones.md   Lo aprendido en las pruebas y en las revisiones externas, y qué se decidió
esquema/
  plantilla-escenario.yaml    Plantilla genérica del esquema (v0.2)
escenarios/
  vision-ultravioleta/
    escenario.yaml            Primer caso de prueba
herramientas/
  orquestador.py              Prepara fichas, valida salidas y actualiza la memoria en el modo ligero
skills/
  aftermath-simular/
    SKILL.md                  Skill que ejecuta un escenario en modo ligero dentro de Claude
simulaciones/                 Biblias de las ejecuciones, informes y comparativas
```

## Hoja de ruta

1. Esquema del escenario — v0.2.
2. Prototipo como skill con el escenario ultravioleta — dos ejecuciones completadas; siguiente: tercera ejecución con el esquema v0.2.
3. Modos de seguimiento en la skill: entrevistar, zoom y rama.
4. Motor MCP: estado persistente, estadísticas y modo intensivo con API del usuario.
5. Primer vertical de negocio sobre el mismo motor.
