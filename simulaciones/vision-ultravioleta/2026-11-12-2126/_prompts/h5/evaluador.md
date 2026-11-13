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
Hora 5 (PT5H desde el suceso)
Estado del mundo al cierre de este tramo:
estado_del_mundo:
  tramo: h5
  resumen: 'En la quinta hora la batalla por el daño se libra en las historias clínicas: la sociedad de oftalmología añade a su protocolo la tinción con fluoresceína, que separa con un signo objetivo la fotoqueratitis del cansancio benigno, y pide OCT ante los primeros casos sospechosos de retinopatía solar, mientras el agitador convierte esa retinopatía en ''daño permanente'', vuelca un recuento de síntomas que mezcla fatiga con lesión y anima a no declarar la exposición en urgencias para fabricar un residuo de casos ''sin causa''; los informativos de sobremesa, sin dato oficial agregado, abren con contadores que no miden lo mismo. El Gobierno pasa del aviso a la orden en dos frentes: Trabajo publica un criterio que convierte el conflicto del deslumbramiento en una obligación de entregar gafas, sin declarar riesgo grave e inminente general, y Consumo ordena retirar los anuncios de lámparas UV-C, que reaparecen con otro título y se desplazan a canales menos vigilados. El fenómeno abre frentes
    que el mensaje centrado en los ojos no cubría: reacciones fototóxicas en la piel de quien toma fármacos comunes y salió sin protector, discusiones en caja por billetes que ''brillan'' y, desde Asia oriental ya de noche, la noticia de que con LED los colores casi desaparecen, que lanza en Europa una búsqueda de fluorescentes que la UE ya retiró antes de su primera noche. El efecto cruzado clave es que el reto adolescente, amplificado por la propia cobertura y escondido a los padres, alimenta a la vez la oleada de urgencias y los rostros del relato del agitador, mientras en el Cono Sur los gobiernos contradicen el abandono del protector cuando las primeras quemaduras ya llegan a su canal.'
  hechos_establecidos:
  - id: h5-01
    texto: 'Antes de las 15:00 el Ministerio de Trabajo, a través de la Inspección y del Instituto Nacional de Seguridad y Salud en el Trabajo, publica una nota provisional que recoge el criterio técnico que la sociedad de oftalmología ofrece a Inspección, mutuas y servicios de prevención: el deslumbramiento es un riesgo nuevo que las empresas deben evaluar y prevenir con filtros solares de uso laboral homologados, sombra y reorganización de tareas, pero no es con carácter general un riesgo grave e inminente; solo puede serlo en tareas donde un deslumbramiento súbito cause un accidente (altura, conducción de vehículos o grúas) mientras no se hayan entregado esos filtros, y cada paralización del artículo 21 se valora caso por caso. El conflicto se desplaza a una obligación de equipo de protección: sindicatos lo leen como respaldo y patronales como aval, los tajos se reanudan a medida que llegan las gafas y los paros puntuales siguen donde todavía no han llegado.'
    origen:
    - politico/h5/1
    - oftalmologa/h5/4
  - id: h5-02
    texto: 'Consumo y las autoridades autonómicas de vigilancia del mercado pasan del aviso a la orden: notifican a los grandes marketplaces los anuncios de lámparas germicidas UV-C presentadas como forma de ver los colores nuevos y Sanidad comunica el riesgo a la red europea Safety Gate, con base en el Reglamento (UE) 2023/988, que obliga a los mercados en línea a actuar sin demora sobre esas órdenes. Las plataformas retiran los anuncios señalados, pero la retirada funciona a medias: los vendedores reetiquetan el mismo producto con otro título (''lámpara de luz'', ''esterilizador''), los vendedores de fuera de la UE y las tiendas en redes sociales siguen vendiéndolas, y la oferta baja en los escaparates grandes y se desplaza a canales menos vigilados. El periodismo de consumo convierte el ''los retiran y vuelven a salir'' en su historia de la tarde, apoyado en el precedente del aviso de la FDA de 2022 sobre varitas UV-C de consumo.'
    origen:
    - politico/h5/2
    - economista/h5/3
    - medios/h5/2
  - id: h5-03
    texto: 'Ante las consultas de personas con escozor, lagrimeo o cansancio ocular que temen los ''síntomas tardíos'', la sociedad de oftalmología añade a su protocolo la tinción con fluoresceína y lámpara de hendidura en todos los casos: la fotoqueratitis deja erosiones epiteliales punteadas visibles y el deslumbramiento y la fatiga del fenómeno dejan la córnea limpia, así que la oleada se registra con un signo objetivo y no solo con testimonios. El agitador ataca a la vez el protocolo que anota la fuente de exposición como un sistema para ''culpar a la víctima'' y anima a su audiencia a no declarar en urgencias que miró al sol o usó lámparas; una parte de sus seguidores lo omite, crece la categoría de fuente no declarada y él la anuncia de antemano como la cifra que demostrará el daño del fenómeno. La tinción acredita la lesión pero no su causa, de modo que el residuo sin fuente declarada queda disponible para su relato.'
    origen:
    - oftalmologa/h5/1
    - agitador/h5/3
  - id: h5-04
    texto: Llegan a las unidades de retina los primeros casos sospechosos de retinopatía solar, sobre todo adolescentes y jóvenes que miraron al sol por el reto de 'abrir la vista' o para buscar los colores, con mancha central o visión deformada. La sociedad pide OCT macular a todo el que refiera mancha central y advierte en público, con el precedente del eclipse de 2017 en Utah (27 consultas por cambios en la visión y 6 exploraciones compatibles), de que la mayoría de quienes consulten por miedo no tendrán lesión, pero los pocos confirmados pueden conservar una pequeña mancha durante meses. El agitador se apropia de la distinción que la propia sociedad hizo entre fotoqueratitis, que se cura, y retinopatía, que puede dejar secuela, la presenta como reconocimiento de que 'hay daño permanente' y convierte a los primeros casos en los rostros de su relato sin mencionar que miraron al sol, apoyado en que la palabra es reconocible tras los avisos del eclipse de agosto de 2026.
    origen:
    - oftalmologa/h5/2
    - agitador/h5/2
  - id: h5-05
    texto: 'El agitador vuelca en directo el recuento de su registro de ''síntomas tardíos'', lleno sobre todo de fatiga visual, deslumbramiento y escozor en exteriores, que mezcla en una sola categoría con los casos de urgencias; el volumen de respuestas, no su contenido, es el titular de su canal y nadie externo puede depurarlo. Los informativos de sobremesa de las 15:00 abren con los primeros casos de quemadura de córnea y, sin un dato oficial agregado, cada cadena construye su propio contador sumando hospital por hospital, de modo que circulan a la vez cifras que no miden lo mismo: casos confirmados por hospitales, distintos entre medios, y el recuento del agitador, siempre el más alto, presentado como ''la cifra que no dan''.'
    origen:
    - agitador/h5/1
    - medios/h5/1
  - id: h5-06
    texto: Los medios descubren el reto adolescente de mirar al sol o a la lámpara de uñas para 'abrir la vista' y lo cubren como reto viral peligroso; la cobertura, que describe lo que se hace, lo da a conocer a menores que no lo habían visto, como ocurrió con el reto de las cápsulas de detergente en 2018, y la retirada de vídeos en las plataformas grandes lo desplaza a grupos de mensajería y perfiles efímeros sin alcance medible. Entre quienes ya lo hicieron, los síntomas de fotoqueratitis empiezan a notarse a media tarde y muchos los ocultan a sus padres para no confesar la conducta, lo consultan en el grupo de amigos y retrasan la visita al médico hasta la noche, lo que suma menores a la oleada nocturna.
    origen:
    - medios/h5/3
    - adolescente/h5/1
  - id: h5-07
    texto: 'Asia oriental, donde el suceso llegó al caer la tarde y lleva horas de noche, se convierte en el laboratorio de la primera noche del fenómeno: desde Japón, China y Corea llegan a Europa testimonios de que con luz LED los colores nuevos casi desaparecen y con tubos y bombillas fluorescentes siguen viéndose, porque los LED blancos domésticos emiten muy poco por debajo de 400 nm y los fluorescentes de mercurio dejan escapar algo de UV-A, y en Japón su prohibición no llega hasta finales de 2027. En Europa, que encara su primera noche hacia las 18:00 tras retirar en 2023 los tubos T5 y T8 y las compactas sin balasto integrado, arranca una búsqueda de fluorescentes y bombillas de bajo consumo antiguas y el stock residual de almacenes, ferreterías y segunda mano se encarece.'
    origen:
    - disruptor/h5/1
  - id: h5-08
    texto: Empiezan a llegar a centros de salud, urgencias y farmacias reacciones fototóxicas en la piel (enrojecimiento, quemazón, ampollas en cara, escote y dorso de las manos) en personas que toman fármacos fotosensibilizantes comunes, como hidroclorotiazida, furosemida, amiodarona, doxiciclina, ciprofloxacino o los antiinflamatorios ibuprofeno y naproxeno, que muchos toman sin receta para la cefalea del deslumbramiento. Son sobre todo mayores y gente que salió al sol a mirar los colores o dejó el protector para no llevar la máscara; la reacción la desencadena sobre todo el UV-A y aparece en minutos u horas, antes que la oleada nocturna de fotoqueratitis, por una vía que el protocolo de urgencias, centrado en los ojos, y el mensaje oficial no contemplan, y que encaja en el relato del agitador como daño de quien 'no estuvo tanto al sol'.
    origen:
    - disruptor/h5/2
  - id: h5-09
    texto: 'En mercados, bares y comercios pequeños donde se paga en efectivo y se atiende cerca de la puerta o en la calle, clientes y dependientes miran los billetes a la luz del día y rechazan los que ''brillan'' o los que ''no tienen fibras de colores'', porque el papel del euro auténtico es mate bajo UV y lleva fibras que se ven en verde, rojo y azul. Afloran algunos billetes falsos que circulaban, pero también se rechazan billetes auténticos lavados o manchados con blanqueantes ópticos de detergentes, y el Banco de España y las policías locales reciben llamadas por discusiones en caja: la regla ''si brilla, es malo'' pasa de la comida al dinero.'
    origen:
    - disruptor/h5/3
  - id: h5-10
    texto: 'En el Cono Sur los ministerios de salud, con Chile a la cabeza sobre su Ley 20.096 de control de la radiación ultravioleta, salen a media mañana local a contradecir el abandono preventivo del protector: el índice UV de primavera es alto o extremo, el fenómeno no cambia el riesgo de quemadura y hay que seguir usándolo, y la autoridad laboral chilena recuerda a los empleadores su obligación de proteger a quien trabaja al sol. El aviso llega tarde para quien ya salió sin protector, y las primeras rojeces y quemaduras de piel de esa mañana llegan en el mismo idioma al canal del agitador, que las suma a su relato de daño diferido y gana audiencia latinoamericana.'
    origen:
    - politico/h5/4
    - agitador/h5/5
  tensiones_abiertas:
  - Si la tinción con fluoresceína y la OCT consiguen imponer la lectura de la oleada nocturna como lesión por conducta con signo objetivo, o si el residuo de casos sin fuente declarada, el recuento del agitador y los primeros casos de retinopatía con secuela sostienen el relato del daño diferido; y si aparece un primer caso con secuela persistente con nombre y edad.
  - Si Sanidad publica un dato oficial agregado de casos que sustituya los contadores dispares de los medios, o si la cifra del agitador queda como referencia por ausencia de otra.
  - Si la apertura de Wall Street a las 15:30 hora de Madrid, ya fuera de este tramo, sostiene volumen en los valores del relato o se limita a un salto inicial ya descontado en preapertura y en Europa; y si los matinales de Estados Unidos abren una segunda ola en inglés que desplaza el relato europeo e importa el debate sobre las 'marcas'.
  - Si la primera noche en Europa, con iluminación LED, apaga los colores nuevos en interiores, qué hace la gente para recuperarlos y si la búsqueda de fluorescentes deriva en presión política contra la retirada europea por el mercurio.
  - Si las reacciones fototóxicas por fármacos obligan a ampliar a la piel y a las farmacias el mensaje sanitario centrado en los ojos, y si el agitador las incorpora a su registro.
  - Si las discusiones por billetes que brillan en el comercio de efectivo obligan al Banco de España o al BCE a explicar en público cómo se comprueban los billetes, y si eso alimenta el relato de las 'marcas'.
  - Si el reto adolescente, desplazado a canales cerrados, sigue sumando menores a urgencias y retinas esta noche, y cómo afecta la ocultación a los padres al momento de la consulta.
  - Si la retirada parcial de lámparas UV-C reduce los casos por germicidas o solo traslada la venta a canales extracomunitarios y redes sociales.
  - Si el abandono preventivo del protector en el Cono Sur produce una oleada visible de quemaduras y si se repite en otros países que amanecen después.
  - Si la oposición se divide ante el relato de ocultación y si el marcado forense difundido produce una ola de borrado de rastros.
  contradicciones_resueltas:
  - entre:
    - oftalmologa/h5/1
    - agitador/h5/1
    decision: 'Entran los dos hechos: el agitador publica un recuento que mezcla fatiga con lesión y la sociedad introduce un signo objetivo, la tinción con fluoresceína, que permite separarlos en cada historia clínica. Qué lectura prevalece en la opinión pública queda como tensión abierta.'
    motivo: La oftalmóloga aporta mecanismo clínico con dato y fuente (EyeRounds), y el agitador un mecanismo plausible derivado de los supuestos del mundo; no se excluyen y ninguno aporta dato sobre el efecto en la opinión pública.
  - entre:
    - politico/h5/1
    - oftalmologa/h5/4
    - disruptor/h3/3
    decision: Se establece que el deslumbramiento no es riesgo grave e inminente con carácter general, pero sí puede serlo en tareas con riesgo de accidente mientras no se entreguen filtros; los paros continúan solo donde no han llegado las gafas.
    motivo: Ambas afirmaciones nuevas convergen con norma con fuente (artículo 21 de la Ley 31/1995 y normas de filtros solares laborales del INSST) y se apoyan en el supuesto de que el deslumbramiento remite sin daño; el artículo 21 de h3-06 queda acotado, no anulado.
  - entre:
    - economista/h5/1
    - medios/h3/2
    decision: 'La reacción de Wall Street no ocurre en este tramo: la sesión regular de Nueva York abre a las 15:30 hora de Madrid. La tensión sobre su apertura se mantiene para el siguiente tramo.'
    motivo: El economista aporta dato con fuente (horario de NYSE) y un cálculo horario verificable; la afirmación del economista no añade otro hecho que cambie el rumbo del mundo y queda recogida como corrección de la tensión.
  - entre:
    - economista/h5/4
    - disruptor/h3/2
    decision: No se modifica h3-10; la escala de la ola de comida tirada sigue sin dato y no se establece que esté limitada ni que sea mayor.
    motivo: La matización del economista sobre el número de hogares con lámpara es una inferencia sin dato que no supera el límite de hechos.
  - entre:
    - agitador/h5/4
    - oftalmologa/h3/3
    decision: No se establece la contaminación coordinada del registro de testimonios de la sociedad, que no forma parte del canon.
    motivo: El registro abierto se descartó en h3 y la afirmación del agitador es especulación sin dato; queda dentro de la tensión sobre la autoridad común.
  descartadas:
  - id: economista/h5/1
    motivo: Dato horario correcto con fuente, pero no establece un hecho nuevo del tramo; se recoge como corrección de la tensión sobre Wall Street.
  - id: economista/h5/2
    motivo: Concreta en el reparto el conflicto laboral ya recogido en h3-06 y h5-01 sin añadir una consecuencia que cambie el rumbo; efecto sectorial de detalle que no supera el límite de hechos.
  - id: economista/h5/4
    motivo: Amplía la ola de reclamaciones por comida de h3-10 sin dato sobre devoluciones ni certificados; la matización de escala es inferencia sin dato.
  - id: economista/h5/5
    motivo: Confianza baja y especulación sin dato.
  - id: politico/h5/3
    motivo: Aviso declarativo de seguridad alimentaria sin dato que amplía h3-10 y repite el patrón de reencuadre del agitador ya establecido; no supera el límite de hechos.
  - id: politico/h5/5
    motivo: Confianza baja y especulación sin dato sobre la Casa Blanca; el dato de la FDA se recoge en h5-02 como precedente.
  - id: medios/h5/4
    motivo: Confianza baja y especulación sin dato; queda como tensión sobre la segunda ola en inglés.
  - id: medios/h5/5
    motivo: Confianza baja y especulación sin dato sobre peticiones de Interior a los medios.
  - id: oftalmologa/h5/3
    motivo: Dato con fuente, pero concreta el gradiente por edad ya recogido en h2-07 en una pauta para familias sin consecuencia que cambie el rumbo; no supera el límite de hechos.
  - id: oftalmologa/h5/5
    motivo: Especulación sin dato sobre la adopción del protocolo por las sociedades del Cono Sur; el límite de hechos prioriza la respuesta gubernamental de h5-10.
  - id: adolescente/h5/2
    motivo: Especulación sin dato y efecto de detalle en redes que no añade consecuencia nueva al relato de daño ya recogido.
  - id: adolescente/h5/3
    motivo: Efecto local y de convivencia sin dato que no cambia el rumbo del mundo.
  - id: adolescente/h5/4
    motivo: Efecto doméstico y de detalle; reacción esperable de las familias que no altera el rumbo del mundo.
  - id: adolescente/h5/5
    motivo: Especulación sin dato sobre el vocabulario de los colores; efecto cultural de detalle.
  - id: agitador/h5/4
    motivo: Especulación sin dato sobre un registro de la sociedad que no está en el canon.
  - id: disruptor/h5/4
    motivo: Confianza baja y especulación sin dato; queda como tensión sobre la presión contra la retirada de fluorescentes.

Tu evaluación del tramo anterior, como referencia:
evaluacion:
  tramo: h3
  metricas:
    - id: alarma_social
      valor: 3
      justificacion: "Los cambios de conducta visibles se amplían: compra de lámparas germicidas, retos entre adolescentes, comida tirada y reclamaciones, trabajadores que interrumpen tajos, líneas de consulta saturadas y abandono preventivo del protector en el Cono Sur. No llega a 4 porque no hay acaparamiento de bienes básicos, protestas en varios países ni servicios colapsados: las urgencias se refuerzan antes de la oleada y la saturación se limita a líneas de consulta."
      apoyos: [h3-01, h3-02, h3-06, h3-08, h3-09, h3-10]
    - id: confianza_institucional
      valor: 3
      justificacion: "La versión oficial gana autoridad (protocolo con fuente de exposición, pauta común del Consejo Interterritorial, orientación técnica de la OMS), pero convive con una sospecha amplia: los primeros casos ponen en entredicho el 'esta noche, no ahora', el agitador abre su registro de 'síntomas tardíos', presenta el triaje como conocimiento previo y amplía las 'marcas' a la comida, e Interior calla sobre el marcado forense. No sube a 4 porque las indicaciones no se siguen de forma mayoritaria y no baja a 2 porque medios, gobiernos y la OMS siguen marcando una referencia común."
      apoyos: [h3-02, h3-03, h3-04, h3-07, h3-08, h3-10]
    - id: respuesta_gobiernos
      valor: comunicacion
      justificacion: "El mundo está entre comunicacion y medidas_sectoriales y se elige la inferior: España ya da pasos sectoriales (refuerzo de urgencias oftalmológicas, pauta común para colegios aprobada por la mayoría de comunidades), pero la UE solo alinea mensajes sin medidas comunes, la OMS publica orientación sin convocar el Comité de Emergencias y no hay medidas de otros países. Además la pauta escolar son recomendaciones sin cierres y el conflicto laboral sigue sin criterio oficial."
      apoyos: [h3-03, h3-05, h3-06, h3-07, h3-08]
    - id: impacto_economico
      valor: 2
      justificacion: "Siguen siendo movimientos sectoriales: desvío de demanda a lámparas germicidas, pedidos por lotes de gafas homologadas al canal profesional, reclamaciones a supermercados y paradas en algunos tajos al aire libre. Está entre 2 y 3 y se elige el inferior porque las interrupciones laborales son puntuales y no hay caídas generales de índices ni disrupción operativa sostenida en varios sectores."
      apoyos: [h3-01, h3-06, h3-10]
    - id: adaptacion
      valor: 2
      justificacion: "Las pautas son más claras y operativas (aviso por tipo de lámpara, protocolo de urgencias, pauta común escolar, gafas homologadas por obligación del empresario, orientación de la OMS), pero poco seguidas: se compran germicidas, los adolescentes miran al sol como reto, se aplica 'si brilla, se tira' y en el Cono Sur se abandona el protector con índice UV extremo. No llega a 3 porque no hay indicio de que una parte relevante de la población las haya adoptado."
      apoyos: [h3-01, h3-02, h3-03, h3-05, h3-06, h3-07, h3-09, h3-10]

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
  tramo: h5
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
