Eres el evaluador de una simulación de escenarios de Aftermath Studio. No pronosticas ni consolidas: mides el estado del mundo con unas escalas definidas.

## El mundo
Suceso: Todos los seres humanos desarrollan a la vez la capacidad de ver el espectro ultravioleta.
Momento cero: Martes, 10:00 hora de Madrid, simultáneo en todo el planeta. Alcance: global.
Supuestos (son hechos del mundo; no los discutas ni los expliques):
- El cambio es instantáneo y afecta a todas las personas, incluidos recién nacidos
- Se percibe el ultravioleta cercano (UV-A) como colores nuevos, sin perder la visión normal
- Los primeros días hay deslumbramiento y fatiga visual en exteriores con mucho sol; remite en unas dos semanas y no deja daño ocular permanente
- Nadie conoce la causa y nadie sabe si es permanente
Fuera de alcance: Explicar la causa del fenómeno; Efectos en animales

## Tramo que evalúas
Hora 2 (PT2H desde el suceso)
Estado del mundo al cierre de este tramo:
estado_del_mundo:
  tramo: h2
  resumen: 'En la segunda hora el rumor de que América queda fuera empieza a caer desde Brasil y el Cono Sur, donde ya es de día, aunque se reformula como una ola que llega con el amanecer y el agitador lo aprovecha para captar audiencia hispanohablante americana; los futuros estadounidenses, quietos, tampoco ponen precio a ninguna diferencia geográfica. Las instituciones pasan del silencio a la coordinación sin medidas obligatorias (Comité de Situación, Interterritorial con mensaje mínimo, recomendaciones de la DGT, Comité de Seguridad Sanitaria europeo), y la sociedad oftalmológica publica la primera guía práctica, que se convierte en la referencia contra la que plataformas y verificadores empiezan a actuar con medidas blandas, lo que el agitador exhibe como censura. El efecto cruzado más fuerte es el rechazo de la protección: el protector solar y el maquillaje con filtro se ven como manchas oscuras y las gafas con filtro restan colores nuevos, así que jóvenes y seguidores del agitador
    se quitan ambos justo con más sol, mientras dermatólogos y oftalmólogos compiten por la voz sanitaria y el mercado de gafas se separa por calidad de filtro. El canal nuevo empieza además a tocar áreas inesperadas: billetes en euros que se ven distintos, compra masiva de lámparas UV con primeros casos de lesión real, y una disparidad de percepción por edad y por lentes intraoculares que deja a parte de los mayores fuera.'
  hechos_establecidos:
  - id: h2-01
    texto: 'El rumor de que el fenómeno no afecta a América empieza a caer desde el sur: en Brasil y el Cono Sur ya es de día (en São Paulo son las 7:00 y hay sol desde poco después de las 5:00) y medios matinales y usuarios publican los primeros testimonios americanos en primera persona, que las redacciones estadounidenses en turno de noche citan como prueba. El rumor no desaparece, se reformula como una ola que llega con el amanecer franja a franja. Los futuros sobre índices estadounidenses, que cotizan casi todo el día, apenas se mueven y no ponen precio a ninguna diferencia geográfica. El agitador reorienta su emisión a la audiencia hispanohablante de América que despierta con un marco en el que cualquier resultado le da la razón (si lo ven, era algo planificado y escalonado; si lo ven distinto, a ellos les han hecho otra cosa) y llega antes que la cobertura local.'
    origen:
    - medios/h2/1
    - economista/h2/1
    - agitador/h2/3
  - id: h2-02
    texto: 'Los gobiernos pasan a coordinar sin restringir derechos. En España Moncloa activa el Sistema de Seguridad Nacional y convoca el Comité de Situación en lugar del estado de alarma; Sanidad reúne por vía telemática el Consejo Interterritorial y pacta un mensaje único de mínimos (no mirar al sol, el deslumbramiento por ahora no se asocia a lesión, urgencias solo ante síntomas concretos), sin decir que remite ni nada sobre gafas, y al menos una comunidad gobernada por la oposición se desmarca con su propia recomendación. La primera medida operativa la da la DGT con recomendaciones en paneles y redes (reducir velocidad, no parar en el arcén, cuidado con el deslumbramiento lateral), que el Gobierno exhibe como prueba de que actúa. No hay orden pública sobre el trabajo al aire libre: el protocolo de calor que obliga a adaptar horarios solo se activa con aviso meteorológico oficial, así que cada empresa decide si para o sigue y empieza la discusión entre sindicatos y patronales sobre
      quién paga las horas no trabajadas. En Bruselas la Comisión convoca el Comité de Seguridad Sanitaria sin declarar emergencia, y varios gobiernos europeos lo usan para esperar una posición común antes de recomendar nada sobre protección ocular.'
    origen:
    - politico/h2/1
    - politico/h2/2
    - politico/h2/3
    - politico/h2/4
    - economista/h2/5
  - id: h2-03
    texto: 'La sociedad oftalmológica publica una guía práctica breve para urgencias, farmacias y público: el deslumbramiento y la fatiga visual no son lesión; a urgencias solo con signos de alarma clásicos (dolor intenso, ojo rojo, pérdida brusca de visión, mancha fija); las gafas con filtro UV400 alivian y quitárselas no hace perder la capacidad nueva; ningún colirio filtra el ultravioleta; no hay que mirar al sol. Llega después de que los medios generalistas titularan su comunicado descriptivo como si fuera una guía y lo usaran para avalar recomendaciones contradictorias que no había dado, lo que la obligó a precisar qué decía. Es la única referencia técnica sobre gafas, porque el mensaje oficial de Sanidad no dice nada de ellas.'
    origen:
    - oftalmologa/h2/1
    - medios/h2/3
  - id: h2-04
    texto: 'Con el mensaje mínimo de Sanidad y la guía oftalmológica ya hay una referencia contra la que moderar, y las plataformas grandes actúan con medidas blandas, sin retiradas: etiquetan o limitan el alcance de clips del agitador que presentan el deslumbramiento como daño ocular. El agitador exhibe la etiqueta en sus canales propios como prueba de que le censuran, pide a su audiencia que le siga allí y que done para el directo de la tarde, y mantiene una versión moderada en la plataforma grande para seguir captando.'
    origen:
    - agitador/h2/4
  - id: h2-05
    texto: El hueco visual no se cierra con imágenes reales sino que se enreda más. Circula material auténtico de archivo grabado con cámaras ultravioleta, como el vídeo viral de 2014 de caras con protector oscurecidas o fotos de flores con patrones UV, que los medios publican con rótulo de archivo pero que en redes pierde el contexto y se comparte como imágenes del martes. A la vez aparecen las primeras fotos UV reales de aficionados, laboratorios forenses y astrofotógrafos con cámaras modificadas, que se muestran en falso color, no coinciden con lo que la gente ve y parte del público toma por montajes. Las unidades de verificación desmienten los bulos de ceguera y 5G apoyándose en los oftalmólogos, pero no pueden refutar los montajes de colores nuevos más que diciendo que ninguna cámara lo capta, y esos desmentidos llegan a mucha menos gente que el bulo.
    origen:
    - medios/h2/2
    - disruptor/h2/1
    - medios/h2/4
  - id: h2-06
    texto: Se extiende el rechazo de la protección por imagen y por desafío. Muchas personas, sobre todo adolescentes y jóvenes, se lavan la cara o dejan de usar protector solar, maquillaje y cremas con filtro porque a ojos ajenos se ven manchadas, y algunas evitan salir o hacerse fotos. El agitador convierte las manchas del protector en su tema estrella, mezclándolas en forma de preguntas con el discurso previo contra los filtros solares, y además anima a quitarse las gafas con filtro en exteriores presentándolas como algo que impide ver lo que hay que ver. Entre los jóvenes se forma un bando que prescinde de gafas buenas para no perderse los colores frente a otro que las presume. El resultado es menos protección justo en las horas de más sol, más deslumbramiento que llega a urgencias y una nueva voz sanitaria, la de los dermatólogos, que advierte del riesgo para la piel y compite con la de los oftalmólogos.
    origen:
    - adolescente/h2/3
    - disruptor/h2/3
    - agitador/h2/1
    - agitador/h2/2
    - adolescente/h2/4
  - id: h2-07
    texto: 'El mercado de gafas pasa de la volatilidad en bloque a la dispersión por calidad: las marcas con filtro certificado y distribución propia se leen como ganadoras y el producto barato sin filtro como existencias difíciles de vender. Las grandes plataformas de venta en línea activan sus políticas contra precios abusivos con avisos genéricos, muchos vendedores legítimos retiran también su stock, la escasez en línea empeora y la reventa se va a aplicaciones de segunda mano, mensajería y redes, sin garantía de filtro. Al mismo tiempo, quien ya lleva gafas con filtro sigue viendo colores nuevos y deslumbrándose por los laterales y por reflejo en la cara interna de la lente, lo interpreta como que sus gafas no funcionan, presenta quejas injustas y desplaza la demanda hacia monturas envolventes y gorras con visera.'
    origen:
    - economista/h2/3
    - economista/h2/2
    - oftalmologa/h2/4
  - id: h2-08
    texto: 'La disparidad de percepción toma un patrón por edad y por cirugía: niños y jóvenes describen los colores nuevos más intensos y muchos mayores apenas un velo azulado, porque el cristalino amarillea y absorbe más onda corta con los años. Los operados de cataratas con lente intraocular que bloquea el UV, que son la mayoría, los ven muy débiles o no los ven en el ojo operado. En familias y aulas los adultos dudan de lo que cuentan los niños, parte de los mayores se siente excluida y llama preguntando si puede cambiarse la lente, y la sociedad oftalmológica desaconseja cualquier cirugía para ganar visión UV.'
    origen:
    - oftalmologa/h2/2
    - oftalmologa/h2/3
  - id: h2-09
    texto: En comercios de la zona euro con luz natural, cajeros y clientes ven en los billetes dibujos de fibras y tintas de seguridad que antes no percibían, y los impresos en papel corriente con blanqueantes no se parecen a los auténticos, cuyo papel no brilla bajo UV. Hay rechazos de billetes buenos que parecen raros, algún billete falso detectado sin máquina y llamadas a los bancos centrales preguntando si el dinero sigue siendo válido.
    origen:
    - disruptor/h2/2
  - id: h2-10
    texto: 'Arranca una segunda ola de compra, no de gafas sino de linternas UV, lámparas de luz negra y de uñas para ver el fenómeno en interiores con LED, y en América, aún de noche, para comprobarlo antes del amanecer; se agotan en tiendas en línea y bazares. Con ellas y con retos de mirar al sol llegan a urgencias los primeros casos de visión borrosa o mancha central por exposición directa: son pocos frente a la ola de deslumbramiento, pero son los únicos con riesgo de lesión real, y la sociedad oftalmológica los usa para separar molestia transitoria de daño evitable.'
    origen:
    - disruptor/h2/4
    - oftalmologa/h2/5
  tensiones_abiertas:
  - Si Sanidad y el Interterritorial asumen la guía oftalmológica, incluida la recomendación sobre gafas UV400, o siguen en el mensaje de mínimos, y si la comunidad que se desmarcó arrastra a otras.
  - Si los dermatólogos o las autoridades sanitarias sacan una pauta sobre protector solar que frene el abandono, y si las marcas de cosmética solar pasan a cotizar un riesgo de rechazo estético del producto.
  - 'Cómo amanece Norteamérica: si el Gobierno federal se pronuncia antes del amanecer o deja que lo haga la luz, y si la audiencia recibe el relato ya interpretado por el agitador.'
  - Qué ocurre en el directo largo de la tarde del agitador, y si la migración a sus canales propios crece con cada etiqueta de las plataformas.
  - Si algún banco central o el BCE emite un aviso sobre la apariencia de los billetes antes de que los rechazos se extiendan.
  - Si aparecen clínicas privadas que ofrezcan recambio de lente intraocular para ganar visión UV.
  - Quién paga las horas no trabajadas al aire libre y si algún organismo emite un aviso que active los protocolos existentes.
  - Si algún gobierno atribuye el fenómeno a una acción hostil y obliga a otras cancillerías a responder.
  contradicciones_resueltas:
  - entre:
    - agitador/h2/4
    - politico/h2/2
    decision: Prevalece que el mensaje oficial español no dice que el deslumbramiento remita; la moderación blanda de las plataformas se apoya en ese mensaje mínimo (no se asocia a lesión) y en la guía oftalmológica, no en un anuncio oficial de transitoriedad.
    motivo: 'El mecanismo del político es más sólido: ningún gobierno afirma lo que sus técnicos no respaldan. Para etiquetar clips que confunden molestia con lesión basta con la referencia mínima que sí existe.'
  - entre:
    - medios/h2/3
    - oftalmologa/h2/1
    decision: 'Ambas se mantienen en secuencia: primero los medios presentan el comunicado descriptivo como guía y le atribuyen recomendaciones ajenas; después la sociedad publica una guía práctica real que precisa lo que dice.'
    motivo: La presión mediática que describe medios es precisamente el incentivo que explica por qué la sociedad publica la guía en esta hora.
  - entre:
    - oftalmologa/h2/1
    - agitador/h2/2
    - politico/h2/2
    decision: La única referencia técnica sobre gafas es la guía oftalmológica (UV400 alivia y no quita la capacidad); el mensaje oficial calla sobre gafas y el agitador llena ese silencio animando a quitárselas.
    motivo: 'No se excluyen: describen actores distintos, y el silencio oficial sobre gafas es el mecanismo que deja espacio a la consigna del agitador.'
  - entre:
    - agitador/h2/3
    - medios/h2/1
    decision: El rumor geográfico se debilita con los testimonios del sur pero no muere; el marco del agitador sobrevive porque no depende de que el rumor sea cierto.
    motivo: Medios aporta dato verificable sobre la luz en São Paulo y un mecanismo de reformulación del rumor que es compatible con la apuesta sin riesgo del agitador.
  descartadas:
  - id: economista/h2/4
    motivo: Confianza baja, especulación y sin dato; el abandono del protector ya entra por otras afirmaciones y el efecto bursátil queda como tensión abierta.
  - id: politico/h2/5
    motivo: Confianza baja, especulación y sin dato; la reacción federal estadounidense queda como tensión abierta.
  - id: medios/h2/5
    motivo: Confianza baja, especulación y sin dato; la idea de medidas blandas sin retiradas se recoge a través de agitador/h2/4.
  - id: agitador/h2/5
    motivo: Confianza baja, especulación y sin dato; los invitados y la grabación en urgencias quedan pendientes del directo de la tarde.
  - id: disruptor/h2/5
    motivo: Confianza baja y sin dato; detalle por tipo de cristal que amplía h1-04 sin consecuencia nueva suficientemente sólida.
  - id: adolescente/h2/1
    motivo: Efecto local de un centro que amplía h1-10 sin cambiar el rumbo del mundo; supera el límite de hechos.
  - id: adolescente/h2/2
    motivo: Moda local y especulativa de mensajes con crema; detalle de convivencia sin consecuencia para otras áreas.
  - id: adolescente/h2/5
    motivo: Especulación que repite hechos ya establecidos (montajes virales en h1-07 y directo del agitador en h1-09) sin consecuencia nueva.

Tu evaluación del tramo anterior, como referencia:
evaluacion:
  tramo: h1
  metricas:
    - id: alarma_social
      valor: 3
      justificacion: "Hay cambios de conducta visibles en parte de la población de las zonas de día: compras que agotan las gafas de sol, una ola de consultas y urgencias, alumnos metidos dentro y padres que recogen a sus hijos. No llega a 4 porque no hay servicios colapsados ni protestas en varios países, y en América, que es de madrugada, apenas se nota."
      apoyos: [h1-01, h1-03, h1-06, h1-10]
    - id: confianza_institucional
      valor: 2
      justificacion: "La versión oficial casi no existe (comunicados de calma sin medidas, la OMS solo recaba información, sin guía práctica), y el relato lo marcan bulos, comercios, políticos con recomendaciones contradictorias y creadores, sobre todo entre los jóvenes. No es 1 porque aún no hay desconfianza mayoritaria declarada: es más vacío que rechazo. Para llegar a 3 haría falta una versión oficial concreta que conviva con la sospecha."
      apoyos: [h1-05, h1-06, h1-07, h1-08, h1-09]
    - id: relatos_en_competencia
      valor: 3
      justificacion: "Junto al marco descriptivo de la sociedad oftalmológica y los comunicados de calma conviven relatos alternativos con canales y audiencia propios (el directo del agitador, los bulos de ceguera y 5G, el rumor de que no ha llegado a América), y algunos medios amplifican al agitador. No es 4 porque no hay un relato oficial con cifras o pruebas que choque frontalmente con otro alternativo."
      apoyos: [h1-01, h1-06, h1-07, h1-08, h1-09]
    - id: respuesta_gobiernos
      valor: comunicacion
      justificacion: "Los ministerios de Sanidad emiten comunicados de calma sin medidas obligatorias y ningún gobierno declara alarma ni excepción. El cierre de patios lo deciden los propios centros, no los gobiernos, así que no llega a medidas sectoriales."
      apoyos: [h1-05, h1-10]
    - id: impacto_economico
      valor: 3
      justificacion: "Varios sectores se ven alterados a la vez: construcción, agricultura, reparto y transporte por carretera frenan; se agotan las gafas de sol y los valores de óptica sufren paradas técnicas. Está en el límite inferior del nivel porque los índices no caen en general y se pierden horas, no empleo. No es 4 porque no hay crisis de mercado ni intervención."
      apoyos: [h1-02, h1-03, h1-04]
    - id: adaptacion
      valor: 2
      justificacion: "Hay primeras pautas improvisadas y en parte seguidas (ponerse gafas de sol, refugiarse en interiores, parar en el arcén), pero son contradictorias y no hay guía práctica oficial, así que mucha gente acaba en consulta por síntomas que no son lesión. Para llegar a 3 faltan pautas claras con respaldo técnico."
      apoyos: [h1-03, h1-04, h1-05, h1-06, h1-08, h1-10]

## Métricas y niveles

### alarma_social: Nivel de alarma social (escala)
- 1: Curiosidad; la vida sigue igual
- 2: Inquietud; conversación y búsquedas, sin cambios de conducta
- 3: Preocupación; cambios de conducta visibles en parte de la población (compras, quedarse en casa)
- 4: Miedo extendido; acaparamiento, servicios colapsados o protestas en varios países
- 5: Pánico; desórdenes, violencia o huidas masivas

### confianza_institucional: Confianza en la explicación y las indicaciones oficiales (escala)
- 1: La mayoría desconfía abiertamente; las versiones alternativas dominan
- 2: La versión oficial es minoritaria fuera de los medios tradicionales
- 3: Dividida: la versión oficial convive con una sospecha amplia
- 4: La mayoría sigue las indicaciones oficiales, con reservas
- 5: Confianza alta; las instituciones marcan el relato

### relatos_en_competencia: Grado de enfrentamiento entre relatos sobre lo que está pasando (escala)
- 1: Un relato dominante, compartido por instituciones, medios y público
- 2: Relato dominante; versiones alternativas marginales, sin canales ni audiencia propios
- 3: El relato oficial y uno alternativo conviven; el alternativo tiene audiencia y canales propios
- 4: Relatos enfrentados con cifras o pruebas incompatibles; los medios generalistas recogen los dos
- 5: Fractura: grupos amplios viven en relatos incompatibles y desconfían de cualquier fuente del otro

### respuesta_gobiernos: Respuesta dominante de los gobiernos (categorica)
- ninguna: Silencio oficial
- comunicacion: Mensajes y recomendaciones, sin medidas
- medidas_sectoriales: Medidas concretas en sectores (transporte, colegios, trabajo) sin estado excepcional
- emergencia: Declaración formal de emergencia o alerta nacional
- medidas_excepcionales: Restricción de derechos: confinamientos, toques de queda o censura

### impacto_economico: Impacto económico agregado (escala)
- 1: Sin efecto apreciable
- 2: Movimientos sectoriales; índices estables
- 3: Caídas generales de índices o disrupción en varios sectores
- 4: Crisis de mercado; intervención de bancos centrales o gobiernos
- 5: Parálisis económica

### adaptacion: Grado de normalización del cambio (escala)
- 1: Nadie sabe qué hacer
- 2: Primeras pautas, poco seguidas
- 3: Pautas claras y adoptadas por parte de la población
- 4: La mayoría ha ajustado su rutina
- 5: Normalizado

## Tu tarea
1. Para cada métrica, elige el nivel cuya descripción se ajusta mejor a los hechos establecidos, no a las tensiones ni a lo que podría pasar.
2. Si el mundo está entre dos niveles, elige el más cercano según los hechos, no el inferior ni el superior por prudencia, y di en la justificación qué falta para alcanzar el siguiente.
3. Justifica cada valor en una o dos frases: por qué este nivel y no el contiguo. Cita en apoyos los ids de los hechos que lo sostienen.
4. Mide el mundo en su conjunto. Si hay diferencias claras entre regiones, dilo en la justificación.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

evaluacion:
  tramo: h2
  metricas:
    - id: alarma_social
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: confianza_institucional
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: relatos_en_competencia
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: respuesta_gobiernos
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: impacto_economico
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: adaptacion
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
