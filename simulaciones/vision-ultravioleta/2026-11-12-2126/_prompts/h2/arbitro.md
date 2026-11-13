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
  resumen: 'En la primera hora el mundo descubre que ve colores nuevos sobre todo al aire libre y bajo ciertas luces, y que no puede enseñarlos: cámaras y pantallas no los reproducen. Ese vacío de pruebas y de causa lo llenan las redes, con reacciones virales, negacionismo y bulos sobre la causa que algunos agitadores blindan de antemano contra la explicación oficial. Los gobiernos se mueven por cauces ordinarios (España no declara el estado de alarma y la OMS solo pide información), los mercados europeos siguen abiertos con volatilidad concentrada en valores de óptica, y la demanda de gafas de sol choca con el hecho de que bloquean justo lo que la gente quiere ver. La primera fricción social inesperada es la piel: manchas solares y protector solar se vuelven visibles y mucha gente cree que los demás han enfermado, mientras institutos y familias improvisan sin instrucciones.'
  hechos_establecidos:
  - id: h1-01
    texto: 'Las bolsas europeas no se detienen en bloque: siguen cotizando con volumen alto y horquillas más anchas, con interrupciones de volatilidad solo en valores sueltos ligados al relato del suceso (óptica, gafas de sol, oftalmología), porque los frenos de Euronext actúan valor a valor. En EE. UU., donde es de madrugada, la reacción se canaliza por los futuros y la algorítmica, y el grueso queda aplazado a la apertura de Wall Street; las plazas asiáticas de contado ya habían cerrado y reaccionarán en su siguiente sesión.'
    origen:
    - economista/h1/1
    - economista/h1/5
  - id: h1-02
    texto: Estalla la demanda de gafas de sol donde coinciden luz diurna, sol intenso y comercio abierto (África, Oriente Medio, sur de Asia), con efecto menor en la Europa de noviembre y casi nulo en América, donde es de noche. EssilorLuxottica y otros valores de gafas de sol suben con fuerza por compras de narrativa, y el economista sostiene en público que la subida está sobredimensionada porque el deslumbramiento es transitorio. Aparecen subidas de precio oportunistas, productos de filtro UV sin certificación, gafas que dicen potenciar o bloquear la visión UV sin base, remedios falsos y estafas que suplantan a autoridades sanitarias; las plataformas intentan moderar, pero el ritmo de publicación las desborda.
    origen:
    - economista/h1/2
    - economista/h1/3
    - economista/h1/4
    - medios/h1/4
    - oftalmologa/h1/3
  - id: h1-03
    texto: 'El Gobierno de España no declara el estado de alarma: convoca un comité de crisis en Moncloa y emite una declaración de contención que reconoce el fenómeno y pide calma sin afirmar que sea inocuo ni permanente. Las primeras medidas reales llegan por cauces ordinarios (tráfico, protección civil, sanidad) con avisos de precaución al volante y en exteriores soleados, emitidos por administraciones distintas sin coordinación. La oposición exige la comparecencia urgente del presidente en el Congreso y acusa al Gobierno de silencio o improvisación; la UE activa el intercambio de información entre Estados miembros sin medidas comunes.'
    origen:
    - politico/h1/1
    - politico/h1/2
    - politico/h1/5
  - id: h1-04
    texto: La OMS se limita a un comunicado de seguimiento y a pedir información a los Estados; no convoca todavía el Comité de Emergencias, porque un cambio simultáneo y global sin agente identificado ni daño acreditado no encaja con claridad en el procedimiento del Reglamento Sanitario Internacional.
    origen:
    - politico/h1/3
  - id: h1-05
    texto: La conversación pública de la primera hora la ocupan las redes sociales, no los medios. Las fotos y vídeos no muestran los colores nuevos porque sensores y pantallas trabajan solo en el espectro visible, así que lo que se vuelve viral son las reacciones, los testimonios y los intentos de describir colores sin nombre. La falta de una prueba compartible alimenta una corriente minoritaria pero ruidosa que lo tacha de alucinación colectiva o montaje, y en el extremo opuesto quien atribuye al cambio poderes añadidos.
    origen:
    - medios/h1/1
    - adolescente/h1/2
    - disruptor/h1/4
    - medios/h1/5
  - id: h1-06
    texto: Antes de que acabe la hora circulan atribuciones falsas de causa con apariencia de autoridad (experimento secreto, ataque químico o radiológico, 5G, satélites, señal extraterrestre, castigo divino), con capturas falsificadas de comunicados oficiales. Agitadores en directo encuadran el suceso como algo que alguien oculta, presentan como 'marcas ocultas' los elementos fluorescentes que siempre estuvieron ahí (marcas de seguridad de billetes y documentos, abrillantadores ópticos, residuos), vinculan el deslumbramiento con la idea de que 'algo nos han hecho' y piden de antemano no fiarse de médicos ni autoridades. Algunos dirigentes de otros países rompen la prudencia y atribuyen el fenómeno a un ataque extranjero, a una señal religiosa o a una ventaja nacional, o lo declaran seguro sin respaldo técnico.
    origen:
    - medios/h1/2
    - agitador/h1/1
    - agitador/h1/2
    - agitador/h1/4
    - politico/h1/4
  - id: h1-07
    texto: Los medios generalistas abren especiales centrados en la pregunta de si es peligroso, con portavoces médicos improvisados y titulares sobre deslumbramiento y fatiga visual, lo único medible. Las sociedades de oftalmología reciben un aluvión de consultas y se posicionan como primera fuente explicativa con el precedente clínico de las personas sin cristalino, que ya percibían algo de UV-A como un tono azul blanquecino o violáceo. Advierten de que mirar al sol o a lámparas UV para buscar los colores nuevos sigue causando las lesiones de siempre. Los operados de cataratas con lentes intraoculares que filtran el UV y los usuarios de gafas o lentillas con filtro perciben los colores nuevos con menos intensidad, a veces de forma distinta entre sus dos ojos, y consultan creyendo que tienen un problema.
    origen:
    - medios/h1/3
    - oftalmologa/h1/1
    - oftalmologa/h1/2
    - oftalmologa/h1/5
  - id: h1-08
    texto: 'La novedad visible depende de que haya UV-A en la escena: es intensa al aire libre, junto a ventanas abiertas, bajo fluorescentes y luz negra y en tejidos o papel con blanqueantes ópticos, y casi nula con iluminación LED doméstica. En las zonas donde es de día, la piel de adolescentes y adultos muestra manchas y moteados de daño solar antes invisibles, mientras los bebés se ven uniformes, y mucha gente cree que quienes la rodean han enfermado o se han quemado por el fenómeno. Quien lleva protector solar o maquillaje con SPF aparece con una máscara oscura (filtro químico) o clara (filtro mineral), lo que genera desconcierto en oficinas, colegios y transporte y abre una fricción social y estética imprevista.'
    origen:
    - oftalmologa/h1/4
    - disruptor/h1/1
    - disruptor/h1/2
  - id: h1-09
    texto: 'El riesgo vial se reparte de forma desigual: el parabrisas laminado bloquea casi todo el UV-A, así que los conductores de turismos que miran al frente sufren poco deslumbramiento, pero las ventanillas laterales dejan pasar bastante más y provocan confusión en cambios de carril e incorporaciones, mientras motoristas, ciclistas y peatones reciben el deslumbramiento completo en exteriores soleados.'
    origen:
    - disruptor/h1/3
  - id: h1-10
    texto: 'En los centros educativos, donde el móvil no se usa en horario lectivo, las clases se paran porque alumnos y profesores ven a la vez colores nuevos en ropa, rotuladores y papel. Las familias llaman a secretaría preguntando si pueden recoger a sus hijos, y los centros no saben qué contestar porque no ha llegado ninguna instrucción oficial: cada profesor improvisa sobre si dejar usar el móvil.'
    origen:
    - adolescente/h1/1
    - adolescente/h1/4
  tensiones_abiertas:
  - 'Las gafas de sol con filtro UV alivian el deslumbramiento pero eliminan la percepción nueva: no está decidido si la gente las adopta en masa (y se sostiene el tirón de demanda y bursátil) o las rechaza para seguir viendo los colores.'
  - 'Qué narrativa sobre la causa se impone en redes: la de ''marcas ocultas'' de los agitadores, las otras atribuciones falsas o la explicación de las sociedades científicas.'
  - 'Cómo interpreta la sociedad la visibilidad de manchas solares y protector solar: alarma sanitaria pasajera o fricción estética, de clase o racial duradera.'
  - Si la falta de coordinación entre administraciones y la presión de la oposición obligan al Gobierno de España a pasar de la contención a medidas concretas, y si la OMS acaba convocando el Comité de Emergencias.
  - Cómo reaccionan Wall Street en su apertura y las bolsas asiáticas en su siguiente sesión, ya con más información.
  contradicciones_resueltas:
  - entre:
    - disruptor/h1/5
    - economista/h1/1
    decision: Se mantiene que el primer efecto económico medible del suceso está en los mercados financieros y en la demanda de gafas de sol, no en el ocio nocturno americano.
    motivo: La afirmación del economista tiene mecanismo y dato con fuente; la del disruptor es de confianza baja, especulativa y sin dato.
  - entre:
    - agitador/h1/5
    - medios/h1/2
    decision: No se fija qué narrativa domina; se recoge la proliferación de atribuciones falsas y la tesis de las 'marcas ocultas' como una de ellas, y la dominancia queda como tensión abierta.
    motivo: Ninguna de las dos aporta dato sobre la cuota de cada narrativa; ante empate se mantiene la tensión para el siguiente tramo.
  - entre:
    - oftalmologa/h1/3
    - economista/h1/2
    decision: Entran a la vez la subida de demanda y de cotización de las gafas de sol y el dilema de que bloquean la percepción nueva; la resolución del dilema se deja abierta.
    motivo: Ambas tienen mecanismo plausible y no se excluyen; el efecto cruzado sobre la demanda no se puede decidir en la primera hora.
  descartadas:
  - id: adolescente/h1/3
    motivo: Efecto local y de detalle (quejas y exageraciones en el recreo); el deslumbramiento en exteriores ya es un supuesto del mundo.
  - id: adolescente/h1/5
    motivo: Efecto local de detalle (competencia por la prenda más llamativa) que solo concreta la visibilidad de tintes y blanqueantes ya recogida en h1-08; especulativa y sin dato.
  - id: agitador/h1/3
    motivo: Detalle táctico del agitador (llevar el tráfico a su canal propio) que no cambia el rumbo del mundo en este tramo.
  - id: agitador/h1/5
    motivo: 'Especulativa y sin dato: su ganancia de audiencia es un efecto local y la dominancia de su narrativa queda como tensión abierta.'
  - id: disruptor/h1/5
    motivo: Confianza baja, especulativa y sin dato; además su conclusión sobre el primer efecto económico choca con un hecho con fuente (h1-01).

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h2
  afirmaciones:
  - texto: En la segunda hora la subida de EssilorLuxottica y de los valores de gafas de sol pierde fuerza y devuelve parte de lo ganado. Los analistas de ventas empiezan a publicar notas que separan el pico de demanda transitorio del negocio recurrente, y el economista repite en público que la subida estaba sobredimensionada y lo presenta como primer acierto.
    mecanismo: La tesis alcista de la hora 1 era 'todo el mundo necesitará gafas de sol', pero en esta hora se extiende la idea de que las gafas homologadas bloquean justo lo que la gente quiere ver, y quien se las pone deja de ver los colores nuevos. Si una parte de la población las rechaza, el tirón de demanda es más corto y más pequeño. Frente a una facturación anual de decenas de miles de millones, dos semanas de ventas extra en zonas soleadas no cambian el valor del grupo. Las compras por narrativa se deshacen cuando entra el análisis fundamental, y el economista gana prestigio si se le ve acertar antes que nadie.
    dato: EssilorLuxottica facturó 28.500 millones de euros en 2025.
    fuente: https://www.marketscreener.com/news/essilorluxottica-and-the-price-of-reinventing-eyewear-ce7e51dcde8df722
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados
    - consumo
    - optica
    id: economista/h2/1
  - texto: 'La volatilidad bursátil salta a una segunda historia fácil de contar: protectores solares y cosmética con SPF. L''Oréal, Beiersdorf y otros valores del sector se mueven con fuerza en ambos sentidos según se imponga el relato de ''nadie querrá ir con la cara enmascarada'' o el de ''el daño solar ahora se ve y todo el mundo comprará protección y tratamientos''.'
    mecanismo: La máscara visible del protector solar y las manchas de daño solar ya establecidas son dos narrativas opuestas sobre el mismo producto. Sin datos de ventas, los operadores apuestan por titulares y los algoritmos que leen noticias amplifican cualquiera de las dos. La señal neta es ambigua, así que el movimiento es de volatilidad y horquillas anchas más que de tendencia clara. Los frenos de Euronext, que actúan valor a valor, pueden dispararse también en estos nombres.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados
    - cosmetica
    - consumo
    id: economista/h2/2
  - texto: 'En EE. UU. la reacción de madrugada no se queda en los futuros: los inversores minoristas que se despiertan con la noticia operan valores sueltos y ETF en las plataformas de mercado nocturno y de preapertura, sobre todo los ligados a óptica, cosmética y ocio nocturno. Así se forman precios de referencia ruidosos antes de la apertura de Wall Street.'
    mecanismo: Algunas plataformas de inversión minorista permiten negociar acciones y ETF seleccionados las 24 horas laborables, de modo que la reacción no tiene que esperar a las 9:30 de Nueva York. Con poca liquidez y mucha emoción, unas pocas órdenes mueven el precio y esos niveles se difunden en redes como si fueran el juicio del mercado. El cierre de discotecas y locales con luz negra en América durante la madrugada da al minorista una historia propia para operar.
    dato: El 24 Hour Market de Robinhood ejecuta órdenes de 00:00 a 20:00 (hora del Este) en días hábiles completos, sobre una lista seleccionada de acciones y ETF.
    fuente: https://robinhood.com/us/en/support/articles/24hour-market
    confianza: media
    evidencia: dato
    areas_afectadas:
    - mercados
    - inversores_minoristas
    id: economista/h2/3
  - texto: Aparece una demanda inesperada de lámparas de luz negra, lámparas de uñas UV y linternas UV para casa, en tiendas físicas y online, por parte de gente que quiere ver los colores nuevos en interiores, donde la iluminación LED no los muestra. Los vendedores con stock suben precios y pronto se agotan.
    mecanismo: 'Que la novedad dependa de que haya UV-A en la escena significa que en casa, con LED, casi no se ve nada. Quien quiere repetir la experiencia de la calle, sobre todo de noche o en la Europa nublada de noviembre, busca fuentes UV-A baratas que ya existen en el mercado. Es el mismo mecanismo de poder de precio que con las gafas de sol, pero al revés: aquí se paga por ver más. Esa demanda choca con la advertencia clínica de no mirar fuentes UV intensas y producirá casos de lesión por conducta.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - comercio_electronico
    - salud
    id: economista/h2/4
  - texto: 'No hay huida generalizada a activos refugio: la deuda alemana, el oro y el dólar se mueven poco en la segunda hora, y el economista lo usa en público para desmontar el relato de pánico financiero, a diferencia de comentaristas que hablan de ''crisis'' sin datos.'
    mecanismo: 'La huida a refugio responde a amenazas sobre flujos de caja agregados: recesión, guerra, quiebras bancarias. En la hora 2 no hay daño económico medible, ni interrupciones de producción, ni cierres de plantas, porque las fábricas y oficinas funcionan con luz artificial y el deslumbramiento es transitorio. La volatilidad sigue confinada a valores con historia. Los bancos centrales no tienen ningún motivo para hablar, y su silencio refuerza la idea de normalidad en los mercados de tipos.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados
    - deuda_publica
    - divisas
    id: economista/h2/5
  reacciona_a:
  - oftalmologa/h1/3
  - disruptor/h1/2
  - disruptor/h1/5
  - oftalmologa/h1/4
- agente: politico
  tramo: h2
  afirmaciones:
  - texto: 'En la hora 2 el Gobierno de España pasa de la contención a la coordinación: convoca el Consejo de Seguridad Nacional (o su Comité de Situación) para ordenar los avisos de Estado, comunidades autónomas y ayuntamientos bajo un mensaje único, pero no declara todavía una situación de interés para la Seguridad Nacional ni el estado de alarma.'
    mecanismo: 'El mosaico de avisos descoordinados de la hora 1 es la munición principal de la oposición, y el Gobierno necesita un órgano que parezca de mando sin comprometerse con medidas excepcionales sin base técnica. La Ley 36/2015 de Seguridad Nacional ofrece justo eso: un sistema de gestión de crisis con un Comité de Situación que coordina a todas las administraciones sin suspender derechos. Declarar la situación de interés exige un real decreto con recursos y medidas concretas, y declarar la alarma exige daño acreditado; ninguna de las dos cosas tiene aún respaldo de los técnicos, así que el Gobierno se queda en el escalón que da imagen de control sin riesgo de rectificar.'
    dato: La Ley 36/2015 regula el Sistema de Seguridad Nacional, el Consejo de Seguridad Nacional como órgano de dirección y la declaración de situación de interés para la Seguridad Nacional mediante real decreto.
    fuente: https://www.boe.es/buscar/pdf/2015/BOE-A-2015-10389-consolidado.pdf
    confianza: media
    evidencia: dato
    areas_afectadas:
    - gobierno
    - coordinacion_administrativa
    - oposicion
    id: politico/h2/1
  - texto: 'Tras esa reunión, la portavoz o el ministro de Sanidad comparecen en rueda de prensa flanqueados por representantes de las sociedades de oftalmología. El mensaje se limita a lo que los técnicos respaldan: el deslumbramiento es transitorio, mirar al sol o a lámparas UV sigue lesionando la vista y conducir en moto o bici en exteriores soleados exige precaución extra. El Gobierno evita pronunciarse sobre causa y permanencia, y anuncia una comparecencia del presidente en el Congreso a petición propia en los próximos días para desactivar la exigencia de la oposición.'
    mecanismo: 'Ningún gobierno puede afirmar lo que sus técnicos no respaldan, y en la hora 1 la única fuente con autoridad empírica son los oftalmólogos y el precedente de los afáquicos. Poner a los médicos en el atril traslada la credibilidad científica al Gobierno y le permite decir algo concreto sin rectificar después. Ofrecer la comparecencia a petición propia le devuelve el control del calendario: la oposición ya no puede acusarle de esconderse, y el presidente llega al Congreso con informes técnicos en lugar de improvisar hoy. El precio es que los agitadores presentarán el aviso de no mirar al sol como confirmación de que se oculta algo.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - gobierno
    - salud_publica
    - comunicacion_institucional
    - oposicion
    id: politico/h2/2
  - texto: 'Las consejerías de Educación de las comunidades autónomas envían a lo largo de la hora 2 instrucciones a los centros, pero distintas entre sí: casi todas mantienen los colegios abiertos y permiten que las familias recojan a sus hijos por el procedimiento ordinario, y varias ordenan recreos en interior; ninguna cierra centros. La disparidad entre comunidades se convierte en el nuevo frente de la crítica por descoordinación, y alguna comunidad gobernada por la oposición se desmarca con un mensaje propio más duro o más tranquilizador que el del Gobierno central.'
    mecanismo: 'La gestión de los centros es competencia autonómica, y en la hora 1 las secretarías quedaron desbordadas por llamadas sin instrucción que dar. Cerrar colegios sin daño acreditado sería una medida desproporcionada y, además, cargaría a las familias trabajadoras, así que nadie la asume. Cada consejería redacta su circular con sus propios técnicos y a su ritmo, y las comunidades de distinto color político tienen incentivos para diferenciarse del Gobierno central: la oposición gana con cada contraste visible entre administraciones.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - comunidades_autonomas
    - familias
    - oposicion
    id: politico/h2/3
  - texto: El Ministerio de Consumo y las autoridades autonómicas de consumo anuncian vigilancia de precios abusivos y de productos sin marcado CE, y piden comprar gafas de sol solo en establecimientos con producto homologado. En la hora 2 es un aviso con amenaza de inspección, no una actuación sobre el terreno, y no llega a las plataformas extranjeras que venden filtros UV sin certificación.
    mecanismo: 'Actuar contra el oportunismo comercial es la medida concreta más barata y con base legal ya existente: las gafas de sol son equipos de protección individual que deben llevar marcado CE según el Reglamento (UE) 2016/425, así que el Gobierno puede señalar a los infractores sin norma nueva. Le permite aparecer protegiendo al ciudadano frente a los aprovechados, un mensaje transversal que la oposición no puede atacar. Pero las inspecciones requieren días y la venta online desde fuera de la UE escapa a su alcance inmediato, por eso el efecto en esta hora es sobre todo declarativo.'
    dato: Consumo recuerda que las gafas de sol son equipos de protección individual y deben llevar marcado CE e información sobre su categoría de filtro.
    fuente: https://portal-cec.consumo.gob.es/es/comunicacion/noticias/2021/cec-espana-recuerda-la-importancia-de-proteger-la-vista-con-gafas-de-sol
    confianza: media
    evidencia: dato
    areas_afectadas:
    - consumo
    - comercio
    - gobierno
    id: politico/h2/4
  - texto: Varios gobiernos europeos, entre ellos España, piden a la Comisión Europea que presione a las plataformas por los bulos y los falsos comunicados oficiales. La Comisión contacta con las plataformas de muy gran tamaño y les recuerda sus obligaciones de mitigar riesgos bajo la Ley de Servicios Digitales, pero no activa en la hora 2 el mecanismo de respuesta a crisis, que exige antes una recomendación de la Junta Europea de Servicios Digitales.
    mecanismo: Las capturas falsificadas de comunicados oficiales atacan directamente la legitimidad de los gobiernos, que necesitan que su mensaje no sea suplantado, y ningún gobierno puede ordenar retirar contenidos por su cuenta sin base legal. El cauce disponible es el Reglamento de Servicios Digitales, pero su artículo 36 requiere que la Comisión decida a recomendación de la Junta, lo que no ocurre en dos horas. La Comisión se queda en requerimientos informales, mientras los agitadores ya han movido su versión dura a canales propios de mensajería donde esa presión no alcanza.
    dato: El artículo 36 del Reglamento de Servicios Digitales permite a la Comisión exigir medidas a las plataformas de muy gran tamaño en situación de crisis, por decisión adoptada a recomendación de la Junta Europea de Servicios Digitales.
    fuente: https://dsa-observatory.eu/2023/02/21/the-dsas-crisis-approach-crisis-response-mechanism-and-crisis-protocols/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - union_europea
    - plataformas_digitales
    - desinformacion
    - gobierno
    id: politico/h2/5
  reacciona_a:
  - medios/h1/2
  - agitador/h1/3
  - agitador/h1/4
  - economista/h1/4
  - adolescente/h1/4
- agente: medios
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora las televisiones y los digitales encuentran por fin una imagen que emitir: recuperan el vídeo viral de 2014 ''How the sun sees you'', grabado con cámara ultravioleta, y piden a laboratorios, policía científica y fotógrafos técnicos imágenes UV propias de caras, protector solar y billetes. Esas imágenes, en blanco y negro o en falso color, se convierten en la ilustración estándar de los especiales y frenan parte de la alarma por la piel: los medios explican que las manchas siempre estuvieron ahí. A la vez, los negacionistas las señalan como prueba de montaje, porque no se parecen a lo que la gente dice ver.'
    mecanismo: La televisión no puede sostener un directo de horas sin imagen, y en la primera hora el fenómeno no se podía fotografiar con cámaras normales. Las cámaras con sensibilidad UV existen desde hace años y ya mostraron que el protector solar se ve negro y que el daño solar antiguo aparece como pecas y manchas. Un vídeo de archivo con autor y fecha cumple el requisito de fuente y se puede emitir sin esperar a nadie. Como esas cámaras traducen el UV a grises o a colores falsos, no reproducen la experiencia, y esa diferencia es justo lo que necesita quien defiende que todo es sugestión.
    dato: En 2014, el vídeo 'How the sun sees you' de Thomas Leveritt mostró con cámara UV que el protector solar aparece negro y que el daño solar antiguo se ve como pecas y manchas invisibles a simple vista.
    fuente: https://petapixel.com/2014/08/14/this-incredible-short-film-shows-what-your-aging-skin-looks-like-to-a-uv-camera
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - medios
    - sanidad
    - sociedad
    - desinformacion
    id: medios/h2/1
  - texto: 'Los verificadores publican en la segunda hora sus primeros desmentidos: señalan las capturas falsas de comunicados oficiales y contestan a la tesis de las ''marcas ocultas'' con documentos públicos que ya describían esas marcas, como la guía del Banco Central Europeo sobre los elementos de seguridad del euro visibles con luz ultravioleta. El desmentido llega a los medios y a un público ya escéptico, pero apenas entra en los canales propios del agitador, que lo presenta como una prueba más de que se sabía y se ocultaba.'
    mecanismo: Un desmentido rápido necesita un documento verificable, y las marcas UV de billetes y documentos están publicadas desde hace años porque sirven para detectar falsificaciones. Es el desmentido más barato y el primero que sale. Pero el agitador ya ha llevado a su audiencia a mensajería sin moderación y la ha vacunado contra las fuentes oficiales, así que 'estaba documentado' se convierte en 'lo sabían y no nos lo dijeron'. La corrección refuerza el relato en vez de desmontarlo.
    dato: La guía del BCE indica que, con luz ultravioleta, en los billetes de euro aparecen fibras rojas, azules y verdes, la bandera de la UE se ve verde con estrellas naranjas y la firma del presidente del BCE se vuelve verde.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/quick_guide_specimen_en.pdf
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - desinformacion
    - medios
    - finanzas
    - confianza_institucional
    id: medios/h2/2
  - texto: En la segunda hora circulan titulares y vídeos sobre los 'primeros heridos oculares'. En realidad, lo que se cuenta como lesión es deslumbramiento, fatiga visual y consultas por ansiedad. Las quemaduras reales de córnea de quienes miraron al sol o a lámparas UV todavía no se notan y aflorarán por la tarde y la noche. Ese retraso abre una segunda ola informativa, 'los efectos tardíos', que los agitadores presentan como prueba de que algo nos han hecho.
    mecanismo: 'La fotoqueratitis no duele en el momento: los síntomas aparecen horas después de la exposición. En la segunda hora los medios necesitan casos y aceptan como fuente el testimonio de urgencias o de un afectado, aunque lo que describe sean molestias benignas del fenómeno. Cuando lleguen las lesiones reales, ya de noche, encajarán con el relato de daño diferido que el agitador preparó en la primera hora. Discrepo en parte de oftalmologa/h1/5: los casos clínicos reales no llegan ''en horas'' próximas, sino con un desfase de seis a doce horas que el ciclo informativo convierte en una segunda noticia de miedo.'
    dato: Los síntomas de la fotoqueratitis suelen aparecer entre 6 y 12 horas después de la exposición.
    fuente: https://www.college-optometrists.org/Clinical-guidance/Clinical-Management-Guidelines/Photokeratitis_Ultraviolet_UV_Burn_ArcEye_SnowBlin
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - medios
    - desinformacion
    id: medios/h2/3
  - texto: 'Las grandes plataformas activan sus protocolos de crisis, con paneles informativos, etiquetas en las búsquedas y menos difusión para los consejos de salud falsos. Pero no tienen una autoridad clara a la que enlazar: la OMS solo hace seguimiento y los gobiernos emiten mensajes de contención distintos. Por eso cada plataforma y cada idioma enlazan a fuentes diferentes, ministerios nacionales o sociedades de oftalmología. Además, el contenido racista sobre las ''caras negras'' del protector solar empieza a retirarse por las normas contra el discurso de odio, y los agitadores lo convierten en otra historia de censura.'
    mecanismo: Los protocolos de desinformación sanitaria que las plataformas montaron en crisis anteriores funcionan enlazando a una autoridad sanitaria de referencia. Sin una declaración de la OMS ni una postura técnica común, cada equipo regional elige su fuente, y el mensaje sale fragmentado. Las bromas y los insultos sobre las máscaras oscuras de los filtros químicos sí encajan en normas ya existentes contra el odio, que se aplican antes que las sanitarias. Cada retirada visible le sirve al agitador para decir que hay algo que callar.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - plataformas
    - desinformacion
    - sociedad
    - confianza_institucional
    id: medios/h2/4
  - texto: En España el encuadre de los medios pasa en la segunda hora de '¿es peligroso?' a '¿quién manda?'. Tertulias, digitales y cabeceras de cada lado ponen en primer plano los avisos contradictorios de las distintas administraciones, la exigencia de comparecencia de la oposición y la comparación con los líderes extranjeros que ya han dado una causa o han declarado el fenómeno seguro. El relato científico de los oftalmólogos pasa a ser un rótulo secundario.
    mecanismo: 'Sobre la salud ya no hay nada nuevo que contar con fuente: el deslumbramiento está contado y nadie sabe la causa. La política, en cambio, ofrece fuentes con nombre, declaraciones grabadas y conflicto, que es lo que retiene audiencia en un directo largo. Cada medio elige además el ángulo que encaja con su público, y la descoordinación de los avisos es un hecho documentable. Los mensajes de contención sin medidas dejan un hueco que la crítica política llena antes que la explicación técnica.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - medios
    - confianza_institucional
    id: medios/h2/5
  reacciona_a:
  - oftalmologa/h1/5
  - agitador/h1/2
  - agitador/h1/4
  - politico/h1/2
- agente: oftalmologa
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora, la sociedad de oftalmología publica una nota de triaje que separa tres cosas: el deslumbramiento y la fatiga del fenómeno (benignos), las consultas por asimetría de percepción (benignas) y las lesiones por mirar al sol o a lámparas UV. Advierte de forma expresa que esas lesiones aún no se ven en urgencias porque tardan horas en dar síntomas, y que la oleada de casos llegará esta noche, no ahora.'
    mecanismo: La fotoqueratitis tiene una latencia de varias horas entre la exposición y el dolor, así que quien miró al sol en la hora 1 todavía se encuentra bien en la hora 2. Si la sociedad no lo dice antes, la ausencia de casos se leerá como prueba de inocuidad y los casos nocturnos parecerán un daño nuevo del fenómeno. Ese segundo relato es justo el que el agitador ha preparado al decir que algo nos han hecho. Anticipar el calendario clínico protege la credibilidad de la sociedad cuando lleguen los casos.
    dato: Los síntomas de la queratitis por ultravioleta suelen aparecer entre 6 y 12 horas después de la exposición.
    fuente: https://wikem.org/wiki/Ultraviolet_keratitis
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - sanidad
    - medios
    - desinformacion
    id: oftalmologa/h2/1
  - texto: Los usuarios de gafas graduadas descubren en la segunda hora que a través de sus lentes ven los colores nuevos muy atenuados y que aparecen al mirar por encima o por fuera de la montura. Muchos se quitan las gafas en la calle para verlos, y la sociedad añade a su nota que no se las quiten para conducir, ir en bici o cruzar.
    mecanismo: 'El policarbonato, un material habitual en las lentes graduadas, bloquea el ultravioleta por sí mismo, y otras lentes llevan un tratamiento anti-UV de serie. Es la misma asimetría que ya notaron los operados de cataratas, pero ahora a escala de cualquiera que lleve gafas: el campo central filtrado contrasta con la periferia sin filtrar. La tentación de ver los colores nuevos choca con la necesidad de ver nítido, y el riesgo se concentra en peatones y ciclistas, que ya reciben el deslumbramiento completo.'
    dato: El policarbonato bloquea los rayos UV por sí mismo, sin necesidad de añadir un tratamiento UV.
    fuente: https://www.allaboutvision.com/eyewear/eyeglasses/lenses/plastic-vs-polycarbonate-lenses/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - trafico
    - optica
    - consumo
    id: oftalmologa/h2/2
  - texto: 'Empieza a aparecer un gradiente por edad en los testimonios y las consultas: los niños describen los colores nuevos con más intensidad y se quejan más del deslumbramiento en el patio, mientras que las personas mayores dicen ver menos. La sociedad lo convierte en la primera recomendación concreta para los centros educativos: recreo a la sombra o con gorra de visera y nada de mirar al sol, sin necesidad de mandar a los alumnos a casa.'
    mecanismo: El cristalino infantil es mucho más transparente al ultravioleta que el adulto y amarillea con la edad. Si la percepción nueva depende de cuánto UV-A llega a la retina, como sugiere el precedente de los afáquicos, los niños reciben más estímulo y más deslumbramiento, y los mayores menos. Los colegios llevan una hora sin instrucciones y las familias quieren recoger a sus hijos; una pauta sencilla de una fuente clínica llena ese vacío antes que la Consejería, y además desmiente a quien exagera síntomas para irse a casa.
    dato: En niños menores de 10 años, el cristalino transmite más del 75 % de la radiación ultravioleta, frente a un 10 % en mayores de 25 años.
    fuente: https://zeiss.com/vision-care/int/better-vision/health-prevention/why-kids-glasses-should-offer-the-best-uv-protection.html
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - educacion
    - familias
    id: oftalmologa/h2/3
  - texto: 'La oftalmóloga sale a desactivar el miedo a la piel: dice en público que las manchas y las máscaras de protector solar no son una enfermedad nueva ni una quemadura del fenómeno, sino lo que siempre estuvo ahí y ahora se ve porque ha cambiado el ojo del observador. Busca el respaldo de los dermatólogos para dar el mensaje juntos.'
    mecanismo: La pigmentación por daño solar acumulado y los filtros solares tienen un contraste muy distinto en UV-A que en luz visible, y por eso la fotografía ultravioleta se usa desde hace tiempo para mostrar el daño solar oculto. Como el cambio está en quien mira y no en quien es mirado, el argumento clínico es directo, y es la única manera de cortar los rumores de contagio antes de que saturen la atención primaria. A la sociedad de oftalmología le interesa liderar esa explicación, porque el fenómeno es visual aunque el síntoma aparente sea cutáneo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - convivencia
    - medios
    id: oftalmologa/h2/4
  - texto: 'Sobre las gafas de sol, la sociedad fija una pauta de uso situacional que rebaja la idea de que todo el mundo las necesita: gafas homologadas con filtro UV a pleno sol, sobre todo para moto, bici y deporte, y sin ellas a la sombra o en interiores, donde se pueden ver los colores nuevos sin molestias. También denuncia que no existen gafas que potencien la visión UV.'
    mecanismo: El deslumbramiento depende de la cantidad de UV-A en la escena, que es alta a pleno sol y baja a la sombra y en interiores con luz LED, así que no hace falta llevar gafas todo el día. Una guía clínica que dé permiso para disfrutar de la novedad donde no molesta resuelve el dilema de ver o no ver mejor que una prohibición, y desactiva el argumento comercial de la protección imprescindible. Coincide con la tesis del economista de que el tirón de demanda está sobredimensionado, y da a la sociedad un mensaje propio frente a los portavoces improvisados.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - optica
    - mercados
    - sanidad
    id: oftalmologa/h2/5
  reacciona_a:
  - disruptor/h1/1
  - economista/h1/2
  - adolescente/h1/3
  - agitador/h1/4
- agente: adolescente
  tramo: h2
  afirmaciones:
  - texto: 'Entre las once y las doce mi clase se va vaciando a trozos: algunos padres se presentan en el instituto y se llevan a sus hijos, otros no, y a los que nos quedamos nos juntan en el aula o en el salón de actos sin dar clase de verdad, con el móvil ya permitido por casi todos los profes.'
    mecanismo: Sigue sin llegar una instrucción clara de la Consejería, así que el centro no puede impedir que un padre recoja a su hijo, pero tampoco puede mandar a todos a casa. Como los profesores no saben qué explicar y muchos padres llaman sin parar, dejar el móvil es la forma más fácil de que nos calmemos y de que en casa sepan que estamos bien. Quedarse o irse depende de si tus padres trabajan cerca o se agobian, no de una norma.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - familias
    - redes_sociales
    id: adolescente/h2/1
  - texto: En el baño y junto a las ventanas las chicas que llevamos base o crema con protector vemos que se nos nota una especie de máscara en la cara, y empieza una ola de ir al baño a lavarse la cara a toda prisa, mientras algunos chicos se ríen y llaman a las que la llevan con motes.
    mecanismo: El reflejo de la ventana deja pasar luz con ultravioleta y el espejo nos enseña lo que los demás ya veían en el patio. A los dieciséis lo que más te importa es cómo te ven, así que cualquier cosa que te haga distinta en la cara se vive como una humillación inmediata; y para quien quiere protagonismo, burlarse del que se nota es la manera más barata de conseguirlo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - imagen_corporal
    - convivencia_escolar
    id: adolescente/h2/2
  - texto: En cuanto tenemos el móvil, en mi grupo y en TikTok empezamos a ponerles nombres inventados a los colores nuevos, y se monta una competición por ver qué nombre se queda; quien consigue que su palabra se repita en los grupos de clase gana muchísimo estatus.
    mecanismo: Como las fotos no enseñan nada, lo único que se puede compartir es cómo lo llamas. Ponerle nombre a algo que todos ven pero nadie sabe decir es lo que más se comenta y lo que más rápido se copia, y entre adolescentes ser quien inventa la palabra que usa todo el mundo es la forma más clara de ser importante en el grupo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - lenguaje
    - cultura_juvenil
    id: adolescente/h2/3
  - texto: Nos llegan por los grupos de clase y por los padres trozos de los directos de las 'marcas ocultas', y varios de clase se ponen a mirar billetes, el DNI y los apuntes contra la ventana para buscar las marcas; unos se lo creen y se asustan y otros nos reímos y lo convertimos en meme.
    mecanismo: Los vídeos son reales, de verdad se ven dibujos en los billetes y en la ropa, y nadie en clase sabe que siempre estuvieron ahí por seguridad o por los blanqueantes. Si no te lo explican, lo que suena a secreto es lo más emocionante. Los grupos de familia reenvían sin mirar, y a la vez a nosotros burlarnos de lo que se creen los mayores también nos da atención, así que el bulo se mueve igual aunque sea en broma.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - desinformacion
    - redes_sociales
    - familias
    id: adolescente/h2/4
  - texto: 'Casi nadie de mi grupo se pone gafas de sol para salir al patio aunque le molesten los ojos: preferimos aguantar el deslumbramiento para seguir viendo los colores, y quien se las pone queda como el que se lo está perdiendo.'
    mecanismo: Ya sabemos por lo que se comenta que las gafas con filtro hacen que dejes de ver lo nuevo. Para nosotros lo que cuenta es poder contarlo y compararlo con los demás, y quedarte fuera de lo que todos ven es peor que la molestia; además la molestia no parece grave y nadie nos obliga a llevarlas. Esto contradice que la demanda de gafas se sostenga entre la gente joven.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - consumo
    - salud_visual
    - cultura_juvenil
    id: adolescente/h2/5
  reacciona_a:
  - agitador/h1/2
  - disruptor/h1/2
  - economista/h1/2
- agente: agitador
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora, cuando bancos centrales, policías y verificadores empiezan a explicar que las marcas que se ven en billetes y documentos son medidas de seguridad conocidas y públicas, el agitador no retrocede: reencuadra la aclaración como una confesión (''ahora admiten que estaba marcado'') y desplaza la sospecha de los billetes a lo que todavía no tiene explicación oficial, como marcas en envases, ropa o señalización.'
    mecanismo: Las fibras y elementos que brillan bajo UV en los billetes de euro están documentados por el BCE en sus guías para el público, así que la explicación llega rápido y es sólida. Para el agitador, desmentir sería perder audiencia; aceptar el hecho y cambiar su significado (de 'medida antifalsificación' a 'prueba de que nos marcan') le permite conservar el relato. Como en la hora 1 ya pidió no fiarse de las autoridades, la aclaración oficial llega desacreditada de antemano ante su audiencia, y el foco se traslada a objetos donde la verificación tarda más.
    dato: El BCE indica que, bajo luz ultravioleta, en los billetes de euro aparecen fibras y elementos impresos que brillan en distintos colores como medida de seguridad.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/quick_guide_specimen_en.pdf
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - desinformacion
    - redes_sociales
    - confianza_institucional
    - banca
    id: agitador/h2/1
  - texto: 'El agitador se apropia del aviso de la oftalmóloga de no mirar al sol ni a lámparas UV y lo presenta ante su audiencia como prueba de que ''no quieren que miremos''. Parte de sus seguidores hace justo lo contrario: busca las marcas con lámparas de luz negra, linternas UV o mirando cerca del sol, lo que suma casos de fotoqueratitis y molestias a las urgencias oftalmológicas en las horas siguientes.'
    mecanismo: Un aviso de prudencia que llega después de una advertencia previa contra las fuentes oficiales funciona como confirmación dentro de una comunidad que se define por 'ver la verdad'. El agitador no necesita recomendar conductas de riesgo; le basta con sembrar sospecha sobre el aviso. La curiosidad por ver las 'marcas' empuja hacia las fuentes de UV más intensas, y la fototoxicidad de siempre sigue actuando aunque el fenómeno no deje daño.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - desinformacion
    - sanidad_oftalmologica
    - redes_sociales
    id: agitador/h2/2
  - texto: 'Con la piel y las ''máscaras'' de protector solar ya en conversación, el agitador amplía su relato a la industria cosmética: presenta el protector visible en UV como otra ''marca'' que nos ponían sin saberlo y pide a su audiencia que mande fotos de caras con la máscara. Su canal se llena de imágenes de personas identificables, sin su consentimiento, que circulan con burla o sospecha, y la fricción estética del protector solar se carga de connotación conspirativa.'
    mecanismo: La máscara oscura o clara del protector es el efecto más visible y personal del suceso, y no se puede enseñar en foto, así que el relato tiene que apoyarse en testimonio y en señalar a quien la lleva. Sumar una industria más al reparto de culpables amplía su audiencia potencial y alimenta la urgencia que sostiene las donaciones. Pedir material a la audiencia, como en la hora 1, le da contenido gratis, pero expone a terceros que no han elegido aparecer.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - cohesion_social
    - privacidad
    - desinformacion
    - sector_cosmetico
    - redes_sociales
    id: agitador/h2/3
  - texto: Las grandes plataformas, que en la segunda hora empiezan a aplicar criterios de moderación sobre el suceso, retiran o limitan algunos fragmentos del agitador por desinformación sanitaria. Él convierte cada retirada en contenido ('me censuran por enseñar las marcas'), lleva a su audiencia a su canal propio de mensajería y la versión más dura del relato pasa a moverse donde no hay moderación.
    mecanismo: 'Las plataformas reaccionan con retraso y valor a valor, y retirar contenido a una cuenta con mucho alcance produce un efecto rebote: la retirada se percibe como confirmación por la audiencia que ya desconfía de las instituciones. El agitador tiene un canal propio que no se puede desmonetizar desde fuera, así que el coste de la retirada es bajo y la ganancia en lealtad y en tráfico migrado, alta. La falsedad se propaga más rápido que la corrección, y la migración la saca además del alcance de los verificadores.'
    dato: Un estudio sobre Twitter (2006-2017) encontró que las noticias falsas llegaban a 1.500 personas unas seis veces más rápido que las verdaderas.
    fuente: https://www.media.mit.edu/publications/the-spread-of-true-and-false-news-online/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - plataformas
    - moderacion_de_contenido
    - desinformacion
    - redes_sociales
    id: agitador/h2/4
  - texto: 'El agitador recoge en directo la descoordinación entre administraciones españolas: compara avisos de tráfico, protección civil y sanidad con matices distintos y los presenta como prueba de que ''cada uno oculta una parte''. Algunos cargos y cuentas de la oposición comparten fragmentos de su directo para reforzar la petición de comparecencia, y el relato de ocultación entra en la conversación política a pesar de su origen.'
    mecanismo: 'El mosaico de avisos no coordinados es un hecho verificable, y al agitador le sirve como material creíble para su tesis porque no tiene que inventar nada: solo cambia la explicación (descoordinación por ocultación). A la oposición le rinde cualquier prueba de improvisación del Gobierno, y un clip con mucho alcance es munición barata, aunque quien lo comparte asume el riesgo de quedar asociado a un bulo. El cruce entre agitación y política institucional le da al agitador una legitimidad que no tenía en la hora 1.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica_espanola
    - confianza_institucional
    - desinformacion
    - medios
    id: agitador/h2/5
  reacciona_a:
  - oftalmologa/h1/5
  - disruptor/h1/2
  - politico/h1/2
  - politico/h1/5
  - medios/h1/4
- agente: disruptor
  tramo: h2
  afirmaciones:
  - texto: 'La tesis de las ''marcas ocultas'' encuentra en la segunda hora un fragmento de verdad que la vuelve más difícil de desmontar: existen marcas pensadas para ser invisibles y ahora las ve todo el mundo. Son los marcadores forenses de propiedad tipo SmartWater en obras, comercios y vehículos de transporte de fondos, los rociadores antiintrusión que marcan a quien entra, los sellos de entrada de locales y las tintas de seguridad de documentos y embalajes. Empresas de seguridad y policías empiezan a recibir consultas, y quien lleva o guarda algo marcado puede verlo y limpiarlo por primera vez.'
    mecanismo: 'Estos sistemas funcionan porque la marca no se ve sin una lámpara UV, y la policía la busca precisamente con esa luz. Si todo el mundo percibe el UV-A, la condición de invisibilidad desaparece de golpe: el marcado deja de disuadir en secreto y el delincuente puede detectar el rastro en su ropa, su piel o en lo robado y eliminarlo antes de que lo encuentren. Además, como estas marcas sí se pusieron a propósito para que no se vieran, al agitador ya no le hace falta inventar la intención oculta: le basta con mezclar marcas de seguridad reales con residuos y blanqueantes. Los desmentidos oficiales tienen que admitir que parte de lo que se ve sí estaba oculto a propósito, y esa admisión parcial alimenta la desconfianza.'
    dato: SmartWater es un líquido con un código identificativo que apenas se ve a simple vista, salvo bajo luz negra ultravioleta; algunos sistemas lo rocían sobre el intruso y la policía localiza las marcas con luz UV.
    fuente: https://en.wikipedia.org/wiki/SmartWater_(forensic)
    confianza: media
    evidencia: dato
    areas_afectadas:
    - seguridad
    - policia
    - desinformacion
    - comercio
    id: disruptor/h2/1
  - texto: En las zonas de día con sol fuerte (África, Oriente Medio, sur de Asia) y en oficinas y centros educativos europeos, una parte de quienes llevan protector solar o maquillaje con SPF se lo quita durante la segunda hora para no mostrar la máscara visible, mientras otros, alarmados por las manchas solares que ahora ven en su piel, compran protector. Los dos flujos opuestos llegan a la vez a las farmacias, a las redes y a los valores cotizados de cosmética y protección solar, que se mueven con volatilidad y sin dirección clara.
    mecanismo: 'La máscara del protector tiene un coste social inmediato y visible: en la oficina o en clase destaca, y quitarse la crema es gratis y rápido. El daño de exponerse al sol sin protección, en cambio, es diferido e invisible en el momento. A la vez, ver de golpe el daño solar acumulado en la propia cara empuja a otra parte de la gente a protegerse más. La señal de demanda se contradice, y el mercado no sabe si descontar una caída del uso de protector por vergüenza o un auge por miedo. Los dermatólogos quedan en la posición incómoda de pedir que se siga usando algo que ahora estigmatiza, y el riesgo real que nadie atribuye bien es el de las quemaduras por quitarse la protección, no por el fenómeno.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - consumo
    - mercados
    - cosmetica
    id: disruptor/h2/2
  - texto: 'Dentro de los edificios la experiencia se rompe por ventanas: según el vidrio, en unos despachos, aulas y habitaciones de hospital se ven los colores nuevos y en otros no, incluso en el mismo edificio. Quien está tras un vidrio que bloquea el UV-A, o en una fachada sellada que no se abre, sale a la calle, a balcones o a terrazas para verlos, lo que interrumpe el trabajo a media mañana y expone a más gente al deslumbramiento exterior.'
    mecanismo: El vidrio común y buena parte del bajo emisivo dejan pasar bastante UV-A, mientras que el laminado lo bloquea casi del todo, como ya se vio con los parabrisas. Las plantas bajas, los escaparates, las mamparas y muchas fachadas modernas usan vidrio laminado por seguridad, de modo que la misma luz de mañana produce experiencias distintas según dónde se siente cada uno. Como la gente no sabe que la diferencia está en el cristal, atribuye a su propia vista ver menos que el compañero de al lado, y la salida para comprobarlo es salir al exterior, justo donde el deslumbramiento es mayor.
    dato: El vidrio bajo emisivo estándar bloquea solo en torno al 75 % de la radiación UVB y es mucho menos eficaz frente al UVA.
    fuente: https://fennel-gopher-pg3p.squarespace.com/blog/did-you-know-modern-architectural-glass-and-uv-protection-limitations
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - trabajo
    - educacion
    - sanidad
    - vivienda
    id: disruptor/h2/3
  - texto: En hospitales, transporte público, hoteles y aseos bajo luz fluorescente o cerca de ventanas aparecen manchas y restos en superficies que parecían limpias (residuos de productos de limpieza, fluidos y marcas de manos), y en la segunda hora surge una alarma de higiene que se descarga sobre el personal de limpieza y los gestores de esos espacios, no sobre el fenómeno.
    mecanismo: Muchos residuos orgánicos y productos químicos absorben o reflejan el UV de forma distinta a la superficie limpia, y por eso los hospitales ya auditan la limpieza con marcadores fluorescentes y lámparas UV. Ahora esa auditoría la hace cualquiera sin lámpara. Una superficie que antes parecía limpia muestra rastros, y el público no distingue entre suciedad real, restos inocuos de detergente y fluorescencia de materiales. La reacción previsible es fotografiar y denunciar en redes, pero como la foto no muestra nada, la queja se vuelve testimonial y se dirige contra quien limpia, mientras empresas de limpieza y hospitales reciben reclamaciones que no pueden refutar con imágenes.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - sanidad
    - transporte
    - hosteleria
    - trabajo
    id: disruptor/h2/4
  reacciona_a:
  - agitador/h1/2
  - agitador/h1/4

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
