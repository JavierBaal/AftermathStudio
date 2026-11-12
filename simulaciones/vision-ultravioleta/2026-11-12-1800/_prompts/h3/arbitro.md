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
Como máximo 10 hechos establecidos en este tramo. Todo lo demás va a descartadas con su motivo.

## Tramo que consolidas
Hora 3 (PT3H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h2
  resumen: 'En la segunda hora el vacío oficial lo ocupan las sociedades de oftalmología, los divulgadores sanitarios y los verificadores. Una prueba casera (quitarse las gafas y mirar el cielo) deshace buena parte del ''yo no lo veo'', pero aparecen dos diferencias reales que mantienen viva la idea de un cambio selectivo: los mayores ven mucho menos porque su cristalino filtra el UV, y los operados de cataratas con lente con filtro UV no ven nada. Esa idea se cruza con el ''no hay indicios de acción hostil'' de defensa, que se lee como prueba de ocultación, y con el bulo de que las ópticas ''lo sabían'', que se apoya en la subida bursátil de la hora anterior. En Europa se confirma que sí hay deslumbramiento por el sol bajo de noviembre, y en las zonas de UV alto la gente deja la sombra y se mete en interiores. La protección pasa a ser un dilema social entre ''proteger'' y ''ver'', los colegios meten a los alumnos dentro y algunos padres los recogen, y crece un mercado de gafas falsas y
    estafas. Los mercados siguen sin hundirse, aunque el miedo pasa a las opciones y caen aerolíneas y cosmética solar. En América cada gobierno responde según su reloj solar: el Cono Sur amanece y toma medidas, mientras Norteamérica, todavía a oscuras, debate si es histeria colectiva.'
  hechos_establecidos:
  - id: h2-01
    texto: 'La primera explicación con autoridad del ''yo no lo veo'' no viene de los gobiernos sino de las sociedades científicas de oftalmología y optometría. Proponen una prueba casera que cualquiera repite en diez segundos: mirar el cielo o una pared blanca al sol con las gafas o lentillas puestas y luego sin ellas. La prueba se viraliza como instrucción y no como imagen, y en grupos donde la gente está junta, como las aulas, el rumor se deshace en minutos. Los verificadores (Maldita, Newtral, EFE Verifica y la red IFCN) desmienten los falsos comunicados de la OMS y de Sanidad apoyándose en esos colectivos médicos y en las exploraciones normales de urgencias, pero su mensaje (''no hay pruebas de daño, pero nadie sabe la causa'') llega tarde a la mensajería privada y se lee como una confirmación a medias. La aclaración deja además un bulo derivado: que las gafas con filtro UV ''protegen'' del fenómeno y que ópticas y fabricantes ''lo sabían'', alimentado por la subida de EssilorLuxottica.'
    origen:
    - oftalmologa/h2/3
    - medios/h2/1
    - medios/h2/2
    - adolescente/h2/1
  - id: h2-02
    texto: La intensidad de los colores nuevos depende de la edad, porque el cristalino amarillea con los años y absorbe cada vez más UV antes de que llegue a la retina. Niños y adolescentes los ven vivos y molestos, los adultos de mediana edad más tenues y muchos mayores casi nada en el centro de la vista. Los operados de cataratas con lente intraocular moderna con filtro UV no ven los colores nuevos en ninguna parte del campo visual y no pueden corregirlo quitándose nada, así que el 'basta con quitarse las gafas' no les sirve y las consultas reciben la pregunta de si se puede cambiar la lente. Sin explicación médica pública, la comparación entre abuelos y nietos en los chats familiares se lee como una propiedad del fenómeno y no del ojo, y da una base real a la idea de un cambio selectivo, con teorías de que va dirigido a las generaciones nuevas.
    origen:
    - oftalmologa/h2/2
    - disruptor/h2/2
    - disruptor/h2/1
  - id: h2-03
    texto: En Europa sí hay deslumbramiento en noviembre aunque el índice UV sea bajo. El UV-A es la mayor parte del ultravioleta que llega al suelo y varía poco con la estación, y con el sol a unos 30 grados sobre el horizonte la luz entra de frente en el ojo. Molesta más en la calle, al conducir hacia el sol y en superficies claras o mojadas que mirando al cielo a mediodía, y los oftalmólogos lo explican en los medios como un problema de ángulo y no de cantidad de sol.
    origen:
    - oftalmologa/h2/1
    - economista/h2/4
  - id: h2-04
    texto: La sombra alivia solo en parte, porque una gran parte del UV-A llega dispersa desde todo el cielo y no solo del disco solar. En las regiones con UV alto la gente deja la sombra al aire libre y se concentra en espacios cerrados con techo y cristal (centros comerciales, estaciones de metro, mezquitas, oficinas, vehículos aparcados con el motor en marcha), y se vacían terrazas, mercados al aire libre y paradas de autobús descubiertas.
    origen:
    - disruptor/h2/3
  - id: h2-05
    texto: 'La protección pasa a ser un dilema social entre ''proteger'' y ''ver''. Los primeros mensajes de salud con difusión masiva vienen de dermatólogos, oftalmólogos y divulgadores con muchos seguidores, que piden no quitarse la crema solar ni las gafas de sol por estética. A la vez, entre adolescentes la conversación sobre la cara pasa de la vergüenza al reto: describir cómo se ve la cara ''en el color nuevo'' y pedir opinión, de modo que ir con la cara lavada, sin crema ni maquillaje, se convierte en lo normal y lo que mola. El consejo sanitario choca con lo que hace atractivo el fenómeno y empieza una guerra cultural incipiente.'
    origen:
    - medios/h2/5
    - adolescente/h2/4
  - id: h2-06
    texto: Los colegios, sin instrucciones oficiales, hacen el recreo y Educación Física dentro 'como precaución' y lo comunican a las familias. Muchos padres, que ya han leído los falsos avisos sanitarios en los grupos familiares, lo interpretan como confirmación de peligro, y algunos recogen a sus hijos antes de tiempo. Los adolescentes se burlan de los bulos en sus grupos pero acaban obedeciéndolos a medias 'por si acaso'.
    origen:
    - adolescente/h2/3
    - adolescente/h2/2
  - id: h2-07
    texto: 'El mercado de la protección y de la prueba imposible se llena de fraude. En las zonas con UV alto, agotadas las gafas homologadas, se venden gafas oscuras sin filtro UV real, que dilatan la pupila y dejan entrar más UV-A, y los usuarios notan que no sirven, lo que aumenta la confusión sobre qué protege. En Europa la compra se mueve por miedo y no por molestia: suben las búsquedas y pedidos en línea de gafas UV400 infantiles, se agota antes el pequeño inventario infantil y en los marketplaces aparecen vendedores con precios abusivos y plazos imposibles. Surgen además aplicaciones y filtros que dicen ''mostrar el color nuevo en tu pantalla'', webs de gafas ''para potenciar la visión UV'' y dominios recién registrados con los nombres virales del color.'
    origen:
    - medios/h2/4
    - oftalmologa/h2/4
    - economista/h2/4
  - id: h2-08
    texto: 'Los mercados europeos siguen sin desplomarse, pero el ajuste pasa del contado a las opciones: el VSTOXX y la volatilidad implícita suben mucho más de lo que caen los índices, porque los gestores compran protección en lugar de vender cartera. Los primeros sectores que caen con claridad son las aerolíneas cotizadas (IAG, Air France-KLM, Lufthansa, Ryanair), con una caída moderada porque el Reglamento 261/2004 las exime de indemnizar por circunstancias extraordinarias y el coste se queda en retrasos operativos, y los valores de protección solar como Beiersdorf y en menor medida L''Oréal, como reverso del impulso de las ópticas.'
    origen:
    - economista/h2/1
    - economista/h2/2
    - economista/h2/3
  - id: h2-09
    texto: Los gobiernos siguen en modo comunicación, pero el secreto empieza a costar. La presidencia rotatoria del Consejo de la UE activa el IPCR en modo de intercambio de información, con un informe conjunto de situación y un punto de contacto por Estado, sin Consejo extraordinario ni medidas comunes. Ante preguntas de periodistas, portavoces de defensa de varias potencias y de la OTAN dicen que 'no hay indicios de acción hostil' sin explicar quién lo ha evaluado, lo que confirma de forma implícita las evaluaciones secretas y en redes se lee como prueba de que los gobiernos sabían más de lo que decían.
    origen:
    - politico/h2/3
    - politico/h2/4
  - id: h2-10
    texto: En América cada gobierno responde según su reloj solar. En Brasil, Argentina y el resto del Cono Sur amanece con sol de primavera en plena hora punta y sus gobiernos pasan de la calma a decisiones operativas (avisos de tráfico, recreos a cubierto, retrasos en obras al aire libre). En Estados Unidos y Canadá, todavía de noche, el Gobierno federal mantiene el mensaje de calma y los informativos matinales y comentaristas reciben el suceso como una noticia europea sin pruebas visuales, que una parte enmarca como 'histeria colectiva' o sugestión. Se abre una brecha transatlántica de credibilidad que durará hasta que allí salga el sol.
    origen:
    - politico/h2/5
    - medios/h2/3
  tensiones_abiertas:
  - Queda por ver qué dirán los gobiernos cuando hablen. En España la rueda de prensa del Consejo de Ministros del martes, entre las 12:00 y las 13:00, es la primera ocasión prevista, y los ministerios de Sanidad aún no han publicado un desmentido formal.
  - Queda por ver si las diferencias reales por edad y por lentes intraoculares, el bulo de que las ópticas 'lo sabían' y la confirmación implícita de las evaluaciones de defensa se funden en una teoría de ocultación o de cambio dirigido.
  - Queda por ver si el dilema entre 'proteger' y 'ver' lleva a la gente a exponerse sin gafas ni crema, y si eso produce un aumento visible de consultas por fatiga, cefaleas o quemaduras en las regiones con UV alto.
  - Queda por ver cómo reacciona Norteamérica al amanecer, cuando el escepticismo de la 'histeria colectiva' choque con la experiencia directa.
  - Queda por ver si la visión UV-A deja a la vista marcas antiguas en la piel, como moratones o lesiones, y qué efecto tendría en colegios, servicios sociales y atención a la violencia. Por ahora no hay base suficiente para establecerlo.
  contradicciones_resueltas:
  - entre:
    - economista/h1/3
    - oftalmologa/h2/1
    - economista/h2/4
    decision: Se establece que en Europa hay deslumbramiento real en noviembre, menor que en las regiones con UV alto. Se cierra la tensión abierta de la hora 1.
    motivo: La oftalmóloga aporta un dato verificable sobre la exposición ocular con el sol bajo, que supera al índice UV, y el propio economista reconoce con dato que el UV-A domina y no desaparece en invierno. El índice UV de 2 no basta para deducir que la molestia sea escasa.
  - entre:
    - disruptor/h2/3
    - oftalmologa/h1/3
    decision: 'Se matiza h1-01: la sombra alivia en parte, pero en las regiones con UV alto la gente prefiere los interiores con techo y cristal.'
    motivo: El mecanismo de la radiación difusa es sólido y el dato del disruptor muestra una reducción de en torno al 40 % bajo sombra construida, lo que confirma un alivio solo parcial. No anula h1-01, lo completa con una consecuencia nueva sobre el uso del espacio.
  - entre:
    - politico/h2/2
    - medios/h2/2
    - oftalmologa/h2/3
    - medios/h2/5
    decision: En la segunda hora no hay todavía desmentidos formales de los ministerios de Sanidad. El vacío lo ocupan sociedades científicas, divulgadores y verificadores.
    motivo: Tres afirmaciones coherentes con el canon (h1-03, gobiernos callados) describen la ausencia de fuente oficial. La del político no aporta dato y su propia afirmación politico/h2/1 sitúa la primera comparecencia española en la hora siguiente.
  descartadas:
  - id: politico/h2/1
    motivo: Tiene mecanismo y dato, pero la rueda de prensa ocurre entre las 12:00 y las 13:00, fuera de este tramo. Queda como tensión abierta y puede entrar en la hora 3.
  - id: politico/h2/2
    motivo: Choca con medios/h2/2, oftalmologa/h2/3 y medios/h2/5, que describen la ausencia de fuente oficial, y no aporta dato. Ver contradicción resuelta.
  - id: oftalmologa/h2/5
    motivo: Es un efecto clínico de detalle sin dato. El cambio en el tipo de consultas no altera todavía el rumbo de otras áreas y queda recogido en las tensiones como posible consecuencia de la exposición.
  - id: disruptor/h2/4
    motivo: Tiene confianza baja y es un efecto local. La descarga de corona es tenue y emite sobre todo en bandas de ultravioleta más cortas que el UV-A, así que no está claro que sea visible a simple vista de forma generalizada. Cede ante efectos de más alcance.
  - id: disruptor/h2/5
    motivo: Tiene confianza baja y se apoya en una fuente divulgativa sobre fotografía UV con iluminación controlada, no con luz natural. Su alcance sería grande, así que queda como tensión abierta en lugar de hecho.
  - id: economista/h2/5
    motivo: Tiene confianza baja y es un efecto sectorial de detalle sobre medios de pago que de momento no cambia el rumbo. Con el límite de diez hechos cede ante efectos de más alcance.
  - id: adolescente/h2/5
    motivo: Solo concreta la disputa por el vocabulario ya recogida en h1-08 sin añadir una consecuencia nueva para otras áreas.
  metricas:
    alarma_social: 3
    respuesta_gobiernos: comunicacion
    impacto_economico: 2
    adaptacion: 2

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h3
  afirmaciones:
  - texto: Entre las 12:00 y las 13:00, en España y el resto de Europa, las empresas con plantillas al aire libre (construcción, logística, reparto, mantenimiento de redes, limpieza viaria) empiezan a pedir en bloque gafas de protección con filtro solar homologado a sus distribuidores de equipos de protección individual. Esos distribuidores reservan su inventario para los clientes con contrato y dejan de servir al canal minorista y a los marketplaces, que pierden una fuente de reposición.
    mecanismo: 'La Ley de Prevención de Riesgos Laborales obliga al empresario a evaluar cualquier riesgo nuevo y a dar el equipo de protección adecuado, y la nota de Sanidad que recomienda gafas UV400 al aire libre (politico/h2/2) convierte el deslumbramiento en un riesgo conocido: si un trabajador se cae de un andamio o tiene un accidente conduciendo deslumbrado, la empresa que no le dio gafas responde. Para el responsable de prevención, comprar ahora es barato y no comprar es una responsabilidad personal. Las gafas laborales con filtro solar se certifican por una norma propia y salen del mismo puñado de fabricantes de EPI, que en noviembre trabajan con existencias de temporada baja. El distribuidor prioriza al cliente recurrente con contrato frente al pedido puntual de un marketplace, así que la escasez de h2-07 se agrava desde el lado de la oferta y no solo por la demanda de los padres.'
    dato: Las gafas de protección laboral contra el deslumbramiento solar se certifican con la norma EN 172 (filtros de protección solar para uso laboral), dentro del marco de EPI recogido por el INSST.
    fuente: https://insst.es/documents/d/portal-insst/normas-proteccion-ocular-y_o-facial-diciembre-2024-
    confianza: media
    areas_afectadas:
    - empleo
    - cadena_de_suministro
    - prevencion_de_riesgos
    - comercio
    id: economista/h3/1
  - texto: En las regiones con sol fuerte que están en plena tarde, como el Golfo y Oriente Medio, las aplicaciones de reparto a domicilio reciben un pico de pedidos de la gente refugiada en interiores justo cuando se reduce el número de repartidores dispuestos a circular. Los tiempos de entrega se alargan, se activan tarifas dinámicas y algunas plataformas limitan pedidos o cierran temporalmente zonas.
    mecanismo: 'Es un desajuste de mercado de dos lados. La demanda sube porque los clientes se han ido a oficinas, centros comerciales y casas (h2-04) y evitan salir; la oferta baja porque el repartidor es el trabajador más expuesto al deslumbramiento y a la fatiga visual, conduce una moto mirando a un cielo que ahora le ciega y muchos dejan de conectarse o hacen menos pedidos. La plataforma responde con precio (tarifa dinámica) y con racionamiento, como ya hace ante lluvias o calor extremo, y no con más oferta, porque no puede fabricar repartidores en una hora. El consumo no desaparece: se encarece y se retrasa.'
    dato: En Emiratos, en las horas de calor del verano, las plataformas de reparto limitan a los repartidores a un máximo de 3 pedidos durante las horas pico de calor; en episodios de lluvia las aplicaciones han cerrado zonas o retrasado entregas.
    fuente: https://www.khaleejtimes.com/uae/uae-delivery-platforms-summer-heat-midday-break-rules-cooling-stations-health
    confianza: media
    areas_afectadas:
    - consumo
    - empleo
    - economia_de_plataformas
    id: economista/h3/2
  - texto: Los fabricantes de lentes intraoculares cotizados (Alcon en Zúrich, Carl Zeiss Meditec en Fráncfort) tienen una sesión de mucha volatilidad pero sin dirección clara. El mercado no compra la idea de una ola de recambios de lentes, y en las clínicas privadas de oftalmología empiezan las primeras llamadas de pacientes con cirugía de cataratas programada que piden aplazarla o preguntan por una lente sin filtro UV.
    mecanismo: 'Discrepo de que la pregunta por cambiar la lente (disruptor/h2/1) sea un negocio a la vista. Explantar una lente intraocular es una cirugía con más riesgo que la primera y ningún cirujano la propondrá para recuperar un color que nadie sabe si durará; además, quitar el filtro UV choca con décadas de práctica clínica pensada para proteger la retina. Así que el analista ve dos efectos contrarios sin poder pesarlos: posible demanda futura de lentes sin filtro si el fenómeno es permanente, frente a aplazamientos inmediatos de pacientes que no quieren perder lo que ahora ven. Lo único que sí es inmediato es el incentivo del paciente mayor con cataratas leves: operarse hoy significa renunciar al color nuevo, y aplazar no le cuesta casi nada. Eso resta actividad a las clínicas a corto plazo, no la suma.'
    dato: Alcon informó en 2026 de que ha superado los 175 millones de lentes intraoculares implantadas en todo el mundo.
    fuente: https://www.alcon.com/media-release/alcon-surpasses-175-million-iols-implanted-globally/
    confianza: media
    areas_afectadas:
    - mercados_financieros
    - sanidad_privada
    - consumo
    id: economista/h3/3
  - texto: En el preapertura de Estados Unidos, todavía de noche, los futuros del S&P 500 y del Nasdaq caen menos que los índices europeos y los futuros del VIX suben menos que el VSTOXX. Se abre un diferencial transatlántico en el precio del riesgo, y los operadores que lo ven compran protección barata sobre índices estadounidenses con vencimiento corto, apostando a que el diferencial se cierre al amanecer.
    mecanismo: 'El precio lo marca quien opera, y a esta hora en Estados Unidos operan sobre todo mesas que reciben el suceso como noticia europea sin prueba visual y en parte como ''histeria colectiva'' (h2-10). Pero la incertidumbre es la misma a ambos lados del Atlántico: lo que cambia es la percepción, no el riesgo. Para un gestor global eso es un arbitraje de relato: la volatilidad implícita estadounidense está barata frente a la europea por una razón que tiene fecha de caducidad, la salida del sol en Nueva York. Comprar opciones a pocos días es la forma más barata de apostar a la convergencia sin tener que acertar el signo del fenómeno.'
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - mercados_financieros
    id: economista/h3/4
  - texto: Los grandes marketplaces que operan en la UE empiezan a retirar en bloque anuncios de gafas de sol y gafas infantiles sin marcado CE ni declaración UV400 verificable, y también las 'gafas para potenciar la visión UV'. La retirada reduce todavía más la oferta disponible y sube el precio de los anuncios que quedan, en lugar de bajarlo.
    mecanismo: 'Desde diciembre de 2024 el Reglamento europeo de seguridad general de los productos obliga a los marketplaces a cooperar con las autoridades y a retirar con rapidez los productos peligrosos, y las gafas de sol son un equipo de protección individual que necesita marcado CE. Con los ministerios ya hablando de UV400 (politico/h2/2), las quejas de que las gafas no sirven (oftalmologa/h2/4) y la prensa contando estafas (medios/h2/4), cada anuncio dudoso es un riesgo regulatorio y de reputación para la plataforma, mucho mayor que la comisión que le deja. La plataforma prefiere el falso positivo: retira por lotes con filtros automáticos sin revisar uno a uno. Como el inventario homologado ya está agotado o reservado, quitar oferta dudosa no se compensa con oferta buena y el precio medio sube.'
    dato: El Reglamento (UE) 2023/988 de seguridad general de los productos es aplicable desde el 13 de diciembre de 2024 e impone obligaciones específicas a los mercados en línea.
    fuente: https://insightplus.bakermckenzie.com/bm/consumer-goods-retail_1/european-union-substantial-reform-of-european-product-safety-law-to-come-into-force-on-13-december-2024
    confianza: media
    areas_afectadas:
    - comercio_electronico
    - regulacion
    - consumo
    id: economista/h3/5
  reacciona_a:
  - disruptor/h2/1
  - politico/h2/2
  - oftalmologa/h2/4
  - medios/h2/4
- agente: politico
  tramo: h3
  afirmaciones:
  - texto: 'En la rueda de prensa posterior al Consejo de Ministros, entre las 12:00 y las 13:00, la ministra portavoz comparece junto a la ministra de Sanidad y no junto a Defensa. El Gobierno hace suya la explicación de las sociedades de oftalmología: repite la prueba de quitarse las gafas, explica que los mayores y los operados de cataratas ven menos por razones del ojo y no del fenómeno, y pide expresamente que nadie solicite cambiar su lente intraocular. A la pregunta sobre la evaluación de defensa responde con la fórmula ''no hay indicios de acción hostil'' y remite al Ministerio de Defensa, sin más detalle.'
    mecanismo: 'Las sociedades científicas han dado al Gobierno un guion con autoridad y ya probado por la población (oftalmologa/h2/3), así que adoptarlo le permite recuperar la voz oficial sin explicar la causa, que nadie conoce. Sentar a Sanidad y no a Defensa enmarca el asunto como sanitario y no de seguridad, que es lo que menos alarma. Lo de las lentes intraoculares es una petición barata y con beneficio inmediato: evita que las consultas se llenen de peticiones de cirugía en un fenómeno que nadie sabe si es permanente (disruptor/h2/1). Pero en defensa el Gobierno no puede decir más sin revelar evaluaciones secretas ni decir menos sin contradecir a la OTAN, así que repite la fórmula y el relato de ocultación sale reforzado justo en el acto que debía cerrarlo.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - gobierno
    - sanidad
    - comunicacion_publica
    - defensa
    id: politico/h3/1
  - texto: La primera acción coercitiva visible de los gobiernos europeos no va contra el fenómeno sino contra el fraude. Consumo y las autoridades de vigilancia del mercado anuncian controles a las gafas de sol sin marcado CE ni filtro UV real y requerimientos a los marketplaces para retirar anuncios de gafas 'para potenciar la visión UV' y productos infantiles con precios abusivos, y las policías avisan de dominios y apps fraudulentos con los nombres del color.
    mecanismo: 'El fraude es el único frente del suceso donde el Gobierno tiene competencia clara, culpables identificables y una norma ya escrita que aplicar. Las gafas de sol son equipos de protección individual con requisitos de marcado CE, de modo que perseguir las falsas no exige explicar nada nuevo. Para un político es la acción perfecta: visible, popular y sin riesgo de equivocarse sobre la causa. Además responde a una queja que la gente ya comprueba con su propio ojo, porque las gafas falsas deslumbran más (oftalmologa/h2/4), y desactiva el bulo de que el Gobierno no hace nada.'
    dato: En la UE las gafas de sol son equipos de protección individual regulados por el Reglamento (UE) 2016/425, que exige marcado CE.
    fuente: https://eur-lex.europa.eu/eli/reg/2016/425/oj
    confianza: media
    areas_afectadas:
    - consumo
    - comercio_electronico
    - seguridad
    - gobierno
    id: politico/h3/2
  - texto: En la costa este de Estados Unidos amanece hacia las 12:40 de Madrid, y las primeras decisiones operativas no las toma el Gobierno federal sino los gobernadores, los departamentos de transporte de los estados y los distritos escolares, que aplican sus protocolos de retraso de apertura y avisos de conducción como si fuera una incidencia meteorológica. La Casa Blanca mantiene el mensaje de calma pero abandona cualquier insinuación de histeria colectiva.
    mecanismo: En el sistema federal estadounidense la gestión ordinaria de emergencias, el tráfico y los colegios dependen de estados y condados, que tienen protocolos de decisión rápida pensados para la nieve o la niebla y los activan antes de las siete de la mañana. El deslumbramiento con sol bajo al amanecer, que es el ángulo que más molesta, coincide con la hora punta de ida al trabajo y al colegio. Ningún responsable federal quiere quedar grabado llamando sugestión a algo que su electorado está sintiendo en ese momento, así que la brecha de credibilidad (medios/h2/3) se cierra por la vía de los gobiernos locales y el escepticismo pasa a ser un coste para quien lo defendió.
    dato: El 10 de noviembre de 2026 el sol sale en Nueva York a las 06:37 hora local (12:37 en Madrid).
    fuente: https://calendriersolaire.com/us/new-york-ny/2026/11
    confianza: media
    areas_afectadas:
    - gobierno
    - transporte
    - educacion
    - relaciones_transatlanticas
    id: politico/h3/3
  - texto: Los partidos de la oposición en España y en otros países europeos registran peticiones de comparecencia urgente del jefe de Gobierno y del ministro de Defensa, centradas en qué se sabía y quién evaluó la hipótesis de un ataque. Los partidos grandes piden transparencia sin respaldar teorías, mientras que formaciones y figuras populistas amplifican en redes la idea de que las ópticas y los gobiernos 'lo sabían'.
    mecanismo: 'Pedir transparencia es la jugada de menor riesgo para la oposición: no obliga a proponer una causa ni a asumir el desgaste de equivocarse, y aprovecha la confirmación implícita de las evaluaciones secretas (h2-09). Los partidos con aspiración de gobierno evitan apoyar el bulo porque podrían heredar la crisis, pero los actores marginales no tienen ese coste y ganan audiencia con la sospecha de lucro de las ópticas (h2-01). La petición de comparecencia mantiene el asunto en la agenda parlamentaria y obliga al Gobierno a fijar fecha, que es lo que buscan.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - parlamento
    - partidos
    - desinformacion
    - legitimidad
    id: politico/h3/4
  - texto: La OMS publica una declaración formal en la que desautoriza los comunicados falsos que usan su logotipo, dice que no tiene constancia de daño ocular permanente y que vigila el fenómeno con los Estados, pero no convoca el comité de emergencias del Reglamento Sanitario Internacional ni declara una emergencia de salud pública de importancia internacional.
    mecanismo: 'La suplantación de su marca convierte el silencio en un coste directo para la OMS, igual que para los ministerios, y desmentirla no exige conocer la causa. Pero el Reglamento Sanitario Internacional define la emergencia de importancia internacional en torno a un riesgo para la salud pública por propagación internacional de una enfermedad, y aquí no hay enfermedad, ni propagación, ni daño demostrado: el cambio ha ocurrido a la vez en todo el mundo. Convocar el comité implicaría tratarlo como una patología y alimentaría el miedo que los propios desmentidos intentan cortar, así que la organización se queda en comunicación y vigilancia.'
    dato: El Reglamento Sanitario Internacional (2005) define la emergencia de salud pública de importancia internacional como un evento extraordinario que constituye un riesgo para la salud pública de otros Estados por la propagación internacional de una enfermedad y que puede exigir una respuesta internacional coordinada.
    fuente: https://www.who.int/publications/i/item/9789241580496
    confianza: media
    areas_afectadas:
    - organismos_internacionales
    - sanidad
    - desinformacion
    id: politico/h3/5
  reacciona_a:
  - oftalmologa/h2/3
  - disruptor/h2/1
  - oftalmologa/h2/4
  - medios/h2/3
  - medios/h2/4
- agente: medios
  tramo: h3
  afirmaciones:
  - texto: 'Hacia las 12:40 de Madrid amanece en la costa este de Estados Unidos y los magacines matinales sacan las cámaras a la calle en directo. El clip más compartido de la hora en todo el mundo es la reacción en antena de un presentador o comentarista que una hora antes hablaba de ''histeria colectiva'' y que, al mirar al cielo, se queda sin palabras. El escepticismo norteamericano no desaparece, pero cambia de argumento: ya no niega el fenómeno sino que culpa a los medios de ''contagiar'' la alarma.'
    mecanismo: 'Los magacines matinales tienen el formato de conexión exterior en directo ya montado y, tras dos horas de debate entre ''lo veo'' y ''es sugestión'', salir a comprobarlo con el sol es el momento de máxima audiencia. Como el color no sale en cámara (h1-06), lo único que se puede emitir es la cara de quien lo ve, y la de un escéptico convertido es la más valiosa porque resuelve el conflicto narrativo en segundos. Quien había apostado por el escepticismo no puede retractarse del todo sin perder credibilidad ante su audiencia, así que se desplaza a la posición más cercana que puede defender: el fenómeno existe, pero la alarma la fabrican los medios.'
    dato: El 12 de noviembre el sol sale en Nueva York (Manhattan) a las 6:39, que son las 12:39 en Madrid.
    fuente: https://sunrise-sunset.org/us/10012
    confianza: media
    areas_afectadas:
    - medios
    - opinion_publica
    - politica_internacional
    id: medios/h3/1
  - texto: En la rueda de prensa posterior al Consejo de Ministros, lo que circula en redes no es el mensaje leído por la portavoz sino un corte de quince segundos con su respuesta a la pregunta de si el Gobierno sabía algo antes, a raíz de la frase de defensa sobre la acción hostil. Cualquier fórmula del tipo 'no tenemos constancia' o 'no podemos descartar nada' se recorta sin contexto y alimenta la teoría de la ocultación, y como la intervención no menciona las diferencias por edad ni las lentes de cataratas, la idea de un cambio selectivo sigue sin respuesta oficial.
    mecanismo: Los periodistas llevan a la rueda de prensa las preguntas que ya son tendencia, y la más compartida es la de la ocultación (h2-09), no la sanitaria. Un mensaje institucional leído es largo y plano, mientras que una respuesta improvisada a una pregunta incómoda tiene el formato que premian los algoritmos de vídeo corto. La prudencia jurídica obliga a la portavoz a no negar de forma tajante lo que no sabe, y esa prudencia, recortada, suena a evasiva. Un mensaje político preparado para calmar no incluye detalles de óptica como el cristalino o las lentes intraoculares, que son justo lo que desmontaría la idea de selección.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - politica
    - medios
    - desinformacion
    - confianza_institucional
    id: medios/h3/2
  - texto: 'La teoría de la ocultación se fusiona y la difunden sobre todo redes conspirativas que ya existían (antivacunas, ''chemtrails'', 5G), que reciclan sus plantillas: el cielo de otro color se presenta como prueba de que ''han echado algo'', la diferencia entre abuelos y nietos como prueba de que el cambio va dirigido a las generaciones nuevas, la frase de defensa como confesión y la subida de las ópticas como el beneficiario. El relato unificado gana tracción en Telegram y en canales de vídeo antes que en las redes abiertas.'
    mecanismo: Construir una narrativa conspirativa desde cero lleva tiempo, pero estas comunidades ya tienen audiencia, influencers, canales con cientos de miles de suscriptores y un marco listo (algo en el cielo, un plan oculto, alguien que se lucra) en el que encajan sin esfuerzo las tres piezas que dejó la segunda hora. El cielo es literalmente distinto para todo el mundo, así que el argumento visual del 'mira arriba' de los chemtrails funciona mejor que nunca. Telegram no limita los reenvíos como WhatsApp ni modera como las grandes plataformas, así que el relato completo se cuece allí y baja después a los grupos familiares en trozos.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - desinformacion
    - opinion_publica
    - confianza_institucional
    id: medios/h3/3
  - texto: 'En las zonas con sol, la tendencia de ir con la cara lavada choca con un descubrimiento que no esperaba nadie: en el color nuevo se ven en los adultos las manchas solares acumuladas que no se veían a simple vista, como pecas oscuras repartidas por la cara. Los dermatólogos recuperan la lógica del vídeo viral ''How the sun sees you'' y lo usan como argumento a favor de la crema, y la tendencia se parte por edad: los adolescentes, con poco daño acumulado, siguen con la cara lavada, y muchos adultos vuelven al maquillaje o la crema porque tienen que elegir entre ''la mancha negra'' y ''las manchas de sol''.'
    mecanismo: 'Discrepo en parte de adolescente/h2/4: la cara lavada no es neutra para todos. La melanina absorbe el ultravioleta, y el daño solar crónico deja depósitos irregulares de pigmento (léntigos solares) que en luz visible apenas se notan pero en UV-A contrastan mucho, que es lo que las cámaras ultravioleta llevan años mostrando. La piel de un adolescente tiene poco daño acumulado, así que su cara en el canal nuevo sale limpia, mientras que la de un adulto de cuarenta o cincuenta años sale moteada. Lo que para los jóvenes es un reto divertido, para los adultos es una exposición incómoda, y eso da a los divulgadores sanitarios un argumento visual que no tenían en la segunda hora.'
    dato: En 2014 el vídeo 'How the sun sees you', grabado con cámara ultravioleta, se hizo viral mostrando manchas y léntigos solares invisibles en la piel a simple vista.
    fuente: https://www.smithsonianmag.com/smart-news/ultraviolet-camera-reveals-secret-price-sunbathing-180952363/
    confianza: media
    areas_afectadas:
    - salud
    - cultura
    - redes_sociales
    - cosmetica
    id: medios/h3/4
  - texto: 'Google y las grandes plataformas publicitarias aplican al fenómeno sus políticas de eventos sensibles y empiezan a bloquear anuncios que usan los nombres virales del color o venden gafas y protección con precios abusivos o plazos imposibles. El fraude no desaparece: se desplaza de los anuncios de pago al contenido orgánico, a las tiendas dentro de TikTok e Instagram, a los marketplaces y a los canales de Telegram, donde la detección es más lenta.'
    mecanismo: La política de eventos sensibles de Google ya prohíbe la subida abusiva de precios, vender lo que no se puede suministrar y el oportunismo con palabras clave ligadas a una crisis, que son justo los patrones de h2-07, así que no hace falta inventar una norma nueva, solo marcar el suceso. Los equipos de seguridad publicitaria lo hacen en horas porque los dominios recién registrados con términos virales son una señal clásica de fraude. Pero el bloqueo actúa sobre el canal de pago, y el estafador, que ya tiene la tienda montada, pasa a moverla con vídeos, influencers pequeños y mensajería, donde el comprador sigue sin poder comprobar la promesa.
    dato: La política de eventos sensibles de Google Ads prohíbe la subida artificial de precios de suministros esenciales, vender bienes que no pueden cubrir la demanda creada por el suceso y usar palabras clave del suceso para captar tráfico.
    fuente: https://support.google.com/adspolicy/answer/16489952
    confianza: media
    areas_afectadas:
    - plataformas
    - fraude
    - comercio_electronico
    - desinformacion
    id: medios/h3/5
  reacciona_a:
  - adolescente/h2/4
  - politico/h2/1
- agente: oftalmologa
  tramo: h3
  afirmaciones:
  - texto: 'Entre las 12:00 y las 13:00 aparece el grupo que rompe la teoría del cambio dirigido a los jóvenes: personas muy mayores operadas de cataratas hace cuarenta años o más, con implantes antiguos sin filtro o sin lente intraocular (afáquicas), que dicen ver los colores nuevos con más intensidad que sus nietos. Los oftalmólogos y divulgadores los usan en los medios como prueba de que la diferencia está en el ojo y no en el fenómeno, y la historia de Monet, que tras operarse de cataratas en 1923 empezó a pintar con tonos azules y violetas, se viraliza como explicación sencilla.'
    mecanismo: El gradiente por edad de h2-02 no viene de la persona sino del cristalino, que filtra cada vez más ultravioleta al envejecer. Si se quita el cristalino y no se pone un filtro, el UV-A llega a la retina con menos obstáculo que en un niño. Los cromóforos que absorben UV se incorporaron a las lentes intraoculares a principios de los ochenta y se generalizaron hacia 1986, así que quienes se operaron antes son hoy octogenarios o nonagenarios. Que el grupo que mejor ve sea el más anciano invierte la lectura generacional, y una anécdota con un pintor famoso viaja mejor por mensajería que una curva de transmisión del cristalino.
    dato: Los cromóforos absorbentes de UV se introdujeron en las lentes intraoculares a principios de los años ochenta y la mayoría de lentes los llevaba en 1986.
    fuente: https://pmc.ncbi.nlm.nih.gov/articles/PMC1920564
    confianza: media
    areas_afectadas:
    - salud
    - medios
    - desinformacion
    - personas_mayores
    id: oftalmologa/h3/1
  - texto: 'Las sociedades de oftalmología publican a mediodía una posición explícita: no se recambiará ninguna lente intraocular para recuperar la visión de los colores nuevos. Las consultas de pacientes operados con lente con filtro pasan de la pregunta a la queja, y aparece un discurso de agravio del tipo ''a nosotros nos lo han quitado'', mientras alguna clínica privada en el extranjero insinúa en redes que podría hacerlo.'
    mecanismo: Explantar una lente intraocular es una cirugía con riesgos reales (desprendimiento de retina, daño del endotelio corneal, rotura de la cápsula, edema macular) y solo se indica por un problema clínico. Ningún cirujano puede justificar ese riesgo ante un beneficio perceptivo que nadie sabe si es permanente, y la responsabilidad legal y el consentimiento informado lo hacen inviable en la sanidad pública y en las clínicas serias. La negativa, correcta, deja sin salida a un colectivo que sí tiene una pérdida real, y ese hueco es el que aprovecha la oferta oportunista que ya existe para las gafas falsas (h2-07).
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - sanidad_privada
    - personas_mayores
    - fraude
    id: oftalmologa/h3/2
  - texto: 'Con el tráfico de mediodía los conductores descubren que el coche no protege por igual: el parabrisas corta casi todo el deslumbramiento, pero las ventanillas laterales no, y las quejas se concentran en la luz que entra de lado y al conducir con la ventanilla bajada. Motoristas, ciclistas y repartidores, sin parabrisas, son los más afectados, y los consejos de tráfico pasan a ser ''ventanillas subidas y gafas UV400 aunque estés dentro del coche''.'
    mecanismo: 'El parabrisas es vidrio laminado con una lámina intermedia de plástico que absorbe casi todo el UV-A, mientras que las ventanillas laterales suelen ser vidrio templado sin esa capa. El hecho h1 de que en vehículos el cambio pasa casi desapercibido vale para quien mira hacia delante, pero con el sol de noviembre bajo y lateral en muchas calles, buena parte de la luz entra por las ventanillas. Matiza también h2-04: los coches aparcados como refugio solo funcionan si el sol no entra de lado.'
    dato: En un estudio de 29 coches, los parabrisas bloqueaban de media el 96 % del UV-A y las ventanillas laterales el 71 %; solo 4 coches tenían ventanillas laterales que bloquearan más del 90 %.
    fuente: https://www.sciencedaily.com/releases/2016/05/160512124928.htm
    confianza: alta
    areas_afectadas:
    - trafico
    - transporte
    - reparto
    - seguridad_vial
    id: oftalmologa/h3/3
  - texto: La prueba casera de quitarse las gafas da resultados distintos según el material de la lente, y a mediodía circulan testimonios contradictorios del tipo 'con mis gafas también lo veo un poco' o 'lo veo alrededor de la montura'. Los ópticos tienen que explicar que unas gafas graduadas no filtran igual que otras y que muchas lentillas llevan filtro UV y otras no, y la consulta típica en las ópticas pasa a ser '¿qué filtran mis gafas?'.
    mecanismo: 'El policarbonato y los materiales de alto índice absorben casi todo el UV-A por sí mismos, mientras que el plástico orgánico clásico sin tratamiento deja pasar una parte. Entre las lentillas blandas, unas llevan bloqueador UV y otras no. Además las gafas no tapan todo el campo visual: el UV-A disperso del cielo (h2-04) entra por los lados y por encima de la montura, y se ve como un halo periférico de color nuevo. La prueba de h2-01 funciona como regla general, pero en cada persona el resultado depende de un dato que casi nadie conoce de sus propias gafas.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - opticas
    - comercio
    - desinformacion
    id: oftalmologa/h3/4
  - texto: Las consultas de oftalmología y los servicios de urgencias dejan de dilatar la pupila en las revisiones no urgentes de mediodía o dan gafas desechables a la salida, porque los primeros pacientes que salen a la calle con la pupila dilatada sufren un deslumbramiento mucho más intenso que el resto.
    mecanismo: Las gotas para explorar el fondo de ojo mantienen la pupila dilatada entre cuatro y seis horas, y una pupila de siete u ocho milímetros deja entrar varias veces más luz que una contraída por el sol. Ese paciente pierde además el reflejo pupilar que protege del exceso de luz, así que el UV-A que antes no percibía le llega como un deslumbramiento fuerte al salir. Es el mismo efecto que las gafas oscuras sin filtro de h2-04, pero producido por la propia consulta, y los servicios lo corrigen con un cambio de protocolo barato y rápido en cuanto tienen las primeras quejas.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - sanidad_publica
    - protocolos_clinicos
    id: oftalmologa/h3/5
  reacciona_a:
  - disruptor/h2/2
  - disruptor/h2/3
- agente: adolescente
  tramo: h3
  afirmaciones:
  - texto: Entre las 12:00 y las 13:00 vemos la rueda de prensa del Gobierno a escondidas en el móvil, en clase o en el baño, y lo que se comparte no es lo que dice la portavoz sino cortes de diez segundos. Los convertimos en memes, sobre todo cuando dice que no nos quitemos la crema ni las gafas, y la frase pasa a ser una coletilla de broma en el grupo de clase.
    mecanismo: La rueda de prensa cae en horario de clase y nadie la ve entera; a nosotras nos llega recortada por TikTok y por los stories, y lo que más se recorta es lo que choca con lo que estamos haciendo. Que una persona adulta del Gobierno nos pida lo mismo que nuestras madres confirma que lo de protegerse es cosa de mayores, y reírse de ello es la forma de demostrar en el grupo que tú no tienes miedo.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - comunicacion_institucional
    - redes_sociales
    - salud_publica
    - juventud
    id: adolescente/h3/1
  - texto: 'Cuando nos enteramos de que los abuelos y muchos padres casi no ven los colores, entre la gente de mi edad no se vive como algo que dé miedo sino como algo que nos hace especiales: empieza a circular que somos la generación que lo ve, y en las videollamadas y chats con los abuelos hacemos de traductoras, describiéndoles cómo se ven las cosas.'
    mecanismo: 'La diferencia por edad es real y la notamos cada vez que comparamos en casa o por WhatsApp. Para los mayores eso suena a que el cambio está dirigido, pero para nosotras es lo primero en mucho tiempo en lo que sabemos más que los adultos, y eso sube el estatus de ser joven. Por eso el bulo del cambio selectivo nos llega al revés: no como amenaza, sino como presumir.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - relaciones_intergeneracionales
    - identidad
    - redes_sociales
    - desinformacion
    id: adolescente/h3/2
  - texto: Los que llevan gafas de graduación empiezan a quitárselas en clase aunque no vean bien la pizarra, solo para seguir viendo los colores nuevos, y a media mañana varios se quejan de dolor de cabeza y piden ir a la enfermería o a conserjería; algunos profesores les obligan a ponérselas otra vez.
    mecanismo: Ya sabemos que las gafas con filtro te quitan el color nuevo, y quedarte sin verlo cuando todo el mundo lo está comentando es quedarte fuera de la conversación. Pero sin gafas el que tiene miopía fuerza la vista para leer, y junto a las ventanas con sol encima se deslumbra, así que entre una cosa y otra acaba con la cabeza cargada al cabo de una o dos horas.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - salud_visual
    - juventud
    id: adolescente/h3/3
  - texto: En el baño y junto a las ventanas alguna chica se da cuenta de que se le notan en el cuello o en los brazos marcas que ya no se veían, sobre todo chupetones y moratones viejos de deporte, y eso se convierte en cotilleo en cuestión de minutos; las que tienen algo que esconder empiezan a ir con sudadera con capucha o bufanda dentro del instituto.
    mecanismo: Si ahora vemos manchas en la piel que antes no se veían, también vemos las marcas que alguien creía que ya habían desaparecido. Entre adolescentes lo primero que se mira no es si es algo grave sino quién ha estado con quién, así que se convierte en chisme. Taparse con ropa es lo único que se nos ocurre, porque no sabemos si el maquillaje lo tapa o lo empeora en el color nuevo.
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - educacion
    - convivencia_escolar
    - privacidad
    - juventud
    id: adolescente/h3/4
  - texto: 'Con el recreo dentro y Educación Física en el gimnasio, los pasillos y las aulas que dan al sol se convierten en el sitio donde todo el mundo quiere estar: nos pegamos a las ventanas para mirar fuera, y los profesores de guardia acaban bajando persianas para que dejemos de amontonarnos y de lagrimear.'
    mecanismo: Si no nos dejan salir pero lo interesante está fuera, buscamos el sitio más cercano a la luz sin salir, que es la ventana, porque por el cristal sigue entrando algo del color nuevo. Al profesorado le preocupa a la vez el lío y que nos dé algo en los ojos, así que bajar persianas es la forma más fácil de cumplir con la precaución que ha mandado el centro.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - convivencia_escolar
    - salud_visual
    id: adolescente/h3/5
  reacciona_a:
  - politico/h2/1
  - politico/h2/2
  - disruptor/h2/2
  - disruptor/h2/5
- agente: disruptor
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora, junto a ventanas y en la calle, nietos e hijos adolescentes empiezan a ver en la cara de sus padres y abuelos un moteado oscuro de manchas, pecas y daño solar que antes no se veía, y se lo dicen. Los mayores, que apenas perciben el color nuevo, no pueden comprobarlo en el espejo y dependen de lo que les cuentan los jóvenes. Las consultas a dermatología y farmacia pasan del miedo por los ojos a la pregunta de si esas manchas son cáncer, y la tendencia adolescente de la ''cara lavada'' se convierte en una marca de edad: la piel joven sale limpia en el color nuevo y la adulta, manchada.'
    mecanismo: 'La fotografía ultravioleta revela el daño solar acumulado porque la melanina irregular que deja la exposición absorbe mucho más UV que la piel sana, aunque en luz visible no destaque. Con la percepción UV-A ese contraste lo ve cualquiera a la luz del día. Se produce una paradoja óptica: quienes más daño acumulado tienen, los mayores, son los que menos lo ven, porque su cristalino amarillento filtra el UV (h2-02), mientras que los niños y adolescentes, con cristalino transparente, lo ven con más nitidez. El diagnóstico lo hace el nieto, no el espejo, y llega por la misma vía de los chats familiares que ya comparaba generaciones. Como nadie sabe distinguir en el canal UV una mancha benigna de una lesión, la duda se deriva a dermatología y farmacia.'
    dato: La Academia Americana de Dermatología muestra con fotos UV que la luz ultravioleta revela daño solar invisible en fotos normales, ya visible en un niño de 4 años y mucho mayor en una persona de 64.
    fuente: https://www.aad.org/public/everyday-care/sun-protection/sun-damage-skin/hidden-sun-damage
    confianza: media
    areas_afectadas:
    - salud
    - dermatologia
    - familias
    - cosmetica
    - cultura
    id: disruptor/h3/1
  - texto: Los interiores con ventanas corrientes no funcionan como refugio. En aulas, oficinas y autobuses junto a la ventana sigue habiendo deslumbramiento y colores nuevos, así que en la tercera hora la gente baja persianas y estores, enciende la luz artificial a mediodía y se aparta hacia pasillos y zonas interiores. Los colegios que metieron el recreo dentro descubren que las aulas con grandes ventanales molestan casi tanto como el patio, y el coche aparcado funciona como refugio por el parabrisas pero no por las ventanillas laterales.
    mecanismo: 'El vidrio común de ventana bloquea casi todo el UV-B pero deja pasar una gran parte del UV-A, que es justo la banda que ahora se percibe. Solo el vidrio laminado, como el de los parabrisas, o los acristalamientos con capas específicas lo cortan casi por completo. La conducta descrita en h2-04 lleva a la gente a ''espacios con techo y cristal'', pero lo que protege es el techo opaco y la distancia a la ventana, no el cristal. El resultado es un consumo de luz eléctrica a mediodía anómalo para un martes soleado y una jerarquía improvisada de espacios: el centro del edificio y el sótano valen más que la planta acristalada.'
    dato: El vidrio residencial común deja pasar entre el 45 y el 75 % del UVA; las ventanillas laterales de los coches, de vidrio templado, entre el 4 % y casi el 56 %; el parabrisas laminado bloquea el 98 %.
    fuente: https://www.uow.edu.au/media/2025/can-you-get-sunburnt-or-uv-skin-damage-through-car-or-homewindows.php
    confianza: alta
    areas_afectadas:
    - educacion
    - trabajo
    - transporte
    - energia
    - salud
    id: disruptor/h3/2
  - texto: 'Las primeras imágenes que ''muestran'' el fenómeno no salen de los móviles sino de una comunidad pequeña: fotógrafos con cámaras convertidas a espectro completo y filtros de paso UV, astrónomos aficionados y laboratorios forenses. En la tercera hora publican fotos UV-A en falso color que se viralizan justo cuando amanece en la costa este de Norteamérica. Funcionan como primera prueba visual, pero cada imagen usa un falso color distinto y ninguno coincide con lo que la gente ve, así que se abre un debate nuevo sobre cuál es el color ''verdadero'' y las cuentas escépticas las presentan como manipulaciones.'
    mecanismo: 'Los sensores de las cámaras sí registran algo de UV-A, pero los móviles llevan filtros que lo cortan (h1-06). Quien tiene una cámara a la que se ha retirado ese filtro y le pone un filtro que solo deja pasar UV, como el Baader U centrado en 350 nm, obtiene imágenes del canal UV, que hay que traducir a colores visibles mediante un balance de blancos arbitrario. Esa comunidad ya existe, sabe hacerlo en minutos y tiene incentivo para ser la primera. La foto en falso color resuelve el problema de la prueba imposible para el público que aún no ha visto el sol, pero introduce otro: como no hay forma de mostrar el color tal cual, cada traducción parece un montaje, y eso alimenta tanto la confirmación como la sospecha en el choque entre ''lo veo'' y ''es sugestión''.'
    dato: El filtro Baader U, usado en fotografía terrestre UV con cámaras convertidas, transmite una banda centrada en unos 350 nm; la fotografía UV requiere asignar falso color mediante balance de blancos.
    fuente: https://savazzi.net/photography/uv-white-balance.html
    confianza: media
    areas_afectadas:
    - medios
    - verificacion
    - ciencia
    - Norteamerica
    id: disruptor/h3/3
  - texto: 'Dermatólogos y divulgadores dan la vuelta a la mancha de la crema: lo que en la primera hora era vergüenza pasa a usarse como prueba de que la crema funciona y de dónde falta. En la tercera hora circulan vídeos de ''si no se te ve oscuro, no te protege'', la gente revisa en la ventana las zonas que se deja sin crema (orejas, cuello, párpados) y empiezan las quejas contra cremas, maquillajes con SPF y protectores baratos que apenas se oscurecen. La protección solar pasa a ser comprobable por el consumidor por primera vez.'
    mecanismo: 'Discrepo en parte de economista/h2/3. Que un filtro solar se vea oscuro en el canal UV-A es un problema estético, pero también es una verificación instantánea de cobertura y de eficacia que antes solo daban las cámaras UV que se usan en campañas dermatológicas. Los divulgadores que en h2-05 perdían la batalla contra la ''cara lavada'' necesitan un argumento que no dependa de la autoridad, y el ojo de cada uno se lo da, igual que la prueba casera de las gafas funcionó porque cada uno la repetía. El golpe para la cosmética solar se reparte: caen los productos que no pasan la prueba a simple vista y ganan los que se ven bien aplicados y uniformes.'
    dato: Los vídeos con cámara UV como 'How the sun sees you' mostraban que la crema solar aparece oscura en UV y deja ver las zonas sin cubrir.
    fuente: https://www.smithsonianmag.com/smart-news/ultraviolet-camera-reveals-secret-price-sunbathing-180952363/
    confianza: media
    areas_afectadas:
    - salud
    - cosmetica
    - consumo
    - redes
    id: disruptor/h3/4
  - texto: En el poniente de Almería y otras zonas de invernaderos, los trabajadores descubren que dentro de muchas naves no se ven los colores nuevos ni hay deslumbramiento, mientras que fuera sí. En la tercera hora los invernaderos funcionan como refugio improvisado para jornaleros y vecinos, y la pregunta de por qué ese plástico 'protege' se suma a la confusión sobre qué materiales filtran el fenómeno.
    mecanismo: Una parte de las cubiertas de invernadero que se usan en la horticultura intensiva son plásticos fotoselectivos que absorben el ultravioleta, por razones agronómicas y de control de plagas. Con el sol de mediodía, el campo de plástico concentra en poco espacio a mucha gente trabajando al aire libre que no puede irse a un centro comercial, y la nave con cubierta anti-UV le da justo lo que le falta. Como no todas las cubiertas filtran igual, unas naves 'protegen' y otras no, y esa diferencia, que el trabajador comprueba con sus ojos, refuerza la idea de que hay materiales que bloquean el fenómeno.
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - agricultura
    - trabajo
    - Espana
    id: disruptor/h3/5
  reacciona_a:
  - economista/h2/3
  - oftalmologa/h2/5
  - medios/h2/3

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
  metricas:
    alarma_social: valor
    respuesta_gobiernos: valor
    impacto_economico: valor
    adaptacion: valor
