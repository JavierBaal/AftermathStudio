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
Hora 3 (PT3H desde el suceso)
Estado del mundo al cierre de este tramo:
estado_del_mundo:
  tramo: h3
  resumen: 'En la tercera hora el daño por conducta se adelanta a su propio calendario: con la luz negra agotada, la demanda se desvía a lámparas germicidas UV-C que no muestran nada y queman la córnea, y los primeros casos reales de fotoqueratitis llegan a urgencias antes de la noche, lo que el agitador usa para decir que los oftalmólogos se equivocan o mienten mientras ya prepara su propio registro de ''síntomas tardíos'' y convierte el aviso preventivo en prueba de que ''ya lo sabían''. Gobierno y sociedad de oftalmología responden con lo mismo, adelantarse: refuerzo de urgencias, protocolo que anota la fuente de exposición de cada caso y un Consejo Interterritorial que reduce sin eliminar la disparidad entre comunidades, mientras la UE sube su dispositivo de crisis y la OMS publica una orientación técnica en vez de convocar el Comité de Emergencias. El fenómeno abre frentes nuevos fuera de la sanidad: un conflicto laboral por el deslumbramiento al aire libre, la comida que fluoresce
    bajo las lámparas caseras y alimenta una ola de reclamaciones y de bulos, y el marcado forense, que Interior calla en público mientras medios y agitador lo explican de facto como tutorial. El efecto cruzado más importante es geográfico: en el Cono Sur, que amanece con el estigma del protector ya construido en Europa y con índice UV extremo, el abandono del protector es preventivo y sus quemaduras serán otra ''lesión tardía'' disponible para el relato del daño diferido.'
  hechos_establecidos:
  - id: h3-01
    texto: 'Agotadas las lámparas de luz negra y las linternas UV-A, los buscadores y marketplaces devuelven para ''lámpara UV'' lámparas germicidas UV-C, abundantes desde la pandemia, y vendedores oportunistas las anuncian como forma de ver los colores nuevos. Quien las compra no ve nada nuevo, porque el fenómeno solo amplía la percepción al UV-A, tiende a acercarse o a dejarlas encendidas más tiempo y se expone a la radiación más lesiva para la córnea y la piel. La sociedad de oftalmología publica un aviso por tipo de producto: la luz negra UV-A muestra los colores y solo es peligrosa mirada de cerca y largo rato; la germicida no muestra nada y quema la córnea con exposiciones cortas, como ya ocurrió con las lámparas domésticas compradas en la pandemia.'
    origen:
    - economista/h3/1
    - oftalmologa/h3/1
  - id: h3-02
    texto: 'Llegan a urgencias y a los medios los primeros casos reales de quemadura de córnea, antes de la oleada nocturna anunciada: personas que miraron de cerca lámparas de uñas o de luz negra, o al sol, durante la primera hora. La latencia de la fotoqueratitis depende de la dosis y con exposiciones intensas puede ser de minutos u horas, así que los casos más graves se adelantan aunque la oleada principal siga siendo de tarde y noche. Los digitales los titulan como ''los primeros afectados reales'' y el mensaje de ''esta noche, no ahora'' queda en entredicho. Entre adolescentes circula además el rumor de que mirar un rato cerca del sol o una lámpara de uñas ''abre'' la vista, y se prueba como reto porque no duele en el momento, lo que suma menores a la oleada por conducta.'
    origen:
    - medios/h3/1
    - adolescente/h3/2
  - id: h3-03
    texto: 'Gobierno y sociedad de oftalmología se adelantan a la oleada: Sanidad, con las comunidades, pide a los hospitales reforzar las urgencias oftalmológicas para la tarde y la noche y difunde que los casos serán lesiones por mirar al sol o a lámparas UV, no un efecto diferido del fenómeno, y Consumo añade un aviso específico sobre lámparas de uñas, linternas y luz negra. La sociedad envía a urgencias un protocolo que obliga a anotar en cada caso la hora y la fuente de exposición (sol, luz negra, lámpara de uñas, germicida), separa la fotoqueratitis, que se cura en pocos días, de la retinopatía solar, menos frecuente pero capaz de dejar una mancha central persistente, y pide no dar colirio anestésico para casa.'
    origen:
    - politico/h3/2
    - oftalmologa/h3/2
  - id: h3-04
    texto: 'El agitador se adelanta también: abre en su canal propio un formulario o hilo fijo para que sus seguidores registren ''síntomas tardíos'' y anuncia que esta noche se verá ''lo que nos han hecho'', con lo que tendrá una base de testimonios que los verificadores no pueden contrastar. Y ataca la nota de triaje precisamente porque acertó: presenta el ''ya sabían que habría heridos esta noche'' como prueba de conocimiento previo, omitiendo que la causa es mirar al sol o a lámparas. Parte de los síntomas que recoja vendrán de seguidores que buscaron ''marcas'' con lámparas o cerca del sol siguiendo su propio encuadre de la hora 2.'
    origen:
    - agitador/h3/1
    - agitador/h3/2
  - id: h3-05
    texto: 'Sanidad convoca un pleno extraordinario y telemático del Consejo Interterritorial del SNS, y Educación su conferencia sectorial, para cerrar una pauta común para colegios y centros sanitarios basada en la nota de la sociedad de oftalmología (recreo a la sombra o con visera, no mirar al sol, sin cierres). La mayoría de comunidades se adhiere, pero alguna gobernada por la oposición vota en contra o se abstiene y mantiene su circular propia: como los acuerdos del Consejo no obligan a quien no los acepta, el Gobierno reduce la disparidad sin eliminarla y obtiene una foto de acuerdo frente al ''¿quién manda?''.'
    origen:
    - politico/h3/1
  - id: h3-06
    texto: 'El deslumbramiento se convierte en conflicto laboral en España. Sindicatos y delegados de prevención reclaman a mediodía que las empresas evalúen el nuevo riesgo para quien trabaja al aire libre (obra en altura, reparto en moto y bici, agricultura, grúas), y en algunos tajos los trabajadores invocan el derecho a interrumpir la actividad por riesgo grave e inminente del artículo 21 de la Ley de Prevención de Riesgos Laborales; Inspección de Trabajo y mutuas reciben consultas que no saben contestar. Las empresas y sus servicios de prevención empiezan a pedir por lotes gafas homologadas a distribuidores de equipos de protección individual, que el empresario debe proporcionar gratis según el Real Decreto 773/1997: el tirón de demanda de gafas se desplaza del minorista, que se enfría, al canal profesional, donde se compra por cumplimiento aunque los trabajadores jóvenes no quieran llevarlas, y sigue siendo transitorio.'
    origen:
    - disruptor/h3/3
    - economista/h3/2
  - id: h3-07
    texto: La presidencia del Consejo de la UE sube el dispositivo integrado de respuesta política a crisis (IPCR) del modo de intercambio de información a una mesa redonda de crisis con Estados, Comisión y Servicio de Acción Exterior para alinear mensajes sanitarios y presión a las plataformas, sin medidas comunes. La OMS no convoca el Comité de Emergencias, porque un cambio de percepción sin daño acreditado ni propagación no encaja en una emergencia de salud pública de importancia internacional, y publica en su lugar una orientación técnica sobre protección ocular que ofrece por fin una autoridad común a la que pueden enlazar gobiernos y plataformas.
    origen:
    - politico/h3/5
  - id: h3-08
    texto: 'La pérdida de invisibilidad del marcado forense salta a los medios generalistas como historia de seguridad (''el fin de la marca invisible''), con empresas de seguridad y portavoces policiales que reconocen consultas sin dar detalles. Interior no se pronuncia en público sobre qué sistemas quedan afectados y canaliza por vía interna instrucciones a Policía Nacional, Guardia Civil y seguridad privada (preservar y documentar pruebas ya marcadas antes de que se limpien, revisar protocolos), limitándose a decir que las investigaciones cuentan con otros medios de prueba. El hueco lo llenan periodistas y el agitador, que mezcla marcadores reales tipo SmartWater, rociadores y tintas de seguridad con fluorescencias inocuas y pide a su audiencia revisar ropa, casa y coche: entre todos difunden de facto cómo detectar y limpiar el marcado, y las líneas de consulta se saturan con particulares asustados mezclados con quien busca borrar rastros.'
    origen:
    - politico/h3/4
    - medios/h3/5
    - agitador/h3/4
  - id: h3-09
    texto: 'En el Cono Sur (Chile, Argentina, Uruguay, sur de Brasil), donde amanece en esta franja en plena primavera austral, la gente vive el fenómeno ya contado por Europa y una parte deja el protector solar y el maquillaje con SPF en casa para no llevar la máscara, antes de que nadie se lo vea: es el primer lugar donde el abandono del protector es preventivo y no reactivo. Coincide con días de índice UV muy alto o extremo, de modo que las quemaduras reales aparecerán allí antes y con más intensidad que en la Europa de noviembre, y se sumarán como otra ''lesión tardía'' disponible para el relato del daño diferido.'
    origen:
    - disruptor/h3/1
  - id: h3-10
    texto: 'Las lámparas de luz negra y linternas UV ya en los hogares se apuntan a la nevera y la despensa, y frutos secos, maíz, especias, cítricos y pan muestran puntos y halos fluorescentes. La fluorescencia bajo UV es un cribado real pero solo presuntivo (se usa para sospechar aflatoxinas en maíz) y da falsos positivos, mientras el consumidor aplica la regla ''si brilla, se tira'': arranca comida tirada, reclamaciones a supermercados y llamadas a las agencias de seguridad alimentaria, y el agitador amplía las ''marcas'' a la comida (''nos envenenan y lo marcan'').'
    origen:
    - disruptor/h3/2
  tensiones_abiertas:
  - Si la oleada de fotoqueratitis de esta tarde y noche, ya adelantada por los primeros casos, se lee como lesión por conducta, como sostienen Gobierno y oftalmólogos con un protocolo que registra la fuente de exposición, o como el daño diferido que el agitador ha preparado con su propio registro de 'síntomas tardíos'; y si aparecen casos de retinopatía solar con secuelas persistentes.
  - 'Si la oposición se divide ante el relato de ocultación: el principal partido ataca la descoordinación y evita las ''marcas ocultas'' mientras otras fuerzas o cargos siguen compartiendo clips del agitador, que se apropia de la comparecencia del presidente y lee el uso del Consejo de Seguridad Nacional como prueba de que el asunto es ''de seguridad''.'
  - Si el amanecer en la Costa Este de Estados Unidos y los matinales de sus cadenas abren una segunda ola viral en inglés que desplaza el relato europeo, y cómo reacciona Wall Street en su apertura, donde los valores de autenticación y seguridad de billetes ya se mueven en preapertura sin dirección clara.
  - Si la orientación técnica de la OMS y el registro estructurado de testimonios que prepara la sociedad de oftalmología se convierten en la autoridad común que les faltaba a las plataformas, y si un registro abierto mezcla datos fiables con sugestión.
  - Si el abandono preventivo del protector en el Cono Sur produce una oleada visible de quemaduras en las próximas horas y si se repite en otros países que amanecen después.
  - 'Cómo se resuelve el conflicto laboral por el deslumbramiento: si Inspección de Trabajo o el Gobierno fijan un criterio sobre el riesgo grave e inminente o si cada tajo decide por su cuenta.'
  - Si la difusión masiva de cómo se ve el marcado forense produce una ola de borrado de rastros y cómo responden policías y empresas de seguridad.
  - Si los pedidos urgentes a fábricas asiáticas de lámparas, gafas y protector sobre las ventas de hoy fabrican los excedentes y rebajas de dentro de unas semanas.
  contradicciones_resueltas:
  - entre:
    - medios/h3/1
    - oftalmologa/h2/1
    decision: Se establece que los casos más graves de fotoqueratitis llegan ya en la tercera hora y que la oleada principal sigue siendo de tarde y noche; el calendario de 6 a 12 horas recogido en h2-05 queda corregido como rango típico, no como mínimo.
    motivo: 'Medios aporta dato con fuente clínica (EyeWiki de la Academia Americana de Oftalmología: síntomas entre 30 minutos y 12 horas tras la exposición) y un mecanismo de dosis que no contradice a la sociedad, solo acota su mensaje; prevalece el mecanismo más sólido con dato verificable.'
  - entre:
    - politico/h3/2
    - agitador/h3/2
    decision: 'Ambos hechos entran: el Gobierno y la sociedad anticipan la oleada como lesión por conducta y el agitador usa esa misma anticipación como prueba de conocimiento previo. Cuál de las dos lecturas prevalece queda como tensión abierta.'
    motivo: Las dos afirmaciones tienen mecanismo plausible y no se excluyen; ninguna aporta dato que decida el efecto en la opinión pública, así que el empate se mantiene para el siguiente tramo.
  - entre:
    - economista/h3/2
    - adolescente/h2/5
    decision: Se recoge que el rechazo de los jóvenes a las gafas no frena la demanda profesional, que se compra por obligación legal del empresario, mientras la demanda minorista se enfría.
    motivo: El economista aporta norma con fuente (Real Decreto 773/1997) y un mecanismo de compra por cumplimiento que no depende de la preferencia del usuario; la afirmación del adolescente seguía sin dato.
  descartadas:
  - id: economista/h3/3
    motivo: Movimiento bursátil de detalle sin dato de precios; se recoge como tensión junto a la apertura de Wall Street.
  - id: economista/h3/4
    motivo: Efecto látigo plausible pero sin dato y con consecuencias a semanas vista; se deja como tensión abierta.
  - id: economista/h3/5
    motivo: Especulación sin dato sobre la postura pública del economista; efecto mediático de detalle que no cambia el rumbo del mundo.
  - id: politico/h3/3
    motivo: Especulación sin dato; coincide con agitador/h3/3 y se recoge como tensión abierta sobre la división de la oposición.
  - id: medios/h3/2
    motivo: Inferencia sin dato; plausible, pero el límite de hechos obliga a priorizar y queda como tensión abierta sobre la segunda ola en Estados Unidos.
  - id: medios/h3/3
    motivo: Amplía la fricción por el protector y el contenido sobre caras ya recogidos en h1-08, h2-03 y h2-10; el aviso de la AEPD es declarativo y sin efecto en el tramo, y no supera el límite de hechos.
  - id: medios/h3/4
    motivo: Especulación sin dato y efecto cultural de detalle que no cambia el rumbo del mundo en este tramo.
  - id: oftalmologa/h3/3
    motivo: El registro tiene mecanismo y dato sobre el cristalino, pero el volumen de respuestas y las adhesiones europeas carecen de fuente; no supera el límite de hechos y queda como tensión sobre la autoridad común.
  - id: oftalmologa/h3/4
    motivo: Confianza baja y especulación sin dato.
  - id: oftalmologa/h3/5
    motivo: Corrección técnica plausible pero sin dato y de detalle; no hay en el canon una pauta oficial ligada al índice UV que corregir.
  - id: adolescente/h3/1
    motivo: Efecto local y de detalle que concreta el gradiente por edad ya recogido en h2-07 sin añadir una consecuencia que cambie el rumbo.
  - id: adolescente/h3/3
    motivo: Efecto local y de detalle; el agotamiento de lámparas ya está en h2-04.
  - id: adolescente/h3/4
    motivo: Confianza baja y especulación sin dato; concreta los sellos de locales ya recogidos en h2-09.
  - id: adolescente/h3/5
    motivo: Efecto local y de detalle sobre la salida del instituto que no cambia el rumbo del mundo.
  - id: agitador/h3/3
    motivo: Especulación sin dato; se recoge como tensión abierta junto a politico/h3/3 sobre la relación entre agitador y oposición.
  - id: agitador/h3/5
    motivo: Inferencia sin dato sobre los ingresos del agitador; detalle que amplía la migración a su canal ya recogida en h2-10 sin cambiar el rumbo del mundo.
  - id: disruptor/h3/4
    motivo: Mecanismo y dato sólidos, pero el límite de hechos obliga a priorizar los que afectan a más áreas; la visibilidad del vitíligo queda fuera de este tramo y puede volver si tiene consecuencias.
  - id: disruptor/h3/5
    motivo: Confianza baja y especulación sin dato.

Tu evaluación del tramo anterior, como referencia:
evaluacion:
  tramo: h2
  metricas:
    - id: alarma_social
      valor: 3
      justificacion: "Siguen los cambios de conducta visibles en parte de la población: compra y agotamiento de lámparas UV, gente que se quita las gafas graduadas o el protector solar, aulas que se vacían según decide cada familia y consultas por ansiedad. No llega a 4 porque no hay acaparamiento de bienes básicos, colapso de servicios ni protestas, y parte de la alarma por la piel se frena con las imágenes UV y la explicación oftalmológica."
      apoyos: [h2-02, h2-03, h2-04, h2-05, h2-07, h2-08]
    - id: confianza_institucional
      valor: 3
      justificacion: "La versión oficial gana cuerpo (mensaje único coordinado con los técnicos, pauta y triaje de oftalmología, desmentidos de verificadores) pero convive con una sospecha amplia: el agitador convierte los desmentidos en confesión apoyado en marcas forenses reales y su audiencia migra a canales sin moderación. No sube a 4 porque las pautas oficiales no se siguen de forma mayoritaria y no baja a 2 porque los medios tradicionales y las plataformas siguen amplificando la versión oficial."
      apoyos: [h2-05, h2-06, h2-08, h2-09, h2-10]
    - id: respuesta_gobiernos
      valor: comunicacion
      justificacion: "El mundo está entre comunicacion y medidas_sectoriales y se elige la inferior: el Gobierno de España coordina avisos bajo un mensaje único sin medidas excepcionales y la Comisión Europea solo recuerda obligaciones a las plataformas, aunque varias consejerías de Educación ordenan recreos en interior sin cerrar centros. Esas instrucciones escolares son desiguales y limitadas a algunas comunidades españolas, por lo que no bastan para que la respuesta dominante sean medidas sectoriales; del resto de países no hay hechos nuevos."
      apoyos: [h2-06, h2-07, h2-10]
    - id: impacto_economico
      valor: 2
      justificacion: "Los movimientos siguen siendo sectoriales: la subida de las gafas de sol se desinfla, la volatilidad salta a la cosmética con protector solar y suben precios y se agotan lámparas UV. No llega a 3 porque no hay caídas generales de índices ni disrupción operativa en varios sectores; Wall Street y Asia aún no han reaccionado en sesión."
      apoyos: [h2-01, h2-03, h2-04]
    - id: adaptacion
      valor: 2
      justificacion: "Ya hay primeras pautas claras (uso situacional de gafas de sol, triaje oftalmológico, pauta para colegios, mensaje oficial único), pero poco seguidas: muchos se quitan las gafas graduadas en la calle, se abandona el protector y parte de la población mira con lámparas UV o cerca del sol. No llega a 3 porque no hay indicio de que esas pautas las haya adoptado una parte relevante de la población y las instrucciones a colegios llegan desiguales."
      apoyos: [h2-01, h2-02, h2-03, h2-04, h2-05, h2-07]

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
2. Si el mundo está entre dos niveles, elige el inferior y dilo en la justificación.
3. Justifica cada valor en una o dos frases: por qué este nivel y no el contiguo. Cita en apoyos los ids de los hechos que lo sostienen.
4. Mide el mundo en su conjunto. Si hay diferencias claras entre regiones, dilo en la justificación.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

evaluacion:
  tramo: h3
  metricas:
    - id: alarma_social
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: confianza_institucional
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
