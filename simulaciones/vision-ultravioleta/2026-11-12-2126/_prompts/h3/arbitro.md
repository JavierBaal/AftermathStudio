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
Hora 3 (PT3H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h2
  resumen: 'En la segunda hora el mundo empieza a ordenar el suceso: los medios encuentran una imagen que emitir en la fotografía ultravioleta de archivo, los oftalmólogos explican que las manchas de la piel siempre estuvieron ahí y fijan un uso situacional de las gafas de sol, y la subida bursátil de las gafas se desinfla mientras la volatilidad salta a la cosmética con protector solar. El Gobierno de España pasa de la contención a la coordinación sin medidas excepcionales, pero las comunidades dan instrucciones distintas a los colegios y el debate mediático gira de ''¿es peligroso?'' a ''¿quién manda?'', terreno en el que el relato de ocultación del agitador entra en la política a través de la oposición. Los desmentidos sobre las ''marcas ocultas'' llegan, pero el agitador los convierte en confesión, apoyado en que algunas marcas forenses sí estaban hechas para no verse, y las retiradas de las plataformas empujan a su audiencia a canales sin moderación. El efecto cruzado más peligroso
    es sanitario: la curiosidad por ver más empuja a lámparas UV y a mirar cerca del sol, y las lesiones reales llegarán con seis a doce horas de retraso, justo cuando encajan con el relato de que ''algo nos han hecho''.'
  hechos_establecidos:
  - id: h2-01
    texto: 'La subida de EssilorLuxottica y de los valores de gafas de sol pierde fuerza y devuelve parte de lo ganado: los analistas separan el pico de demanda transitorio del negocio recurrente y el economista presenta en público su advertencia de la hora 1 como primer acierto. Contribuye la pauta de la sociedad de oftalmología, que rebaja la idea de que todo el mundo necesita gafas: gafas homologadas con filtro UV a pleno sol, sobre todo para moto, bici y deporte, y sin ellas a la sombra o en interiores, donde los colores nuevos se ven sin molestias; denuncia además que no existen gafas que potencien la visión UV.'
    origen:
    - economista/h2/1
    - oftalmologa/h2/5
  - id: h2-02
    texto: Los usuarios de gafas graduadas descubren que a través de sus lentes ven los colores nuevos muy atenuados, porque materiales como el policarbonato bloquean el ultravioleta por sí mismos o llevan tratamiento anti-UV, y que los ven al mirar por encima o por fuera de la montura. Muchos se quitan las gafas en la calle, y la sociedad de oftalmología pide que no lo hagan para conducir, ir en bici o cruzar, lo que suma riesgo a peatones y ciclistas, ya expuestos al deslumbramiento completo.
    origen:
    - oftalmologa/h2/2
  - id: h2-03
    texto: 'La visibilidad del protector solar genera dos flujos opuestos a la vez: parte de quienes lo llevan, sobre todo en zonas de sol fuerte y en oficinas y centros educativos europeos, se lo quita para no mostrar la máscara, mientras otros, alarmados por el daño solar que ahora ven en su piel, compran protección. Sin datos de ventas, los valores de cosmética y protección solar como L''Oréal o Beiersdorf se mueven con fuerza en ambos sentidos y sin tendencia clara, y los dermatólogos quedan en la posición incómoda de recomendar algo que ahora estigmatiza; el riesgo real que nadie atribuye bien son las quemaduras por quitarse la protección.'
    origen:
    - economista/h2/2
    - disruptor/h2/2
  - id: h2-04
    texto: Surge una demanda inesperada de lámparas de luz negra, lámparas de uñas UV y linternas UV para ver los colores nuevos en interiores, donde la iluminación LED no los muestra, con subidas de precio y agotamiento de existencias. El agitador presenta el aviso de no mirar al sol ni a lámparas UV como prueba de que 'no quieren que miremos', y parte de su audiencia busca las 'marcas' con esas fuentes o mirando cerca del sol. Ambas conductas preparan casos de fotoqueratitis por exposición, no por el fenómeno.
    origen:
    - economista/h2/4
    - agitador/h2/2
  - id: h2-05
    texto: 'Circulan titulares y vídeos sobre los ''primeros heridos oculares'', que en realidad son deslumbramiento, fatiga y consultas por ansiedad. La sociedad de oftalmología publica una nota de triaje que separa lo benigno del fenómeno (deslumbramiento, fatiga, asimetría de percepción) de las lesiones por mirar al sol o a lámparas UV, y avisa de que estas aún no se ven porque la fotoqueratitis da síntomas entre 6 y 12 horas después de la exposición: la oleada de casos llegará esta tarde y noche, y se anticipa para que no se lea como un daño nuevo del fenómeno.'
    origen:
    - medios/h2/3
    - oftalmologa/h2/1
  - id: h2-06
    texto: 'El Gobierno de España pasa de la contención a la coordinación: convoca el Consejo de Seguridad Nacional o su Comité de Situación, previsto en la Ley 36/2015, para ordenar bajo un mensaje único los avisos de Estado, comunidades y ayuntamientos, sin declarar situación de interés para la Seguridad Nacional ni estado de alarma. Después comparecen la portavoz o el ministro de Sanidad junto a representantes de las sociedades de oftalmología con un mensaje limitado a lo que respaldan los técnicos (deslumbramiento transitorio, no mirar al sol ni a lámparas UV, precaución extra en moto y bici), sin pronunciarse sobre causa ni permanencia, y anuncian una comparecencia del presidente en el Congreso a petición propia en los próximos días.'
    origen:
    - politico/h2/1
    - politico/h2/2
  - id: h2-07
    texto: 'Las consejerías de Educación envían instrucciones a lo largo de la hora, distintas entre comunidades: casi todas mantienen los centros abiertos, permiten la recogida por el procedimiento ordinario y varias ordenan recreos en interior; ninguna cierra. Mientras llegan, las aulas se vacían a trozos según decide cada familia y los alumnos que quedan se agrupan sin clase y con el móvil permitido. La sociedad de oftalmología aporta la primera pauta clínica para colegios (recreo a la sombra o con gorra de visera y no mirar al sol, sin mandar a nadie a casa) a partir de un gradiente por edad: los niños, con un cristalino mucho más transparente al ultravioleta, describen los colores nuevos con más intensidad y sufren más deslumbramiento, y los mayores ven menos. La disparidad entre comunidades se convierte en nuevo frente de crítica, y alguna gobernada por la oposición se desmarca con mensaje propio.'
    origen:
    - politico/h2/3
    - adolescente/h2/1
    - oftalmologa/h2/3
  - id: h2-08
    texto: 'Televisiones y digitales encuentran imagen que emitir: recuperan el vídeo de 2014 ''How the sun sees you'', grabado con cámara UV, y piden imágenes ultravioleta propias a laboratorios, policía científica y fotógrafos técnicos. Esas imágenes en grises o falso color se convierten en la ilustración estándar y, junto con el mensaje de la oftalmóloga de que las manchas y las máscaras de protector no son una enfermedad ni una quemadura sino lo que siempre estuvo ahí y ahora se ve porque cambió el ojo del observador, frenan parte de la alarma por la piel. A la vez, los negacionistas las señalan como prueba de montaje porque no se parecen a lo que la gente dice ver.'
    origen:
    - medios/h2/1
    - oftalmologa/h2/4
  - id: h2-09
    texto: 'Los verificadores desmienten las capturas falsas de comunicados y la tesis de las ''marcas ocultas'' con documentos públicos como la guía del BCE sobre los elementos de seguridad del euro visibles con luz ultravioleta. El agitador no retrocede: presenta la aclaración como confesión (''ahora admiten que estaba marcado'') y desplaza la sospecha a envases, ropa y señalización. Le ayuda un fragmento de verdad: hay marcas hechas para no verse que ahora ve todo el mundo, como los marcadores forenses tipo SmartWater, los rociadores antiintrusión, los sellos de locales y las tintas de seguridad, de modo que el marcado forense pierde su invisibilidad, quien lleva algo marcado puede detectarlo y limpiarlo, y empresas de seguridad y policías reciben consultas. El bulo se mueve también en broma por grupos de clase y de familia.'
    origen:
    - medios/h2/2
    - agitador/h2/1
    - disruptor/h2/1
    - adolescente/h2/4
  - id: h2-10
    texto: Las grandes plataformas activan protocolos de crisis (paneles, etiquetas, menos difusión de consejos de salud falsos) pero, sin una autoridad sanitaria común a la que enlazar, cada plataforma e idioma remite a fuentes distintas; además retiran contenido racista sobre las 'caras negras' del protector por sus normas contra el odio. España y otros gobiernos piden a la Comisión Europea que presione, y esta recuerda a las plataformas de muy gran tamaño sus obligaciones bajo la Ley de Servicios Digitales sin activar el mecanismo de respuesta a crisis, que exige antes una recomendación de la Junta. El agitador convierte cada retirada en historia de censura y lleva a su audiencia a su canal propio de mensajería, donde la versión más dura circula sin moderación ni verificadores.
    origen:
    - medios/h2/4
    - politico/h2/5
    - agitador/h2/4
  tensiones_abiertas:
  - Si la oleada nocturna de fotoqueratitis se lee como lesión por conducta, como anticipan los oftalmólogos, o como el daño diferido del fenómeno que el agitador lleva horas anunciando.
  - En España el encuadre mediático pasa de '¿es peligroso?' a '¿quién manda?' y cuentas de la oposición comparten clips del agitador sobre la descoordinación; no está decidido si la coordinación del Consejo de Seguridad Nacional y la comparecencia anunciada desactivan esa presión o si el relato de ocultación se consolida en la política institucional, ni si la OMS convoca el Comité de Emergencias.
  - Si el abandono del protector solar por vergüenza produce quemaduras reales y si la demanda neta de cosmética con SPF cae o sube.
  - Si los jóvenes rechazan las gafas de sol para seguir viendo los colores y con ello se acorta del todo el tirón de demanda.
  - Cómo responden policías y empresas de seguridad a la pérdida de invisibilidad del marcado forense y si se produce una ola de borrado de rastros.
  - Cómo reaccionan Wall Street en su apertura, con precios de referencia previos formados de madrugada, y las bolsas asiáticas en su siguiente sesión.
  contradicciones_resueltas:
  - entre:
    - medios/h2/3
    - oftalmologa/h1/5
    decision: Se establece que las lesiones reales por mirar al sol o a lámparas UV aflorarán con un desfase de 6 a 12 horas, no en las horas inmediatas, y que la propia sociedad de oftalmología lo anticipa en su nota de triaje.
    motivo: Medios y oftalmologa/h2/1 coinciden en la latencia con dato y fuente clínica; la propia oftalmóloga corrige en este tramo su calendario anterior.
  - entre:
    - politico/h2/3
    - adolescente/h2/1
    decision: Las circulares autonómicas llegan a lo largo de la hora y de forma desigual; en muchos centros aún no habían llegado cuando las aulas empezaron a vaciarse según la decisión de cada familia.
    motivo: Ambas tienen mecanismo plausible y son compatibles si se entiende que la llegada de instrucciones es escalonada; ninguna aporta dato que excluya a la otra.
  - entre:
    - adolescente/h2/5
    - economista/h1/2
    decision: Se recoge que el tirón bursátil de las gafas se desinfla y que la pauta clínica reduce su uso a pleno sol, pero el rechazo masivo entre los jóvenes no entra como hecho y queda como tensión abierta.
    motivo: La afirmación del adolescente es especulación sin dato; la del economista sobre la pérdida de fuerza tiene mecanismo y dato con fuente.
  descartadas:
  - id: economista/h2/3
    motivo: Amplía y concreta el hecho h1-01 sobre la reacción estadounidense de madrugada sin cambiar el rumbo del mundo; su efecto queda recogido como tensión de la apertura de Wall Street.
  - id: economista/h2/5
    motivo: Inferencia sin dato que confirma la normalidad ya descrita en h1-01; no añade una consecuencia nueva.
  - id: politico/h2/4
    motivo: Aviso declarativo sin efecto en este tramo que solo concreta el oportunismo comercial ya recogido en h1-02.
  - id: adolescente/h2/2
    motivo: Efecto local y de detalle (burlas y lavados de cara en un instituto) que concreta la fricción por el protector ya recogida en h1-08 y h2-03.
  - id: adolescente/h2/3
    motivo: Especulación sin dato y efecto cultural de detalle que no cambia el rumbo del mundo en este tramo.
  - id: adolescente/h2/5
    motivo: Especulación sin dato; se deja como tensión abierta sobre la demanda de gafas entre los jóvenes.
  - id: agitador/h2/3
    motivo: Especulación sin dato; la extensión del relato a la cosmética y la difusión de caras sin consentimiento no tienen respaldo suficiente para entrar en el canon.
  - id: agitador/h2/5
    motivo: 'Se recoge solo como tensión abierta: el cruce entre agitador y oposición es plausible pero sin dato, y ocupa el mismo hueco que el cambio de encuadre mediático.'
  - id: medios/h2/5
    motivo: Se recoge como tensión abierta junto a agitador/h2/5; es inferencia sin dato y el límite de hechos obliga a priorizar los que cambian el rumbo en otras áreas.
  - id: disruptor/h2/3
    motivo: Efecto de detalle que amplía la dependencia del UV-A en la escena ya establecida en h1-08 y h1-09; la fuente del dato es poco sólida y no supera el límite de hechos.
  - id: disruptor/h2/4
    motivo: Confianza baja y especulación sin dato.

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h3
  afirmaciones:
  - texto: Agotadas las lámparas de luz negra y las linternas UV-A, los buscadores y marketplaces devuelven para 'lámpara UV' lámparas germicidas UV-C, muy extendidas desde la pandemia, y vendedores oportunistas las promocionan como forma de ver los colores nuevos. Quien las compra no ve nada nuevo con ellas, insiste en mirarlas o acercarse y suma quemaduras de córnea y de piel, que se añadirán a la oleada clínica de la tarde y la noche.
    mecanismo: Cuando un producto se agota, la demanda se desvía al sustituto más parecido en el buscador, y el consumidor no distingue UV-A de UV-C porque ambos se venden con la etiqueta 'UV'. El inventario de lámparas germicidas acumulado tras la pandemia es stock disponible e inmediato, y al vendedor le basta con cambiar el título del anuncio. Como solo el UV-A se percibe como colores nuevos, el comprador defraudado cree que la lámpara es débil y se expone más tiempo y más cerca, justo con la radiación más lesiva. El aviso de Consumo de la hora 2 es declarativo y no llega a vendedores fuera de la UE.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - comercio_online
    - salud
    - regulacion
    id: economista/h3/1
  - texto: Las empresas con plantillas al aire libre (construcción, reparto, agricultura, seguridad privada, mantenimiento de carreteras) y sus servicios de prevención empiezan a pedir por lotes gafas de sol homologadas a distribuidores de equipos de protección individual. El tirón de demanda de gafas se desplaza del minorista, que se enfría, al canal profesional, donde las compras sí se ejecutan aunque los trabajadores jóvenes no quieran llevarlas.
    mecanismo: La normativa de prevención obliga al empresario a evaluar los riesgos nuevos y a proporcionar gratis los equipos de protección adecuados; un deslumbramiento documentado por la sociedad de oftalmología y por el Gobierno es un riesgo que ningún servicio de prevención quiere dejar sin respuesta ante una inspección o un accidente. Al empresario le sale más barato comprar gafas que asumir responsabilidad por un siniestro en moto o en andamio. Es demanda por cumplimiento, no por gusto, así que no depende de que el trabajador quiera ver los colores; pero sigue siendo transitoria y no cambia el valor de los fabricantes.
    dato: El Real Decreto 773/1997 regula las obligaciones del empresario de proporcionar gratuitamente a los trabajadores los equipos de protección individual adecuados, en desarrollo del artículo 17 de la Ley 31/1995 de Prevención de Riesgos Laborales.
    fuente: https://www.boe.es/eli/es/rd/1997/05/30/773/con
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - empleo
    - consumo
    - salud_laboral
    - empresas
    id: economista/h3/2
  - texto: 'En la preapertura de Nueva York, que funciona desde las 10:00 hora de Madrid, los valores de autenticación y seguridad de billetes, como Crane NXT, se mueven con fuerza sin dirección clara: unos venden por ''las marcas UV han dejado de ser secretas'' y otros compran por ''los bancos centrales tendrán que rediseñar elementos de seguridad''. El economista dice en público que ambas lecturas exageran.'
    mecanismo: La pérdida de invisibilidad del marcado forense y de las tintas de seguridad ya es hecho establecido, y el mercado busca el valor cotizado que represente esa historia. Crane NXT es de los pocos nombres cotizados que fabrican elementos de seguridad para billetes y que compró en 2025 la división de autenticación de De La Rue, así que concentra la apuesta. Pero los elementos UV son solo una capa entre muchas (marca de agua, hilo, holograma, tacto) y un rediseño de billetes tarda años y se contrata por licitación, de modo que el efecto en los flujos de caja es lento en ambos sentidos. La preapertura tiene poca liquidez y amplifica cualquier orden.
    dato: Crane NXT completó en 2025 la adquisición de De La Rue Authentication Solutions.
    fuente: https://investors.cranenxt.com/press-releases/news-details/2025/Crane-NXT-Completes-Acquisition-of-De-La-Rue-Authentication-Solutions/default.aspx
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados_financieros
    - seguridad
    - bancos_centrales
    id: economista/h3/3
  - texto: Los mayoristas de lámparas UV, de gafas de sol básicas y de protector solar hacen pedidos urgentes a fábricas asiáticas sobre las ventas de esta mañana. Esos pedidos tardarán semanas en llegar, cuando el deslumbramiento ya habrá remitido y la novedad se habrá enfriado, de modo que el suceso fabrica hoy los excedentes y las rebajas de dentro de un mes.
    mecanismo: 'Es el efecto látigo clásico de las cadenas de suministro: cada eslabón extrapola la demanda del pico y añade margen de seguridad, y el plazo de fabricación y transporte marítimo desde Asia es de semanas. El pico de demanda de gafas está ligado a un deslumbramiento que remite en unas dos semanas, y el de lámparas a una curiosidad que se agota; los pedidos se firman sobre la demanda de hoy y se reciben con la de mañana. Quien pide primero y más gana con el agotamiento actual, y el sobrestock lo absorberán distribuidores y comercios pequeños con rebajas.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - cadenas_de_suministro
    - comercio
    - consumo
    id: economista/h3/4
  - texto: 'Empiezan a circular en tertulias y redes estimaciones del ''coste económico del suceso'' en miles de millones, hechas sin método. El economista se niega a dar una cifra y señala en público los únicos canales medibles: horas de trabajo perdidas por recogida de hijos y salidas a la calle, siniestros de tráfico en moto y bici, y asistencia sanitaria por lesiones de conducta; ninguno toca la producción industrial, que funciona con luz artificial.'
    mecanismo: 'En un acontecimiento sin precedente, la cifra redonda es el titular más barato y los comentaristas compiten por darla primero. Al economista le perjudica sumarse a un número que luego no se sostenga y le beneficia separar ruido de canales con dato: una mañana irregular en oficinas y colegios es un coste puntual y pequeño frente a la producción de un trimestre, mientras los siniestros y las urgencias sí generarán datos de aseguradoras y sanidad en los próximos días. Esa postura le posiciona antes de la apertura de Wall Street como la voz que no se sumó al pánico.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - medios
    - empleo
    - seguros
    - macroeconomia
    id: economista/h3/5
  reacciona_a:
  - disruptor/h2/2
  - adolescente/h2/5
- agente: politico
  tramo: h3
  afirmaciones:
  - texto: En la hora 3 el Ministerio de Sanidad convoca un pleno extraordinario y telemático del Consejo Interterritorial del Sistema Nacional de Salud, y Educación hace lo mismo con su conferencia sectorial, para cerrar una pauta común para colegios y centros sanitarios basada en la nota de la sociedad de oftalmología (recreo a la sombra o con visera, no mirar al sol, sin cierres). La mayoría de comunidades se adhiere, pero alguna gobernada por la oposición vota en contra o se abstiene y mantiene su circular propia, con lo que el Gobierno reduce la disparidad sin poder eliminarla.
    mecanismo: La gestión sanitaria y educativa es autonómica y el Gobierno no puede imponer instrucciones sin declarar medidas excepcionales que sus técnicos no respaldan. El cauce ordinario para homogeneizar es el Consejo Interterritorial, órgano de coordinación previsto en la Ley 16/2003, que adopta acuerdos y recomendaciones pero no obliga a quien no los acepta. Al Gobierno le sirve para convertir el frente de '¿quién manda?' en una foto de acuerdo con nombres y apellidos; a la comunidad de la oposición que se desmarca le rinde mantener el contraste, porque la oposición gana con cada diferencia visible.
    dato: El Consejo Interterritorial es el órgano permanente de coordinación, cooperación, comunicación e información de los servicios de salud entre ellos y con la Administración del Estado (Ley 16/2003, de cohesión y calidad del SNS).
    fuente: https://www.sanidad.gob.es/organizacion/consejoInterterri/introduccion.htm
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - sanidad
    - educacion
    - coordinacion_territorial
    id: politico/h3/1
  - texto: 'El Gobierno se adelanta a la oleada nocturna de fotoqueratitis: Sanidad, junto a las comunidades, pide a los hospitales reforzar las urgencias oftalmológicas para la tarde y la noche y difunde un mensaje explícito de que los casos que lleguen serán lesiones por mirar al sol o a lámparas UV, no un efecto diferido del fenómeno. Consumo añade un aviso específico sobre lámparas de uñas, linternas y lámparas de luz negra.'
    mecanismo: Un gobierno pierde legitimidad si rectifica y la gana si parece haberlo previsto. La sociedad de oftalmología ya ha fijado el calendario clínico (síntomas entre 6 y 12 horas después de la exposición), y eso da al Gobierno respaldo técnico para anunciarlo sin riesgo de que le desmientan. Si las urgencias se llenan esta noche sin aviso previo, el relato del agitador ('algo nos han hecho') y la oposición capitalizan el silencio; si se anuncia antes, cada caso confirma al Gobierno. El aviso sobre lámparas es la medida más barata y con base ya existente, y apunta a la conducta, no al fenómeno.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - comunicacion_publica
    - politica
    - consumo
    id: politico/h3/2
  - texto: 'La oposición se divide ante el relato de ocultación: el principal partido de la oposición registra peticiones de información y de comparecencia sobre la coordinación y los avisos, pero sus portavoces evitan citar las ''marcas ocultas''; otra fuerza o cargos sueltos siguen compartiendo clips del agitador y piden explicaciones sobre qué ''estaba marcado''. El Gobierno aprovecha la fisura y acusa a quien comparte esos clips de difundir bulos en plena crisis.'
    mecanismo: Compartir clips del agitador da munición barata, pero cuando los verificadores ya han desmentido las 'marcas ocultas' y se acerca una noche con lesiones, quedar asociado a un bulo sanitario es un coste que un partido con aspiración de gobierno no quiere asumir. Le conviene más atacar la descoordinación, que es un hecho verificable, que la ocultación, que no lo es. Una fuerza que compite por el voto desconfiado no tiene ese freno. Para el Gobierno, señalar a quien amplifica el bulo es la forma de recuperar la iniciativa sin tener que explicar la causa, que no conoce.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - politica
    - desinformacion
    - parlamento
    id: politico/h3/3
  - texto: 'Interior evita pronunciarse en público sobre la pérdida de invisibilidad del marcado forense: no confirma qué sistemas quedan afectados ni da instrucciones abiertas, y canaliza la respuesta por vía interna a Policía Nacional, Guardia Civil y empresas de seguridad privada (preservar pruebas ya marcadas, documentar antes de que se limpien, revisar protocolos). En público se limita a decir que las investigaciones en curso cuentan con otros medios de prueba.'
    mecanismo: Explicar en rueda de prensa qué marcas forenses ya no son secretas sería dar una guía a quien quiere borrar rastros y, a la vez, confirmar al agitador que 'había marcas ocultas'. Ningún gobierno puede afirmar lo que sus técnicos no han evaluado, y en tres horas nadie ha medido cuánto pierde cada sistema. El silencio público con instrucción interna protege la eficacia policial sin abrir un frente de rectificación, aunque deja a las consultas de ciudadanos y empresas de seguridad sin respuesta oficial.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - seguridad
    - justicia
    - comunicacion_publica
    id: politico/h3/4
  - texto: En el plano internacional la presidencia del Consejo de la UE sube el dispositivo de respuesta política a crisis del modo de intercambio de información a una mesa redonda de crisis con Estados, Comisión y Servicio de Acción Exterior para alinear mensajes sanitarios y la presión a las plataformas, sin medidas comunes. La OMS sigue sin convocar el Comité de Emergencias y publica en su lugar una orientación técnica sobre protección ocular que sirve de autoridad de referencia a la que pueden enlazar gobiernos y plataformas.
    mecanismo: El dispositivo de respuesta política a crisis de la UE tiene escalones (seguimiento, intercambio de información, activación plena) y su activación y su nivel los decide la presidencia del Consejo; la mesa redonda es el instrumento que da imagen de coordinación europea sin exigir base legal para medidas nuevas. La OMS, por su parte, solo convoca el Comité de Emergencias del Reglamento Sanitario Internacional cuando hay un evento que puede constituir una emergencia de salud pública de importancia internacional, y un cambio de percepción sin daño acreditado ni propagación no encaja; pero la falta de una autoridad común está fragmentando los paneles de las plataformas, y una orientación técnica es la forma de llenar ese hueco sin comprometerse con una declaración que tendría que retirar.
    dato: El IPCR tiene tres modos (seguimiento, intercambio de información y activación plena) y la presidencia del Consejo decide su activación; según el artículo 12 del RSI, el director general de la OMS convoca el Comité de Emergencias cuando considera que un evento puede constituir una emergencia de salud pública de importancia internacional.
    fuente: https://www.consilium.europa.eu/en/policies/ipcr-response-to-crises ; https://www.who.int/features/qa/39/en/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - politica_internacional
    - union_europea
    - sanidad
    - plataformas_digitales
    id: politico/h3/5
  reacciona_a:
  - medios/h2/4
  - disruptor/h2/1
  - oftalmologa/h2/1
- agente: medios
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora los medios difunden los primeros casos clínicos reales de quemadura de córnea, antes de la oleada nocturna anunciada: personas que miraron de cerca lámparas de uñas o de luz negra, o al sol, durante la primera hora llegan a urgencias con dolor, lagrimeo y sensación de arena. Los digitales los titulan como ''los primeros afectados reales'' y el calendario de ''esta noche, no ahora'' que fijó la sociedad de oftalmología queda en entredicho, lo que el agitador usa para decir que también en eso se equivocan o mienten.'
    mecanismo: 'La latencia de la fotoqueratitis no es fija: depende de la dosis, y con exposiciones intensas y cercanas los síntomas pueden aparecer mucho antes que el rango de seis a doce horas que se ha popularizado. Quien acercó una lámpara UV a los ojos a las 10:30 puede tener síntomas a mediodía. Un medio que compite por ser el primero acepta como fuente el testimonio de urgencias o del afectado, y un caso real temprano le da la exclusiva. Discrepo en parte de oftalmologa/h2/1: la oleada principal será nocturna, pero los casos más graves llegan antes y rompen el mensaje de que ''aún no hay lesiones'', que era la baza de credibilidad de la sociedad.'
    dato: Según la EyeWiki de la Academia Americana de Oftalmología, los síntomas de la fotoqueratitis aparecen entre 30 minutos y 12 horas después de la exposición, y el epitelio corneal se cura en 24 a 72 horas.
    fuente: https://eyewiki.aao.org/Photokeratitis
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - medios
    - desinformacion
    - confianza_institucional
    id: medios/h3/1
  - texto: 'Las grandes cadenas de Estados Unidos abren sus programas matinales con el amanecer en la Costa Este, y la conversación global cambia de centro: las imágenes de gente viendo su primera salida del sol con los colores nuevos generan una segunda ola viral en inglés, con encuadres propios (seguridad al volante en la hora punta matinal, colegios, la Casa Blanca), que desplaza en las plataformas el relato europeo y obliga a los medios españoles a importar el ángulo estadounidense.'
    mecanismo: En la Costa Este el suceso cayó de madrugada y en oscuridad, donde casi no hay UV-A que ver; la experiencia de la luz solar llega con el amanecer, al final de la tercera hora en hora de Madrid. Los matinales estadounidenses son el mayor escaparate televisivo de la mañana y las plataformas dominantes tienen allí su mercado principal, así que sus algoritmos priorizan ese contenido nuevo en inglés. Para los medios europeos, que llevan tres horas sin novedad sanitaria con fuente, el contenido estadounidense es material nuevo para el directo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - redes_sociales
    - politica_internacional
    id: medios/h3/2
  - texto: 'Las fotos de personas identificables con la ''máscara'' de protector que circulan por el canal del agitador y por grupos de clase se convierten en noticia de acoso: los medios recogen testimonios de chicas burladas en institutos y de adultos expuestos sin consentimiento, y la Agencia Española de Protección de Datos o sus portavoces recuerdan que difundir imágenes de terceros puede ser ilícito y remiten a su canal prioritario de retirada. El aviso llega a los medios pero apenas a la mensajería cerrada donde circulan las imágenes.'
    mecanismo: El acoso a menores y la exposición de personas concretas es un ángulo humano con víctimas y fuentes con nombre, justo lo que necesita un directo que se ha quedado sin novedad técnica. La AEPD tiene ya un cauce para pedir la retirada urgente de contenido sensible difundido sin consentimiento, así que puede pronunciarse sin norma nueva y con bajo coste. Pero el canal propio del agitador está fuera del alcance práctico de las retiradas, de modo que la respuesta institucional es sobre todo declarativa y el agitador la presenta como otra forma de censura.
    dato: La AEPD mantiene un canal prioritario para comunicar la difusión ilícita de contenido sensible en internet y solicitar su retirada urgente.
    fuente: https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/presentacion-del-canal-prioritario-para-comunicar-la-difusion
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - educacion
    - privacidad
    - menores
    - desinformacion
    id: medios/h3/3
  - texto: 'Los medios adoptan los nombres inventados por los adolescentes para los colores nuevos y los convierten en tema propio: piezas de ''cómo se llama este color'', encuestas a la audiencia y consultas a lingüistas, a la Fundéu o a la RAE, que piden prudencia y no fijan ningún término. Cada idioma y cada país acaba con nombres distintos, y la falta de vocabulario común complica que testigos, médicos y periodistas se entiendan sobre lo que cada uno ve.'
    mecanismo: Las cámaras no reproducen el fenómeno, así que la palabra es lo único compartible, y un contenido ligero y participativo da respiro a un directo cargado de miedo y política. Las instituciones del idioma no acuñan términos en horas, solo orientan, de modo que los nombres los fija el uso en redes, que es fragmentado por idioma y plataforma. Sin una palabra común, las descripciones clínicas y los testimonios se vuelven difíciles de comparar, y eso deja más espacio a quien dice ver cosas distintas o 'más' que los demás.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - medios
    - redes_sociales
    - cultura
    - salud
    id: medios/h3/4
  - texto: 'La pérdida de invisibilidad del marcado forense salta de los foros a los medios como historia de seguridad: piezas sobre ''el fin de la marca invisible'' con declaraciones de empresas de seguridad y portavoces policiales que reconocen consultas pero no dan detalles operativos. La cobertura funciona sin querer como tutorial, porque explica qué se marcaba y dónde, y el agitador la cita como confirmación de que ''nos marcaban a todos''.'
    mecanismo: Es un ángulo con fuentes con nombre, conflicto y novedad, y encaja con el interés por las 'marcas' que ya ha creado el agitador, así que garantiza audiencia. La policía no puede detallar sus métodos sin perjudicar investigaciones y las empresas evitan admitir que su producto ha perdido valor, de modo que el hueco lo llenan expertos y periodistas que describen el funcionamiento del sistema. Al explicar el mecanismo, el medio difunde a la vez cómo detectar y limpiar los rastros, y el relato de vigilancia gana un ejemplo verificable.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - seguridad
    - policia
    - desinformacion
    id: medios/h3/5
  reacciona_a:
  - oftalmologa/h2/1
  - adolescente/h2/3
  - agitador/h2/3
  - disruptor/h2/1
- agente: oftalmologa
  tramo: h3
  afirmaciones:
  - texto: 'Con las lámparas de luz negra agotadas, parte de la demanda se desvía a lo que queda en las tiendas y en los marketplaces con la etiqueta ''lámpara UV'': esterilizadores y lámparas germicidas de UV-C. La sociedad de oftalmología publica en la hora 3 un aviso por tipo de producto: la luz negra de UV-A muestra los colores nuevos y solo es peligrosa si se mira de cerca y durante mucho rato, mientras que la lámpara germicida no muestra nada nuevo y quema la córnea con exposiciones cortas.'
    mecanismo: El fenómeno amplía la percepción al UV-A, no al UV-C, así que una lámpara germicida (UV-C) no enseña ningún color nuevo y quien la enciende tiende a acercarse más o a dejarla encendida para 'ver algo', con lo que se expone a la radiación más lesiva para el epitelio corneal. El comprador no distingue entre bandas porque los anuncios dicen solo 'UV'. Ya ocurrió con las lámparas germicidas compradas en la pandemia, que produjeron fotoqueratitis en usuarios domésticos. Separar los productos por banda le da a la sociedad un mensaje útil y concreto, distinto del genérico 'no mires lámparas UV' que el agitador ya ha reencuadrado como ocultación.
    dato: Serie de 7 pacientes con fotoqueratitis por lámparas germicidas de uso doméstico compradas durante la pandemia de COVID-19, con erosiones epiteliales punteadas difusas en todos; la mayoría resolvió en 2-3 días.
    fuente: https://pubmed.ncbi.nlm.nih.gov/33215961/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - consumo
    - comercio_online
    - informacion_publica
    id: oftalmologa/h3/1
  - texto: La sociedad de oftalmología difunde a las urgencias hospitalarias un protocolo para la oleada de la noche que obliga a anotar en cada caso la hora y la fuente de exposición (sol, luz negra, lámpara de uñas, germicida) y que separa la fotoqueratitis, molesta pero que se cura en pocos días, de la retinopatía solar, menos frecuente pero capaz de dejar una mancha central persistente. Pide también no dar colirio anestésico para casa.
    mecanismo: La retinopatía solar es la única lesión de esta jornada que puede no curarse del todo, y por eso es la que mejor encajaría en el relato de daño permanente del agitador si se presenta sin contexto. Si cada historia clínica registra que hubo una conducta de exposición previa, la sociedad puede demostrar con datos propios que las lesiones vienen de mirar al sol o a lámparas y no del fenómeno, y protege su credibilidad cuando lleguen los casos. El colirio anestésico alivia el dolor de la fotoqueratitis pero su uso repetido retrasa la curación del epitelio, y la presión asistencial de una noche saturada empuja a recetarlo para despachar pacientes.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - urgencias
    - informacion_publica
    - politica
    id: oftalmologa/h3/2
  - texto: La sociedad lanza un registro abierto de testimonios estructurado (edad, si ha sido operado de cataratas y con qué lente, si lleva gafas y de qué material, ojo por ojo) para medir el gradiente de percepción, y lo presenta como el primer estudio sistemático del fenómeno. En pocas horas recibe miles de respuestas y otras sociedades europeas piden adherirse o copiar el formulario.
    mecanismo: 'Lo único que la oftalmología puede medir sin conocer la causa es cuánto UV-A llega a la retina de cada persona, y eso depende de variables conocidas: la edad del cristalino, la lente intraocular y el filtro de las gafas. Los afáquicos, los operados con y sin filtro y los niños forman un experimento natural que ya existe. Quien publique primero un protocolo de recogida se convierte en la referencia a la que enlazan plataformas y gobiernos, que en la hora 2 no tenían una autoridad común; ese es justo el incentivo de la sociedad. El riesgo es que un registro abierto mezcla testimonios fiables con sugestión, y los primeros resultados serán descriptivos, no concluyentes.'
    dato: El cristalino adulto absorbe casi toda la energía incidente hasta cerca de 400 nm; el pico de absorción está en 365 nm a los 8 años y en 450 nm a los 65, y en niños hasta unos 10 años hay una pequeña ventana de transmisión hacia 320 nm.
    fuente: https://www.dovepress.com/ultraviolet-damage-to-the-eye-revisited-eye-sun-protection-factor-e-sp-peer-reviewed-fulltext-article-OPTH
    confianza: media
    evidencia: dato
    areas_afectadas:
    - ciencia
    - salud
    - informacion_publica
    - plataformas
    id: oftalmologa/h3/3
  - texto: Empiezan a llegar a las clínicas oftalmológicas privadas consultas de personas mayores que preguntan si operarse de cataratas o cambiar su lente intraocular les permitiría ver los colores nuevos como los demás, y alguna clínica lo aprovecha en redes sugiriendo que la cirugía de cristalino 'devuelve' la visión ultravioleta. La sociedad lo denuncia como publicidad sanitaria engañosa.
    mecanismo: 'El gradiente por edad ya es público y el precedente de los afáquicos, que la propia sociedad difundió en la hora 1, deja una inferencia peligrosa al alcance de cualquiera: si sin cristalino se ve más UV, quitar el cristalino amarillento haría ver más. Las clínicas privadas ya venden la cirugía de cristalino como refractiva y tienen incentivo para captar ese interés, aunque las lentes intraoculares actuales suelen llevar filtro UV y nadie sabe si el fenómeno es permanente. Para la sociedad, cortar este uso comercial de su propio argumento es una cuestión de credibilidad: no puede dejar que su referencia clínica se convierta en reclamo de quirófano.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - salud
    - sanidad_privada
    - publicidad
    - consumo
    id: oftalmologa/h3/4
  - texto: 'Cuando medios y comunidades piden ligar la pauta de gafas al índice ultravioleta que publican los servicios meteorológicos, la sociedad advierte que ese índice no sirve para medir el deslumbramiento del fenómeno: un índice bajo en noviembre no garantiza poco deslumbramiento, porque el índice mide sobre todo el riesgo de quemadura y el deslumbramiento depende del UV-A.'
    mecanismo: El índice UV está ponderado por el espectro de eritema, en el que pesa mucho más el UV-B, que cae con fuerza en invierno y con el sol bajo, mientras que el UV-A, la banda que ahora se percibe, varía menos con la estación y atraviesa mejor las nubes. Usar el índice como semáforo para las gafas daría falsa tranquilidad en el norte de Europa nublado y descolocaría la pauta situacional que la sociedad fijó en la hora 2. Corregir a tiempo una regla fácil pero equivocada es lo que separa a la sociedad de los portavoces improvisados y refuerza su papel de referencia técnica.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - meteorologia
    - educacion
    - informacion_publica
    id: oftalmologa/h3/5
  reacciona_a:
  - economista/h2/4
  - agitador/h2/2
- agente: adolescente
  tramo: h3
  afirmaciones:
  - texto: 'En mi grupo y en los de clase se monta el pique de ''quién ve más'': cuando se enteran de que los niños ven los colores más fuertes que los mayores, nosotros lo usamos para decir que vemos cosas que nuestros padres y los profes no ven, y salen memes y vídeos de ''los boomers no lo ven'' que se comparten muchísimo.'
    mecanismo: 'La pauta de los oftalmólogos sobre la edad llega a los grupos convertida en titular simple: cuanto más joven, más ves. Por una vez algo nos pone por encima de los adultos, que llevan toda la mañana diciéndonos qué hacer sin saber nada, y presumir de eso da estatus en clase y en redes. Como nadie puede demostrar con una foto lo que ve, cada uno exagera lo suyo y nadie puede pillarle.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes_sociales
    - juventud
    - relaciones_familiares
    id: adolescente/h3/1
  - texto: Entre los de mi edad corre el rumor de que si miras un rato cerca del sol o muy de cerca una lámpara de uñas 'se te abre' más la vista y ves más colores, y algunos lo prueban como reto en el patio, en el camino a casa o en la habitación, sin que les duela en el momento.
    mecanismo: Si ver más colores da estatus, cualquier truco para ver más se copia rápido, y el aviso de no mirar al sol suena a lo típico que dicen los mayores. Como mirarlo no duele en el momento, quien lo hace dice que no pasa nada y eso anima a otros. Así entran adolescentes en la oleada de lesiones de esta noche que ya anticipan los oftalmólogos, por conducta y no por el fenómeno.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - juventud
    - redes_sociales
    id: adolescente/h3/2
  - texto: 'La amiga que tiene una lámpara de uñas UV o una linterna de luz negra en casa se convierte en el centro del plan de la tarde: se queda gente para ir a su casa a mirar ropa, maquillaje, dientes y billetes con la luz, y lo grabamos contándolo aunque el vídeo no enseñe nada.'
    mecanismo: En casa con luz LED casi no se ven los colores y las lámparas se están agotando en las tiendas, así que quien ya tiene una tiene algo que los demás no pueden comprar hoy. Entre adolescentes, tener lo que todos quieren te da poder para decidir quién viene y quién no. Además los padres prefieren que estemos en casa de alguien conocido que por la calle, así que nos dejan.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - juventud
    - consumo
    - salud
    id: adolescente/h3/3
  - texto: En clase algunos descubren en la mano o en la muñeca restos del sello de la discoteca o del local del fin de semana, que antes no se veía, y empiezan los cotilleos y las capturas sobre quién salió a sitios donde no deberían dejarle entrar o sin que lo supieran sus padres.
    mecanismo: Los sellos de entrada de los locales están hechos para verse solo con luz negra y ahora los vemos todos, igual que otras marcas que se ponían para no verse. Si no te has frotado bien, queda rastro en la piel o en la pulsera del móvil. A los dieciséis, saber dónde ha estado alguien es información que da poder en el grupo, y que se entere tu familia es el miedo número uno, así que hay quien se va al baño a frotarse y quien lo usa para dejar en evidencia a otro.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - juventud
    - relaciones_familiares
    - seguridad
    id: adolescente/h3/4
  - texto: 'Cuando acaban las clases a mediodía y salimos a la calle con el sol más alto, la salida del instituto se convierte en un rato largo en la puerta: nadie se va directo a casa, nos quedamos mirando la calle y grabándonos mientras contamos lo que vemos, y llegamos tarde a comer, lo que provoca broncas y llamadas de padres que ya estaban nerviosos.'
    mecanismo: Llevamos toda la mañana dentro, con recreo en interior y ventanas que no siempre dejan ver los colores, así que la salida es el primer momento libre para verlo todo al aire libre y con el grupo. Como casi nadie lleva gafas de sol para no perderse los colores, el deslumbramiento hace que vayamos más despacio y nos paremos. Los padres, con el móvil localizándonos y el miedo que traen de la mañana, ven que no llegamos y llaman, y lo que para ellos es preocupación para nosotros es control.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - juventud
    - relaciones_familiares
    - educacion
    - salud
    id: adolescente/h3/5
  reacciona_a: []
- agente: agitador
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora el agitador se adelanta a la oleada nocturna de fotoqueratitis: abre en su canal propio un formulario o hilo fijo para que sus seguidores registren ''síntomas tardíos'' (escozor, lagrimeo, sensación de arena) y anuncia que esta noche se verá ''lo que nos han hecho''. Así, cuando los casos lleguen a urgencias, ya tendrá una base de testimonios propia y un marco previo que convierte la lesión por conducta en daño del fenómeno.'
    mecanismo: La fotoqueratitis aparece horas después de la exposición, y la nota de triaje de la sociedad de oftalmología ya ha anunciado la oleada para esta tarde y noche. Ese anuncio es público, así que el agitador sabe cuándo llegará la noticia y puede preparar su versión antes. Recoger testimonios propios le da material que los verificadores no pueden contrastar, porque está en un canal cerrado y es testimonial. Además, parte de esos síntomas vendrá de seguidores que buscaron marcas con lámparas UV o cerca del sol tras su propio encuadre de la hora 2, de modo que el relato se alimenta del daño que contribuyó a provocar. Para él, que la oleada se lea como conducta sería perder la historia; adelantarse es la única forma de ganarla.
    dato: La fotoqueratitis es una quemadura corneal por UV cuyos síntomas aparecen con varias horas de retraso tras la exposición.
    fuente: https://eyewiki.aao.org/Photokeratitis
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - salud
    - informacion
    - redes
    id: agitador/h3/1
  - texto: 'El agitador ataca la nota de triaje de la sociedad de oftalmología precisamente porque anticipó los casos: presenta que ''ya sabían que habría heridos esta noche'' como prueba de conocimiento previo, y no como predicción clínica. El anuncio preventivo, pensado para desactivar su relato, se convierte en su pieza central del tramo.'
    mecanismo: 'Es el mismo patrón que le funcionó en la hora 2 con el BCE: tomar una explicación correcta y cambiar su significado de ''lo conocemos'' a ''lo ocultaban''. Una predicción acertada de una autoridad es, para una audiencia ya vacunada contra fuentes oficiales, más sospechosa que un error, porque sugiere que alguien sabía. No necesita negar la latencia de la fotoqueratitis, solo omitir que la causa es mirar al sol o a lámparas UV. La sociedad de oftalmología no puede retirar el aviso sin perder credibilidad, así que su mensaje queda fijado y él puede citarlo una y otra vez.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - informacion
    - confianza_institucional
    id: agitador/h3/2
  - texto: 'Con la oposición compartiendo sus clips sobre descoordinación, el agitador sube la apuesta en el terreno de ''¿quién manda?'': se apropia de la comparecencia anunciada del presidente como ''lo que nosotros forzamos'' y señala la reunión del Consejo de Seguridad Nacional como prueba de que el asunto es ''de seguridad, no de salud''. Algunos cargos de la oposición empiezan a tomar distancia pública de él para no quedar asociados al bulo, y él convierte esa distancia en una historia de traición que le acerca aún más a su núcleo duro.'
    mecanismo: 'El agitador gana relevancia cuando puede atribuirse efectos visibles, y la comparecencia es un hecho con fecha. Que el Gobierno haya usado un órgano de seguridad nacional, aunque sea solo para coordinar, le da una palabra (''seguridad'') que su audiencia lee como confirmación de amenaza oculta. Para la oposición, el clip era munición barata en la hora 2, pero en la hora 3 el relato de las ''marcas ocultas'' ya está desmentido en medios generalistas y asociarse a él tiene coste reputacional; lo racional es usar la descoordinación sin el marco conspirativo. Para el agitador, la ruptura no es una pérdida: el abandono por parte de la política institucional confirma ante su audiencia que nadie de dentro es de fiar.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - politica
    - informacion
    - confianza_institucional
    id: agitador/h3/3
  - texto: 'El agitador se sube al hallazgo del marcado forense que pierde su invisibilidad y lo convierte en el eje de su relato: mezcla en su canal ejemplos reales de marcadores tipo SmartWater, rociadores antiintrusión y tintas de seguridad con residuos y blanqueantes sin relación, y anima a sus seguidores a revisar su ropa, su casa y sus coches en busca de ''marcas''. El efecto colateral es que su contenido funciona de facto como guía para detectar y limpiar marcado forense, y empresas de seguridad y policía ven crecer las consultas de particulares asustados mezcladas con quienes buscan borrar rastros.'
    mecanismo: En la hora 2 los desmentidos tuvieron que admitir que parte de lo que se ve sí estaba oculto a propósito; ese fragmento de verdad es su activo más creíble y lo explota porque necesita credibilidad ante su audiencia. Pedir a la audiencia que revise sus cosas le da contenido gratis y participación, como en las horas anteriores. Como no distingue entre marcadores forenses y fluorescencia inocua, multiplica las falsas alarmas y satura las líneas de consulta, y a la vez difunde a un público masivo cómo se ve el marcado de seguridad, lo que beneficia a quien tiene algo marcado que ocultar. Él no lo busca, pero tampoco le cuesta nada.
    dato: Los marcadores forenses tipo SmartWater se basan en una traza invisible que se detecta con luz ultravioleta.
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - seguridad
    - policia
    - informacion
    id: agitador/h3/4
  - texto: 'La migración a su canal propio de mensajería le sale rentable en audiencia pero cara en ingresos: las plataformas grandes limitan su alcance y desmonetizan algunos directos, y él compensa pidiendo donaciones directas y suscripciones en su canal, con llamamientos ligados a ''seguir investigando las marcas'' y a ''cubrir esta noche los casos de urgencias''. La urgencia de la noche que viene se convierte en motor de recaudación.'
    mecanismo: Sus restricciones dicen que las plataformas grandes pueden retirarle contenido y desmonetizarlo, y en la hora 2 ya empezaron. El canal propio no se puede desmonetizar desde fuera, pero tampoco paga por publicidad, así que su ingreso pasa a depender del pago directo de la audiencia. La donación responde a urgencia y a sensación de pertenencia, y el calendario clínico anunciado por los oftalmólogos le regala una fecha concreta, esta noche, para pedir dinero con un motivo. Cuanto más miedo hay ante lo que viene, más dona su núcleo duro, que es exactamente su incentivo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes
    - economia_creadores
    - informacion
    id: agitador/h3/5
  reacciona_a:
  - oftalmologa/h2/1
  - medios/h2/3
  - disruptor/h2/1
  - politico/h2/1
  - politico/h2/2
- agente: disruptor
  tramo: h3
  afirmaciones:
  - texto: 'En el Cono Sur (Chile, Argentina, Uruguay, sur de Brasil), donde amanece entre la hora 2 y la hora 3 en plena primavera austral, la gente vive el fenómeno ya contado por Europa y decide su rutina antes de salir de casa: una parte deja el protector solar y el maquillaje con SPF en el baño para no llevar la máscara que ha visto descrita en redes europeas. Es el primer lugar donde el abandono del protector es preventivo y masivo, no reactivo, y coincide con la época de índice UV más alto del año, así que las quemaduras reales aparecerán allí antes y con más intensidad que en la Europa de noviembre.'
    mecanismo: 'En Europa la gente se quitó el protector al descubrir la máscara; en Sudamérica la decisión se toma con horas de información previa, en el momento más barato (no ponérselo cuesta menos que quitárselo en la oficina) y con el estigma ya construido, incluido el contenido burlón y racista sobre las caras negras. Pero noviembre en Santiago o Buenos Aires no es noviembre en Madrid: el índice UV ronda niveles muy altos o extremos a mediodía, de modo que el coste diferido de ir sin protección es mucho mayor. La tensión sobre si el abandono produce quemaduras se resuelve primero en el hemisferio sur, y esas quemaduras, que aparecen horas después, se sumarán a la noche de fotoqueratitis como otra ''lesión tardía'' disponible para el relato de daño diferido.'
    dato: Meteored y Meganoticias anticipan en noviembre índice UV extremo para Santiago y la Región Metropolitana.
    fuente: https://www.meganoticias.cl/nacional/505260-indice-uv-radiacion-extremo-muy-alto-calor-temperaturas-santiago-region-metropolitana-13-11-2025.html
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - cosmetica
    - redes_sociales
    - latinoamerica
    id: disruptor/h3/1
  - texto: 'Las lámparas de luz negra y las linternas UV compradas en la hora 2 se apuntan, una vez en casa, a la nevera y la despensa: frutos secos, maíz, especias, cítricos y pan muestran puntos y halos fluorescentes. Arranca una ola de comida tirada, reclamaciones a supermercados y llamadas a las agencias de seguridad alimentaria, y el agitador amplía las ''marcas'' a la comida (''nos envenenan y lo marcan'').'
    mecanismo: 'La fluorescencia bajo UV-A de 365 nm es un método de cribado real: la fluorescencia verde-amarilla brillante se usa como prueba presuntiva de aflatoxinas en maíz, y el moho, las magulladuras y algunos tratamientos poscosecha se ven distintos bajo esa luz. Pero es una prueba de sospecha que genera falsos positivos y no mide cantidad. El consumidor no distingue entre moho real, piel o cera inocua y residuos legales, así que actúa por la regla más simple: si brilla, se tira o se reclama. Para el agitador es el salto perfecto, porque la comida es universal, íntima y de verificación lenta, y además hay un fragmento de verdad: el sector sí usaba esa luz para detectar lo que no se ve.'
    dato: La FAO describe la prueba de fluorescencia verde-amarilla brillante (BGY) bajo luz UV como método presuntivo para estimar aflatoxinas en maíz.
    fuente: https://www.fao.org/4/X5036E/x5036E0G.HTM
    confianza: media
    evidencia: dato
    areas_afectadas:
    - alimentacion
    - consumo
    - desinformacion
    - distribucion
    id: disruptor/h3/2
  - texto: En España los sindicatos y los delegados de prevención reclaman a mediodía que las empresas evalúen el nuevo riesgo para quien trabaja al aire libre (obra en altura, repartidores en moto y bici, agricultura, conductores de reparto, operarios de grúa), y en algunos tajos los trabajadores invocan el derecho a interrumpir la actividad por riesgo grave e inminente. La Inspección de Trabajo y las mutuas reciben consultas que no saben contestar.
    mecanismo: 'La Ley de Prevención de Riesgos Laborales obliga al empresario a evaluar los riesgos nuevos y su artículo 21 permite al trabajador interrumpir la actividad y abandonar el lugar de trabajo ante un riesgo grave e inminente. El deslumbramiento en altura o en moto encaja de forma discutible en ese supuesto, y la pauta oftalmológica de precaución extra en moto y bici ofrece justo el respaldo técnico que necesita un delegado para pararlo. Ningún protocolo de empresa contempla el caso, nadie quiere responder de un accidente laboral, y el mediodía de la hora 3 concentra el sol más intenso del día en España. El conflicto no es sanitario ni político: es laboral y local, y escapa al mensaje único del Consejo de Seguridad Nacional.'
    dato: 'Artículo 21 de la Ley 31/1995 de Prevención de Riesgos Laborales: derecho del trabajador a interrumpir su actividad ante riesgo grave e inminente.'
    fuente: https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - trabajo
    - sindicatos
    - construccion
    - reparto
    - prevencion
    id: disruptor/h3/3
  - texto: 'Las personas con vitíligo y otras alteraciones de la pigmentación pasan de golpe a ser mucho más visibles en exterior: sus zonas despigmentadas destacan con un contraste que antes solo veía un dermatólogo con lámpara de Wood. Empiezan los comentarios y las fotos en la calle y el transporte, y las asociaciones de pacientes salen a pedir respeto antes de que nadie en el debate público se acuerde de ellas.'
    mecanismo: 'La lámpara de Wood, que emite UV-A, se usa en dermatología precisamente porque acentúa la diferencia entre piel pigmentada y despigmentada: la melanina absorbe el ultravioleta y la piel sin melanina lo refleja. Si todo el mundo ve en UV-A, la luz de mediodía hace de lámpara de Wood permanente. El canon ya cuenta las manchas y el protector como fenómenos de todos, pero aquí la visibilidad nueva recae sobre un grupo concreto que ya sufría estigma, y lo hace en un clima de burla sobre caras y pieles que las plataformas solo moderan cuando encaja como odio racial.'
    dato: El Manual MSD indica que el examen con lámpara de Wood ayuda a detectar y delimitar las lesiones de vitíligo.
    fuente: https://www.msdmanuals.com/es/professional/trastornos-dermatol%C3%B3gicos/trastornos-de-la-pigmentaci%C3%B3n/vitiligo
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - discriminacion
    - dermatologia
    - asociaciones_pacientes
    id: disruptor/h3/4
  - texto: Anticuarios, galerías, casas de subastas y coleccionistas empiezan a recibir llamadas de compradores que, con la lámpara recién comprada o junto a una ventana, ven en sus cuadros, cerámicas y muebles retoques, repintes y piezas reconstruidas que nadie les dijo. A la vez, en oficinas y casas aparecen correcciones y borrados en documentos (tachaduras con corrector, tinta borrada, firmas repasadas), y surgen las primeras reclamaciones por piezas o papeles 'manipulados'.
    mecanismo: 'El examen con fluorescencia UV es una técnica estándar de conservación y de peritaje: el barniz antiguo fluoresce de forma distinta al repinte moderno, y las alteraciones de tinta y papel se detectan con la misma luz. Esa información estaba reservada a restauradores y peritos; ahora la tiene cualquiera, sin contexto para saber si una restauración declarada es legítima o un engaño. El efecto se reparte entre reclamaciones fundadas, sospechas infundadas y oportunistas que intentan devolver una compra antigua, y abre una vía que el agitador puede usar (''todo está retocado''), aunque su impacto principal es comercial y jurídico.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - arte
    - comercio
    - documentos
    - consumo
    id: disruptor/h3/5
  reacciona_a: []

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

estado_del_mundo:
  tramo: h3
  resumen: "..."
  hechos_establecidos:
    - id: h3-01
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
