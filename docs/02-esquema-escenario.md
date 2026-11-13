# Aftermath Studio — Esquema del escenario v0.2

12 de noviembre de 2026 · Fran Barbero

Documento vivo de la v0.1: https://claude.ai/artifact/DetSZyD3cQea6c3j9XhYrc

El esquema es un archivo YAML que describe una simulación completa: el configurador lo genera entrevistando al usuario, el motor lo ejecuta sin saber nada del tema y la biblia del escenario guarda todo lo que produce.

- Plantilla completa: [`esquema/plantilla-escenario.yaml`](../esquema/plantilla-escenario.yaml)
- Ejemplo real: [`escenarios/vision-ultravioleta/escenario.yaml`](../escenarios/vision-ultravioleta/escenario.yaml)
- Por qué cambió de la v0.1 a la v0.2: [`docs/03-aprendizajes-y-decisiones.md`](03-aprendizajes-y-decisiones.md)

## Los bloques del esquema

Diez bloques cubren cualquier simulación. Los cuatro primeros describen el mundo; los seis siguientes, cómo se ejecuta y qué se obtiene.

| Bloque | Qué describe | Quién lo usa |
| --- | --- | --- |
| `meta` | Identidad: título, tipo (especulativo o negocio), idioma, versión | Todos |
| `evento` | La premisa, el momento cero, el alcance y los supuestos que se dan por fijos, con su procedencia | Configurador, agentes, árbitro |
| `cronologia` | Los tramos en los que avanza la simulación | Motor |
| `agentes` | Cada rol: tipo, perfil, objetivos, incentivos, restricciones, conocimiento privado, herramientas y modelo | Motor, agentes |
| `arbitro` | Cómo consolida cada tramo, resuelve contradicciones y cuántos hechos admite como máximo por tramo | Árbitro |
| `interaccion` | Qué ve cada agente de los demás y qué exige cada afirmación | Motor, agentes |
| `variables` | Lo que cambia entre repeticiones para obtener futuros distintos | Motor |
| `ejecucion` | Repeticiones, semilla, modo (ligero o intensivo), proveedor por defecto y, opcionalmente, un subconjunto de agentes y tramos para pruebas | Motor |
| `resultados` | Métricas con la descripción de cada nivel, quién las evalúa y estructura del informe | Evaluador, análisis |
| `seguimiento` | Qué se guarda en la biblia y qué modos de exploración se permiten | Motor, Claude |

Reglas del formato:

- **Todo supuesto es explícito y tiene procedencia.** `usuario` si lo dijo el usuario, `configurador` si lo decidió la IA y está pendiente de confirmar, `externa` si sale de una fuente documentada, con su `referencia`.
- **El motor no interpreta el tema.** Solo lee bloques, lanza agentes y guarda salidas. Todo el conocimiento del escenario está en el archivo.
- **Cuatro tipos de agente.** `experto` analiza desde su área; `a_pie` vive el suceso en primera persona; `disruptor` busca lo que nadie ha previsto; `actor` actúa en el mundo guiado por sus incentivos. Los `incentivos` (qué gana o pierde cada uno) son la principal herramienta contra el sesgo hacia la calma.
- **Narrar y medir son tareas distintas.** El árbitro decide qué ocurre; un evaluador aparte puntúa las métricas con la descripción de cada nivel.
- **Una cifra sin fuente no entra en el canon como hecho.**

## Contratos de salida

Agentes, árbitro y evaluador responden siempre con la misma estructura. Así el motor puede guardar, comparar y contar sin entender el contenido.

**Intervención de un agente en un tramo.** Cada afirmación lleva su mecanismo, su dato si lo hay, su grado de confianza y su tipo de evidencia:

```yaml
intervencion:
  agente: economista
  tramo: h1
  afirmaciones:
    - texto: "Las bolsas suspenden la cotización en las primeras horas"
      mecanismo: "Los reguladores activan los cortacircuitos ante caídas bruscas por incertidumbre"
      dato: "Descripción del mecanismo de suspensión del mercado en cuestión"
      fuente: "URL consultada"        # vacío si no hay dato buscado
      confianza: media               # baja | media | alta
      evidencia: dato                # dato | inferencia | especulacion
      areas_afectadas: [finanzas, politica]
  reacciona_a: [politico/h1/2]       # afirmaciones de otros agentes que tiene en cuenta
```

**Estado del mundo al cerrar un tramo.** Lo redacta el árbitro y es el punto de partida del tramo siguiente:

```yaml
estado_del_mundo:
  tramo: h1
  resumen: "Tres o cuatro frases que cualquier agente pueda leer"
  hechos_establecidos:               # canon: lo que ya no se puede contradecir
    - id: h1-01
      texto: "..."
      origen: [psicologo/h1/1, sociologo/h1/3]
  tensiones_abiertas: ["..."]        # lo que el siguiente tramo debe resolver
  contradicciones_resueltas:
    - entre: [economista/h1/2, politico/h1/1]
      decision: "..."
      motivo: "..."
  descartadas:                       # afirmaciones que no entran en el canon
    - id: medios/h1/4
      motivo: "Cifra sin fuente"
```

**Evaluación de las métricas de un tramo.** La redacta el evaluador a partir del estado del mundo, con los niveles definidos en `resultados.metricas`:

```yaml
evaluacion:
  tramo: h1
  metricas:
    - id: alarma_social
      valor: 3
      justificacion: "Por qué este nivel y no el anterior o el siguiente"
      apoyos: [h1-02, h1-05]         # hechos del canon que lo sostienen
```

Los identificadores del tipo `agente/tramo/número` y `tramo-NN` permiten rastrear cualquier hecho o puntuación del informe hasta la intervención que lo originó.

## Historial

- **v0.2, revisión del 13/11/2026.** Sin cambios de formato. El evaluador ya no elige el nivel inferior cuando duda entre dos: elige el más cercano según los hechos y explica qué falta para el siguiente. Nueva métrica recomendada para escenarios de crisis: `relatos_en_competencia`. Motivos en [`docs/03-aprendizajes-y-decisiones.md`](03-aprendizajes-y-decisiones.md).
- **v0.2 (12/11/2026).** Procedencia `externa` en supuestos; tipo de agente `actor`; `incentivos` y `restricciones`; tipo de evidencia por afirmación; regla de cifras sin fuente; evaluador separado del árbitro; niveles descritos en las métricas; registro de modelos por ejecución. Motivos en [`docs/03-aprendizajes-y-decisiones.md`](03-aprendizajes-y-decisiones.md).
- **v0.1 (12/11/2026).** Primera versión. Se añadieron después `ejecucion.agentes`, `ejecucion.tramos` y `arbitro.max_hechos_por_tramo`. Decisiones cerradas antes de la skill: supuestos del ultravioleta confirmados, visibilidad `estado_e_intervenciones`, primera prueba con 6 agentes y 4 tramos, YAML como formato y cuatro métricas iniciales.
