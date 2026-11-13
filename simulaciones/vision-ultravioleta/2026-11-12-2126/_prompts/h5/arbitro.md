Eres el árbitro de una simulación de escenarios de Aftermath Studio. No pronosticas: consolidas lo que han dicho los agentes en un estado del mundo coherente.

## El mundo
Suceso: Todos los seres humanos desarrollan a la vez la capacidad de ver el espectro ultravioleta.
Momento cero: Martes, 10:00 hora de Madrid, simultáneo en todo el planeta. Alcance: global.
Supuestos (son hechos del mundo; no los discutas ni los expliques):
- El cambio es instantáneo y afecta a todas las personas, incluidos recién nacidos
- Se percibe el ultravioleta cercano (UV-A) como colores nuevos, sin perder la visión normal
- Los primeros días hay deslumbramiento y fatiga visual en exteriores con mucho sol; remite en unas dos semanas y no deja daño ocular permanente
- Nadie conoce la causa y nadie sabe si es permanente
Fuera de alcance: Explicar la causa del fenómeno; Efectos en animales

## Tus criterios
- Prevalece la afirmación con mecanismo más sólido y dato verificable
- Ante empate, se mantiene la tensión abierta para el siguiente tramo
- Entran primero los hechos que cambian el rumbo del mundo o afectan a otras áreas; los efectos locales o de detalle se descartan aunque sean plausibles
- Se descarta lo que solo repite, amplía o concreta un hecho ya establecido sin añadir una consecuencia nueva
- Se descartan las afirmaciones de confianza baja que no tengan dato
Plausibilidad: Las afirmaciones sin mecanismo no entran en el canon
Regla fija: una cifra sin fuente no entra en el canon como hecho. Descarta la afirmación o recoge su contenido sin la cifra.
Como máximo 10 hechos establecidos en este tramo. Todo lo demás va a descartadas con su motivo.

## Tramo que consolidas
Hora 5 (PT5H desde el suceso)
Estado del mundo anterior:
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

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h5
  afirmaciones:
  - texto: 'La ''reacción de Wall Street'' que tertulias y digitales llevan toda la mañana anunciando no llega en este tramo: la sesión regular de Nueva York abre a las 15:30 hora de Madrid, después del cierre de la hora 5. Las bolsas europeas pasan la sobremesa con menos volumen en los valores del relato (gafas, cosmética, autenticación) y mirando los futuros estadounidenses, y el economista dice en público que la apertura llegará con seis horas de relato ya descontado en preapertura y en Europa, así que lo relevante no será el primer minuto sino si el volumen se sostiene.'
    mecanismo: En noviembre Europa ya ha salido del horario de verano y Estados Unidos también, así que la diferencia entre Madrid y Nueva York es de seis horas y la campana de las 9:30 de Nueva York cae a las 15:30 en Madrid. A mediodía europeo los operadores reducen posiciones a la espera de la apertura americana, que es la que fija la referencia de liquidez. Al economista le conviene marcar antes de la campana qué mirar, el volumen sostenido y no el salto inicial, porque el primer minuto de una sesión con relato previo suele exagerar en cualquier sentido y él ha construido su prestigio en no sumarse a esos picos.
    dato: La sesión regular de NYSE va de 9:30 a 16:00 hora del Este.
    fuente: https://www.nyse.com/markets/hours-calendars
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - mercados financieros
    - medios
    id: economista/h5/1
  - texto: 'Las plataformas de reparto y las empresas de última milla en España tienen huecos de servicio en el pico de comidas: algunos repartidores asalariados invocan el riesgo grave e inminente o se niegan a salir sin gafas, y las empresas no paran el servicio sino que alargan los tiempos de entrega, concentran pedidos en menos repartidores y compran gafas homologadas por lotes. El conflicto laboral del deslumbramiento golpea primero al reparto porque es el sector al aire libre con más trabajadores jóvenes y con la demanda concentrada justo en las horas de más sol.'
    mecanismo: 'Desde que Glovo y otras plataformas pasaron a contratar a sus repartidores como asalariados, la Ley de Prevención de Riesgos Laborales se les aplica de lleno: la empresa tiene que evaluar el riesgo nuevo y dar los equipos de protección, y el repartidor puede acogerse al artículo 21 sin el riesgo de perder un encargo como autónomo. La franja de 13:00 a 15:00 es el pico de pedidos de comida y coincide con el sol más alto. Parar el servicio le cuesta a la plataforma el día de facturación y la cuota de mercado frente a la competencia; comprar gafas y aceptar entregas más lentas le cuesta poco, así que eso es lo que hace, aunque parte de los repartidores jóvenes no se las ponga.'
    dato: Glovo anunció en diciembre de 2024 que contrataría como asalariados a sus unos 15.000 repartidores en España.
    fuente: https://www.bolsamania.com/noticias_print/empresas/glovo-cambia-modelo-laboral-contratara-repartidores-espana--18229208.html
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - empleo
    - consumo
    - relaciones laborales
    - reparto
    id: economista/h5/2
  - texto: 'Consumo y otras autoridades de vigilancia del mercado europeas notifican a los grandes marketplaces los anuncios de lámparas germicidas UV-C presentadas como forma de ver los colores nuevos, y estos empiezan a retirarlos. La retirada funciona a medias: los vendedores reetiquetan el mismo producto con otro título (''lámpara de luz'', ''esterilizador'') y los vendedores fuera de la UE y las tiendas en redes sociales siguen vendiéndolas, de modo que la oferta baja en los escaparates grandes y se desplaza a canales menos vigilados.'
    mecanismo: El reglamento europeo de seguridad general de los productos obliga a los mercados en línea a retirar o desactivar sin demora indebida las ofertas de productos peligrosos cuando lo requiere una autoridad, y a retirar el producto en un plazo máximo de dos días hábiles tras la notificación. A un marketplace grande le sale más caro arriesgarse a una sanción y a un titular sobre quemaduras de córnea que perder unas ventas, así que actúa rápido sobre lo que le notifican. Pero la notificación va anuncio por anuncio y al vendedor oportunista le basta con cambiar el título, mientras que los vendedores que operan fuera del marco europeo o por redes sociales no responden a esas órdenes. Construye sobre la desviación de demanda a UV-C ya establecida.
    dato: Con las nuevas normas de seguridad de productos, un producto debe retirarse del mercado como máximo en dos días hábiles desde que la autoridad de vigilancia notifica al operador, y los mercados en línea deben retirar o bloquear sin demora indebida las ofertas peligrosas que les señalen.
    fuente: https://www.pinsentmasons.com/en-gb/out-law/news/heightened-eu-product-safety-rules-introduce-obligations-for-online-marketplaces
    confianza: media
    evidencia: dato
    areas_afectadas:
    - consumo
    - comercio electrónico
    - regulación
    - salud
    id: economista/h5/3
  - texto: 'Las cadenas de supermercados responden a la ola de reclamaciones por comida que fluoresce aceptando devoluciones y reembolsos sin reconocer defecto, y por detrás piden a sus proveedores de frutos secos, especias y maíz certificados de laboratorio de aflatoxinas para tener un papel que enseñar. El economista discrepa de que esto sea un problema económico relevante: el desperdicio se limita a los hogares que tienen lámpara, que son minoría tras el agotamiento, y el coste real recae en la relación entre cadenas y proveedores, no en el consumo agregado.'
    mecanismo: 'Para un supermercado, reembolsar una bolsa de almendras cuesta muy poco y discutir en caja si brilla o no brilla cuesta un vídeo viral; la política de devolución generosa es el seguro más barato. Pero la cadena necesita blindarse ante una posible inspección o un bulo que la señale, y la forma de trasladar ese riesgo es exigir analítica al proveedor, que paga el laboratorio y el retraso. La fluorescencia verde-amarilla bajo UV es una prueba solo presuntiva de aflatoxinas, con falsos positivos, y el propio sector la usa para decidir qué muestras mandar al laboratorio, no para tirar producto: ese matiz llega a la cadena y al proveedor, no al consumidor. Discrepo en parte de disruptor/h3/2: la ola existe, pero su escala la limita el número de lámparas en los hogares, que el propio agotamiento fijó.'
    dato: La fluorescencia verde-amarilla brillante bajo luz negra se usa como prueba presuntiva de aflatoxinas en maíz y debe confirmarse con análisis químico porque produce falsos positivos.
    fuente: https://crops.extension.iastate.edu/files/inline-files/blacklightprocess_20120829.pdf
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - distribución alimentaria
    - industria agroalimentaria
    id: economista/h5/4
  - texto: 'Con la apertura de las bolsas latinoamericanas en este tramo, la volatilidad de cosmética y protector solar que Europa tuvo en la hora 2 se repite en São Paulo sobre los valores locales de cosmética, pero con la lectura invertida respecto a Europa: allí pesa más el abandono preventivo del protector en plena primavera austral que la promesa de que todos comprarán protección. El economista señala que el único dato útil no será el precio de esas acciones sino las ventas de protector en farmacias del Cono Sur de los próximos días.'
    mecanismo: La bolsa brasileña abre a primera hora de la tarde europea y es el mercado líquido más cercano al Cono Sur, donde el abandono preventivo del protector ya es hecho establecido. Los operadores buscan un valor cotizado que represente la historia del día, y en cosmética latinoamericana hay pocos nombres grandes, así que concentran la apuesta. En Europa el relato podía leerse en los dos sentidos; en el Cono Sur la conducta observada esta mañana es dejar el protector en casa, lo que inclina la primera lectura a la baja. Al economista le interesa separar otra vez relato de dato verificable, porque las ventas de farmacia sí se publicarán y permitirán decir quién acertó.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - mercados financieros
    - consumo
    - Cono Sur
    id: economista/h5/5
  reacciona_a:
  - disruptor/h3/2
- agente: politico
  tramo: h5
  afirmaciones:
  - texto: 'Antes de las 15:00 el Ministerio de Trabajo, a través de la Inspección de Trabajo y del Instituto Nacional de Seguridad y Salud en el Trabajo, publica una nota informativa provisional sobre el deslumbramiento: lo califica como riesgo nuevo que las empresas deben evaluar y prevenir con gafas homologadas, sombra y reorganización de tareas en altura, moto y maquinaria, pero no lo declara con carácter general riesgo grave e inminente y remite cada paralización del artículo 21 a la valoración caso por caso. Sindicatos lo leen como respaldo a sus reclamaciones y patronales como aval para seguir trabajando, y los paros puntuales continúan en algunos tajos.'
    mecanismo: 'Un Gobierno que deja que cada tajo decida por su cuenta parece no tener el control, pero tampoco puede afirmar lo que sus técnicos no respaldan: el deslumbramiento remite en unas dos semanas y no deja daño ocular, así que no hay base técnica para un riesgo grave e inminente generalizado, y declararlo paralizaría la obra y el reparto en pleno mediodía. La Ley de Prevención ya obliga a evaluar riesgos nuevos y a dar los equipos de protección gratis, de modo que la nota no necesita norma nueva: recuerda obligaciones existentes. La fórmula ambigua es la que menos rectificación exige después, aunque deja el conflicto abierto en los centros donde el delegado ya ha parado.'
    dato: El artículo 21 de la Ley 31/1995 de Prevención de Riesgos Laborales permite al trabajador interrumpir su actividad y abandonar el lugar de trabajo cuando considere que la actividad entraña un riesgo grave e inminente para su vida o su salud.
    fuente: https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - laboral
    - gobierno
    - empresas
    - prevencion
    id: politico/h5/1
  - texto: 'Consumo y las autoridades autonómicas de vigilancia del mercado pasan del aviso declarativo a la orden: comunican a los grandes marketplaces que retiren los anuncios de lámparas germicidas UV-C publicitadas como forma de ver los colores nuevos, y Sanidad notifica el riesgo a la red europea Safety Gate. Las plataformas grandes retiran los anuncios más visibles en horas, pero los vendedores cambian el título, y los envíos directos desde fuera de la UE siguen llegando.'
    mecanismo: 'Con quemaduras de córnea por lámparas germicidas ya en urgencias, seguir solo con avisos sería un silencio que la oposición y el agitador capitalizarían. A diferencia de la hora 2, ahora hay base legal clara: el Reglamento europeo de seguridad general de los productos obliga a los mercados en línea a atender las órdenes de las autoridades de vigilancia en plazos breves, y el daño está acreditado por la sociedad de oftalmología. Para el Gobierno es una medida con efecto visible y sin riesgo de rectificación, porque ataca la conducta y el producto, no el fenómeno. Su límite es el de siempre: el anuncio se reescribe en minutos y la orden no alcanza al vendedor extracomunitario.'
    dato: El Reglamento (UE) 2023/988, aplicable desde diciembre de 2024, obliga a los proveedores de mercados en línea a actuar sin demora sobre las órdenes de las autoridades de vigilancia del mercado relativas a productos peligrosos.
    fuente: https://eur-lex.europa.eu/eli/reg/2023/988/spa
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - plataformas
    - sanidad
    - ue
    id: politico/h5/2
  - texto: La Agencia Española de Seguridad Alimentaria y Nutrición, con las autoridades autonómicas, publica a primera hora de la tarde un aviso de que la fluorescencia de un alimento bajo luz UV no indica que sea peligroso ni que esté manipulado, pide no tirar comida por ese motivo y canalizar las sospechas reales por los cauces de reclamación ordinarios. El aviso frena las llamadas pero no el bulo, porque el agitador lo presenta como otra prueba de que 'lo sabían'.
    mecanismo: 'Las reclamaciones a supermercados y las llamadas a seguridad alimentaria ya existen, y la comida es el terreno donde un vacío oficial más rápido se convierte en miedo. La agencia sí tiene respaldo técnico para decir que la fluorescencia es solo un cribado presuntivo que da falsos positivos, así que puede hablar sin riesgo de que la desmientan. Al Gobierno le sirve para mostrar control en un frente nuevo. Pero el mismo patrón de las horas anteriores se repite: cada explicación correcta que admite que el sector usaba esa luz es un fragmento de verdad que el agitador reencuadra como ocultación.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - alimentacion
    - consumo
    - desinformacion
    - gobierno
    id: politico/h5/3
  - texto: 'En el Cono Sur los ministerios de salud, con Chile a la cabeza, salen a media mañana local a contradecir el abandono preventivo del protector: recuerdan que el índice UV de primavera es alto o extremo, que el fenómeno no cambia el riesgo de quemadura y que el protector debe seguir usándose aunque ''se vea'', y en Chile la autoridad laboral recuerda a las empresas su obligación de proteger a quien trabaja al sol. El mensaje llega tarde para quien ya salió de casa sin protector.'
    mecanismo: Esos gobiernos tienen ya marcos legales y campañas permanentes contra la radiación solar, así que pueden reaccionar con una base existente y sin afirmar nada sobre el fenómeno, que sus técnicos no respaldan. Ganan legitimidad si parecen anticiparse a las quemaduras, que en su caso son previsibles y masivas, y la pierden si las urgencias se llenan de quemados sin aviso. Pero la decisión de no ponerse protector se tomó al amanecer, antes de cualquier mensaje oficial, de modo que el aviso reduce el daño de la tarde y no el de la mañana.
    dato: La Ley 20.096 de Chile establece mecanismos de control de la radiación ultravioleta, incluida la difusión del índice UV y obligaciones de información y protección, y la normativa laboral chilena obliga al empleador a proteger a los trabajadores expuestos a radiación UV de origen solar.
    fuente: https://www.bcn.cl/leychile/navegar?idLey=20096
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - cono_sur
    - laboral
    - internacional
    id: politico/h5/4
  - texto: 'Con el amanecer en la Costa Este, la respuesta federal de Estados Unidos sale fragmentada: la Casa Blanca convierte el fenómeno en mensaje político propio y evita advertencias sanitarias, mientras la agencia federal del medicamento y los centros de control de enfermedades reactivan sus avisos existentes sobre lámparas y varitas UV-C. La diferencia de tono entre el escaparate político y la voz técnica se convierte en material para los matinales y obliga a los gobiernos europeos a defender que su mensaje sanitario no es alarmismo.'
    mecanismo: 'Algunos líderes ya rompieron la prudencia en la primera hora, y un ejecutivo que compite por la conversación matinal gana más con un encuadre de oportunidad o de orgullo que con un aviso de riesgo. Las agencias técnicas, en cambio, no necesitan decidir nada nuevo: la agencia del medicamento ya advirtió en la pandemia de que ciertas lámparas y varitas UV-C emiten radiación capaz de dañar ojos y piel, así que les basta con reactivar ese aviso. Esa doble voz da a la oposición y al agitador europeos un contraste fácil (''allí no alarman''), y a los gobiernos europeos un incentivo para anclarse en la orientación técnica de la OMS.'
    dato: La FDA emitió una comunicación de seguridad advirtiendo de que algunas varitas UV para desinfección emiten niveles de radiación UV-C que pueden causar lesiones en piel y ojos tras pocos segundos de uso.
    fuente: https://www.fda.gov/medical-devices/safety-communications/do-not-use-ultraviolet-uv-wands-give-unsafe-levels-radiation-fda-safety-communication
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - estados_unidos
    - internacional
    - comunicacion
    - sanidad
    id: politico/h5/5
  reacciona_a:
  - disruptor/h3/3
  - economista/h3/1
  - disruptor/h3/2
  - disruptor/h3/1
  - medios/h3/2
- agente: medios
  tramo: h5
  afirmaciones:
  - texto: 'Los informativos de sobremesa, que en España emiten en torno a las 15:00 y son la franja informativa de más audiencia del día, abren con los primeros casos de quemadura de córnea y cada cadena construye su propio ''contador de afectados'' sumando hospital por hospital. Como no hay un dato oficial agregado, las cifras difieren entre medios, y circulan a la vez tres números que no miden lo mismo: los casos que confirman los hospitales, las ''miles de respuestas'' del registro de la sociedad de oftalmología, que algunos titulares presentan como afectados, y el recuento de ''síntomas tardíos'' del agitador, que siempre es el más alto y se presenta como ''la cifra que no dan''.'
    mecanismo: 'Un medio necesita una cifra para abrir un informativo, y la competencia por darla primero lleva a sumar fuentes parciales (un hospital, una comunidad, un portavoz) en vez de esperar al dato de Sanidad, que el protocolo de registro por fuente de exposición todavía no ha agregado. El registro de testimonios de la sociedad de oftalmología se mide en respuestas, no en pacientes, pero ''miles'' es un número disponible y con fuente con nombre, y la confusión entre participantes y afectados es el error típico de un directo con prisa. El agitador no necesita inventar nada: su formulario abierto no filtra, así que su número crece más rápido que cualquier recuento clínico y la diferencia entre ambos le sirve para hablar de ocultación.'
    dato: El Telediario 1 de La 1 de TVE se emite a las 15:00.
    fuente: https://en.wikipedia.org/wiki/Telediario
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - sanidad
    - desinformacion
    - politica
    id: medios/h5/1
  - texto: 'El periodismo de consumo convierte las lámparas germicidas en su historia propia de la tarde: digitales y programas de televisión localizan en los marketplaces anuncios de lámparas UV-C promocionadas para ''ver los colores nuevos'' y piden explicaciones a las plataformas. Los marketplaces retiran los anuncios señalados en España y en la UE, pero los vendedores los vuelven a publicar con otro título, y la pieza ''los retiran y vuelven a salir'' se repite durante horas.'
    mecanismo: 'Es un ángulo con culpable identificable, víctimas en urgencias y una prueba que el periodista puede capturar en pantalla, justo lo que pide una sobremesa. Existe un precedente con autoridad que da fuente inmediata: tras la pandemia, la agencia estadounidense del medicamento avisó de que algunos dispositivos UV-C de consumo emitían radiación capaz de dañar ojos y piel en segundos. Los marketplaces responden rápido a la presión mediática con retiradas puntuales porque les sale barato, pero su moderación se hace anuncio a anuncio y el vendedor solo tiene que cambiar el título, sobre todo si opera fuera de la UE, donde el aviso de Consumo no le alcanza.'
    dato: La FDA advirtió en 2022 de que algunas varitas UV de consumo emiten niveles de radiación inseguros que pueden lesionar piel y ojos tras pocos segundos de exposición.
    fuente: https://www.fda.gov/medical-devices/safety-communications/do-not-use-ultraviolet-uv-wands-give-unsafe-levels-radiation-fda-safety-communication
    confianza: media
    evidencia: dato
    areas_afectadas:
    - medios
    - consumo
    - sanidad
    - plataformas
    id: medios/h5/2
  - texto: Los medios descubren el reto adolescente de mirar al sol o a la lámpara de uñas para 'abrir la vista' y lo cubren como 'reto viral peligroso', con advertencias y testimonios de padres. La cobertura lo da a conocer a menores que no lo habían visto, y las plataformas grandes empiezan a retirar los vídeos por sus normas sobre retos peligrosos, con lo que el reto pasa a grupos de mensajería y a perfiles efímeros, donde ni medios ni plataformas pueden seguir su alcance.
    mecanismo: Un reto con menores en riesgo es una de las piezas que más se comparten entre padres, y cada medio la publica con el nombre del reto y la descripción de lo que se hace, que es justo la información que hace falta para copiarlo. Ya ocurrió con el reto de las cápsulas de detergente en 2018, cuando la cobertura masiva coincidió con un aumento de llamadas a los centros de toxicología. Como mirar al sol no duele en el momento, el aviso del medio no frena al adolescente que ya ve en el reto una forma de ganar estatus, y la retirada en plataformas grandes desplaza el contenido a espacios cerrados, igual que ya pasó con el agitador.
    dato: En enero de 2018 los centros de toxicología de Estados Unidos habían recibido 86 llamadas relacionadas con el reto de las cápsulas de detergente en las primeras semanas del año, en pleno pico de cobertura mediática.
    fuente: https://wptv.com/news/national/the-tide-pod-challenge-has-prompted-86-calls-to-poison-control-centers-in-2018
    confianza: media
    evidencia: dato
    areas_afectadas:
    - medios
    - menores
    - sanidad
    - plataformas
    id: medios/h5/3
  - texto: 'Con los matinales de Estados Unidos en antena entre las 13:00 y las 15:00 hora de Madrid, la conversación en inglés se parte por líneas partidistas: unas cadenas encuadran el suceso como salud pública y seguridad vial en la hora punta, y otras dan espacio a la pregunta de qué sabía el Gobierno sobre el marcado UV. Los medios españoles importan los vídeos de amaneceres estadounidenses para la sobremesa y, con ellos, el debate sobre las ''marcas'', que llega reforzado desde fuera.'
    mecanismo: 'Es la misma tesis que propuse en la hora 3, ajustada al reloj: en la Costa Este el suceso cayó de madrugada y la primera luz del día llega a primera hora de la mañana local, que en Madrid es el arranque de la tarde, así que la ola en inglés se produce en este tramo. El ecosistema mediático estadounidense está polarizado por audiencias, y el marcado forense y de billetes tiene allí un encaje directo en la desconfianza hacia el Gobierno federal. Para un medio español, el contenido estadounidense es material nuevo, en imagen y gratuito por agencias, y la versión conspirativa en inglés da al agitador local una fuente extranjera que citar.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - medios
    - internacional
    - desinformacion
    id: medios/h5/4
  - texto: Policía e Interior piden en privado a directores y jefes de sección que no detallen en sus piezas qué productos de marcado forense existen, dónde se aplican y cómo se limpian. Las cabeceras generalistas editan sus textos sin avisarlo o lo hacen con una nota, mientras digitales de clic y el agitador mantienen los detalles; el agitador presenta las ediciones, con capturas del antes y el después, como prueba de censura coordinada.
    mecanismo: Interior ha elegido el silencio público y la vía interna, y la forma ordinaria de extender esa vía a los medios es la petición extraoficial a los responsables editoriales, que no deja rastro de censura formal. A una cabecera seria le cuesta poco quitar detalles operativos y le conviene no quedar como manual para delincuentes, pero el contenido ya está copiado y archivado. Los digitales que viven del tráfico no tienen ese freno. Cualquier cambio en un artículo publicado se puede comparar con versiones archivadas, y para el agitador una edición silenciosa es la confirmación más barata de que 'les han llamado'.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - medios
    - seguridad
    - desinformacion
    - politica
    id: medios/h5/5
  reacciona_a:
  - oftalmologa/h3/3
  - agitador/h3/1
  - adolescente/h3/2
  - economista/h3/1
  - politico/h3/4
- agente: oftalmologa
  tramo: h5
  afirmaciones:
  - texto: 'A primera hora de la tarde las urgencias reciben, además de los primeros casos de fotoqueratitis, muchas consultas de personas con escozor, lagrimeo o cansancio ocular que temen los ''síntomas tardíos'' anunciados por el agitador. La sociedad de oftalmología añade a su protocolo una instrucción sencilla: tinción con fluoresceína y lámpara de hendidura en todos los casos, porque la fotoqueratitis deja una queratitis punteada visible y el deslumbramiento y la fatiga del fenómeno dejan la córnea limpia. Lo comunica en público como la forma de distinguir con una prueba objetiva la lesión por exposición del cansancio benigno.'
    mecanismo: 'El registro del agitador es testimonial y los síntomas que recoge (escozor, arena, lagrimeo) son comunes a la fatiga visual, al ojo seco y a la fotoqueratitis, así que con palabras no se pueden separar. La tinción con fluoresceína es una exploración barata, rápida y disponible en cualquier urgencia, y la fotoqueratitis produce erosiones epiteliales punteadas que se ven con luz azul cobalto, mientras que el deslumbramiento del fenómeno no lesiona el epitelio. Cada historia clínica con hora, fuente de exposición y resultado de la tinción convierte la oleada en datos verificables, que es lo único que la sociedad puede oponer a una base de testimonios que los verificadores no pueden contrastar. Discrepo del encuadre de agitador/h3/1: los síntomas tardíos existen, pero tienen un signo objetivo y una causa conocida.'
    dato: Los síntomas de la queratitis por ultravioleta aparecen típicamente entre 6 y 12 horas tras la exposición; la fluoresceína muestra erosiones epiteliales punteadas y el epitelio se regenera en unas 36 a 72 horas; los anestésicos tópicos no deben usarse como tratamiento porque retrasan la curación.
    fuente: https://eyerounds.org/cases/306-ultraviolet-keratitis.htm
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - sanidad
    - informacion
    - desinformacion
    id: oftalmologa/h5/1
  - texto: Llegan a las unidades de retina los primeros casos sospechosos de retinopatía solar, sobre todo adolescentes y jóvenes que miraron al sol por el reto de 'abrir la vista' o para buscar los colores nuevos, con mancha central o visión deformada. La sociedad pide tomografía de coherencia óptica (OCT) macular a todo el que refiera mancha central y advierte en público de que la mayoría de quienes consulten por miedo no tendrán lesión, pero que los pocos confirmados pueden conservar una pequeña mancha durante meses.
    mecanismo: La retinopatía solar da síntomas el mismo día de la exposición, a diferencia de la fotoqueratitis, y su lesión foveal se documenta con OCT, de modo que es la única secuela de la jornada que puede acreditarse con imagen y que puede no curarse del todo. Tras los eclipses, muchas más personas consultan por miedo que las que tienen hallazgos compatibles, y esa proporción es la que la sociedad necesita fijar antes de que el agitador presente cada consulta como un daño. Dar ya la regla (muchos sustos, pocos casos, todos con exposición directa al sol) protege su credibilidad cuando aparezca el primer caso con secuela, que será real y llevará nombre y edad.
    dato: Tras el eclipse solar de 2017, en Utah, 27 pacientes consultaron por cambios en la visión y 6 tenían una exploración compatible con retinopatía solar; uno de los casos refirió síntomas desde el mismo día del eclipse.
    fuente: https://www.dovepress.com/the-ophthalmic-fallout-in-utah-after-the-great-american-solar-eclipse-peer-reviewed-fulltext-article-OPTH
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - menores
    - desinformacion
    id: oftalmologa/h5/2
  - texto: 'La sociedad de oftalmología y la de pediatría difunden una nota conjunta para familias con bebés y niños pequeños: el deslumbramiento del fenómeno es más intenso en ellos porque su cristalino deja pasar mucho más ultravioleta que el de un adulto, y son también los más vulnerables si miran al sol. Recomiendan capota o sombrilla en carritos, gorra con visera y no sacar a los bebés al sol directo de mediodía, sin gafas de juguete sin homologar.'
    mecanismo: 'El gradiente por edad del canon tiene una base física conocida: el cristalino amarillea con los años y filtra cada vez más ultravioleta, de modo que en un niño pequeño llega mucho más UV-A a la retina. Eso explica que los niños vean los colores con más intensidad y se quejen más del deslumbramiento, pero también que un niño que mira al sol reciba en la retina una dosis mayor que un adulto en el mismo tiempo. Los recién nacidos no pueden decir que les molesta la luz y lo expresan llorando o cerrando los ojos, lo que ya está llenando las consultas de pediatría. Una nota conjunta convierte el gradiente en una pauta concreta y deja a la sociedad como referencia también fuera de la oftalmología.'
    dato: En menores de 10 años el cristalino transmite más del 75 % de la radiación ultravioleta, frente a alrededor del 10 % en mayores de 25 años (cifra atribuida a una revisión de Fishman de 1986).
    fuente: https://www.zeiss.com/vision-care/us/eye-health-and-care/health-prevention/why-kids-glasses-should-offer-the-best-uv-protection.html
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - menores
    - familias
    - consumo
    id: oftalmologa/h5/3
  - texto: 'Ante las consultas de Inspección de Trabajo, mutuas y servicios de prevención, la sociedad de oftalmología ofrece un criterio técnico para el conflicto laboral: el deslumbramiento del fenómeno es una molestia transitoria que se controla con filtros solares de uso laboral homologados, no un riesgo grave e inminente por sí mismo, salvo en tareas donde un deslumbramiento súbito pueda causar un accidente (trabajo en altura, conducción de vehículos o grúas) mientras no se hayan entregado esos filtros. El criterio desplaza los paros a una obligación de equipo de protección y la mayoría de tajos se reanudan en cuanto llegan las gafas.'
    mecanismo: 'Inspección y mutuas no pueden contestar sin un criterio técnico y nadie más lo tiene: la sociedad ya fijó que el deslumbramiento remite en unas dos semanas y no deja daño. La normativa de equipos de protección ya contempla filtros solares para uso laboral, así que el problema tiene una solución dentro de la norma vigente sin crear una nueva. Distinguir entre la molestia general y el riesgo de accidente en tareas concretas da a los delegados de prevención la razón donde la tienen y quita base al paro generalizado. Discrepo en parte de disruptor/h3/3: el artículo 21 encaja en algunos puestos y momentos, no en el trabajo al aire libre en general. Para la sociedad, que su criterio aparezca en la respuesta de Inspección amplía su autoridad al terreno laboral.'
    dato: La normativa de protección ocular laboral incluye filtros de protección solar para uso laboral (EN 172), en transición a la serie EN ISO 16321.
    fuente: https://insst.es/documents/d/portal-insst/normas-proteccion-ocular-y_o-facial-diciembre-2024-
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - trabajo
    - prevencion
    - sanidad
    id: oftalmologa/h5/4
  - texto: 'Las sociedades de oftalmología de Chile, Argentina y Uruguay adoptan casi sin cambios la nota de triaje, el aviso por tipo de lámpara y el protocolo de urgencias de la sociedad española, y lo difunden en su mañana citándola como fuente. La sociedad española pasa a ser la referencia clínica del fenómeno en español, pero queda también expuesta: los casos del Cono Sur, con más sol, se compararán con sus previsiones.'
    mecanismo: En el Cono Sur el fenómeno llega con horas de retraso, en el mismo idioma y con los documentos ya escritos, así que adoptarlos es lo más rápido y barato para unas sociedades que no tienen tiempo de elaborar los suyos; las redes de sociedades iberoamericanas facilitan la circulación. La primavera austral, con más radiación que el noviembre europeo, hará que allí los casos de fotoqueratitis y retinopatía solar sean más frecuentes e intensos, de modo que el protocolo español se pondrá a prueba antes y con más carga en otro país. Si funciona, la autoridad de la sociedad sale reforzada; si los casos superan lo anunciado, el agitador tendrá un argumento importado.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - sanidad
    - internacional
    - informacion
    id: oftalmologa/h5/5
  reacciona_a:
  - agitador/h3/1
  - adolescente/h3/2
  - disruptor/h3/3
  - disruptor/h3/1
- agente: adolescente
  tramo: h5
  afirmaciones:
  - texto: 'A media tarde, después de comer, dos o tres de mi entorno que hicieron el reto de mirar cerca del sol o la lámpara de uñas empiezan a notar escozor, lagrimeo y como arena en los ojos, y lo preguntan primero en el grupo de amigas y no a sus padres: se ponen gafas de sol dentro de casa o se encierran en la habitación diciendo que les duele la cabeza, y esperan a ver si se pasa.'
    mecanismo: Lo hicieron hace unas horas y la quemadura de córnea aparece con retraso, así que les llega ahora, ya en casa. Contarlo a los padres es confesar que hicieron justo lo que la tele y el instituto llevan todo el día diciendo que no se haga, y eso significa bronca, castigo y quedarse sin móvil. Entre nosotras preferimos taparnos y buscar en internet o preguntar al grupo, y eso retrasa que vayan al médico hasta que el dolor es demasiado fuerte, ya por la noche.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - familia
    - menores
    id: adolescente/h5/1
  - texto: 'Cuando uno de los que fue a urgencias sube un vídeo o una historia contándolo, con el ojo rojo y el parche o las gotas, se hace viral en clase y fuera: tiene más visualizaciones que todo lo que ha subido en su vida, y otros empiezan a contar ''mi experiencia'' aunque solo les piquen un poco los ojos.'
    mecanismo: En todo el día los vídeos no podían enseñar los colores, y un ojo rojo es lo primero del fenómeno que sí se ve en cámara. Contar que has acabado en urgencias da atención y estatus aunque sea por haber hecho una tontería, y como nadie puede comprobar cuánto te duele, cada uno lo exagera. Esos vídeos acaban sirviendo de testimonio a quien quiere decir que esto hace daño, aunque el que lo cuenta diga que miró al sol.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - salud
    - menores
    - desinformacion
    id: adolescente/h5/2
  - texto: 'En el grupo de WhatsApp de madres de mi clase empiezan a circular nombres de quiénes hicieron el reto y quiénes estuvieron en casa de la amiga con la lámpara, y en mi grupo se monta un lío de chivatos: hay quien acusa a otro de haberlo animado y capturas que pasan de nuestros grupos al de los padres.'
    mecanismo: Con las noticias de quemaduras en menores, los padres tienen miedo y buscan quién estaba con su hijo y quién llevó la lámpara o propuso el reto, y el grupo de madres es donde eso se pregunta. Nosotros, para no ser el culpable ante nuestros padres, señalamos a otro; y quien ya tenía pique con alguien lo aprovecha. Lo que pasa dentro del grupo de amigas deja de ser privado justo cuando más nos importa que no se sepa.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - familia
    - menores
    - educacion
    - convivencia
    id: adolescente/h5/3
  - texto: Mis padres y los de mis amigas esconden o tiran la lámpara de uñas y la linterna de luz negra y nos prohíben quedar esta tarde, así que el plan se pasa a videollamadas y a salir a la calle o a la azotea a última hora, cuando el sol está bajo y ya no deslumbra tanto, que vendemos a los padres como 'solo un rato'.
    mecanismo: El aviso de Consumo sobre lámparas de uñas y los primeros casos de quemaduras hacen que los padres vean la lámpara de casa como un peligro concreto que pueden quitar ellos mismos, y prohibir quedar es lo que tienen a mano. Nosotros dependemos de su permiso, pero seguimos queriendo ver los colores juntos, y al atardecer la luz molesta menos y parece más inofensivo, así que es lo que podemos negociar sin pelearnos del todo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - familia
    - menores
    - consumo
    id: adolescente/h5/4
  - texto: Por la tarde mi TikTok se llena de vídeos en inglés de gente de Estados Unidos viendo su primer amanecer con los colores nuevos, y en mi grupo empezamos a usar sus palabras en inglés para los colores en vez de las que nos inventamos esta mañana, porque suenan más guay y entran en más tendencias.
    mecanismo: El algoritmo empuja lo nuevo y lo que más se comparte, y por la tarde en España lo nuevo es la mañana de allí. Entre los de mi edad lo que viene en inglés y de creadores grandes tiene más estatus que lo de nuestra clase, y usar su palabra te mete en la tendencia mundial. Así los nombres de la mañana, que se peleaban grupo a grupo, pierden contra uno o dos términos en inglés, al menos entre adolescentes, mientras los mayores y los medios siguen con otros.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - lenguaje
    - cultura
    id: adolescente/h5/5
  reacciona_a:
  - medios/h3/2
  - medios/h3/4
- agente: agitador
  tramo: h5
  afirmaciones:
  - texto: 'Hacia la hora 5 el agitador vuelca en directo el recuento de su registro de ''síntomas tardíos'' y lo presenta como prueba masiva de daño: el formulario se llena sobre todo de fatiga visual, deslumbramiento y escozor en exteriores, que mezcla en una sola categoría con los casos de urgencias. El volumen de respuestas, no su contenido, se convierte en el titular de su canal, y verificadores y medios no tienen forma de contrastarlo.'
    mecanismo: 'Los supuestos del mundo garantizan que casi todo el que sale a la calle sufre deslumbramiento y fatiga visual los primeros días, sin daño permanente. Un formulario que pregunta por molestias oculares recoge por tanto respuestas afirmativas de casi cualquiera, y el registro se confirma a sí mismo. Al agitador no le hace falta inventar nada: le basta con no separar la molestia esperada y benigna de la lesión por conducta. El dato está en un canal cerrado y es testimonial, así que nadie externo puede depurarlo, y la cifra grande le da relevancia y donaciones justo antes de la noche.'
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - salud
    - informacion
    - redes
    id: agitador/h5/1
  - texto: El agitador se apropia de la distinción que hizo la sociedad de oftalmología entre fotoqueratitis, que se cura, y retinopatía solar, que puede dejar una mancha central persistente, y la presenta como reconocimiento de que 'hay daño permanente'. Cuando aparecen los primeros casos de retinopatía con visión borrosa o mancha central, los convierte en los rostros de su relato, sin mencionar que vienen de mirar al sol.
    mecanismo: 'La retinopatía solar da síntomas en horas tras mirar al sol y puede dejar un escotoma central que no se resuelve del todo; es la única lesión del día que encaja con ''daño irreversible'', y la propia sociedad la ha nombrado en su protocolo. España tiene además el precedente reciente del eclipse de agosto de 2026, con avisos públicos sobre esta lesión, lo que hace la palabra reconocible para su audiencia. Repite el patrón que le funcionó con el BCE y con la nota de triaje: tomar una explicación técnica correcta y cambiar su significado, omitiendo la causa conductual. Un solo caso con secuela vale más para él que cien fotoqueratitis que se curan en días.'
    dato: La retinopatía solar se produce al mirar al sol sin protección y puede causar una mancha central o visión borrosa persistente; tras el eclipse de agosto de 2026 hubo avisos públicos sobre cómo reconocer el daño ocular.
    fuente: https://www.health.wa.gov.au/Articles/S_T/Solar-retinopathy ; https://www.euronews.com/2026/08/12/how-to-tell-if-the-eclipse-damaged-your-eyes-key-warning-symptoms
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - informacion
    - politica
    id: agitador/h5/2
  - texto: 'El agitador ataca el protocolo de urgencias que anota la fuente de exposición: lo presenta como un sistema para ''culpar a la víctima'' y anima a sus seguidores a no declarar en urgencias que miraron al sol o usaron lámparas. Una parte de los pacientes de su audiencia omite la exposición, crece en las historias clínicas la categoría de fuente desconocida o no declarada, y él la anuncia de antemano como la cifra que demostrará el daño del fenómeno.'
    mecanismo: 'El protocolo de la sociedad es la herramienta con la que se piensa demostrar, con datos propios, que las lesiones vienen de la conducta; por eso es la amenaza principal a su historia y no puede ignorarlo. No necesita desmontarlo técnicamente: basta con que una minoría de pacientes no informe de la exposición para que aparezca un residuo de casos ''sin causa'' que nadie puede explicar, y ese residuo es exactamente el material que necesita. Además desplaza el foco de la conducta de sus seguidores, que él mismo empujó a buscar marcas con lámparas en la hora 2, a la supuesta mala fe del médico que pregunta.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - datos_clinicos
    - informacion
    id: agitador/h5/3
  - texto: En paralelo, el agitador manda a su audiencia a rellenar también el registro abierto de testimonios de la sociedad de oftalmología con sus síntomas, convertido en campaña de participación. El registro, que se presentaba como el primer estudio sistemático del fenómeno, recibe una oleada de respuestas sugestionadas y coordinadas que la sociedad no puede filtrar a tiempo, y tiene que anunciar controles o cerrar campos abiertos.
    mecanismo: 'Un formulario abierto sin verificación de identidad ni control de duplicados es vulnerable a la entrada masiva de una comunidad organizada, y la sociedad lo lanzó precisamente para ser la autoridad común de gobiernos y plataformas. Si sus primeros resultados descriptivos salen cargados de ''síntomas tardíos'', el agitador gana dos veces: o el registro respalda su relato, o la sociedad tiene que depurarlo y él lo presenta como manipulación de datos. Discrepa del supuesto de oftalmologa/h3/3 de que el riesgo es solo la sugestión individual: aquí la contaminación es coordinada.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - salud
    - investigacion
    - informacion
    id: agitador/h5/4
  - texto: 'El agitador abre su canal a testimonios de Chile, Argentina y Uruguay: las primeras rojeces y quemaduras de piel de quienes salieron sin protector por la mañana le llegan en su mismo idioma y las suma a su relato de daño diferido, con lo que gana audiencia latinoamericana justo cuando en Europa el directo empieza a quedarse sin novedad.'
    mecanismo: La quemadura solar aparece varias horas después de la exposición, así que quienes dejaron el protector al amanecer austral empiezan a notarla a lo largo de la mañana y la tarde de allí, en plena franja de la hora 5 en Madrid. El abandono del protector fue preventivo y alimentado por el estigma construido en Europa, en parte en su propio canal, y el índice UV es alto en esa época. Compartir idioma le permite captar ese público sin traducción, mientras la segunda ola viral en inglés de Estados Unidos desplaza el relato europeo en las plataformas grandes; para él, Latinoamérica es la expansión natural que el mercado en inglés no le ofrece.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - redes
    - internacional
    id: agitador/h5/5
  reacciona_a:
  - oftalmologa/h3/2
  - oftalmologa/h3/3
  - disruptor/h3/1
  - medios/h3/2
- agente: disruptor
  tramo: h5
  afirmaciones:
  - texto: 'Asia oriental, donde el suceso llegó al caer la tarde (17:00 en Tokio, 16:00 en Pekín) y lleva ya horas de noche, se convierte sin quererlo en el laboratorio de la primera noche del fenómeno: desde Japón, China y Corea llegan a Europa, antes de su atardecer, testimonios de que con luz LED los colores nuevos casi desaparecen y con tubos y bombillas fluorescentes siguen viéndose. En Europa, que encara su primera noche hacia las 18:00, arranca una búsqueda de tubos fluorescentes y bombillas de bajo consumo antiguas, que la UE ya ha retirado del mercado, y el stock residual de almacenes, ferreterías y segunda mano se encarece.'
    mecanismo: Los LED blancos de uso doméstico emiten muy poco por debajo de 400 nm, mientras que los fluorescentes de mercurio dejan escapar algo de UV-A a través del fósforo y del vidrio. En Japón y buena parte de Asia oriental los fluorescentes siguen muy presentes en casas y oficinas porque su prohibición de fabricación e importación no llega hasta finales de 2027, así que allí la diferencia entre lámparas se nota en millones de hogares a la vez. Europa, que ya ha hecho la transición a LED por la retirada del RoHS de 2023, recibe ese conocimiento horas antes de necesitarlo y reacciona comprando lo que ya no se fabrica para su mercado, que es por definición escaso. El relato de las horas anteriores se ha centrado en el sol y en las lámparas de luz negra; nadie ha pensado en qué pasa con la iluminación general cuando se haga de noche.
    dato: La UE retiró los tubos lineales T5 y T8 el 25 de agosto de 2023 y las fluorescentes compactas sin balasto integrado el 25 de febrero de 2023; Japón prohíbe fabricar, exportar e importar fluorescentes de iluminación general a finales de 2027.
    fuente: https://www.licht.de/en/service/timetable-for-lamp-exit ; https://www.city.inagi.tokyo.jp/en/kurashi/gomi/1005088/1005103/1013185.html
    confianza: media
    evidencia: dato
    areas_afectadas:
    - consumo
    - iluminacion
    - comercio
    - asia
    - europa
    - cadena_de_suministro
    id: disruptor/h5/1
  - texto: Empiezan a aparecer en centros de salud, urgencias y farmacias reacciones fototóxicas en la piel (enrojecimiento, quemazón, ampollas en cara, escote y dorso de las manos) en personas que toman fármacos fotosensibilizantes muy comunes, sobre todo mayores con diuréticos o antihipertensivos y gente que se automedica con ibuprofeno o naproxeno para el dolor de cabeza del deslumbramiento. Son personas que salieron al sol a mirar los colores o que dejaron el protector para no llevar la máscara, y sus lesiones llegan antes que la oleada nocturna de fotoqueratitis, por una vía que el protocolo de urgencias, centrado en los ojos, no contempla.
    mecanismo: 'La fototoxicidad por fármacos la desencadena sobre todo el UV-A y aparece en minutos u horas en la piel expuesta, no al día siguiente. Dos conductas ya establecidas en el canon la activan a la vez: el abandono del protector solar por la máscara visible y las salidas a la calle a mediodía para ver los colores. A eso se suma una tercera: la fatiga visual y el deslumbramiento provocan cefaleas que mucha gente trata con antiinflamatorios sin receta, que también son fotosensibilizantes. Quien toma hidroclorotiazida, amiodarona o doxiciclina no suele saberlo, y el mensaje oficial de las horas anteriores habla de ojos, no de piel. Para el agitador, unas quemaduras en la piel de ancianos que ''no estuvieron tanto al sol'' encajan mejor en el relato de daño del fenómeno que una córnea quemada por mirar una lámpara.'
    dato: Las reacciones fototóxicas aparecen en minutos u horas en la piel expuesta al sol; entre los fármacos implicados figuran hidroclorotiazida, furosemida, amiodarona, doxiciclina, ciprofloxacino, ibuprofeno y naproxeno.
    fuente: https://dermnetnz.org/topics/drug-induced-photosensitivity
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - farmacia
    - dermatologia
    - personas_mayores
    - comunicacion_de_riesgo
    id: disruptor/h5/2
  - texto: En mercados, bares y comercios pequeños, donde se paga en efectivo y se atiende cerca de la puerta o en la calle, clientes y dependientes empiezan a mirar los billetes a la luz del día y a rechazar los que 'brillan' o los que 'no tienen fibras de colores'. Salen a la luz algunos billetes falsos que llevaban tiempo circulando, pero también se rechazan billetes auténticos que pasaron por la lavadora o se mancharon con productos de limpieza, y el Banco de España y las policías locales reciben llamadas por discusiones en caja.
    mecanismo: 'El papel del billete en euros auténtico se ve apagado bajo ultravioleta y lleva fibras que se iluminan en verde, rojo y azul; una falsificación impresa en papel corriente suele brillar porque lleva blanqueantes ópticos. Esa comprobación la hacían antes solo las máquinas y los cajeros con lámpara; ahora la luz de la calle la pone al alcance de todos, sin formación para interpretarla. Los blanqueantes de los detergentes se adhieren al billete lavado y lo hacen brillar como uno falso, y el desgaste borra parte del contraste. Quien rechaza un billete lo hace por la regla más simple, igual que con la comida en el tramo anterior: si brilla, es malo. El conflicto se concentra en el comercio de efectivo y en zonas soleadas, no en los bancos.'
    dato: Bajo luz UV el papel del billete auténtico no brilla ('el papel es mate') y las fibras incrustadas se ven en verde, rojo y azul.
    fuente: https://www.bundesbank.de/content/755350
    confianza: media
    evidencia: dato
    areas_afectadas:
    - efectivo
    - comercio_minorista
    - banca_central
    - seguridad
    - orden_publico
    id: disruptor/h5/3
  - texto: 'La retirada europea de la iluminación fluorescente cambia de signo en el debate público de la tarde: aparecen las primeras peticiones, de asociaciones de consumidores, de hosteleros nocturnos y de algún cargo político, para que la UE o los Gobiernos autoricen de forma temporal la venta del stock de fluorescentes que queda en almacenes, y los fabricantes de iluminación anuncian ''LED con UV-A'' que todavía no existen para uso doméstico. Ecologistas y la propia normativa contra el mercurio se convierten en blanco inesperado del enfado.'
    mecanismo: 'Cuando un producto deseado está prohibido, la frustración busca un culpable con nombre, y aquí lo hay: una norma europea reciente y concreta. Para un partido de la oposición o un sector como el ocio nocturno, pedir una excepción temporal es barato y visible. Los fabricantes tienen incentivo a anunciar antes de poder fabricar, porque captar la intención de compra hoy vale más que el producto dentro de meses; los LED de 365 nm existen como componente, pero no como lámpara de iluminación general segura y homologada. El efecto es político y comercial a la vez, y abre un frente que nadie ha previsto entre una medida ambiental y un deseo nuevo de la población.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - politica
    - regulacion_ue
    - medio_ambiente
    - industria_iluminacion
    - consumo
    id: disruptor/h5/4
  reacciona_a: []

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

estado_del_mundo:
  tramo: h5
  resumen: "..."
  hechos_establecidos:
    - id: h5-01
      texto: "..."
      origen: [ids]
  tensiones_abiertas: ["..."]
  contradicciones_resueltas:
    - entre: [ids]
      decision: "..."
      motivo: "..."
  descartadas:
    - id: ...
      motivo: "..."
