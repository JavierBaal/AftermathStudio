# Aftermath Studio

**Simulación de escenarios con IA.**

Aftermath Studio es un motor agnóstico de simulación de escenarios con agentes de IA: varios agentes con roles distintos simulan un suceso por tramos de tiempo, un árbitro consolida lo que ocurre y el usuario puede seguir explorando ese mundo después (entrevistar a un agente, hacer zoom en un tema o abrir una rama contrafactual).

Estado: **prototipo**. La skill `aftermath-simular` ejecuta un escenario dentro de Claude con subagentes aislados; aún sin repeticiones ni modos de seguimiento.

## Estructura del repositorio

```
docs/
  01-briefing.md              Concepto, arquitectura, riesgos, negocio y hoja de ruta
  02-esquema-escenario.md     El formato declarativo que describe cualquier simulación
esquema/
  plantilla-escenario.yaml    Plantilla genérica del esquema (v0.1)
escenarios/
  vision-ultravioleta/
    escenario.yaml            Primer caso de prueba
skills/
  aftermath-simular/
    SKILL.md                  Skill que ejecuta un escenario en modo ligero dentro de Claude
simulaciones/                 Biblias de las ejecuciones (se crea al simular)
```

## Hoja de ruta

1. Esquema del escenario — v0.1 cerrado.
2. Prototipo como skill con el escenario ultravioleta — skill v0.1 lista, pendiente de la primera prueba.
3. Modos de seguimiento en la skill: entrevistar, zoom y rama.
4. Motor MCP: estado persistente, estadísticas y modo intensivo con API del usuario.
5. Primer vertical de negocio sobre el mismo motor.
