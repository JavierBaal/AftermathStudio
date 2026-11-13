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
Hora 2 (PT2H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h1
  resumen: 'En la primera hora el fenómeno se vive sobre todo en exteriores soleados de Europa, África y Oriente Medio, mientras América duerme y recibe un relato ya formado por otros, con el rumor de que allí no ha llegado. Gobiernos, Sanidad y la OMS comunican sin decretar nada, y ese vacío lo ocupan recomendaciones contradictorias, bulos sanitarios y creadores como el agitador, lo que empuja a la gente a consultas y urgencias por deslumbramiento, diferencias de percepción y manchas de protector solar. El deslumbramiento cruza áreas: frena el tráfico y el trabajo al aire libre, vacía las existencias de gafas de sol, mueve en bolsa a los valores de óptica y hace que los institutos metan a los alumnos dentro y algunos padres los recojan. Como las cámaras no captan los colores nuevos, lo que se comparte son relatos y montajes, lo que alimenta a la vez la desinformación y la frustración.'
  hechos_establecidos:
  - id: h1-01
    texto: El fenómeno se nota sobre todo donde es de día con sol (Europa, África y Oriente Medio), que fijan el relato global de la primera hora. En América es de madrugada, casi nadie puede comprobarlo con sus propios ojos y circula el rumor de que el cambio no afecta al continente o que avanza en ola hacia el oeste; solo se desmentirá con el amanecer.
    origen:
    - medios/h1/1
    - disruptor/h1/3
  - id: h1-02
    texto: No hay desplome generalizado de la renta variable europea, pero sí paradas técnicas por los mecanismos de protección de Euronext en valores de óptica, gafas, pantallas y cámaras, que se mueven bruscamente en ambas direcciones. Los fabricantes de gafas de sol se convierten en el termómetro del suceso, entre la apuesta por un pico de demanda y la duda de que sea transitorio.
    origen:
    - economista/h1/1
    - economista/h1/2
  - id: h1-03
    texto: 'En las zonas de día se agotan las gafas de sol en farmacias, ópticas y gasolineras y aparecen reventas a precios inflados en línea, con la demanda americana aún por llegar. Al ponérselas, la gente comprueba a simple vista si filtran el ultravioleta: las baratas sin filtro quedan en evidencia y empiezan las quejas públicas contra marcas y vendedores.'
    origen:
    - economista/h1/3
    - disruptor/h1/4
  - id: h1-04
    texto: 'El cambio se concentra en exteriores y junto a ventanas; en interiores con LED todo se ve casi igual. En carretera, el contraste entre parabrisas, que filtra casi todo el UV-A, y ventanillas laterales, que dejan pasar más, sumado al deslumbramiento, provoca maniobras bruscas, paradas en arcén y alcances leves en ciudad. Construcción, agricultura, reparto y transporte por carretera frenan por seguridad: es pérdida de horas, no de empleo.'
    origen:
    - disruptor/h1/1
    - economista/h1/4
    - oftalmologa/h1/3
  - id: h1-05
    texto: 'Ningún gobierno declara estado de excepción o alarma: salen comunicados de calma de los ministerios de Sanidad sin medidas obligatorias, y la OMS solo dice que recaba información, sin convocar aún su Comité de Emergencias. En España el Consejo de Ministros del martes se reconvierte en reunión de seguimiento y la rueda de prensa se aplaza sin hora. El vacío lo ocupan la oposición, que exige comparecencia, y políticos autonómicos o locales, profesionales y comercios que lanzan recomendaciones contradictorias sin base técnica, incluida la de usar o quitarse gafas con filtro UV.'
    origen:
    - politico/h1/1
    - politico/h1/2
    - politico/h1/3
    - politico/h1/4
    - oftalmologa/h1/5
  - id: h1-06
    texto: 'Consultas oftalmológicas, farmacias y urgencias reciben una primera ola de personas alarmadas por síntomas que no son lesión: deslumbramiento presentado como daño por bulos de WhatsApp, TikTok y reenvíos del agitador (ceguera, encerrarse a oscuras, 5G), diferencias muy grandes de percepción entre personas que se leen como fallo propio, y la piel con protector solar o maquillaje con filtro, que a ojos ajenos se ve oscura a manchas.'
    origen:
    - medios/h1/3
    - adolescente/h1/3
    - agitador/h1/4
    - oftalmologa/h1/2
    - disruptor/h1/2
    - oftalmologa/h1/4
  - id: h1-07
    texto: Las cámaras y pantallas no muestran los colores nuevos, así que el primer formato viral es la frustración de que la cámara no ve lo que yo veo, junto con reacciones y descripciones exageradas. El hueco visual lo llenan filtros y montajes presentados como reales. Entre los jóvenes el relato lo construyen creadores, las plataformas apenas moderan porque no hay pauta oficial contra la que comparar, y aparecen anuncios oportunistas de gafas y gotas contra el ultravioleta.
    origen:
    - medios/h1/2
    - adolescente/h1/2
    - medios/h1/5
  - id: h1-08
    texto: 'La sociedad oftalmológica es la primera voz técnica: difunde un comunicado que ancla el fenómeno en el precedente de las personas sin cristalino o con lentes intraoculares que dejan pasar el UV, que ya lo percibían como un azul o violeta blanquecino. Da un marco descriptivo, pero no una guía práctica.'
    origen:
    - oftalmologa/h1/1
  - id: h1-09
    texto: El agitador abre en minutos un directo que agrega vídeos de sus seguidores antes de cualquier comparecencia oficial, pasa hacia la media hora a sugerir con preguntas, sin nombres, que el silencio oficial es deliberado, y anuncia un directo largo por la tarde. Algunos medios recogen sus clips y lo amplifican fuera de su burbuja.
    origen:
    - agitador/h1/1
    - agitador/h1/2
    - agitador/h1/5
  - id: h1-10
    texto: En los centros educativos las clases se paran porque alumnos y profesores lo viven a la vez; tras las quejas de deslumbramiento en patio y Educación Física se mete a todo el mundo dentro y algunos padres empiezan a recoger a sus hijos, de forma desigual.
    origen:
    - adolescente/h1/1
    - adolescente/h1/4
  tensiones_abiertas:
  - Si la sociedad oftalmológica publica pronto una guía práctica o si el espacio lo siguen ocupando bulos, comercios y políticos con recomendaciones contradictorias.
  - Si las plataformas endurecen la moderación cuando haya una pauta sanitaria oficial, y si eso empuja a creadores como el agitador hacia canales propios.
  - 'Cómo reacciona América al amanecer: si su experiencia directa desmiente el rumor geográfico o llega ya filtrada por el relato europeo y el del agitador.'
  - Si el mercado lee la demanda de gafas de sol como pico transitorio o como cambio duradero de la categoría.
  - Si algún gobierno atribuye el fenómeno a una acción hostil y obliga a otras cancillerías a responder.
  contradicciones_resueltas:
  - entre:
    - medios/h1/3
    - oftalmologa/h1/1
    decision: 'Ambas se mantienen: la sociedad oftalmológica comunica un marco descriptivo, pero ningún organismo sanitario publica todavía una guía práctica que desmienta los bulos.'
    motivo: Una sociedad científica no es la autoridad sanitaria; el comunicado describe lo que se ve, no dice qué hacer, así que el hueco práctico sigue abierto.
  - entre:
    - medios/h1/5
    - politico/h1/2
    decision: Hay comunicados de calma de Sanidad, pero las plataformas siguen sin un consenso oficial concreto contra el que moderar.
    motivo: Un mensaje genérico sin medidas ni orientación específica no sirve como referencia para las políticas de moderación, que se apoyan en orientaciones concretas de las autoridades sanitarias.
  - entre:
    - agitador/h1/3
    - medios/h1/5
    decision: Prevalece que las plataformas apenas moderan en la primera hora; no entra la migración masiva del agitador a sus canales propios por miedo a la moderación.
    motivo: 'El mecanismo de medios es más sólido: la propia norma citada por el agitador exige contradecir una orientación sanitaria oficial, que aún no existe, así que la moderación no puede activarse con rapidez.'
  descartadas:
  - id: economista/h1/5
    motivo: Confianza baja, especulación y sin dato.
  - id: politico/h1/5
    motivo: Confianza baja, especulación y sin dato; queda como tensión abierta.
  - id: medios/h1/4
    motivo: Detalle de cobertura que amplía hechos ya establecidos (vacío explicativo, falta de expertos) sin añadir una consecuencia nueva.
  - id: adolescente/h1/5
    motivo: Efecto local de convivencia, especulativo y sin dato; no cambia el rumbo del mundo en esta hora.
  - id: agitador/h1/3
    motivo: Choca con la ausencia de moderación efectiva en la primera hora (ver contradicciones resueltas); el pico de suscriptores y donaciones es un detalle sin dato.

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h2
  afirmaciones:
  - texto: 'Los futuros sobre índices estadounidenses, que cotizan casi de forma continua mientras el contado de Wall Street sigue cerrado, se mueven poco durante la segunda hora. Eso contradice en la práctica el rumor de que América está a salvo: el mercado no pone precio a una diferencia geográfica, sino a un suceso global sin daño físico, y el foco sigue en valores sueltos, no en índices.'
    mecanismo: 'El contado de Nueva York no abre hasta las 15:30 de Madrid, pero los futuros sobre el S&P 500 negocian casi las 24 horas en la plataforma electrónica de CME. Son el primer lugar donde el dinero estadounidense puede expresar una opinión. Si los operadores creyeran que América queda fuera del fenómeno, se vería una divergencia con Europa; si temieran un golpe a los beneficios, una caída general. Ninguna de las dos cosas tiene base: no hay fábricas ni puertos dañados y los propios operadores europeos, que sí lo ven con sus ojos, no venden índices enteros. El rumor geográfico vive en redes, no en los precios, y quien mire los precios en lugar de los titulares tiene ya una señal de que el relato de la ola hacia el oeste no se sostiene.'
    dato: Los futuros E-mini S&P 500 negocian en la plataforma electrónica de CME prácticamente 23 horas al día, cinco días a la semana.
    fuente: https://www.cmegroup.com/openmarkets/equity-index/2025/Why-Around-the-Clock-Liquidity-Matters.html
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados
    - medios
    id: economista/h2/1
  - texto: 'Las grandes plataformas de venta en línea activan sus políticas contra precios abusivos en gafas de sol: retiran ofertas y avisan a vendedores. El efecto secundario es que muchos vendedores legítimos retiran también su stock por miedo a sanciones, la escasez en línea empeora y la reventa se desplaza a aplicaciones de segunda mano, grupos de mensajería y redes sociales, donde no hay ese control.'
    mecanismo: 'Las plataformas ya tienen el procedimiento montado desde la pandemia y un incentivo reputacional claro para mostrarse duras ante los titulares de reventa. Pero sus avisos son genéricos y no dicen qué precio es aceptable, así que el vendedor que no ha subido precios también calcula que le sale más barato dejar de vender que arriesgar la cuenta. La demanda no desaparece: se va a canales sin moderación de precios, donde el revendedor cobra lo que quiere y el comprador no tiene garantía de que la lente filtre el ultravioleta, justo el atributo que ahora puede comprobar a simple vista.'
    dato: En marzo de 2020 Amazon retiró más de medio millón de ofertas y suspendió más de 3.900 cuentas de vendedores en EE. UU. por precios abusivos; vendedores y consultores contaron después que los avisos genéricos llevaron a retirar productos que no habían subido de precio, lo que agravó la escasez.
    fuente: https://www.aboutamazon.com/news/company-news/price-gouging-has-no-place-in-our-stores ; https://www.supplychainbrain.com/articles/31475-amazon-price-gouging-crackdown-worsened-shortage-of-sanitizer-wipes
    confianza: media
    evidencia: dato
    areas_afectadas:
    - consumo
    - comercio_en_linea
    - plataformas
    id: economista/h2/2
  - texto: 'El mercado empieza a separar dentro del sector de gafas: las marcas con filtro UV certificado y cadena de distribución propia se leen como ganadoras, mientras que el producto barato sin filtro, que ya ha quedado en evidencia ante el consumidor, pasa a verse como existencias difíciles de vender. La volatilidad de la primera hora da paso a una dispersión entre empresas, no a un movimiento del sector en bloque.'
    mecanismo: 'Por primera vez el comprador verifica sin instrumentos una promesa de etiqueta, así que el filtro UV deja de ser un sello invisible y pasa a ser la característica que se compra. Eso traslada poder de precio a quien puede demostrar el filtro y reponer rápido: los grupos integrados que controlan marcas, fabricación y tiendas propias. Los importadores de gama baja quedan con mercancía que el cliente rechaza a la vista y con riesgo de devoluciones y reclamaciones. Para un analista es más fácil defender en público esta lectura por calidad que apostar por un pico de toda la categoría, que podría deshacerse si el deslumbramiento remite.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados
    - consumo
    - industria_optica
    id: economista/h2/3
  - texto: 'Una parte de los consumidores deja de usar protector solar y cosméticos con filtro, o los retira de la cara a media mañana, porque bajo visión ultravioleta se ven manchas oscuras. Los fabricantes de cosmética solar y dermocosmética pasan a moverse en bolsa por un riesgo nuevo: no de demanda inmediata, sino de rechazo estético del producto.'
    mecanismo: 'El coste de llevar crema se ha vuelto visible y social: la cara oscura a manchas se comenta en el trabajo, en el instituto y en redes, y para mucha gente la imagen pesa más que un beneficio sanitario que no se ve. Al mismo tiempo, los bulos ya asocian esas manchas a enfermedad. El resultado es una caída de uso precisamente cuando hay más gente al sol mirando los colores nuevos. Para el mercado, el dilema de las marcas es caro: reformular para que el filtro no se note es lento, y defender el producto exige una pauta sanitaria que todavía no ha llegado.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - consumo
    - salud
    - mercados
    id: economista/h2/4
  - texto: 'En España las empresas de construcción, agricultura y reparto no reciben ninguna orden pública para parar, así que cada una decide por su cuenta: unas reorganizan turnos para evitar las horas centrales, otras siguen trabajando. La pérdida de horas es desigual y empieza a abrir una discusión sobre quién paga el tiempo parado, no sobre despidos.'
    mecanismo: 'España ya tiene un precedente normativo que obliga a adaptar o suspender el trabajo al aire libre cuando hay avisos meteorológicos por calor, de modo que muchas empresas y servicios de prevención tienen protocolos de cambio de horario. Pero esos protocolos se disparan con una alerta oficial, y aquí ningún organismo ha emitido aviso por deslumbramiento. Sin norma, la decisión recae en cada empresa y en su servicio de prevención, con incentivos distintos: la que teme un accidente para y asume el coste; la que tiene plazos y penalizaciones sigue. Eso lleva a sindicatos y patronales a hablar de quién asume las horas no trabajadas, una discusión mucho más probable en esta fase que cualquier dato de empleo.'
    dato: El Real Decreto-ley 4/2023 obliga a adaptar las condiciones del trabajo al aire libre, incluida la reducción o modificación de horas, cuando la AEMET o el órgano autonómico emiten aviso naranja o rojo por fenómenos meteorológicos adversos.
    fuente: https://elderecho.com/impacto-prohibicion-trabajar-al-aire-libre-con-condiciones-meteorologicas-extremas
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - empleo
    - empresas
    - relaciones_laborales
    id: economista/h2/5
  reacciona_a:
  - disruptor/h1/3
  - disruptor/h1/4
  - disruptor/h1/2
- agente: politico
  tramo: h2
  afirmaciones:
  - texto: Al terminar la reunión de seguimiento, Moncloa activa el Sistema de Seguridad Nacional y convoca el Comité de Situación, en lugar de recurrir al estado de alarma. Así puede decir que coordina sin restringir ningún derecho y gana tiempo para que Sanidad tenga algo respaldado por los técnicos.
    mecanismo: El Gobierno necesita parecer que tiene el control sin decretar nada que luego deba rectificar. La Ley de Seguridad Nacional prevé un órgano de apoyo para gestionar crisis que afectan a varios ministerios y administraciones, y este suceso toca a Sanidad, Interior (tráfico), Educación, Economía y Exteriores a la vez. Convocarlo no exige votación en el Congreso ni limita derechos, y da una imagen de gabinete de crisis que ocupa los titulares que la oposición estaba llenando con el silencio.
    dato: La Ley 36/2015 de Seguridad Nacional regula la gestión de crisis mediante un Comité de Situación de apoyo al Consejo de Seguridad Nacional.
    fuente: https://www.boe.es/buscar/pdf/2015/BOE-A-2015-10389-consolidado.pdf
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - gobernanza
    - comunicacion
    id: politico/h2/1
  - texto: 'Sanidad convoca de urgencia un Consejo Interterritorial telemático con las comunidades autónomas para cortar las recomendaciones contradictorias de la primera hora. Pacta un mensaje único que se queda en lo que nadie discute: no mirar al sol, el deslumbramiento por ahora no se asocia a lesión y solo hay que ir a urgencias ante síntomas concretos. Al menos una comunidad gobernada por la oposición rompe ese consenso y mantiene su propia recomendación.'
    mecanismo: 'La salud pública está repartida entre el Estado y las comunidades, y la primera hora dejó a presidentes autonómicos y alcaldes recomendando cosas incompatibles, lo que desgasta a todos. El Interterritorial es el foro ordinario para acordar actuaciones coordinadas y se puede reunir por videoconferencia en minutos. Como ningún gobierno puede afirmar lo que sus técnicos no respaldan, el mensaje común se queda en lo mínimo: no se dice que el deslumbramiento remite ni nada sobre si hay que llevar gafas con filtro. La comunidad de la oposición gana visibilidad si se desmarca y se presenta como más protectora.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - politica
    - comunicacion
    id: politico/h2/2
  - texto: 'La primera medida concreta y operativa no la dicta Sanidad sino la DGT: los paneles de mensaje variable y las redes oficiales recomiendan reducir velocidad, no detenerse en el arcén salvo emergencia y tener cuidado con el deslumbramiento lateral. Es una recomendación, no una restricción, y el Gobierno la presenta en su comparecencia como prueba de que actúa.'
    mecanismo: El tráfico es el único riesgo de la primera hora que se puede medir ya (alcances, paradas en arcén) y la DGT puede emitir recomendaciones de seguridad vial y activar sus paneles sin una base legal excepcional, igual que hace con niebla o temporales. Al Gobierno le conviene enseñar una medida tangible que no dependa de saber la causa ni de que los oftalmólogos se pronuncien sobre el ojo, y que no se pueda rectificar porque solo pide prudencia al volante.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - trafico
    - politica
    - economia
    id: politico/h2/3
  - texto: En Bruselas la Comisión convoca de urgencia el Comité de Seguridad Sanitaria con los Estados miembros para compartir información, sin declarar emergencia de salud pública a escala de la Unión. Varios gobiernos europeos usan esa convocatoria para justificar que esperan una posición común antes de recomendar nada sobre gafas o protección ocular.
    mecanismo: El reglamento europeo sobre amenazas transfronterizas graves para la salud da a la Comisión y al Comité de Seguridad Sanitaria un cauce para coordinar respuestas sin crear restricciones. Convocarlo es barato y rápido. Una declaración formal de emergencia, en cambio, obligaría a justificar un riesgo que ningún técnico ha caracterizado. Igual que pasó con la OMS en la primera hora, a los gobiernos les sirve tener una autoridad superior que está evaluando para no comprometerse solos con un mensaje que luego tendrían que corregir.
    dato: El Reglamento (UE) 2022/2371 sobre amenazas transfronterizas graves para la salud establece el Comité de Seguridad Sanitaria como órgano de coordinación entre la Comisión y los Estados miembros.
    fuente: https://boe.es/doue/2022/314/L00026-00063.pdf
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - sanidad
    - relaciones_internacionales
    id: politico/h2/4
  - texto: 'En la segunda hora la Casa Blanca y el Departamento de Salud estadounidense no salen a desmentir el rumor de que el fenómeno no afecta a América. Cuando sus técnicos lo confirman con fuentes de luz ultravioleta artificial, sacan un comunicado mínimo antes del amanecer: el fenómeno es global y habrá información al despertar. Algunos gobernadores y cargos estatales se adelantan con mensajes propios en redes, unos para pedir calma y otros dando por bueno el rumor.'
    mecanismo: A esas horas en la costa este de Estados Unidos es de madrugada, y sin sol no hay nada que comprobar a simple vista. Ningún portavoz federal puede negar el rumor sin respaldo técnico, pero tampoco puede dejar que el amanecer lo desmienta por él, porque eso lo pagaría en legitimidad. La salida es apoyarse en una comprobación técnica rápida con lámparas UV y prometer información. Los cargos estatales compiten por visibilidad, igual que los autonómicos españoles en la primera hora, y no tienen la misma restricción técnica.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - politica
    - comunicacion
    - relaciones_internacionales
    id: politico/h2/5
  reacciona_a:
  - disruptor/h1/3
  - oftalmologa/h1/5
- agente: medios
  tramo: h2
  afirmaciones:
  - texto: 'El rumor de que el cambio no afecta a América empieza a caer en la segunda hora desde el sur, no desde Estados Unidos: en Brasil y en el Cono Sur ya es de día y medios, presentadores matinales y usuarios brasileños y argentinos publican los primeros testimonios americanos en primera persona. Las redacciones de Estados Unidos, aún en turno de noche, pasan a citar a Brasil como prueba de que el fenómeno ha llegado al continente, y el relato de la ola que avanza hacia el oeste se reformula en lugar de desaparecer: ahora se dice que llega con el amanecer y se sigue franja a franja.'
    mecanismo: 'A las 11:00 de Madrid (10:00 UTC) son las 7:00 en São Paulo, y allí amanece hacia las 5:15 en noviembre, así que hay luz solar con UV-A desde hace casi dos horas. Los programas matinales de televisión brasileños están en emisión y tienen equipos en la calle. Una explicación geográfica falsa no muere con un desmentido sino que se adapta: la coincidencia entre amanecer y percepción encaja con la idea de la ola, y los mapas de franja solar se convierten en el formato que la confirma a ojos del público, aunque lo único que avanza es la luz.'
    dato: En São Paulo amanece a las 05:14 el 15 de noviembre de 2026; São Paulo está en UTC-3, por lo que las 10:00 UTC son las 07:00 locales.
    fuente: https://www.weather2travel.com/brazil/sao-paulo/november/?Units=1
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - medios
    - sociedad
    - politica
    id: medios/h2/1
  - texto: 'El hueco visual que dejaron las cámaras lo empieza a llenar en la segunda hora contenido real de archivo sacado de contexto: vídeos antiguos grabados con cámaras ultravioleta, como el de caras con protector solar que se ven oscuras o las fotografías de flores con patrones UV, se recirculan como así nos vemos ahora. Los medios serios los usan como ilustración con rótulo de archivo, pero en redes el rótulo se pierde y se comparten como capturas del martes.'
    mecanismo: Existe un archivo amplio y ya viral de fotografía UV, porque se usó durante años en campañas de protección solar y divulgación sobre la visión de insectos. Es material auténtico, con autor y fecha, lo que permite a un medio publicarlo cumpliendo la regla de la fuente. Pero una cámara UV traduce el ultravioleta a grises o falsos colores, no a lo que ahora percibe el ojo, y al recortarse y reenviarse pierde la explicación. Como coincide con lo que la gente nota en la piel con crema, parece una confirmación y circula más que cualquier montaje inventado.
    dato: En 2014 el vídeo de Thomas Leveritt How the sun sees you, grabado con cámara ultravioleta y que muestra el protector solar como manchas oscuras en la cara, se hizo viral y lo recogieron medios generalistas.
    fuente: https://petapixel.com/2014/08/14/this-incredible-short-film-shows-what-your-aging-skin-looks-like-to-a-uv-camera
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - salud
    - sociedad
    id: medios/h2/2
  - texto: 'Los medios generalistas convierten el comunicado de la sociedad oftalmológica en su fuente única y lo estiran: en la segunda hora titulan como si fuera una guía práctica (los oftalmólogos explican qué ves y qué hacer) y lo mezclan en el mismo directo con consejos de farmacéuticos, ópticos y políticos locales. El resultado es que la recomendación de la sociedad, que solo describe, se cita como aval de recomendaciones que no ha dado, incluidas las contradictorias sobre ponerse o quitarse gafas con filtro UV.'
    mecanismo: Es la única fuente técnica con nombre institucional disponible y la redacción necesita cumplir la regla de la fuente para pasar de contar lo que ve a decir qué hacer, que es lo que más audiencia retiene. Sin rueda de prensa del Gobierno ni posición de la OMS, el periodista atribuye a la fuente más fiable lo que oye de fuentes menos fiables en el mismo directo, y el titular de servicio se escribe antes de que exista el contenido que promete. Eso obliga a la sociedad a precisar públicamente qué no ha dicho.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - salud
    - politica
    id: medios/h2/3
  - texto: Las unidades de verificación publican en la segunda hora sus primeros desmentidos, pero solo pueden atacar con eficacia los bulos sanitarios de ceguera y 5G apoyándose en el comunicado oftalmológico; los montajes de colores nuevos no los pueden desmentir con prueba visual, porque nadie puede enseñar cómo se ve de verdad. Su desmentido tipo es una pieza que dice que ninguna cámara puede captarlo, lo que deja sin refutar el contenido concreto y llega a mucha menos gente que el bulo.
    mecanismo: La verificación funciona contrastando una afirmación con una referencia comprobable. Para el daño ocular ya hay una voz técnica que citar; para la apariencia de los colores nuevos no existe referencia, solo testimonios que no coinciden entre personas. Además lo falso y novedoso se difunde más rápido y más lejos que lo verdadero, y el desmentido parte en desventaja aunque sea correcto.
    dato: Un análisis de unas 126.000 cascadas de noticias en Twitter entre 2006 y 2017 halló que la información falsa se difundía más lejos, más rápido y más ampliamente que la verdadera, sobre todo por su novedad.
    fuente: https://www.media.mit.edu/publications/the-spread-of-true-and-false-news-online/
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - salud
    - sociedad
    id: medios/h2/4
  - texto: Las grandes plataformas no retiran todavía los bulos de ceguera en la segunda hora, pero sí empiezan a colocar paneles informativos genéricos en las búsquedas y etiquetas que remiten a organismos sanitarios que no han dicho nada sustantivo. Ese gesto se convierte en munición para el agitador, que lo presenta en su canal propio como la prueba de que ya empieza la censura, antes de que se haya retirado nada.
    mecanismo: Las plataformas necesitan mostrar a anunciantes y reguladores que actúan, y el panel informativo es la herramienta que pueden activar sin una pauta oficial contra la que juzgar el contenido. Pero el panel apunta a fuentes que solo dicen que están recabando información, así que no informa y sí señala. Para quien vive de la historia de culpables, una etiqueta visible es más útil que una retirada real, porque la puede enseñar sin que su contenido desaparezca.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - medios
    - tecnologia
    - politica
    id: medios/h2/5
  reacciona_a:
  - disruptor/h1/3
  - oftalmologa/h1/5
  - agitador/h1/3
- agente: oftalmologa
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora la sociedad oftalmológica publica una guía práctica breve, pensada para urgencias, farmacias y público: el deslumbramiento y la fatiga visual no son lesión; se va a urgencias solo con signos de alarma clásicos (dolor ocular intenso, ojo rojo, pérdida brusca de visión, visión de una mancha fija); las gafas con filtro UV400 alivian y quitárselas no hace perder la capacidad nueva; ningún colirio filtra el ultravioleta; y no hay que mirar al sol. La guía desmonta de paso los anuncios de gotas y el consejo de encerrarse a oscuras.'
    mecanismo: 'La sociedad ya tiene la posición de referencia por su comunicado de la primera hora, pero la pierde si el hueco lo siguen llenando políticos, comercios y bulos. Para no afirmar nada sin base, se limita a lo que la clínica y la física ya sostienen: los criterios de triaje de urgencias oftalmológicas existen antes del martes, un filtro UV400 absorbe el UV-A por diseño y una gota en la superficie del ojo no puede actuar como filtro óptico estable. No dice cuánto dura el fenómeno ni su causa, porque eso no lo sabe nadie. Una guía de triaje es además lo que piden los servicios de urgencias desbordados por la primera ola de consultas sin lesión.'
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - comunicacion
    - consumo
    - medios
    id: oftalmologa/h2/1
  - texto: 'La disparidad de percepción entre personas empieza a tener un patrón visible: niños y jóvenes describen los colores nuevos más intensos y saturados, y muchos mayores apenas notan un velo azulado. En familias y aulas, los adultos dudan de lo que cuentan los niños y algunos mayores consultan creyendo que su vista falla.'
    mecanismo: 'El cristalino cambia con la edad: en el niño es más transparente en la zona corta del espectro y la pupila es mayor, y con los años amarillea y absorbe cada vez más luz de onda corta. Aunque todos tengan la capacidad nueva, el estímulo UV-A que llega a la retina queda más atenuado en un ojo de 70 años que en uno de 8. La sociedad usa ese dato para explicar parte de la disparidad de la primera hora y quitarle el aire de fallo individual.'
    dato: El pico de absorción del cristalino se sitúa cerca de 365 nm a los 8 años y cerca de 450 nm a los 65; los niños conservan una ventana de transmisión cerca de 320 nm hasta los 10 años aproximadamente, y la exposición infantil es mayor por cristalino más claro y pupila más amplia.
    fuente: https://www.dovepress.com/ultraviolet-damage-to-the-eye-revisited-eye-sun-protection-factor-e-sp-peer-reviewed-fulltext-article-OPTH
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - educacion
    - familias
    - redes_sociales
    id: oftalmologa/h2/2
  - texto: 'Los operados de cataratas con lente intraocular que bloquea el UV ven los colores nuevos muy débiles o no los ven en el ojo operado, y quienes solo tienen un ojo operado notan una diferencia clara entre ambos. El precedente clínico se invierte: los afáquicos fueron los pioneros, y ahora una parte de los mayores se siente excluida y llama a consultas preguntando si se puede cambiar la lente. La sociedad desaconseja cualquier cirugía para ganar visión UV.'
    mecanismo: Igual que el parabrisas o una lente UV400 bloquean el UV-A por fuera del ojo, una lente intraocular con cromóforo absorbente lo bloquea por dentro, antes de la retina. Las lentes intraoculares se fabrican para bloquear el UV desde principios de los años ochenta, así que la mayoría de operados de cataratas llevan una. Recambiar una lente intraocular es una cirugía con riesgos reales y sin indicación médica, y además nadie sabe si el fenómeno es permanente, de modo que la sociedad no puede respaldarla sin perder credibilidad; las clínicas privadas que vean negocio en ello son el riesgo siguiente.
    dato: Desde principios de los años ochenta las lentes intraoculares se fabrican para bloquear la luz UV; las personas afáquicas sin lente intraocular perciben UV-A, descrito como azul o violeta blanquecino.
    fuente: https://www.healio.com/news/optometry/20230518/blog-the-link-between-uv-light-iols-and-claude-monets-water-lilies
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - mayores
    - clinicas_privadas
    - consumo
    id: oftalmologa/h2/3
  - texto: Mucha gente que ya tiene gafas de sol con filtro UV sigue viendo colores nuevos y sigue deslumbrándose por los lados y por reflejo en la cara interna de la lente, y lo interpreta como que sus gafas no funcionan. Eso alimenta quejas injustas contra gafas que sí filtran y empuja la demanda hacia monturas envolventes y gorras con visera.
    mecanismo: 'La luz UV no entra solo de frente: llega por los laterales, por arriba y rebotada desde detrás en la cara interior de la lente, sobre todo si lleva antirreflejante. Con visión UV, esa fuga periférica se ve directamente como color y brillo en el borde del campo visual. La guía práctica recomienda monturas envolventes y visera porque reducen esa entrada lateral, pero el consumidor que comprobó su lente en la primera hora ahora duda de la prueba.'
    dato: En un estudio con maniquí, el 6,6 por ciento del UV incidente llegó al dosímetro del ojo detrás de gafas graduadas incluso con las lentes tapadas con cinta opaca; separar las gafas 6 mm de la frente multiplicó la exposición ocular entre 5 y 10 veces; la luz que llega desde unos 135 a 150 grados por detrás se refleja en la cara posterior de la lente.
    fuente: https://www.dovepress.com/ultraviolet-damage-to-the-eye-revisited-eye-sun-protection-factor-e-sp-peer-reviewed-fulltext-article-OPTH
    confianza: media
    evidencia: dato
    areas_afectadas:
    - consumo
    - optica
    - sanidad
    - redes_sociales
    id: oftalmologa/h2/4
  - texto: Aparecen los primeros casos de personas que han mirado al sol o a lámparas UV para ver mejor los colores nuevos y llegan a urgencias con visión borrosa o una mancha central. Son pocos frente a la ola de deslumbramiento, pero son los únicos con riesgo de lesión real, y la sociedad los usa para separar en su comunicación molestia transitoria de daño evitable.
    mecanismo: 'La curiosidad por ver más empuja a mirar a la fuente: retos en redes, niños en el patio y adultos que prueban con lámparas de uñas o trampas de insectos. Mirar al sol de forma directa produce retinopatía solar con independencia del fenómeno, como se ve tras cada eclipse. Para la sociedad es útil: le permite dar una advertencia concreta y con base, y desmontar el relato del agitador sin negar que existan riesgos.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - redes_sociales
    - educacion
    id: oftalmologa/h2/5
  reacciona_a:
  - medios/h1/3
  - medios/h1/5
  - agitador/h1/4
  - disruptor/h1/4
  - adolescente/h1/5
- agente: adolescente
  tramo: h2
  afirmaciones:
  - texto: 'Entre las once y las doce el instituto manda un mensaje a las familias diciendo que las clases siguen dentro y que no hace falta recoger a nadie, pero llega tarde: la mitad de mi clase ya se ha ido. Muchos de los que se van no se quedan en casa, sino que quedan con amigos en la calle o en una terraza para mirar, justo al sol.'
    mecanismo: El instituto no puede decir nada hasta que alguien de arriba le diga qué hacer, y Sanidad no ha dicho nada concreto. Mientras, mis padres se asustan con lo que leen en el grupo de familias y vienen a por mí. Pero en casa, con la luz del LED, no se ve casi nada nuevo, y mis padres vuelven al trabajo o se ponen a ver la tele. Lo interesante está fuera, y si tus amigos están quedando y tú no vas, te lo pierdes. Así que sacarnos del instituto por seguridad acaba poniéndonos más al sol que si nos hubieran dejado en clase.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - familias
    - salud
    id: adolescente/h2/1
  - texto: 'Empieza entre los de mi edad la moda de escribir o dibujar con crema solar en la piel o en una cartulina mensajes que solo se ven con los ojos nuevos: nombres, corazones, insultos. Se hace junto a la ventana o en la calle y se cuenta en redes como algo que tienes que ver en persona.'
    mecanismo: Ya sabemos que la crema solar se ve oscura con los colores nuevos, así que cualquiera puede probarlo con lo que tiene en la mochila o en el baño. Como la cámara no lo coge, el mensaje es secreto para el móvil pero visible para quien está delante, y eso lo hace perfecto para declaraciones, bromas y también para meterse con alguien sin que quede grabado ni lo puedan denunciar con captura.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - educacion
    - convivencia
    id: adolescente/h2/2
  - texto: Muchas chicas se quitan el maquillaje y la crema hidratante en el baño del instituto o al llegar a casa porque los demás les dicen que tienen la cara manchada, y algunas se niegan a salir a la calle o a hacerse fotos con el grupo hasta saber cómo se ven.
    mecanismo: La base de maquillaje y muchas cremas llevan filtro, y a ojos de los demás se ven oscuras a parches. A mi edad lo peor que te puede pasar es que comenten tu cara, y basta con que una persona popular diga que alguien parece sucia para que todas corran al espejo. Como no hay nadie que explique que es solo la crema, la reacción más rápida es quitársela, aunque luego salgamos al sol sin protección.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - autoestima
    - consumo
    - redes_sociales
    id: adolescente/h2/3
  - texto: 'Las gafas de sol pasan a ser cosa de estatus en mi grupo: quien tiene unas buenas que bloquean el ultravioleta las presta o presume, y quien lleva unas baratas que dejan pasar los colores queda en evidencia delante de todos. Algunos dicen que prefieren las baratas para no perderse los colores, y se crea un bando de los que se protegen y otro de los que no.'
    mecanismo: Ahora cualquiera puede comprobar mirando si unas gafas filtran o no, así que la marca deja de ser solo un logo y se nota en el momento. Como en las tiendas ya no quedan, tener unas buenas es tener algo que los demás quieren. Y como nadie oficial ha dicho si hay que llevarlas o quitárselas, cada uno elige lo que le hace quedar mejor, y quitárselas para ver más parece de valientes.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - salud
    - redes_sociales
    id: adolescente/h2/4
  - texto: Alguien conocido de mi instituto sube un vídeo con un filtro de colores diciendo que así se ve de verdad, consigue muchísimas visitas en poco rato y luego en los comentarios la gente de clase le acusa de mentir porque lo que ellos ven no se parece. Aun así el vídeo sigue circulando fuera del instituto como si fuera real, y la cita del directo de la tarde del agitador se comparte en los grupos como plan para ver juntos.
    mecanismo: Subir lo primero algo que parezca mostrar los colores da muchas visitas, y eso a mi edad es estatus. Los que lo conocen pueden comparar con lo que ven delante y pillar el montaje, pero quien lo ve lejos no tiene con qué comparar y se lo cree. El directo largo del agitador se convierte en un plan porque nadie oficial ha quedado a ninguna hora para explicar nada, y verlo juntos es otra forma de estar en el grupo, aunque muchos digamos que es para reírnos de él.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - desinformacion
    - medios
    id: adolescente/h2/5
  reacciona_a:
  - disruptor/h1/2
  - disruptor/h1/4
  - medios/h1/2
  - agitador/h1/5
- agente: agitador
  tramo: h2
  afirmaciones:
  - texto: 'En la hora 2 el agitador convierte las manchas oscuras del protector solar en su tema estrella: presenta en directo, en forma de preguntas, que si la crema se ve así es porque llevamos años poniéndonos algo que no conocíamos, y mezcla los testimonios de piel manchada con el viejo discurso contra los filtros solares que ya circulaba en redes. Parte de su audiencia joven anuncia que deja de usar protector, justo en las zonas y horas de más sol.'
    mecanismo: 'Es el único elemento del fenómeno que todo el mundo puede comprobar en la cara de otro sin cámara, y que encaja con una desconfianza previa hacia los filtros solares que ya existía entre los jóvenes. El agitador no necesita inventar nada visual: el hecho físico (el filtro absorbe UV-A y se ve oscuro) es real y él solo cambia la interpretación. Además, culpar a un producto cotidiano de grandes marcas le da un villano concreto sin nombrar a personas, lo que reduce su riesgo de sanción. Como la sociedad oftalmológica solo ha dado un marco descriptivo y no hay guía dermatológica, nadie le corrige en la hora.'
    dato: 'Encuesta de la Academia Americana de Dermatología de 2024: el 28 % de los adultos de la generación Z dice que broncearse le importa más que prevenir el cáncer de piel y el 37 % solo usa protector cuando alguien insiste.'
    fuente: https://www.aad.org/news/gen-z-adults-at-risk-skin-cancer
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - redes
    - consumo
    - jovenes
    id: agitador/h2/1
  - texto: 'El agitador se monta sobre el destape de las gafas sin filtro y da la vuelta a la recomendación técnica: sugiere que las gafas con filtro UV son lo que interesa que lleve la gente para que no vea lo que hay que ver, y anima a su audiencia a quitárselas en exteriores. Esto choca de frente con oftalmólogos y ópticas y prolonga el deslumbramiento en sus seguidores, que siguen llegando a urgencias.'
    mecanismo: 'En la hora 1 se ha visto a simple vista que muchas etiquetas mentían (gafas baratas sin filtro), lo que hace creíble a ojos de su audiencia la idea de que la industria óptica no es de fiar. Las gafas con filtro reducen a la vez el deslumbramiento y la percepción de los colores nuevos, así que el agitador puede presentar la protección como una forma de quitarte algo. Ese marco le favorece: mantiene la experiencia del fenómeno intensa y emocional, que es lo que le da audiencia, y le enfrenta a un enemigo con intereses comerciales visibles (las cotizaciones de óptica que se disparan).'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - consumo
    - redes
    - mercados
    id: agitador/h2/2
  - texto: 'Con América aún de noche (en Ciudad de México y Nueva York es de madrugada en la hora 2), el agitador cambia su emisión para captar a la audiencia hispanohablante de América que se despierta: no afirma que el fenómeno no llegue al continente, sino que plantea una apuesta sin riesgo para él. Si al amanecer lo ven, era algo planificado y escalonado; si lo ven distinto, es que a ellos les han hecho otra cosa. Sus canales propios suman suscriptores americanos antes de que allí haya ninguna cobertura local propia.'
    mecanismo: El rumor geográfico ya está en el canon y solo el amanecer lo desmiente. Un agitador que vive de la credibilidad ante su audiencia no se ata a una predicción que puede caer en horas; formula el marco para que cualquier resultado lo confirme. Las redacciones americanas están en turno de noche con plantilla mínima, de modo que quien emite en directo en su idioma llega antes que cualquier medio local, y el público que despierta recibe el relato ya interpretado.
    dato: Las afirmaciones falsas tienen un 70 % más de probabilidad de ser compartidas que las verdaderas (estudio de Vosoughi, Roy y Aral en Science, 2018, sobre Twitter).
    fuente: https://mitsloan.mit.edu/press/false-news-spreads-widely-and-easily
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes
    - medios
    - america
    - politica
    id: agitador/h2/3
  - texto: 'Cuando algunos ministerios de Sanidad empiezan a publicar mensajes de que el deslumbramiento es transitorio, la plataforma grande etiqueta o limita uno de los clips del agitador sobre daño ocular. El agitador no lo esconde: lo exhibe en sus canales propios como prueba de que le censuran por contar lo que pasa, y pide a su audiencia que le siga allí y que done para el directo de la tarde.'
    mecanismo: 'Las plataformas moderan contra la pauta sanitaria oficial; en cuanto aparece un primer mensaje de Sanidad, aunque sea solo de calma, tienen algo contra lo que comparar y actúan sobre el contenido más claramente dañino, que es el que confunde molestia con lesión. Para el agitador la sanción es un activo: confirma ante su audiencia la tesis del silencio deliberado y empuja la migración a canales sin moderación, donde controla la relación y el cobro. Por eso modera su versión en la plataforma grande pero no la retira del todo: necesita la visibilidad para captar y el castigo para fidelizar.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes
    - salud
    - medios
    id: agitador/h2/4
  - texto: 'Para el directo de la tarde el agitador busca autoridad prestada: anuncia como invitados a un médico o científico de fuera del consenso y a varios seguidores que dicen haber perdido vista, y pide a su audiencia que lleve a urgencias el móvil grabando para documentar cómo les atienden. Algunos centros de salud y urgencias oftalmológicas registran pacientes que graban la consulta y exigen pruebas, lo que alarga las esperas.'
    mecanismo: 'Sin imágenes del fenómeno (las cámaras no lo captan), la credibilidad depende del testimonio y del título: un invitado con bata compensa la falta de pruebas y le permite decir más sin decirlo él. Convertir a los seguidores en reporteros dentro de los centros sanitarios le da contenido gratis y continuo, y cualquier respuesta seca o espera larga de un sanitario saturado se lee como prueba de que el sistema oculta algo. Cada vídeo de ese tipo alimenta el directo de la tarde y mantiene la incertidumbre que le da audiencia frente a cualquier explicación que la normalice.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - salud
    - redes
    - medios
    id: agitador/h2/5
  reacciona_a:
  - oftalmologa/h1/5
  - disruptor/h1/2
  - disruptor/h1/4
  - medios/h1/5
  - disruptor/h1/3
- agente: disruptor
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora aparecen las primeras fotos que de verdad captan el ultravioleta, hechas por aficionados a la fotografía UV, laboratorios forenses y astrofotógrafos con cámaras modificadas de espectro completo. En vez de cerrar el debate lo empeoran: como se muestran en falso color, no coinciden con lo que la gente ve, y una parte del público las toma por montajes iguales a los filtros falsos de la primera hora.'
    mecanismo: Los sensores de silicio captan algo de UV-A, pero las cámaras de serie llevan un filtro que lo bloquea. Las cámaras modificadas, con un filtro que solo deja pasar el UV, sí lo registran. El problema es que una pantalla solo puede mostrar colores visibles, así que la imagen UV se traduce a una paleta elegida por quien la procesa. Cada fotógrafo la representa con colores distintos y ninguno coincide con la sensación nueva del espectador. Después de una hora de montajes, el público ya desconfía de cualquier imagen de colores raros y no distingue una foto UV auténtica de un filtro.
    dato: En fotografía ultravioleta no hay un balance de blancos correcto para representar el UV como imagen visible, y las imágenes UV se muestran en falso color.
    fuente: https://savazzi.net/photography/uv-white-balance.html
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - tecnologia
    - desinformacion
    id: disruptor/h2/1
  - texto: 'En comercios con luz natural de la zona euro, cajeros y clientes notan que los billetes se ven distintos en el canal nuevo: las fibras y tintas de seguridad forman dibujos que antes no se veían, y los billetes impresos en papel corriente no se parecen a los auténticos. Hay rechazos de billetes buenos que parecen raros, algún billete falso detectado sin máquina y llamadas a los bancos centrales para preguntar si el dinero sigue siendo válido.'
    mecanismo: 'Los billetes en euros llevan fibras y tintas que reaccionan al ultravioleta, y su papel no brilla bajo UV, a diferencia del papel de oficina con blanqueantes ópticos que suelen usar los falsificadores caseros. Hasta ahora esa diferencia solo la veía quien tenía una lámpara UV. Con luz solar en el escaparate o junto a la puerta, cualquiera percibe dibujos y tonos que no esperaba. Sin una guía, se mezclan dos reacciones contrarias: desconfiar del billete auténtico porque se ve extraño y descubrir de golpe el falso que antes pasaba.'
    dato: Según la guía del BCE, bajo luz ultravioleta el papel de los billetes en euros no brilla.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/Quick_Guide_EN_Specimen.pdf
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - economia
    - comercio
    - seguridad
    id: disruptor/h2/2
  - texto: Mientras las autoridades sanitarias siguen sin pauta, mucha gente, sobre todo adolescentes y jóvenes, se lava la cara o deja de ponerse protector solar y maquillaje con filtro porque la hace verse oscurecida a manchas. Los dermatólogos empiezan a advertir en medios y redes que quitarse el protector para verse bien es un riesgo para la piel, y ese mensaje compite con la voz de los oftalmólogos.
    mecanismo: La vergüenza social actúa antes que el riesgo sanitario, que es invisible y aplazado. Si el protector deja manchas oscuras a ojos de los demás, quitárselo resuelve al instante un problema de imagen, mientras que el daño solar se paga años después. Entre adolescentes, que ya comparan su físico en el canal nuevo, el incentivo es todavía más fuerte. Los dermatólogos ven en esto un riesgo concreto y, como nadie ha dicho nada oficial, salen por su cuenta, lo que añade otra recomendación sanitaria en un espacio ya saturado.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - sociedad
    - cosmetica
    - educacion
    id: disruptor/h2/3
  - texto: 'Arranca una segunda ola de compra que nadie esperaba: no de gafas para bloquear el ultravioleta, sino de linternas UV, lámparas de luz negra y lámparas de uñas para verlo en interiores. Se agotan en tiendas en línea y en bazares, y aparecen los primeros avisos de gente que se ilumina los ojos o la cara de otros con ellas para probar.'
    mecanismo: Lo nuevo solo se ve fuera o junto a ventanas, y en casas y oficinas con LED desaparece. Quien quiere seguir viéndolo, enseñárselo a otros o comprobar qué brilla en su casa necesita una fuente de UV-A propia. Esos aparatos son baratos y estaban ya en el mercado para uñas, detección de billetes o fiestas. En América, todavía de noche, son la única forma de comprobar el fenómeno antes del amanecer. Mirar de cerca una fuente UV concentrada es justo el uso que sus fabricantes desaconsejan, y la curiosidad empuja a hacerlo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - comercio
    - salud
    - consumo
    id: disruptor/h2/4
  - texto: 'La experiencia se divide por el tipo de cristal del edificio: en oficinas modernas con vidrio laminado o de baja emisividad junto a la ventana no se ve casi nada nuevo, y en casas, colegios y comercios con cristal sencillo antiguo sí. Esto genera en la segunda hora una lectura falsa de que el fenómeno se está apagando o afecta a unos sí y a otros no, y empuja a trabajadores de oficina a salir a la calle en plena hora de más deslumbramiento.'
    mecanismo: Los vidrios laminados y muchos recubrimientos de control solar filtran mucho más UV-A que el cristal sencillo, igual que ocurre en el coche entre parabrisas y ventanillas. Quien trabaja en un edificio moderno se asoma a la ventana, no ve lo que cuentan en redes, y lo interpreta como fallo propio o como que el efecto ya pasa. Para comprobarlo sale fuera, justo cuando el sol se acerca al mediodía, y suma consultas por deslumbramiento. La misma diferencia alimenta el relato de que el fenómeno es desigual o selectivo.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: inferencia
    areas_afectadas:
    - trabajo
    - salud
    - desinformacion
    id: disruptor/h2/5
  reacciona_a:
  - medios/h1/2
  - oftalmologa/h1/3
  - adolescente/h1/5

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

estado_del_mundo:
  tramo: h2
  resumen: "..."
  hechos_establecidos:
    - id: h2-01
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
