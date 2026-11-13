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
Hora 1 (PT1H desde el suceso)
Estado del mundo anterior:
Primer tramo.

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h1
  afirmaciones:
  - texto: 'Las bolsas europeas, abiertas desde las 9:00, no se paran en bloque: siguen cotizando con volumen alto y horquillas más anchas, y solo saltan interrupciones de volatilidad en valores sueltos ligados al relato del suceso (óptica, gafas de sol, oftalmología).'
    mecanismo: Euronext no tiene un cortacircuitos para todo el mercado; sus frenos actúan valor a valor cuando el precio supera una banda respecto a la última cotización o a la apertura. Las mesas trabajan en interiores con luz artificial, donde casi no hay deslumbramiento, así que los operadores siguen activos. Ante un suceso sin precedentes y sin efecto económico medible, los creadores de mercado amplían horquillas para cubrirse en vez de retirarse. La volatilidad se concentra donde hay una historia fácil de contar, no en el índice entero.
    dato: Euronext aplica bandas dinámicas de ±3% para valores de índices principales (CAC 40, AEX, etc.) y ±5% para el resto, y bandas estáticas de ±8% y ±10%, con reservas mínimas de 3 minutos; no describe un cortacircuitos de mercado completo.
    fuente: https://www.euronext.com/en/for-investors/market-quality/trading-safeguards
    confianza: media
    evidencia: dato
    areas_afectadas:
    - mercados financieros
    - bolsa europea
    id: economista/h1/1
  - texto: EssilorLuxottica y otros valores de gafas de sol suben con fuerza en la primera hora por compras de narrativa, y el economista dice en público que la subida está sobredimensionada.
    mecanismo: 'El supuesto de deslumbramiento durante unas dos semanas crea una historia simple: todo el mundo necesitará gafas de sol. Pero un pico de demanda de dos semanas es pequeño frente a la facturación anual de un grupo de ese tamaño, y la capacidad de producción y el inventario en tienda no se multiplican en días. Si el efecto remite, el valor presente del flujo extra es reducido. Defender esto en público protege su prestigio: no se suma a una euforia que probablemente se corrija.'
    dato: EssilorLuxottica facturó 28.490 millones de euros en 2025.
    fuente: https://stockanalysis.com/quote/epa/EL/revenue/
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados financieros
    - sector óptico
    - consumo
    id: economista/h1/2
  - texto: 'El impacto en consumo durante la primera hora es muy desigual por husos horarios y estaciones: hay colas y agotamiento de gafas de sol en tiendas de zonas con sol fuerte de día (África, Oriente Medio, sur de Asia), mientras en la Europa de noviembre el efecto comercial es menor y en América casi nulo porque es de noche.'
    mecanismo: A las 10:00 de Madrid (09:00 UTC) es de día en Europa, África, Oriente Medio y gran parte de Asia, y de madrugada en América. El deslumbramiento depende de la radiación ultravioleta, que en noviembre es baja en el hemisferio norte y alta en el sur y en latitudes tropicales. La demanda inmediata aparece donde coinciden luz diurna, sol intenso y comercio abierto; en América el choque de consumo llega horas más tarde.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - comercio minorista
    - distribución
    id: economista/h1/3
  - texto: 'Aparecen los primeros aprovechados: subidas de precio oportunistas de gafas de sol en comercios y plataformas online, y anuncios de productos de filtro UV sin certificación.'
    mecanismo: Ante una demanda súbita y un producto cuyo valor el comprador no puede comprobar en el momento, el vendedor con stock tiene poder de precio inmediato. Las plataformas online permiten cambiar precios y lanzar anuncios en minutos, mucho antes de que reaccionen las autoridades de consumo. La incertidumbre sobre si el fenómeno es permanente se explota para vender protección.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - consumo
    - comercio electrónico
    - protección del consumidor
    id: economista/h1/4
  - texto: Los futuros sobre índices estadounidenses negocian con volumen inusual para la madrugada, pero el grueso de la reacción de Wall Street queda aplazado a la apertura de la tarde europea, y los mercados asiáticos de contado ya habían cerrado.
    mecanismo: 'A las 10:00 de Madrid son las 4:00 en Nueva York: la mayoría de inversores estadounidenses están dormidos y se despiertan ya con el fenómeno en marcha, así que la primera reacción en EE. UU. pasa por futuros y operadores algorítmicos que reaccionan a titulares. Tokio y otras plazas asiáticas cerraron su sesión de contado antes del suceso, de modo que su reacción llegará en la sesión siguiente con más información y, previsiblemente, menos ruido.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados financieros
    - futuros
    - bolsa estadounidense
    - bolsa asiática
    id: economista/h1/5
  reacciona_a: []
- agente: politico
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora el Gobierno de España no declara el estado de alarma: convoca un comité de crisis en Moncloa y emite una declaración de contención que reconoce el fenómeno, pide calma y no afirma que sea inocuo ni permanente.'
    mecanismo: La Ley Orgánica 4/1981 solo ampara el estado de alarma ante supuestos tasados, como crisis sanitarias o catástrofes, y exige un real decreto del Consejo de Ministros con medidas proporcionadas. A las 11:00 no hay ni daño acreditado ni un informe técnico que permita encajar el suceso en esos supuestos. Además, ningún portavoz puede decir que es seguro sin que los oftalmólogos lo respalden. Sale más barato en legitimidad decir que se tiene el control del proceso, con reuniones y expertos convocados, que comprometerse con un diagnóstico que luego habría que rectificar.
    dato: El artículo 4.b de la LO 4/1981 cita las crisis sanitarias como supuesto del estado de alarma; el artículo 6 fija una duración máxima inicial de quince días por decreto del Consejo de Ministros, con dación de cuentas al Congreso.
    fuente: https://www.boe.es/eli/es/lo/1981/06/01/4
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - gobierno
    - legitimidad
    - marco_legal
    id: politico/h1/1
  - texto: 'Las primeras medidas reales no son excepcionales: llegan por los cauces ordinarios de tráfico, protección civil y sanidad, con avisos para extremar la precaución al volante y en exteriores soleados, y emitidas por administraciones distintas que no se coordinan entre sí.'
    mecanismo: Para recomendar prudencia no hace falta ninguna base legal nueva, y el deslumbramiento en exteriores es el único efecto que los técnicos pueden respaldar desde el primer minuto. Las competencias están repartidas entre el Estado, las comunidades autónomas y los ayuntamientos, y cada administración quiere aparecer actuando antes que las demás. El resultado es un mosaico de avisos con matices distintos en la primera hora, que la oposición y los medios señalarán como descoordinación.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - trafico
    - proteccion_civil
    - coordinacion_territorial
    id: politico/h1/2
  - texto: La OMS se limita a un comunicado de seguimiento y a pedir información a los Estados. No convoca todavía el Comité de Emergencias, porque el suceso no encaja con claridad en el concepto de riesgo para la salud pública que define el Reglamento Sanitario Internacional.
    mecanismo: El RSI está pensado para la propagación internacional de enfermedades. Un cambio simultáneo y global, sin agente identificado ni daño acreditado, no encaja en el procedimiento de evaluación. Los centros nacionales de enlace disponen de un plazo para notificar y evaluar, y la Dirección General necesita sus informes antes de convocar el comité. Mientras tanto, la OMS evita adelantarse y equivocarse, como le reprocharon en crisis anteriores.
    dato: El artículo 6 del RSI (2005) obliga a los Estados a notificar a la OMS en un plazo de 24 horas desde la evaluación cualquier evento que pueda constituir una emergencia de salud pública de importancia internacional; el artículo 12 reserva al Director General la determinación de esa emergencia, previa consulta al Comité de Emergencias.
    fuente: https://www.afro.who.int/sites/default/files/2017-06/9789243580418_spa.pdf
    confianza: media
    evidencia: dato
    areas_afectadas:
    - organismos_internacionales
    - salud_publica
    id: politico/h1/3
  - texto: 'Al menos algunos líderes de otros países rompen la prudencia en la primera hora: atribuyen el fenómeno a un ataque extranjero, a una señal religiosa o a una ventaja nacional, o aseguran sin respaldo técnico que es seguro.'
    mecanismo: Que el fenómeno sea simultáneo en todo el planeta convierte la primera hora en una carrera por fijar el relato. Para un dirigente que vive de la polarización, el coste de equivocarse es menor que la ganancia de hablar primero. Esas declaraciones sin base presionan a los gobiernos prudentes, que quedan como lentos o callados, y dan munición a sus oposiciones para comparar.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - politica_internacional
    - desinformacion
    - legitimidad
    id: politico/h1/4
  - texto: En España la oposición exige una comparecencia urgente del presidente en el Congreso y acusa al Gobierno de silencio o improvisación antes de que termine la primera hora. La UE activa el intercambio de información entre Estados miembros sin adoptar todavía ninguna medida común.
    mecanismo: A la oposición le rinde cualquier hueco entre el suceso y una respuesta concreta, y una declaración de contención, sin medidas, ofrece justo ese hueco. Pedir una comparecencia es barato y obliga al Gobierno a fijar posición antes de tener informes técnicos. En Bruselas, el mecanismo de respuesta política a las crisis empieza por compartir información, porque ninguna medida común tiene aún base técnica ni competencial clara.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica_nacional
    - union_europea
    - parlamento
    id: politico/h1/5
  reacciona_a: []
- agente: medios
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora la conversación pública la ocupan las redes sociales y no los medios: millones de vídeos y fotos caseros intentan enseñar los colores nuevos y fracasan, porque las cámaras y pantallas no reproducen el UV-A como lo ve el ojo. Esa imposibilidad de enseñarlo se convierte en el propio tema viral (vídeos de reacción, gente llorando ante flores o el cielo, retos para describir el color).'
    mecanismo: Los medios serios necesitan al menos una fuente y tardan en confirmar; las redes no tienen ese freno y además son ya la vía principal de acceso a noticias para gran parte del público. El contenido emocional y de sorpresa es el que mejor se propaga, y un fenómeno que no se puede fotografiar empuja a contenidos de reacción y testimonio, no de documentación.
    dato: En EE. UU., el acceso a noticias por redes sociales y plataformas de vídeo (54 %) superó por primera vez a la televisión (50 %) en 2025.
    fuente: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/overview-and-key-findings-2025-digital-news-report
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - redes_sociales
    - medios
    - opinion_publica
    id: medios/h1/1
  - texto: 'Antes de que acabe la primera hora circulan atribuciones falsas de causa con apariencia de autoridad: experimento secreto, ataque químico o radiológico, 5G, satélites, señal extraterrestre o castigo divino, a menudo con capturas falsificadas de supuestos comunicados oficiales o de científicos.'
    mecanismo: Nadie conoce la causa, y ese vacío informativo se llena con la versión más sorprendente o amenazante, que es la que más se comparte. La falsedad se mueve más rápido que la verificación, y los verificadores llegan con horas de retraso.
    dato: Las noticias falsas se difundían significativamente más lejos, más rápido y más ampliamente que las verdaderas en Twitter; tenían un 70 % más de probabilidad de ser retuiteadas y estaban asociadas a sorpresa, miedo y asco.
    fuente: https://www.media.mit.edu/publications/the-spread-of-true-and-false-news-online/
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - desinformacion
    - redes_sociales
    - salud_publica
    - politica
    id: medios/h1/2
  - texto: Los medios generalistas abren directos y especiales informativos centrados en testimonios y en la pregunta '¿es peligroso?', con portavoces médicos improvisados (oftalmólogos locales, divulgadores) antes de cualquier declaración oficial coordinada. Los titulares priorizan el deslumbramiento y la fatiga visual, porque es lo único medible y con fuentes ya disponibles.
    mecanismo: 'Los medios compiten por ser los primeros y necesitan al menos una fuente: el testimonio de un médico de urgencias o un oftalmólogo cumple el requisito antes que un ministerio. Las molestias visuales en exteriores con sol son reales y verificables, así que son el ángulo publicable de miedo; eso amplifica la percepción de riesgo aunque el daño no sea permanente.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - salud_publica
    - opinion_publica
    id: medios/h1/3
  - texto: 'Aparecen los primeros oportunistas en la primera hora: cuentas que venden gafas o ''filtros UV'' como protección imprescindible, supuestos remedios (colirios, suplementos) y estafas que suplantan a autoridades sanitarias con enlaces a ''pruebas de visión'' o registros. Las plataformas empiezan a limitar el contenido que da consejos de salud falsos, pero el ritmo de publicación supera su capacidad de moderar.'
    mecanismo: El miedo y la incertidumbre sobre la salud crean demanda inmediata de soluciones; los estafadores reutilizan el guion que ya conocen de otras crisis. Las normas de las plataformas contra desinformación sanitaria se aplican, pero la moderación es reactiva y un evento global simultáneo satura los equipos y los sistemas automáticos, que además no tienen aún criterios para un fenómeno sin precedentes.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - desinformacion
    - consumo
    - fraude
    - plataformas
    id: medios/h1/4
  - texto: 'Surge una corriente minoritaria pero muy ruidosa de negacionismo y de acusaciones de histeria colectiva: gente que afirma no ver nada distinto o que todo es sugestión, y medios o influencers que lo amplifican por la polémica. También hay quien exagera lo contrario y atribuye al cambio poderes añadidos (ver auras, detectar enfermedades, ver lo invisible).'
    mecanismo: Percibir un color nuevo es subjetivo y no se puede demostrar con una foto, así que cada persona interpreta su experiencia con sus propios marcos; la ambigüedad favorece tanto la negación como la exageración. Ambos extremos generan indignación y debate, que es lo que más engagement da y lo que más premian los algoritmos, así que se sobrerrepresentan frente a la mayoría que simplemente describe lo que ve.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - opinion_publica
    - desinformacion
    id: medios/h1/5
  reacciona_a: []
- agente: oftalmologa
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora, las sociedades de oftalmología reciben un aluvión de consultas, y la oftalmóloga sale en los medios con una referencia clínica que nadie más tiene: las personas sin cristalino (afáquicas tras cirugía antigua de cataratas) ya percibían algo de UV-A antes del suceso. Con eso, su sociedad científica se presenta como la primera fuente que explica qué se está viendo.'
    mecanismo: En el ojo humano, el cristalino filtra casi todo el UV-A antes de que llegue a la retina, y los conos S (azules) conservan cierta sensibilidad en ese rango. Hay casos documentados de afáquicos que describen la luz UV como un tono azul blanquecino o violáceo. Ese precedente clínico es la única base empírica disponible en la hora 1, y quien la tenga a mano gana autoridad mientras los demás especulan.
    dato: Las personas a las que se ha extirpado el cristalino perciben luz ultravioleta, que describen como azul blanquecina o violeta; se cita el caso de Monet tras su cirugía de cataratas.
    fuente: https://petapixel.com/2012/04/17/the-human-eye-can-see-in-ultraviolet-when-the-lens-is-removed
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - salud
    - medios
    - comunidad_cientifica
    id: oftalmologa/h1/1
  - texto: Los pacientes operados de cataratas con lentes intraoculares que filtran el UV, y los usuarios de lentes de contacto o gafas con filtro UV, son los primeros en notar que perciben los colores nuevos de otra manera, o con menos intensidad, que quienes tienen a su lado. En la primera hora, las urgencias oftalmológicas reciben consultas por esa asimetría, a veces entre los dos ojos de la misma persona.
    mecanismo: 'Lo que un ojo percibe en UV-A depende de cuánta radiación llega a la retina. Las lentes intraoculares, los cristales y las lentillas con bloqueo UV la reducen, y quien lleva una lente así en un solo ojo ve una diferencia de color entre ambos ojos. Como el supuesto del mundo no especifica cómo interactúa el fenómeno con esos filtros, la observación inmediata es comparativa: unos ven más que otros, y el que ve menos piensa que tiene un problema.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - optica
    - consumo
    id: oftalmologa/h1/2
  - texto: En la primera hora, las ópticas y los fabricantes de gafas de sol sufren su primera confusión comercial. Hay quien se quita las gafas con filtro UV para ver los colores nuevos y quien se las pone para aliviar el deslumbramiento, y algún comercio aprovecha para anunciar gafas que «potencian» o «bloquean» la visión UV sin ninguna base.
    mecanismo: Las gafas de sol homologadas están diseñadas precisamente para bloquear el UV, de modo que ponérselas elimina la percepción nueva y además alivia la fatiga del deslumbramiento en exteriores. Esa contradicción entre ver o no ver, y entre comodidad y novedad, se resuelve en la calle antes que en ninguna guía, y abre un hueco para el oportunismo comercial.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - optica
    - regulacion_sanitaria
    id: oftalmologa/h1/3
  - texto: 'En interiores, la novedad visible en la primera hora es menor de lo que la gente espera: con iluminación LED doméstica apenas se ve nada nuevo, mientras que los fluorescentes, las lámparas de luz negra, los blanqueantes ópticos de la ropa y del papel y la luz que entra por las ventanas abiertas muestran colores nuevos. Por eso las primeras fotos y vídeos virales salen de exteriores y de comercios, no de las casas.'
    mecanismo: Que se perciba el UV-A depende de que haya UV-A en la escena. El sol emite mucho; los LED blancos habituales emiten muy poco; el vidrio de las ventanas atenúa parte del UV; los blanqueantes ópticos absorben UV y fluorescen, y las superficies con filtros solares o pigmentos que reflejan o absorben UV se diferencian de golpe. La experiencia cotidiana cambia sobre todo al aire libre y bajo determinadas fuentes de luz.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - vida_cotidiana
    - medios
    - comercio
    id: oftalmologa/h1/4
  - texto: La oftalmóloga advierte en público que el alivio del deslumbramiento no se mida por la comodidad. Aunque el fenómeno no deje daño permanente, quien mire directamente al sol o a lámparas UV para buscar los colores nuevos se expone a las lesiones de siempre (fotoqueratitis, retinopatía solar), y eso va a producir los primeros casos clínicos reales en horas.
    mecanismo: La curiosidad empuja a mirar las fuentes más intensas. El supuesto del mundo garantiza que la percepción nueva no deja daño, pero no anula la fototoxicidad conocida de mirar al sol o a fuentes UV intensas. Separar las molestias del fenómeno, que son benignas, de las lesiones por conducta, que son reales, es la línea clínica que da credibilidad a su sociedad.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - salud
    - comunicacion_publica
    id: oftalmologa/h1/5
  reacciona_a: []
- agente: adolescente
  tramo: h1
  afirmaciones:
  - texto: A las diez estoy en clase y el móvil está guardado en la mochila o en la caja del aula, así que la primera hora la vivo sin poder mirar redes; la clase se para porque la gente se pone a señalar paredes, ropa y pupitres que de repente tienen colores raros, y el profe no consigue seguir con el temario.
    mecanismo: En los institutos de Madrid el móvil no se puede usar en horario lectivo, así que la única fuente de información es lo que vemos en el aula; como todos vemos a la vez colores nuevos en cosas cotidianas (tintes de la ropa, rotuladores fluorescentes, papel blanco), nadie se puede concentrar y el profesor tampoco sabe qué decir porque a él le pasa lo mismo.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - vida_cotidiana
    id: adolescente/h1/1
  - texto: 'En cuanto alguien saca el móvil a escondidas o en el cambio de clase, mi grupo descubre que los grupos de clase y las redes ya están llenos de vídeos y fotos, y nos frustra muchísimo que en las fotos los colores nuevos no salen: el móvil no los capta y la pantalla tampoco los puede mostrar.'
    mecanismo: Las cámaras y pantallas de los móviles están hechas para los colores que veíamos antes, así que lo que se publica parece normal; eso hace que la gente compense con texto, mayúsculas, audios y vídeos de reacciones de caras sorprendidas, y que lo que se vuelve viral sean las reacciones, no las imágenes.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes_sociales
    - tecnologia
    - comunicacion
    id: adolescente/h1/2
  - texto: En el recreo, quien sale al patio a pleno sol vuelve quejándose de que le molestan los ojos, y algunos se ponen gafas de sol o se quedan dentro; a la vez, hay quien exagera y dice que se está quedando ciega para llamar la atención o para irse a casa.
    mecanismo: El deslumbramiento en exteriores con sol es real, pero nadie nos ha explicado aún que se pasa ni que no deja daño; en ese vacío, entre adolescentes exagerar un síntoma da protagonismo en el grupo y es una excusa perfecta para pedir que te recojan tus padres.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - salud
    - educacion
    - familias
    id: adolescente/h1/3
  - texto: Mis padres y los de mis amigas empiezan a mandar mensajes y a llamar a secretaría preguntando si estamos bien y si nos pueden sacar del instituto, y el centro no sabe qué contestar porque no hay ninguna instrucción oficial todavía.
    mecanismo: Los adultos se enteran por la radio, la tele o el trabajo de que es algo de todo el planeta y su reflejo es saber dónde están sus hijos; como el instituto depende de indicaciones de la Consejería y en una hora no ha llegado ninguna, cada profesor improvisa y unos dejan usar el móvil para tranquilizar a casa y otros no.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - familias
    - educacion
    - administracion
    id: adolescente/h1/4
  - texto: Mi grupo y yo ya estamos buscando qué cosas de nuestra ropa, maquillaje o mochilas brillan con los colores nuevos, y empezamos a competir por quién tiene la prenda que más llama la atención, con la idea de subirlo en cuanto salgamos.
    mecanismo: Encajar y ganar atención en el grupo depende de ser la primera en tener algo distinto; los tintes, blanqueantes de la ropa y algunos cosméticos se ven ahora de otra manera, así que lo que ayer era ropa normal hoy puede ser lo más llamativo de la clase, y quien lo descubre antes gana estatus.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - moda
    - redes_sociales
    - consumo
    id: adolescente/h1/5
  reacciona_a: []
- agente: agitador
  tramo: h1
  afirmaciones:
  - texto: En los primeros veinte o treinta minutos, el agitador abre un directo en su canal de mensajería y en una red de vídeo sin guion ni comprobación. Encuadra el suceso como algo que alguien está ocultando, no como un fenómeno natural, y pide a su audiencia que mande vídeos de lo que ve.
    mecanismo: Su negocio vive de llegar el primero cuando aún no hay explicación oficial. En la primera hora ningún organismo puede dar la causa, porque nadie la conoce. Ese vacío lo rellena quien publica antes, y las versiones de culpables corren más que las aclaraciones. Pedir vídeos a la audiencia le da material gratis y hace que sus seguidores se sientan partícipes, lo que dispara los reenvíos.
    dato: En Twitter, las noticias falsas tenían un 70 % más de probabilidad de ser retuiteadas que las verdaderas, y las verdaderas tardaban unas seis veces más en llegar a 1.500 personas.
    fuente: https://news.mit.edu/2018/study-twitter-false-news-travels-faster-true-stories-0308
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - informacion
    - redes_sociales
    - confianza_institucional
    id: agitador/h1/1
  - texto: 'El agitador junta los vídeos que le mandan: superficies, billetes, señales y ropa que de pronto muestran marcas o patrones nuevos en UV. Los presenta como pruebas de que había cosas marcadas a propósito para que no las viéramos. Con eso aparece una narrativa de ''marcas ocultas'' que señala vagamente a gobiernos y grandes empresas.'
    mecanismo: 'Con visión UV-A, la gente ve de golpe elementos fluorescentes o con tintes UV que siempre estuvieron ahí: medidas de seguridad en billetes y documentos, abrillantadores ópticos en la ropa y el papel, manchas y residuos. Su audiencia no sabe por qué están, y el agitador convierte esa falta de contexto en intención oculta. A él le basta con que las imágenes sean reales para que el relato resulte creíble.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - informacion
    - confianza_institucional
    - sistema_financiero_percepcion
    - comercio
    id: agitador/h1/2
  - texto: Antes de que acabe la hora, el agitador lleva el tráfico principal a su canal propio de mensajería y deja solo fragmentos suavizados en las plataformas grandes. Así la versión más dura se mueve en un espacio donde no hay moderación de contenido.
    mecanismo: Sabe que las plataformas grandes pueden retirar o desmonetizar contenido sobre una emergencia sanitaria o de salud pública. En la primera hora las plataformas todavía no han fijado criterios de moderación, pero él se adelanta para que no le corten el alcance cuando lleguen. Su canal propio no se puede desmonetizar desde fuera y conserva la audiencia aunque le borren vídeos.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - redes_sociales
    - moderacion_contenidos
    - ecosistema_informativo
    id: agitador/h1/3
  - texto: El agitador conecta el deslumbramiento y la fatiga visual en exteriores con la idea de que 'algo nos han hecho'. Pide a su audiencia que no se fíe de lo que digan médicos y autoridades en las próximas horas. Con eso blinda su relato contra la explicación oficial antes de que esa explicación exista.
    mecanismo: El malestar físico es real y lo nota todo el mundo a la vez, así que la gente ya cree en el síntoma antes de oír relato alguno. Desacreditar de antemano a las fuentes institucionales protege su negocio, porque pierde audiencia si el fenómeno se explica y se normaliza. Cualquier aviso oficial que llegue luego, como no mirar al sol, lo podrá presentar como confirmación de que había algo que esconder.
    dato: En TikTok y otras redes de vídeo, los usuarios prestan más atención a personalidades e influencers que a periodistas y medios a la hora de informarse.
    fuente: https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2024/dnr-executive-summary
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud_publica
    - confianza_institucional
    - comunicacion_de_crisis
    id: agitador/h1/4
  - texto: En esta primera hora, el agitador gana muchos seguidores y activa donaciones y suscripciones de pago durante el directo. Varios creadores más pequeños copian su encuadre para aprovechar el tirón, y la tesis de las 'marcas ocultas' se convierte en una de las narrativas dominantes del suceso en redes en su idioma.
    mecanismo: En un suceso global sin explicación, la demanda de contenido se dispara y la oferta verificada todavía no existe. Las plataformas premian la interacción y los creadores pequeños imitan lo que ya funciona. Él se beneficia directamente del miedo, porque las donaciones en directo responden a la sensación de urgencia y de pertenencia a un grupo que 've la verdad'.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - economia_creadores
    - ecosistema_informativo
    id: agitador/h1/5
  reacciona_a: []
- agente: disruptor
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora, en las zonas donde es de día (Europa, África, Oriente Medio, sur de Asia), mucha gente cree que quienes la rodean han enfermado de la piel, no que ha cambiado su propia vista: aparecen en caras y manos de adolescentes y adultos manchas, pecas y moteados que antes no se veían, mientras los bebés se ven uniformes.'
    mecanismo: La visión en UV-A resalta la pigmentación irregular causada por exposiciones solares pasadas, que en luz visible apenas se nota. Como el cambio está en el observador y no en el observado, y nadie conoce la causa, la intuición inmediata es atribuir lo nuevo al otro (algo le ha salido) y no a uno mismo. Eso produce un primer pico de consultas médicas, mensajes alarmados en grupos familiares y rumores de contagio o de quemadura por el propio fenómeno antes de que se entienda que nada ha cambiado en la piel.
    dato: Las imágenes con cámara UV muestran la pigmentación moteada como señal de daño UV acumulado en zonas expuestas como cara y manos; bebés y niños pequeños suelen verse uniformes y los adolescentes ya muestran irregularidades claras.
    fuente: https://nivea.co.uk/highlights/uv-sun-camera
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - sanidad_primaria
    - redes_sociales
    - percepcion_social
    id: disruptor/h1/1
  - texto: 'Quien lleva protector solar o maquillaje con SPF aparece ante los demás con una máscara: oscura si el filtro es químico, clara o casi blanca si es mineral. En la primera hora esto genera escenas de desconcierto en oficinas, colegios y transporte, y las primeras imágenes descritas en redes hablan de caras negras o pintadas.'
    mecanismo: Los filtros químicos absorben el UV y se ven oscuros en UV; los físicos lo reflejan y se ven claros. Las zonas mal cubiertas quedan como huecos en la máscara. Como el protector diario y las bases con SPF son habituales, una parte de la población se vuelve de golpe visiblemente distinta del resto, y alguien interpretará la diferencia en clave estética, de clase o incluso racial, lo que abre una fricción social que nadie había previsto para un fenómeno óptico.
    dato: Los protectores con filtros químicos absorben el UV y aparecen oscuros en imagen UV; los de filtros físicos lo reflejan y la piel protegida se ve más clara, a veces casi blanca.
    fuente: https://nivea.co.uk/highlights/uv-sun-camera
    confianza: media
    evidencia: dato
    areas_afectadas:
    - cosmetica
    - percepcion_social
    - redes_sociales
    - trabajo
    id: disruptor/h1/2
  - texto: 'El riesgo vial de la primera hora no se reparte por igual: los conductores de turismos que miran al frente sufren mucho menos deslumbramiento UV que motoristas, ciclistas y peatones, y la mayor confusión dentro del coche aparece al mirar por las ventanillas laterales, por ejemplo en cambios de carril e incorporaciones.'
    mecanismo: El parabrisas laminado bloquea casi todo el UV-A, así que a través de él el mundo se ve casi como antes; las ventanillas laterales dejan pasar bastante más, de modo que al girar la cabeza el conductor salta entre dos paletas de color y dos niveles de brillo. Quien no tiene cristal delante (moto, bici, a pie) recibe el deslumbramiento completo en exteriores soleados. La narrativa de accidentes en general ignora esta asimetría, que concentra el daño en los usuarios vulnerables y en maniobras laterales.
    dato: En un estudio con 29 coches, el parabrisas bloqueaba de media el 96 % del UV-A y las ventanillas laterales el 71 %; solo 4 de los 29 coches superaban el 90 % de bloqueo en la ventanilla lateral.
    fuente: https://www.sciencedaily.com/releases/2016/05/160512124928.htm
    confianza: media
    evidencia: dato
    areas_afectadas:
    - trafico
    - seguridad_vial
    - emergencias
    - movilidad
    id: disruptor/h1/3
  - texto: Las fotos y vídeos que la gente sube en la primera hora no muestran lo que ve, y eso alimenta enseguida una corriente que lo tacha de alucinación colectiva o montaje, mientras otros intentan describir con palabras colores que no tienen nombre.
    mecanismo: 'Los sensores de móviles y cámaras están diseñados y filtrados para la luz visible, y las pantallas solo emiten en ese rango; aunque el sensor captara algo de UV, la pantalla no puede reproducirlo. No hay ningún observador de control sin el cambio con quien comparar, así que la prueba visual habitual de internet no funciona. Esa falta de prueba compartible es terreno fértil para quien exagera o se aprovecha: vendedores de gafas, gurús y cuentas que buscan viralidad con explicaciones inventadas.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - redes_sociales
    - desinformacion
    - lenguaje
    id: disruptor/h1/4
  - texto: En las zonas donde es de noche (América, de madrugada), los locales y aparatos que usan luz negra o lámparas UV-A —discotecas, bares, lámparas de uñas, detectores de billetes, matamosquitos— pasan de ser luz tenue a fuentes deslumbrantes, y lo que esa luz hace visible deja de ser un efecto decorativo para convertirse en algo que todos ven.
    mecanismo: Esas lámparas emiten la mayor parte de su energía en UV-A precisamente porque era invisible; ahora se perciben a toda su intensidad. En un local a oscuras, con pupilas dilatadas, eso produce molestias y salidas en masa, y deja a la vista manchas, marcas de seguridad con tinta invisible y sellos de entrada que nadie esperaba que fueran visibles. El primer efecto económico del suceso no está en los mercados, sino en el ocio nocturno americano a esa hora.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - ocio_nocturno
    - seguridad
    - comercio
    - privacidad
    id: disruptor/h1/5
  reacciona_a: []

## Tu tarea
1. Decide qué afirmaciones pasan a ser hechos establecidos. Solo entran las que tienen mecanismo plausible y no contradicen el canon anterior ni los supuestos. Combina las que dicen lo mismo y cita todos sus ids en origen.
2. Cuando dos afirmaciones choquen, decide según tus criterios y explica el motivo. Si no se puede decidir, deja la cuestión como tensión abierta.
3. Busca efectos cruzados: si una afirmación de un área cambia lo que dice otra, recógelo en el resumen.
4. Escribe un resumen de tres o cuatro frases que cualquier agente pueda leer.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

estado_del_mundo:
  tramo: h1
  resumen: "..."
  hechos_establecidos:
    - id: h1-01
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
