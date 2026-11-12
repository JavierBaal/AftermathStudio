# Aftermath Studio

**Simulación de escenarios con IA.**

Aftermath Studio es un motor agnóstico de simulación de escenarios con agentes de IA: varios agentes con roles distintos simulan un suceso por tramos de tiempo, un árbitro consolida lo que ocurre y el usuario puede seguir explorando ese mundo después (entrevistar a un agente, hacer zoom en un tema o abrir una rama contrafactual).

Estado: **diseño**. Todavía no hay código; el primer prototipo será una skill de Claude con el escenario del ultravioleta.

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
```

## Hoja de ruta

1. Esquema del escenario — v0.1 redactado, con decisiones abiertas.
2. Prototipo como skill con el escenario ultravioleta.
3. Modos de seguimiento en la skill: entrevistar, zoom y rama.
4. Motor MCP: estado persistente, estadísticas y modo intensivo con API del usuario.
5. Primer vertical de negocio sobre el mismo motor.
