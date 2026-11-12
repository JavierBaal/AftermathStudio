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
Plausibilidad: Las afirmaciones sin mecanismo no entran en el canon

## Tramo que consolidas
Hora 5 (PT5H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h3
  resumen: 'En la tercera hora (12:00 a 13:00 de Madrid) el amanecer en la costa este de EE. UU. es un anticlímax: con el sol pegado al horizonte apenas se ven los colores nuevos, el ''he salido y no veo nada'' alimenta al bando del bulo y lo que convence son las luces negras caseras, que además destapan manchas de fluidos en colchones y hoteles; a la vez aparece una brecha norte-sur en Europa que da al escepticismo un segundo bastión nórdico. Los gobiernos siguen en modo comunicación pero ya con salidas operativas: la rueda de prensa de Moncloa convierte el ''no lo sabemos'' en titular, CCTV fija una línea científica y calmada, EASA deja reanudar las inspecciones fluorescentes con gafas que absorben el UV y los bancos centrales de economías informales recuerdan que un billete que se ve raro sigue siendo de curso legal, mientras en los mercados de la India y Brasil el pago por QR resuelve las discusiones. Los efectos se cruzan en la cara y en los ojos: al sol del mediodía se ven manchas
    solares y daño acumulado (vergüenza adolescente, consultas dermatológicas y abandono anunciado de crema solar y maquillaje), los mayores ven un velo por la fluorescencia de su cristalino, las lentes de contacto con bloqueador y las monturas sin protección lateral deciden quién ve qué, y la demanda de gafas se desplaza a modelos certificados y envolventes empujada por las empresas, que compran EPI para su plantilla en exteriores. La disputa por la imagen buena se aparca y se convierte en una disputa por el nombre del color nuevo, mientras la corrección de los chatbots, desigual y sin explicar, genera su propio bulo.'
  hechos_establecidos:
  - id: h3-01
    texto: 'El amanecer en Nueva York (6:39 EST, 12:39 de Madrid), retransmitido en directo desde azoteas de Nueva York y Boston como el momento de la verdad, resulta un anticlímax: con el sol a pocos grados el UV-A que llega al suelo es una fracción mínima del de mediodía, y quienes salen a la calle o se asoman a la ventana describen apenas un tinte raro o nada claro, sobre todo con nubes. Los escépticos recortan esos directos y el ''he salido y no veo nada'' circula justo cuando se esperaba el ''lo estamos viendo todos''; la confirmación en EE. UU. llegará a goteo a medida que suba el sol, con el pico unas seis horas después.'
    origen:
    - medios/h3/1
    - disruptor/h3/1
  - id: h3-02
    texto: 'La contraprueba casera con luz negra en EE. UU. sigue siendo la que convence y se desvía hacia otro descubrimiento: al apuntar la lámpara por la casa aparecen manchas fluorescentes de orina, sudor y otros fluidos en colchones, sofás, alfombras y baños, y empiezan los vídeos desde habitaciones de hotel y apartamentos turísticos. Como nadie graba su propio colchón para fingir un bulo, el asco convence a escépticos y desplaza la conversación hacia lo que no se veía, con hoteles, alquileres turísticos y transporte sin protocolo de limpieza para clientes que ven la fluorescencia.'
    origen:
    - disruptor/h3/5
  - id: h3-03
    texto: Entre las 6:00 y las 7:00 de Washington la Casa Blanca anuncia que el presidente hablará después del amanecer y deja lo operativo a las agencias federales (FAA y servicio meteorológico), que emiten avisos técnicos sobre deslumbramiento al volante y en vuelo; varios gobernadores de la costa este dan avisos de tráfico para la hora punta sin esperar a Washington. El anticlímax del amanecer le quita a la declaración presidencial el momento de experiencia compartida que buscaba.
    origen:
    - politico/h3/5
    - medios/h3/1
    - disruptor/h3/1
  - id: h3-04
    texto: 'En pleno mediodía europeo aparece una brecha norte-sur: en Noruega, Suecia, Finlandia, los bálticos y buena parte de Escocia, donde el sol de mediados de noviembre apenas sube unos 12 grados en Oslo, la experiencia es tenue, mientras en España, Italia o Grecia es intensa. La diferencia física se lee como cultural y en los medios nórdicos el relato pasa a ser el de un fenómeno de los países del sur exagerado por sus redes, de modo que el escepticismo tiene un segundo bastión dentro de Europa.'
    origen:
    - disruptor/h3/2
  - id: h3-05
    texto: En el norte de Europa, y en menor medida en EE. UU., los solarios reciben llamadas y visitas de gente que quiere ver los colores nuevos con la fuente de UV-A más potente a mano, y algunos centros abren antes de hora; dentro de la cabina hay quien se quita las gafas protectoras para mirar, lo que abre un frente sanitario de exposición ocular a corta distancia que el aviso sobre gafas baratas no cubre.
    origen:
    - disruptor/h3/3
  - id: h3-06
    texto: 'El Consejo de Ministros español del martes se celebra según lo previsto y su rueda de prensa en Moncloa, entre las 12:30 y las 13:30, es la primera comparecencia de un gobierno europeo grande ante preguntas abiertas: parte operativo (tráfico, colegios, urgencias oftalmológicas, aviso sobre gafas sin filtro UV400), insistencia en que no consta daño ocular permanente y negativa a hablar de causa o duración. El ''no lo sabemos'' en directo se recorta y circula como confesión de ignorancia, y la oposición pide comparecencia en el Congreso.'
    origen:
    - politico/h3/1
  - id: h3-07
    texto: 'A las 19:00 de Pekín (12:00 de Madrid) el Xinwen Lianbo de CCTV recoge el suceso con encuadre sobrio y científico: expertos de la Academia China de Ciencias, fenómeno mundial que no afecta a la salud y llamamientos a la calma y a la información oficial, sin mencionar ataques ni a otros países. Como en China el suceso llegó casi al anochecer y buena parte de la población solo lo ha visto con lámparas UV, los censores de Weibo y Douyin rebajan los vídeos de ''lo que nos ocultaban''.'
    origen:
    - politico/h3/2
  - id: h3-08
    texto: EASA y varias autoridades nacionales de aviación civil aclaran a los talleres que pueden reanudar las inspecciones fluorescentes si los inspectores llevan gafas de seguridad que absorben el UV, equipo que ya existe en esos puestos, como alternativa provisional sin modificar el procedimiento certificado. La parada empieza a revertirse en Europa y la FAA queda presionada para hacer lo mismo al abrir su jornada.
    origen:
    - politico/h3/3
  - id: h3-09
    texto: 'El Banco de la Reserva de la India y otros bancos centrales de países con mucha economía informal (Egipto, Nigeria, Kenia, los del Golfo) difunden por SMS de operadoras, radio y altavoces de mercado un mensaje corto: un billete sucio, lavado o que se vea diferente al sol sigue siendo de curso legal y no puede rechazarse por eso. No cambia la percepción, pero da al comprador un argumento de autoridad.'
    origen:
    - politico/h3/4
  - id: h3-10
    texto: En los mercados callejeros del sur de Asia (16:30 en la India) y en el comercio ambulante de Brasil (8:00 en São Paulo), vendedores y compradores zanjan las discusiones por billetes raros pasando al pago por QR con UPI y Pix, que ya está impreso en casi todos los puestos y no tiene coste para el comercio. Nadie lo ordena; el efectivo pierde peso en el pago pequeño, pero los rechazos sin alternativa persisten en zonas rurales y entre vendedores sin móvil.
    origen:
    - economista/h3/2
  - id: h3-11
    texto: 'La demanda de gafas no se desinfla por el rechazo adolescente porque el volumen se desplaza al canal de empresa: constructoras, logística, cooperativas agrícolas (con la campaña de la aceituna en marcha en Andalucía) y ayuntamientos piden a sus distribuidores de EPI lotes de gafas con filtro UV certificado para el personal en exteriores, amparados en la obligación de proteger a los trabajadores (art. 17.2 de la Ley 31/1995). Este comprador exige marcado y certificación y refuerza el cuello de botella de las lentes certificadas.'
    origen:
    - economista/h3/3
  - id: h3-12
    texto: Quienes compraron gafas UV400 auténticas vuelven a las ópticas porque siguen viendo un resplandor del color nuevo por el lado, sobre todo en el borde nasal del campo visual, por la focalización periférica de la luz lateral que entra por el hueco de las monturas planas desde un cielo que emite UV-A difuso. Los ópticos recomiendan monturas envolventes o con protección lateral, y la demanda se desplaza hacia ese modelo, con menos stock y otro cuello de botella.
    origen:
    - oftalmologa/h3/3
  - id: h3-13
    texto: En el Golfo, a primera hora de la tarde, repartidores en moto de plataformas de comida y entrega rápida se desconectan o rechazan pedidos a pleno sol mientras la demanda de entregas sube porque la gente se refugia en interiores; los tiempos de entrega se alargan y las plataformas reutilizan los incentivos y recargos que ya tienen para calor extremo o lluvia, de modo que el coste lo paga primero el consumidor.
    origen:
    - economista/h3/4
  - id: h3-14
    texto: En España, con las cocinas preparando el servicio de comidas, hostelería y alimentación llaman a sus empresas de control de plagas por los mataínsectos apagados, y la respuesta que se impone es tapar o reubicar los aparatos fuera de la línea de visión o pasar a placas adhesivas sin luz, sin comprar equipos nuevos. Las grandes empresas del sector no se mueven en bolsa porque el cambio cabe en contratos ya firmados.
    origen:
    - economista/h3/5
  - id: h3-15
    texto: Al sol del mediodía en el sur de Europa, adultos y adolescentes ven en su cara y en la de los demás pecas, manchas solares y daño acumulado que en el visible no se notaban, porque la melanina absorbe el UV-A mucho más que el visible. Se viralizan vídeos de caras al sol que derivan en vergüenza estética, tertulias con dermatólogos y una variante conspirativa según la cual la industria cosmética y sanitaria lo sabía y lo callaba; consultas de dermatología y farmacias reciben preguntas sobre si esas manchas son cáncer, sobre todo de quienes han tomado mucho sol (trabajadores al aire libre, agricultores, deportistas), lo que abre un segundo pico de consultas, dermatológico.
    origen:
    - medios/h3/2
    - disruptor/h3/4
  - id: h3-16
    texto: Después del recreo muchas adolescentes se quitan en el baño la crema con color y el corrector, y en los grupos se extiende que mañana nadie se pondrá crema solar ni maquillaje porque se ve como una máscara; los avisos de las madres para que se pongan crema igual se reciben como no entender nada.
    origen:
    - adolescente/h3/2
  - id: h3-17
    texto: A media mañana los adolescentes que aguantaron sin gafas en el patio o en las ventanas empiezan a tener dolor de cabeza y ojos rojos por la fatiga visual; bajan a conserjería o jefatura a pedir que llamen a casa, y algunos padres, con los audios de 'te quedas ciega' en la cabeza, vienen a recogerlos aunque la Consejería dijo que no hacía falta, lo que arrastra más peticiones.
    origen:
    - adolescente/h3/3
  - id: h3-18
    texto: Los adolescentes miopes con gafas graduadas se convierten en el chiste de la clase porque sin gafas ven borrosos los colores nuevos y con ellas ven menos; algunos se las quitan en el patio aunque no vean, para no quedarse fuera.
    origen:
    - adolescente/h3/4
  - id: h3-19
    texto: 'La guerra sobre la imagen buena no se resuelve con una convención visual sino que se aparca: la conversación se desplaza a cómo se llama el color nuevo. En redes compiten nombres en cada idioma convertidos en etiquetas y memes, en los institutos cada grupo usa el suyo (''el brillo'', ''el morado fantasma'') y decir la palabra del grupo funciona como señal de pertenencia, y las redacciones empiezan a pedir criterio a libros de estilo y a Fundéu para nombrarlo en titulares.'
    origen:
    - medios/h3/5
    - adolescente/h3/1
  - id: h3-20
    texto: 'Las empresas de IA empiezan a corregir la respuesta de sus asistentes con avisos de suceso en curso y búsqueda en noticias, pero de forma desigual: a mediodía muchas consultas, también en clases donde los profesores convierten el fenómeno en tema, siguen devolviendo que los humanos no ven el ultravioleta. Las capturas de antes y después circulan como prueba de que alguien edita lo que la máquina puede decir, lo que el bando escéptico estadounidense lee como plegarse a la versión oficial, y los adolescentes concluyen que solo pueden fiarse de lo que ven y de lo que cuentan los suyos.'
    origen:
    - medios/h3/3
    - adolescente/h3/5
  - id: h3-21
    texto: Verificadores españoles y cuentas de hospitales y sociedades médicas desmienten el audio de la 'prima enfermera' en lo de quedarse ciega, apoyados en los signos de alarma ya publicados, pero no pueden desmentir que sea para siempre porque nadie sabe si es permanente; el audio sigue circulando de grupo en grupo y aparecen contraaudios igual de anónimos de supuestos médicos tranquilizadores.
    origen:
    - medios/h3/4
  - id: h3-22
    texto: Muchos mayores de 50 sin operar describen en exteriores al mediodía un velo o neblina azulada que lo lava todo en lugar de colores nuevos nítidos, y las consultas explican que en buena parte viene de la fluorescencia de su propio cristalino, que aumenta con la edad y produce deslumbramiento de velo; es el mecanismo de que los abuelos vean apagado lo que los nietos ven vivo, distinto del efecto de las lentes intraoculares.
    origen:
    - oftalmologa/h3/1
  - id: h3-23
    texto: 'Los usuarios de lentes de contacto descubren que el modelo decide lo que ven: las blandas con bloqueador UV de clase 1 o 2 apagan casi todo el color nuevo al mirar de frente, mientras las que no llevan filtro, muchas rígidas y diarias baratas, lo dejan ver. Las ópticas reciben a la vez peticiones de cambiar a lentes sin filtro para ver y de lo contrario para apagarlo sin llevar gafas de sol, la primera forma barata y reversible de elegir.'
    origen:
    - oftalmologa/h3/2
  - id: h3-24
    texto: Llegan a cirugía refractiva y de cataratas las primeras peticiones de operados que quieren cambiar su lente intraocular por una sin filtro y de jóvenes que preguntan por cirugía de cristalino para ver más; las sociedades de oftalmología recomiendan expresamente no indicar ni cambiar lentes por este motivo mientras no se sepa si el fenómeno es permanente.
    origen:
    - oftalmologa/h3/4
  - id: h3-25
    texto: 'Algunas consultas oftalmológicas empiezan a usar el fenómeno como cribado improvisado: comparar un ojo con otro frente a una lámpara de Wood o una linterna UV de 365 nm revela de forma orientativa una lente intraocular con filtro, una catarata incipiente o una lente de contacto con bloqueador, y lo incorporan al triaje para separar a quienes ven distinto con cada ojo por causa óptica benigna de los que tienen signos de alarma.'
    origen:
    - oftalmologa/h3/5
  tensiones_abiertas:
  - Qué dice el presidente de EE. UU. en su comparecencia sin el momento de experiencia compartida del amanecer, si la retrasa hasta que el sol suba y si el marco de bulo resiste hasta el mediodía de la costa este, ahora con la corrección de los chatbots leída como manipulación.
  - Cómo reacciona la volatilidad y Wall Street a la apertura de Nueva York (15:30 de Madrid) si la confirmación en EE. UU. llega a goteo y no de golpe.
  - Si la brecha norte-sur se convierte en un conflicto de relato dentro de la UE y si alguna autoridad nórdica o europea explica la diferencia por latitud y estación.
  - Si el abandono anunciado de crema solar y maquillaje entre adolescentes se materializa mañana y si autoridades sanitarias, dermatólogos o marcas responden antes; y si el pico de consultas dermatológicas satura atención primaria y farmacias.
  - Si el uso de solarios sin gafas para ver el UV produce casos clínicos y obliga a las autoridades a pronunciarse.
  - Si la FAA y los reguladores no europeos aceptan la reanudación de inspecciones fluorescentes con gafas que absorben el UV, y si el mercado deja de castigar a MTU, Safran y Lufthansa.
  - Si el paso al QR y el recordatorio de curso legal frenan los rechazos de billetes o si la economía informal sin móvil sufre un deterioro del efectivo.
  - Si la demanda de gafas certificadas y envolventes, empujada por las compras de EPI de las empresas, choca con el cuello de botella de lentes certificadas y transporte aéreo y alimenta el mercado de gafas sin filtro.
  - Qué nombre se impone para el color nuevo y si Fundéu u otras instancias lingüísticas se pronuncian.
  - Si el aumento de incidentes de tráfico en maniobras laterales es medible y empuja a medidas obligatorias (sigue abierta desde h1).
  contradicciones_resueltas:
  - entre:
    - economista/h3/1
    - medios/h3/1
    - disruptor/h3/1
    decision: 'Prevalece el anticlímax del amanecer: la confirmación en EE. UU. llega a goteo, no en el amanecer, y se descarta la caída de la volatilidad europea atribuida a esa confirmación.'
    motivo: medios/h3/1 y disruptor/h3/1 aportan dato verificable (amanecer a las 6:39 EST, 12:39 de Madrid) y un mecanismo físico sólido (camino atmosférico largo con el sol bajo que atenúa el UV-A); la premisa de economista/h3/1, que la experiencia directa del amanecer resuelve el riesgo binario, queda contradicha y no aporta dato.
  - entre:
    - politico/h3/5
    - medios/h3/1
    decision: 'Se combinan: la Casa Blanca anuncia que el presidente hablará tras el amanecer y las agencias y gobernadores dan avisos operativos, pero el amanecer tibio le quita el momento compartido; si la comparecencia se retrasa queda como tensión abierta.'
    motivo: Anunciar la comparecencia y tener motivos para esperar no se excluyen; el contenido y el momento de la declaración no pueden decidirse con lo dicho en este tramo.
  - entre:
    - medios/h3/3
    - adolescente/h3/5
    decision: 'Se combinan: las empresas de IA empiezan a corregir, pero la corrección es desigual y a mediodía muchos asistentes siguen negando la visión UV.'
    motivo: Ajustar instrucciones o activar búsqueda lleva horas y no llega a la vez a todos los productos; la convivencia de respuestas viejas y nuevas es lo que alimenta las capturas de antes y después.
  - entre:
    - medios/h3/2
    - disruptor/h3/4
    - adolescente/h3/2
    decision: Se combinan medios/h3/2 y disruptor/h3/4 en un solo hecho sobre la piel; adolescente/h3/2 se mantiene aparte como reacción específica de las adolescentes con cosméticos.
    motivo: 'Las tres se apoyan en el mismo mecanismo (melanina y filtros absorben el UV-A con mucho contraste) y operan en grupos y consecuencias distintas: viralización y consultas en adultos, abandono de crema solar y maquillaje entre adolescentes.'
  - entre:
    - medios/h3/5
    - adolescente/h3/1
    decision: 'Se combinan: la disputa por la imagen se aparca y pasa a ser una disputa por el nombre, visible a la vez en redes, redacciones e institutos.'
    motivo: Mismo mecanismo (fracaso de la imagen como prueba y necesidad de un sustantivo para compartir la experiencia) observado a dos escalas.
  - entre:
    - disruptor/h3/2
    - h2-01
    decision: 'Se matiza el canon: el escepticismo no queda solo concentrado en Norteamérica, también arraiga en el norte de Europa por la baja elevación solar de noviembre.'
    motivo: Dato geométrico verificable (elevación solar máxima en Oslo de unos 12 grados a mediados de noviembre); h2-01 sigue siendo cierto para América.
  - entre:
    - politico/h3/3
    - h2-16
    decision: 'Se refina el canon: el regulador europeo no valida un procedimiento nuevo sino que permite el equipo de protección existente, y la parada empieza a revertirse en Europa.'
    motivo: 'Mecanismo sólido y dato verificable: la indicación fluorescente sigue emitiendo en el visible y las gafas que absorben el UV devuelven al inspector a su visión anterior; resuelve en parte la tensión abierta desde h1.'
  - entre:
    - economista/h3/2
    - politico/h3/4
    decision: 'Se mantienen las dos como hechos complementarios: salida espontánea al QR donde hay infraestructura y recordatorio de curso legal por canales masivos.'
    motivo: Actúan sobre segmentos distintos (comercio con móvil frente a economía informal sin alternativa) y no se contradicen.
  - entre:
    - economista/h3/3
    - oftalmologa/h3/3
    - adolescente/h2/2
    decision: 'Se mantienen las tres: la demanda agregada de gafas se sostiene por el canal de empresa y se desplaza a modelos certificados y envolventes, mientras entre adolescentes siguen perdiendo estatus.'
    motivo: Operan en escalas distintas y las dos nuevas tienen mecanismo con dato (obligación legal de EPI y focalización periférica); ambas refuerzan el cuello de botella de h2-14 en lugar de aliviarlo.
  descartadas:
  - id: economista/h3/1
    motivo: Su mecanismo depende de que el amanecer en la costa este confirme el fenómeno por experiencia directa, lo que contradice h3-01, apoyado en dato horario y en la atenuación atmosférica del UV-A con el sol bajo; no aporta dato verificable.
  metricas:
    alarma_social: 3
    respuesta_gobiernos: comunicacion
    impacto_economico: 2
    adaptacion: 3

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h5
  afirmaciones:
  - texto: Entre las 13:00 y las 15:00 de Madrid se disparan en Noruega, Suecia, Dinamarca y Finlandia las búsquedas y las reservas de última hora de vuelos y paquetes a Canarias, Málaga y Alicante para el fin de semana. Las aerolíneas de bajo coste y los turoperadores nórdicos suben las tarifas de las plazas que quedan con su precio dinámico, sin añadir todavía vuelos, y el sur de Europa empieza a cobrar la brecha norte-sur como turismo antes de que nadie la explique.
    mecanismo: 'Quien no ve el fenómeno en su país tiene dos salidas: un solario, que es caro por minuto y ya tiene mala prensa sanitaria, o ir a donde el sol sí sube. Canarias y la costa mediterránea son el destino de invierno habitual de los nórdicos, con rutas, chárter y alojamiento ya montados para esta temporada, así que el coste de decidir es solo comprar el billete. Los sistemas de precios de las aerolíneas no necesitan que nadie entienda la causa: suben la tarifa en cuanto la ocupación de un vuelo crece más rápido de lo previsto. Añadir capacidad lleva días (aviones, tripulaciones y franjas), así que en esta hora el ajuste es todo precio y no volumen. Además, el relato nórdico de que es una exageración del sur se erosiona por la vía del bolsillo: quien reserva quiere comprobarlo.'
    dato: Canarias recibió 1.278.000 turistas nórdicos en 2025 según FRONTUR (Noruega 428.000, Suecia 351.000, Dinamarca 302.000, Finlandia 197.000).
    fuente: https://investigacion.turismodeislascanarias.com/sites/default/files/2026-03/Promotur_n%C3%B3rdicos_2025.pdf
    confianza: media
    areas_afectadas:
    - turismo
    - aviacion
    - consumo
    - precios
    id: economista/h5/1
  - texto: 'El cuello de botella de las gafas envolventes se alivia en Europa por una vía que nadie había previsto: las gafas de ciclismo y running envolventes y las máscaras de esquí que las tiendas deportivas acaban de recibir para la temporada de invierno. Decathlon y las cadenas de deporte agotan esas secciones en las ciudades del sur durante la tarde, y los ópticos empiezan a mandar allí a los clientes que vuelven quejándose del resplandor lateral.'
    mecanismo: 'La demanda se desplazó a monturas envolventes con protección lateral (h3-12), un modelo que no se fabrica en masa para el comercio de verano y del que hay poco stock en las ópticas. Pero a mediados de noviembre las tiendas de deporte tienen los almacenes llenos de producto de invierno: máscaras de esquí que cierran por completo el campo visual y gafas deportivas curvadas, casi todas con filtro UV400 y categoría marcada porque la normativa de EPI y de gafas de sol lo exige. Es inventario europeo ya en tienda, que no depende de los pedidos urgentes a China ni del transporte aéreo. El comprador lo descubre por el boca a boca de los ópticos y de los ciclistas, y el precio no sube porque estas cadenas no tienen precio dinámico en tienda física: se agota en lugar de encarecerse. El canal de empresa (h3-11) no compite aquí porque exige referencias certificadas como EPI laboral, no gafas deportivas.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - comercio_minorista
    - cadenas_de_suministro
    - consumo
    - optica
    id: economista/h5/2
  - texto: 'Las preguntas sobre si las manchas de la cara son cáncer (h3-15) no saturan primero la atención primaria pública sino las aplicaciones y centralitas de las aseguradoras de salud privadas: a primera hora de la tarde las citas de dermatología y teledermatología de Sanitas, Adeslas, Asisa y DKV para esta semana se agotan, y las listas se van a varias semanas. Las clínicas privadas de dermatología estética aprovechan para lanzar ofertas de revisión de lunares con dermatoscopia.'
    mecanismo: 'En la sanidad pública el camino a un dermatólogo pasa por el médico de cabecera y una derivación que tarda semanas, así que la persona preocupada no gana nada llamando hoy. En la privada el asegurado pide cita directa al especialista desde el móvil, sin coste por consulta o con un copago pequeño, y el seguro de salud lo tiene una parte grande de la población adulta urbana. El que pide cita es justo el perfil que más se mira al espejo y tiene más miedo a envejecer: urbano, de renta media o alta. La capacidad de dermatólogos es fija a corto plazo, de modo que el ajuste es la cola. Las clínicas estéticas, que viven de convertir preocupación en tratamiento, ven un flujo de clientes que no les ha costado captar, y la revisión con dermatoscopio es su producto de entrada barato.'
    dato: Hasta 12,8 millones de españoles tienen un seguro de salud privado.
    fuente: https://www.diarioestrategia.cl/texto-diario/mostrar/5869149/hasta-128-millones-espanoles-tienen-seguro-privado-unos-200000-ano
    confianza: media
    areas_afectadas:
    - sanidad
    - seguros
    - consumo
    - empleo
    id: economista/h5/3
  - texto: En la sesión de tarde europea MTU Aero Engines, Safran y Lufthansa recuperan parte, no todo, de lo que perdieron frente al índice en la hora 2, después de la aclaración de EASA sobre las gafas que absorben el UV. El rebote se queda a medias hasta que la FAA se pronuncie, y en las notas de los analistas el riesgo pasa de capacidad perdida a días de retraso acumulados en talleres que ya iban con cola.
    mecanismo: 'El castigo bursátil de la hora 2 descontaba una parada de duración desconocida en ensayos que son obligatorios para devolver motores al servicio. La aclaración de EASA (h3-08) acota esa duración en Europa con un equipo que ya existe, así que la parte del descuento que dependía de una parada larga se retira. Pero una parte relevante de la flota y de los contratos de mantenimiento de estos grupos depende de operadores estadounidenses y de motores certificados ante la FAA, que todavía no ha abierto su jornada, y unas horas de parada en talleres saturados no se recuperan solas: se acumulan en la cola de entregas de motores. Por eso el mercado devuelve el descuento del peor caso, pero mantiene uno pequeño por la incertidumbre regulatoria americana y por las horas perdidas.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados_financieros
    - aviacion
    - mantenimiento_industrial
    id: economista/h5/4
  - texto: A media mañana en EE. UU., antes de la apertura de Wall Street, las linternas UV de 365 nm y las lámparas de luz negra se agotan en Amazon, Walmart y las ferreterías, y los vendedores de marketplace suben precios. Al mismo tiempo, las grandes cadenas hoteleras y los gestores de alquiler turístico compran esas mismas linternas para sus equipos de limpieza y les ordenan revisar colchones y baños con ellas, de modo que el comprador profesional compite con el particular por el mismo producto barato.
    mecanismo: La luz negra es la prueba casera que convence en EE. UU. (h3-02) y su segundo uso, buscar manchas en colchones y hoteles, la convierte de curiosidad en necesidad defensiva. Para un hotel el riesgo no es el coste de limpieza, que es pequeño, sino un vídeo de un huésped con la linterna en su habitación, que pesa en las valoraciones y en las reservas. La respuesta más barata y rápida es dar a las camareras de piso la misma herramienta que el cliente y adelantarse, lo que cabe en el gasto ordinario de suministros. Estas linternas son producto de importación con stock modesto en el canal minorista y reposición desde China que no llega en horas, así que la demanda simultánea de hogares y empresas agota las existencias y el precio lo fija el revendedor de marketplace. Las cotizadas de hoteles y alquiler turístico no tienen un flujo de caja destruido que justifique una venta fuerte en preapertura, y el movimiento se queda en el producto, no en la bolsa.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - comercio_minorista
    - hosteleria
    - turismo
    - cadenas_de_suministro
    id: economista/h5/5
  reacciona_a:
  - politico/h3/3
  - disruptor/h3/2
  - disruptor/h3/4
  - disruptor/h3/5
  - oftalmologa/h3/3
- agente: politico
  tramo: h5
  afirmaciones:
  - texto: 'El presidente de EE. UU. no habla al amanecer, sino entre las 8:00 y las 9:00 de Washington (14:00 a 15:00 de Madrid), y cambia el guion: deja de pedir que la gente salga a comprobarlo y presenta el fenómeno como un hecho confirmado por terceros. Cita a aliados, a tropas y personal diplomático destinados en Europa, Oriente Medio y Asia, y a las agencias federales; afirma que no hay indicios de ataque, sin descartar nada, pide paciencia hasta el mediodía y deja lo operativo a gobernadores y agencias. No declara emergencia nacional.'
    mecanismo: 'El anticlímax del amanecer (h3-01) destruye el plan de escenificar una experiencia compartida, y retrasar la comparecencia hasta el mediodía dejaría seis horas más al marco de bulo y a la lectura de que los chatbots se pliegan a la versión oficial (h3-20). La salida que queda es la autoridad de testigos que el escéptico americano no puede tachar de histeria extranjera: militares y diplomáticos propios que llevan horas viéndolo a pleno sol. Decir que no hay indicios de ataque sin descartarlo protege al presidente si inteligencia cambia de criterio, y no declarar emergencia evita activar poderes que la oposición leería como sobrerreacción ante algo que en su costa todavía no se ve bien.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - politica
    - comunicacion_institucional
    - desinformacion
    - eeuu
    id: politico/h5/1
  - texto: 'Al abrir su jornada, la FAA publica un SAFO (alerta de seguridad para operadores) que replica la salida de EASA: los talleres pueden reanudar las inspecciones fluorescentes con gafas que absorben el UV, sin cambiar el procedimiento certificado. Transport Canada y otras autoridades americanas se alinean en las horas siguientes.'
    mecanismo: El SAFO es un instrumento informativo, no regulatorio, que la FAA puede emitir en horas sin pasar por un proceso de reglamentación ni una directiva de aeronavegabilidad. Como EASA ya ha fijado la solución (h3-08) y el equipo de protección ya existe en los puestos, la FAA no asume riesgo técnico propio al copiarla, y si no lo hace las aerolíneas y talleres estadounidenses quedarían parados frente a sus competidores europeos justo cuando empieza su operación de mañana. La presión llega por los mismos canales de la industria que movieron a EASA.
    dato: La FAA regula los SAFO y los InFO mediante la Orden 8000.87A; su cumplimiento es voluntario y sirven para difundir información de seguridad con rapidez.
    fuente: https://www.faa.gov/documentLibrary/media/Order/8000.87A.pdf
    confianza: alta
    areas_afectadas:
    - aviacion
    - regulacion
    - mantenimiento
    - eeuu
    id: politico/h5/2
  - texto: 'Las autoridades de protección radiológica nórdicas (la sueca SSM, la noruega DSA y la finlandesa STUK) publican antes de las 15:00 de Madrid una nota conjunta o coordinada que hace dos cosas: explica con el índice UV que ya miden a diario por qué en Escandinavia el fenómeno se ve tenue en noviembre, y recuerda que en los solarios es obligatorio llevar la gafa protectora y que quitársela para mirar expone el ojo a una dosis muy superior a la del sol local. Es la primera autoridad europea que explica la brecha norte-sur por latitud y estación.'
    mecanismo: 'Estos organismos ya tienen las dos competencias en la mano: publican el índice UV en sus webs y regulan los solarios con normas que exigen gafas. El auge de visitas a solarios (h3-05) les crea una obligación de actuar y les da el motivo para hablar, y el índice UV casi nulo de noviembre en Oslo o Estocolmo es el dato que desmonta el relato del ''fenómeno del sur exagerado'' (h3-04) sin tener que opinar sobre la causa. A los gobiernos nórdicos les conviene que la explicación salga de un organismo técnico y no de un ministro, porque así el escepticismo local se corrige sin parecer que Bruselas o el sur imponen un relato.'
    dato: La normativa sueca sobre solarios (SSMFS 2012:5) regula estas instalaciones y la protección de los usuarios, incluidas las gafas protectoras.
    fuente: https://www.stralsakerhetsmyndigheten.se/contentassets/ca098d0df9904f0a9adfb4ee1be58c0c/ssmfs-20125-stralsakerhetsmyndighetens-foreskrifter-om-solarier-och-artificiella-solningsanlaggningar-ursprunglig-version.pdf
    confianza: media
    areas_afectadas:
    - salud_publica
    - union_europea
    - desinformacion
    - paises_nordicos
    id: politico/h5/3
  - texto: 'En España el Gobierno se adelanta a la petición de la oposición y registra la comparecencia a petición propia de la ministra de Sanidad, para la próxima semana, en lugar de esperar a que la Mesa y la Junta de Portavoces tramiten la solicitud ajena. A la vez, Sanidad y la Academia Española de Dermatología y Venereología difunden un mensaje corto antes de la salida de los institutos: la crema solar se sigue usando aunque se vea, y las manchas que ahora se ven no son por sí mismas una urgencia, con derivación a atención primaria solo si cambian, sangran o crecen.'
    mecanismo: 'Pedir la comparecencia uno mismo convierte la exigencia de la oposición en iniciativa propia, fija la fecha con margen para tener más información y desactiva el titular de que el Gobierno huye del Congreso tras el ''no lo sabemos'' (h3-06). El frente dermatológico es el que se puede ganar ya: el abandono de la crema solar anunciado para mañana (h3-16) y el pico de consultas (h3-15) tienen respuesta técnica sin tocar la causa, y la salida de clase entre las 14:00 y las 15:00 es la última ventana para llegar a las familias antes de la mañana siguiente. Apoyarse en la sociedad científica da al mensaje la autoridad que el Gobierno, cuestionado por su rueda de prensa, ya no tiene por sí solo.'
    dato: El Reglamento del Congreso prevé que los miembros del Gobierno comparezcan ante el Pleno o las comisiones a petición propia o a solicitud de los grupos parlamentarios.
    fuente: https://www.congreso.es/cem/tit11
    confianza: media
    areas_afectadas:
    - politica
    - sanidad
    - educacion
    - espana
    id: politico/h5/4
  - texto: 'En el canal intergubernamental la reacción sigue sin llegar a los líderes: no hay cumbre ni declaración del G7 ni del Consejo Europeo en la hora 5. Lo que sí ocurre es que el informe de situación del Centro de Coordinación de la Respuesta a Emergencias añade mapas de índice UV por latitud y un apartado sobre solarios y dermatología, y varios Estados del sur piden en la plataforma IPCR que la Comisión difunda esa explicación en todas las lenguas.'
    mecanismo: 'Una cumbre exige un objetivo político concreto y un texto que firmar, y nadie sabe qué firmar sobre un fenómeno sin causa conocida ni daño permanente; un comunicado vacío costaría más que el silencio. El dispositivo IPCR en modo de intercambio de información (politico/h2/1) sí tiene un uso inmediato: convertir la brecha norte-sur, que amenaza con volverse un conflicto de relato entre socios, en un dato técnico compartido. A los gobiernos del sur les interesa que la explicación por latitud la dé Bruselas, porque los protege de la acusación de exagerar sin que tengan que replicar ellos a los medios nórdicos.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - union_europea
    - coordinacion_internacional
    - desinformacion
    id: politico/h5/5
  reacciona_a: []
- agente: medios
  tramo: h5
  afirmaciones:
  - texto: 'Los magacines matinales de las cadenas estadounidenses (de 7:00 a 9:00 en Nueva York) llevan la luz negra al plató como demostración en directo y convierten las manchas de colchones y hoteles en una sección de consumo, pero el bando escéptico encuentra una réplica eficaz: las manchas de orina bajo luz negra se han visto siempre, así que esos vídeos no prueban nada nuevo. La prueba que se busca a partir de ahí ya no es la mancha, sino ver el color de la propia lámpara y de superficies que antes parecían negras o apagadas bajo ella.'
    mecanismo: 'Un plató no tiene sol y la televisión necesita una demostración repetible a hora fija; la lámpara de 365 nm es la única que cabe en un estudio. Pero la fluorescencia de los fluidos es luz visible que reemiten al absorber el UV-A, y por eso las linternas UV se venden desde hace años para localizar orina en moquetas: cualquiera que haya usado una puede decir que eso ya se veía. El testimonio costoso del colchón propio (disruptor/h3/5) convence al que lo graba, pero en televisión pierde fuerza frente a un escéptico que sabe cómo funciona la lámpara. La discusión obliga a separar lo que reemite en visible de lo que solo se ve con el canal nuevo, y la televisión no tiene preparado ese matiz técnico.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios
    - desinformacion
    - estados_unidos
    - hosteleria
    id: medios/h5/1
  - texto: 'Las televisiones públicas nórdicas (NRK, SVT, Yle) y los servicios meteorológicos y de radioprotección responden a la brecha norte-sur con mapas del índice UV en tiempo real, y el mapa del índice UV de Europa y del mundo se convierte en la primera imagen viral que funciona: no enseña cómo se ve el color nuevo, sino dónde y cuándo se puede ver. El relato de la exageración del sur pierde fuerza en los medios de referencia nórdicos, aunque sobrevive en redes como agravio.'
    mecanismo: Las imágenes en falso color fracasaron porque intentaban representar una experiencia (h2-05); un mapa de índice UV representa un dato medible que ya existe, se publica cada día y tiene autor institucional. Noruega tiene una red de medición del UV con valores diarios públicos, y los servicios públicos de radiodifusión tienen secciones de ciencia y meteorología que pueden emitir esos mapas sin esperar al gobierno. El mapa explica a la vez la brecha norte-sur (h3-04), el anticlímax del amanecer estadounidense (h3-01) y el uso de solarios (h3-05) con una sola variable, por eso lo reutilizan medios de todos los países. No cierra el agravio porque quien vive en Oslo sigue viendo poco, pero quita a los medios serios el argumento cultural.
    dato: La autoridad noruega de radioprotección (DSA) mantiene una red de medición del UV con valores diarios publicados y remite al índice UV del día y a las previsiones de Yr y NILU.
    fuente: https://uvnett.dsa.no/dagsverdier_en.aspx
    confianza: media
    areas_afectadas:
    - medios
    - europa
    - desinformacion
    - ciencia
    id: medios/h5/2
  - texto: 'Antes de la mañana siguiente se libra en los móviles de los adolescentes una batalla por el protector solar: dermatólogos y cuentas de cuidado de la piel rescatan los vídeos de cámara UV que ya existían con el lema ''si se ve como una máscara, está funcionando'', mientras el movimiento antiprotector que ya circulaba en TikTok aprovecha el mismo vídeo para decir que la crema tapa la piel y que no hace falta. El mismo material sirve a los dos bandos y el desenlace depende de qué creador llega antes a cada grupo.'
    mecanismo: 'Lo que las adolescentes ven en el recreo como mancha (h3-16) es el filtro haciendo su trabajo: el protector absorbe el UV y por eso las cámaras UV lo muestran oscuro, un formato que ya se usaba en campañas y en vídeos virales de dermatología. Los dermatólogos tienen ese contenido grabado y solo tienen que volver a publicarlo con el contexto nuevo, que es lo más rápido que pueden hacer. Pero los creadores antiprotector ya tenían audiencia y un relato de desconfianza hacia la industria que encaja con la variante conspirativa de la piel (h3-15). Como los adolescentes solo se fían de lo que ven y de los suyos (h3-20), la persuasión no la gana la autoridad médica sino quien consigue que una influencer de su edad diga que el brillo de la crema mola.'
    dato: Bajo cámara UV el protector aparece oscuro sobre la piel; y antes del suceso ya existía en TikTok una corriente de creadores contra el protector solar que dermatólogos de Columbia se dedicaron a desmentir.
    fuente: https://www.cancer.columbia.edu/news/shining-light-sun-safety-debunking-TikToks-anti-sunscreen-claims
    confianza: media
    areas_afectadas:
    - medios
    - salud
    - adolescentes
    - cosmetica
    id: medios/h5/3
  - texto: Los telediarios de las 15:00 en España, la franja informativa con más audiencia del día, se convierten en el primer gran resumen generalista del suceso para los mayores que no lo han seguido en redes, y para nombrarlo optan por una fórmula descriptiva y neutra (el color ultravioleta o lo ultravioleta) en lugar de cualquiera de las palabras de los grupos. La palabra de la tele pasa a ser, para los adolescentes, la de quien no lo ve bien, y la brecha generacional se marca ya en el vocabulario.
    mecanismo: Las redacciones generalistas no pueden adoptar un término de TikTok que puede durar horas, y su libro de estilo y las consultas lingüísticas (h3-19) recomiendan en estos casos describir antes que acuñar, porque un neologismo prematuro obliga a rectificar. Para el público mayor, que ve apagado lo que los nietos ven vivo (h3-22), la tele de la sobremesa es la fuente que ordena el día. Los adolescentes, que usan la palabra del grupo como señal de pertenencia (adolescente/h3/1), leen la fórmula neutra como la prueba de que los adultos hablan de algo que no ven, y la usan en burla.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios
    - lenguaje
    - adolescentes
    - mayores
    id: medios/h5/4
  - texto: Aparecen directos en TikTok, Instagram y Twitch desde cabinas de solario y con linternas UV a pocos centímetros de la cara sin gafas para enseñar quién aguanta más, y las plataformas los retiran o les quitan alcance aplicando sus normas sobre retos y actividades peligrosas. La retirada se convierte en otro episodio de censura para el bando conspirativo, que la suma a la corrección de los chatbots como prueba de que alguien decide qué se puede ver.
    mecanismo: 'La norma adolescente de aguantar sin gafas (h2-25) y el uso de solarios sin gafas (h3-05) ya tienen el formato del reto: una prueba de resistencia que se demuestra en directo y da estatus. Las plataformas tienen equipos de moderación y políticas ya escritas contra retos peligrosos, aplicadas en casos anteriores, y retirar contenido que expone los ojos a una fuente UV intensa no exige decidir nada sobre la causa del suceso. Pero la retirada se ve y la razón sanitaria no se explica en el momento, lo mismo que pasó con la corrección de los asistentes de IA (h3-20), y el marco de que alguien edita lo que se puede ver encuentra su segunda prueba en el mismo día.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios
    - plataformas
    - salud
    - desinformacion
    - adolescentes
    id: medios/h5/5
  reacciona_a:
  - disruptor/h3/5
  - disruptor/h3/2
  - adolescente/h3/2
  - adolescente/h3/1
  - disruptor/h3/3
- agente: oftalmologa
  tramo: h5
  afirmaciones:
  - texto: 'Entre las 14:00 y las 15:00 de Madrid todavía no llega a urgencias ningún caso de queratitis por los solarios de la hora 3, y eso se lee como prueba de que no pasa nada. Las sociedades de oftalmología y algunas consejerías de sanidad amplían el aviso de las gafas baratas a las cabinas de bronceado de forma preventiva: no quitarse nunca la gafa del solario, y acudir a urgencias si esa noche aparecen dolor intenso, sensación de arena y lagrimeo. Prevén los primeros casos para la madrugada del miércoles en el norte de Europa y en EE. UU.'
    mecanismo: 'La fotoqueratitis no duele en el momento: el epitelio corneal dañado por la radiación ultravioleta tarda horas en desprenderse, y los síntomas aparecen con una latencia típica de 6 a 12 horas. Quien se quitó la gafa en una cabina hacia las 12:00 o las 13:00 está ahora sin síntomas y lo cuenta en redes como prueba de que es inocuo, justo cuando más gente se anima a imitarlo. El supuesto de que el deslumbramiento no deja daño permanente se refiere a la percepción del fenómeno, no a la dosis física de una lámpara a pocos centímetros, que es la misma que antes del suceso y que ya justificaba la gafa obligatoria. Por eso el oftalmólogo tiene que avisar antes de ver ningún caso, y las urgencias nocturnas serán las primeras en notarlo.'
    dato: Los síntomas de la queratitis por ultravioleta suelen aparecer entre 6 y 12 horas después de la exposición, por lo que los pacientes acuden de noche o de madrugada; las camas de bronceado figuran entre las fuentes artificiales.
    fuente: https://wikem.org/wiki/UV_keratitis
    confianza: media
    areas_afectadas:
    - salud
    - urgencias
    - solarios
    - comunicacion_sanitaria
    id: oftalmologa/h5/1
  - texto: 'Los padres de bebés y niños pequeños llenan las consultas de pediatría y las ópticas: los niños lloran en el carrito al sol, cierran los ojos o se frotan, y no pueden explicar qué ven. Pediatras y oftalmólogos recomiendan sombra, gorras con visera y capotas en los carritos antes que gafas, y las gafas infantiles con filtro certificado se convierten en el modelo más escaso de todos.'
    mecanismo: 'El cristalino del niño es mucho más transparente al ultravioleta que el del adulto, porque los cromóforos que lo amarillean se van acumulando con la edad. Así, el estímulo del canal nuevo y el deslumbramiento son mayores cuanto más pequeño es el niño: es el extremo opuesto del velo de los mayores (h3-22). Un bebé no puede decir que le molesta ni ponerse gafas por su cuenta, y muchas gafas de bebé se caen o se las quitan, así que la recomendación clínica práctica es reducir la exposición con sombra y viseras. Las tallas infantiles certificadas son una parte pequeña de la producción y compiten con la compra de EPI de las empresas (h3-11) en el mismo cuello de botella de lentes certificadas.'
    dato: En menores de 10 años el cristalino deja pasar más del 75 % de la radiación ultravioleta, frente a alrededor del 10 % en mayores de 25.
    fuente: https://www.zeiss.com/vision-care/en/eye-health-and-care/health-prevention/why-kids-glasses-should-offer-the-best-uv-protection.html
    confianza: media
    areas_afectadas:
    - salud_infantil
    - opticas
    - cadena_suministro_gafas
    - familias
    id: oftalmologa/h5/2
  - texto: 'Se abre una brecha generacional en el uso de gafas: los mayores de 50 sin operar las adoptan en masa y sin discusión al salir a comer y a pasear a primera hora de la tarde, mientras los jóvenes las siguen rechazando. Los oftalmólogos lo recomiendan expresamente a ese grupo, porque para ellos la gafa con filtro quita el velo y casi no les quita colores.'
    mecanismo: El velo azulado que ven los mayores (h3-22) es fluorescencia de su propio cristalino, y solo se produce cuando el UV-A llega a ese cristalino y es absorbido. Una gafa UV400 o una envolvente corta el UV-A antes de que entre en el ojo, así que apaga a la vez el canal nuevo y la fuente del velo. Para un joven ponerse gafas es perder lo que ve; para un mayor con el cristalino amarillento, que ya veía apagado el color nuevo, es recuperar el contraste. El cálculo de coste y beneficio es opuesto según la edad, y eso divide el uso por edades, con efecto en la conducción y la marcha de los mayores por la tarde.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - salud
    - mayores
    - opticas
    - trafico
    id: oftalmologa/h5/3
  - texto: Las ópticas reciben a primera hora de la tarde a adolescentes miopes, a veces con sus padres, que piden lentes de contacto sin filtro UV para no seguir siendo el chiste de clase (h3-18). Muchos ópticos se niegan a adaptarlas con prisa a menores sin revisión previa, y el que lo consigue vuelve al instituto como el miope que sí lo ve.
    mecanismo: 'El ojo tiene aberración cromática longitudinal: las longitudes de onda cortas se enfocan delante de la retina, con unas 2 dioptrías de diferencia entre 400 y 700 nm, y más aún hacia el UV-A. En un ojo miope todo se enfoca ya delante de la retina, así que el color nuevo es lo más borroso que ve sin gafas. Con gafas lo ve enfocado pero muy atenuado, porque el policarbonato y muchos orgánicos absorben el UV. La lente de contacto sin filtro (h3-23) es la única forma de corregir la miopía sin apagar el canal. Los ópticos frenan por responsabilidad profesional, porque adaptar una lente a un menor exige una revisión y enseñarle a manejarla, y con eso se alarga la espera y la desigualdad dentro del aula.'
    dato: La aberración cromática longitudinal del ojo humano es de unas 2 dioptrías entre 400 y 700 nm, con las longitudes de onda cortas enfocadas más cerca.
    fuente: https://telescope-optics.net/eye_chromatism.htm
    confianza: media
    areas_afectadas:
    - adolescentes
    - opticas
    - salud
    - educacion
    id: oftalmologa/h5/4
  - texto: 'El cribado casero ojo contra ojo con una linterna UV, que las consultas han empezado a usar en el triaje (h3-25), da falsos resultados cuando el paciente lo hace en casa: con las linternas baratas de 395 nm los dos ojos ven luz y la diferencia desaparece. Los servicios de oftalmología precisan en sus criterios telefónicos que la prueba solo vale con una lámpara de 365 nm con filtro, como la de Wood, y dejan de pedirla a quien no la tiene.'
    mecanismo: La mayoría de las linternas UV domésticas y las lámparas de uñas usan LED de 395 a 405 nm, cuya emisión se sale en buena parte al violeta visible, que atraviesa sin problema una lente intraocular con filtro, una lente de contacto con bloqueador o una catarata incipiente. El ojo con filtro sigue viendo una luz violeta brillante y el paciente informa de que ve igual con los dos ojos. Una fuente de 365 nm con filtro de vidrio de Wood emite casi solo UV-A, que es justo la banda en la que esos filtros marcan la diferencia. Como el triaje se hace por teléfono y el paciente usa lo que tiene en casa, el procedimiento solo es fiable si se especifica la fuente.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - triaje_sanitario
    - urgencias
    - consumo_lamparas_uv
    id: oftalmologa/h5/5
  reacciona_a:
  - disruptor/h3/3
  - adolescente/h3/4
- agente: adolescente
  tramo: h5
  afirmaciones:
  - texto: 'A la salida del insti, entre las 14:00 y las 15:00, en los grupos circula una lista de ''maquillaje que no se ve'' y la regla que se impone es mirar la etiqueta: si pone SPF, fuera. Los polvos y las bases sin protección solar se salvan y las cremas con color, los correctores con SPF y la crema solar quedan como lo que delata.'
    mecanismo: En el recreo vimos que lo que hace la mancha no es el maquillaje en sí, sino lo que tapa el sol, y alguien con muchos seguidores lo dice en un vídeo con dos productos al lado. Leer 'SPF' en el bote es una prueba fácil que cualquiera puede hacer en el baño o en casa sin salir al sol, así que se convierte en la norma del grupo. El problema es que lo que te deja bien delante de las amigas es justo quitarte la protección, y eso no lo piensa nadie.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - consumo
    - cosmetica
    - adolescentes
    id: adolescente/h5/1
  - texto: En la comida en casa los que llevamos gafas graduadas le pedimos a nuestros padres lentillas, y los que ya las llevan comparan en el grupo la marca de su caja para saber cuáles 'dejan verlo'. Sale una lista de marcas buenas y malas que se pasa de grupo en grupo antes de que abran las ópticas por la tarde.
    mecanismo: A los miopes se les ha hecho el chiste toda la mañana y quitarse las gafas significa ver borroso. Cuando se corre la voz de que unas lentillas sí dejan ver y otras no, es la única salida para ver bien y no quedarse fuera. Como no sabes qué lentilla te toca, lo más rápido es preguntar a quien ya las lleva y mirar la caja; los padres, que ya vienen preocupados, son los que tienen que pagar y pedir cita, así que la pelea pasa a la mesa de la comida.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - optica
    - salud
    - familia
    - adolescentes
    id: adolescente/h5/2
  - texto: 'Al llegar a casa sacamos la lámpara de uñas de gel o una linterna UV y hacemos nuestra versión del vídeo americano: grabamos la habitación, la ropa, los dientes y el baño. Lo que más se sube no son los colchones sino ''mira cómo me brillan los dientes'' o la ropa, y algunos vídeos del baño o de la habitación se borran a los pocos minutos porque se ven cosas que dan vergüenza.'
    mecanismo: Mucha gente de mi edad tiene en casa una lámpara de uñas o una linterna UV de juguete, y después de ver los vídeos de EE. UU. es lo primero que haces al llegar a casa y no tener sol. Delante de la lámpara se ve muchísimo más fuerte que al aire libre, así que es la forma de enseñar el color nuevo sin depender del sol. Pero lo que sale en tu casa no lo controlas, y como todo el mundo mira y comenta, te arriesgas a que te hagan captura antes de borrarlo.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes_sociales
    - hogar
    - adolescentes
    id: adolescente/h5/3
  - texto: En el grupo de clase y en los de todo el insti circula una captura falsa de la Consejería diciendo que mañana se suspenden las clases presenciales. Mucha gente se lo cree o hace como que se lo cree, y los padres empiezan a preguntar en el grupo de madres si es verdad antes de que el instituto lo desmienta por la aplicación.
    mecanismo: Con los padres que vinieron a recoger a sus hijos y con la rueda de prensa del Gobierno hablando de colegios, que se suspendan las clases parece lo siguiente lógico. Una captura con el logo es fácil de hacer y es lo que todos queremos que sea verdad, así que nadie la comprueba antes de reenviarla. Y como los profes tampoco saben nada hasta que les llega la instrucción, durante un rato no hay nadie que la desmienta.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - desinformacion
    - familia
    id: adolescente/h5/4
  - texto: 'Volviendo a casa del insti a pie o en bus, mis amigas y yo vamos por la acera de la sombra y nos paramos a grabar las cosas de la calle que brillan: los coches, los carteles, la ropa tendida en los balcones. Algunos que llegan con dolor de cabeza se echan en la cama con la persiana bajada y se pierden la tarde, y en el grupo se dice que ''mejor descansar los ojos hoy para verlo bien mañana''.'
    mecanismo: Después de toda la mañana aguantando sin gafas tenemos la vista cansada, pero el camino a casa es el primer momento sin profes en que puedes mirar lo que quieras por la calle. La sombra te deja mirar sin que te duela tanto. Los que ya tienen dolor de cabeza no se ponen gafas para no quedar mal, prefieren meterse en casa a oscuras, y le dan la vuelta diciendo que descansan para mañana, así no parece que se rindan.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - movilidad
    - adolescentes
    id: adolescente/h5/5
  reacciona_a:
  - oftalmologa/h3/2
  - disruptor/h3/5
- agente: disruptor
  tramo: h5
  afirmaciones:
  - texto: 'Entre las 13:00 y las 15:00 de Madrid el índice UV de las apps del tiempo y de los servicios meteorológicos se convierte en la herramienta con la que la gente intenta prever dónde y cuándo verá el color nuevo, y falla de una forma que nadie había previsto: en Escandinavia, en Escocia y en la costa este de EE. UU. a primera hora marca 0 o 1 mientras mucha gente sigue viendo el canal nuevo con claridad. Cuando institutos meteorológicos nórdicos o el servicio meteorológico estadounidense explican la brecha citando su índice UV casi nulo, el dato oficial refuerza sin querer el relato de que en el norte no hay nada que ver, y aparece la petición de un índice o una previsión específica de UV-A que ningún servicio tiene lista.'
    mecanismo: 'El índice UV no mide el UV-A: pondera la radiación con el espectro de acción eritemático de la CIE, pensado para la quemadura de la piel clara, que da mucho más peso al UV-B. Aunque el 94 % del UV que llega al suelo es UV-A, el 83 % del índice lo aporta el UV-B. Con el sol bajo (noviembre en el norte, amanecer en EE. UU.) el UV-B, más absorbido por el ozono y más dispersado en un camino atmosférico largo, cae mucho más deprisa que el UV-A, así que el índice se desploma antes que el estímulo que ahora ve la gente. Es la única cifra de UV que existe en las apps y en las webs oficiales, y quien lo explica por latitud y estación (la tensión abierta de h3-04) la usa sin advertir que exagera la diferencia norte-sur. Los servicios meteorológicos disponen de mediciones espectrales en algunas estaciones, pero no de un producto de previsión de UV-A para el público, y montarlo lleva días, no horas.'
    dato: La radiación UV global en superficie es en un 94 % UV-A y en un 6 % UV-B, pero de la radiación eritemática que compone el índice UV el 17 % es UV-A y el 83 % UV-B.
    fuente: https://temis.nl/uvradiation/info/index.html
    confianza: media
    areas_afectadas:
    - meteorologia
    - comunicacion_publica
    - desinformacion
    - brecha_norte_sur
    - estados_unidos
    - paises_nordicos
    id: disruptor/h5/1
  - texto: 'A la hora de comer en el sur de Europa, el foco de la piel visible pasa de las pecas y el maquillaje a quienes tienen vitíligo, melasma o pitiriasis versicolor: manchas que se disimulaban con maquillaje o pasaban inadvertidas en pieles claras aparecen ahora con un contraste fuerte a ojos de todos. Asociaciones de pacientes con vitíligo y dermatólogos salen en redes y medios a explicar que no es contagioso, y las mujeres embarazadas con melasma y los adolescentes con pitiriasis se suman al flujo de consultas a farmacias y atención primaria con una pregunta distinta a la del cáncer: si eso se pega o si es una enfermedad nueva.'
    mecanismo: La lámpara de Wood, que es UV-A, se usa en dermatología precisamente porque acentúa las zonas sin melanina, que se ven blanco azuladas y muy contrastadas, y porque algunas infecciones fúngicas de la piel fluorescen. Lo que antes era un examen en consulta con la luz apagada lo hace ahora cualquiera al sol y sin aparato. El vitíligo afecta a entre el 0,5 % y el 2 % de la población, así que en cualquier patio, oficina o terraza hay alguien con lesiones que el canal nuevo hace evidentes, y en una población que acaba de leer que lo que se veía en la cara era daño oculto (medios/h3/2) la primera lectura de una mancha nueva y llamativa es la de enfermedad o contagio. Es el estigma de siempre, multiplicado por la visibilidad y sin la defensa del maquillaje, que ahora también se ve como mancha (h3-16).
    dato: El vitíligo afecta a aproximadamente entre el 0,5 % y el 2 % de la población mundial; bajo la lámpara de Wood las zonas despigmentadas se ven de un blanco azulado brillante.
    fuente: https://www.unboundmedicine.com/5minute/view/5-Minute-Clinical-Consult/116646/all/Vitiligo
    confianza: media
    areas_afectadas:
    - salud
    - dermatologia
    - estigma
    - atencion_primaria
    - farmacias
    - educacion
    id: disruptor/h5/2
  - texto: 'En la compraventa de segunda mano empieza a verse lo restaurado: compradores que quedan a mediodía para recoger un mueble, una lámpara, una porcelana o un cuadro de Wallapop, Vinted o un anticuario lo miran al sol o con la linterna UV que ya tienen en casa y ven retoques, pegados, barnices nuevos y repintes que el vendedor no mencionó. Hay entregas que se cancelan en la calle, regateos sobre la marcha y anticuarios y casas de subastas que retiran piezas de escaparate o aplazan entregas hasta revisar sus descripciones, porque el comprador medio acaba de conseguir la herramienta que antes solo tenían los restauradores.'
    mecanismo: 'Los conservadores llevan décadas usando la fluorescencia ultravioleta para detectar intervenciones: barnices envejecidos, retoques, adhesivos y materiales modernos absorben o emiten de forma distinta a los originales, y lo que es homogéneo con luz visible se ve en parches con UV. La herramienta no estaba al alcance del comprador porque exigía una lámpara y saber mirar. Ahora el canal se ve sin aparato al sol, y la luz negra doméstica se ha generalizado en unas horas por la contraprueba (h3-02). En el mercado de segunda mano el vendedor tiene más información que el comprador sobre el estado de la pieza; el suceso reduce de golpe esa asimetría justo en el momento del intercambio, que en las plataformas entre particulares es en persona y a menudo en la calle. El efecto se concentra en objetos cuyo precio depende de la originalidad (antigüedades, arte, muebles de época, coleccionismo), no en la ropa o la electrónica.'
    dato: El examen con radiación ultravioleta se usa en conservación de colecciones para detectar restauraciones, retoques, barnices y adhesivos que no se ven con luz normal.
    fuente: https://www.nps.gov/museum/publications/conserveogram/01-10.pdf
    confianza: media
    areas_afectadas:
    - comercio_segunda_mano
    - antiguedades
    - mercado_del_arte
    - plataformas_digitales
    - consumo
    id: disruptor/h5/3
  - texto: 'En Noruega, Suecia, Finlandia y Dinamarca se disparan las búsquedas de vuelos y paquetes a Canarias, Málaga y Alicante para esta misma semana: el viaje al sur se convierte en la forma de comprobar por uno mismo si el fenómeno es real o una exageración de los países del sur. Las aerolíneas y turoperadores nórdicos que ya operan esas rutas de invierno ven el pico antes que los medios y no tienen asientos extra que poner en días.'
    mecanismo: La brecha norte-sur (h3-04) deja a los nórdicos ante dos versiones que no pueden comprobar en casa salvo con un solario (h3-05), que ya tiene mala prensa por la exposición ocular. Canarias y la Costa del Sol son en noviembre el destino de invierno por defecto de los países nórdicos, con rutas directas y una gran población residente escandinava que manda testimonios en su idioma, de modo que el viaje de comprobación tiene infraestructura y fricción baja. Como la temporada de invierno empieza en estas semanas y la capacidad de las rutas está planificada con meses de antelación, el efecto inmediato no son más vuelos sino tarifas que suben en la reserva de última hora, y la duda sobre si es permanente empuja a no esperar.
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - turismo
    - aviacion
    - paises_nordicos
    - canarias
    - brecha_norte_sur
    id: disruptor/h5/4
  reacciona_a:
  - medios/h3/2

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.
5. Puntúa las métricas:
- alarma_social: Nivel de alarma social (escala; de 1 a 5)
- respuesta_gobiernos: Respuesta dominante de los gobiernos (categorica; opciones: ninguna, comunicacion, emergencia, medidas_excepcionales)
- impacto_economico: Impacto económico agregado (escala; de 1 a 5)
- adaptacion: Grado de normalización del cambio (escala; de 1 a 5)

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
  metricas:
    alarma_social: valor
    respuesta_gobiernos: valor
    impacto_economico: valor
    adaptacion: valor
