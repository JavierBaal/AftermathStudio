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
Hora 5 (PT5H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h3
  resumen: 'En la tercera hora los gobiernos recuperan la voz: el español hace suya la explicación oftalmológica, la OMS desmiente los comunicados falsos sin declarar emergencia y la primera acción coercitiva europea va contra el fraude de gafas, pero en redes circula sobre todo el corte de la respuesta sobre defensa y la oposición exige comparecencias. La teoría de la ocultación se funde en las redes conspirativas de siempre, aunque aparece un contraargumento con fuerza: los ancianos operados sin filtro ven mejor que sus nietos, y los adolescentes viven la diferencia por edad como orgullo y no como amenaza. Al amanecer en Norteamérica la experiencia directa desarma la ''histeria colectiva'' y las primeras fotos UV en falso color dan una prueba visual que abre otra disputa. Como efecto cruzado, el canal nuevo vuelve visible la piel: el daño solar de los adultos y la crema mal aplicada, lo que parte por edad la moda de la cara lavada y convierte la protección solar en algo que el consumidor
    comprueba; a la vez se descubre que el cristal corriente no protege y que la oferta de gafas se estrecha por la retirada de anuncios y por la demanda de las empresas.'
  hechos_establecidos:
  - id: h3-01
    texto: 'En la rueda de prensa del Consejo de Ministros, entre las 12:00 y las 13:00, la portavoz comparece con la ministra de Sanidad y no con Defensa. El Gobierno adopta el guion de las sociedades de oftalmología (la prueba de quitarse las gafas, que mayores y operados de cataratas ven menos por razones del ojo) y pide que nadie solicite cambiar su lente intraocular ni deje la crema y las gafas. Sobre defensa repite ''no hay indicios de acción hostil'' y remite al ministerio. Lo que circula no es el mensaje sanitario sino cortes de diez a quince segundos: la respuesta evasiva sobre si el Gobierno sabía algo, que refuerza el relato de ocultación, y la petición de usar crema y gafas, que los adolescentes convierten en meme y coletilla. La explicación oficial sobre la edad existe, pero apenas llega.'
    origen:
    - politico/h3/1
    - medios/h3/2
    - adolescente/h3/1
  - id: h3-02
    texto: 'Hacia las 12:40 de Madrid amanece en la costa este de Estados Unidos, con el sol bajo justo en la hora punta. Los gobernadores, los departamentos de transporte estatales y los distritos escolares aplican sus protocolos de incidencia meteorológica (retrasos de apertura, avisos de conducción), y la Casa Blanca mantiene la calma pero abandona la idea de histeria colectiva. Los magacines matinales salen en directo y el clip más compartido del mundo es el de un comentarista escéptico que se queda sin palabras al mirar al cielo. El escepticismo norteamericano no desaparece, cambia de argumento: ya no niega el fenómeno, culpa a los medios de contagiar la alarma. La brecha transatlántica de credibilidad se cierra por la vía de los gobiernos locales.'
    origen:
    - politico/h3/3
    - medios/h3/1
  - id: h3-03
    texto: 'La teoría de la ocultación se funde en un relato único que difunden sobre todo redes conspirativas ya existentes (antivacunas, chemtrails, 5G) desde Telegram y canales de vídeo hacia los grupos familiares: el cielo distinto como prueba de que ''han echado algo'', la diferencia entre abuelos y nietos como cambio dirigido, la frase de defensa como confesión y las ópticas como beneficiarias. A la vez surgen dos fuerzas en contra. Los oftalmólogos difunden el caso de los ancianos operados de cataratas antes de mediados de los ochenta, con lentes sin filtro UV o sin lente, que ven los colores nuevos con más intensidad que sus nietos, junto a la historia de Monet, lo que invierte la lectura generacional. Y entre los adolescentes la diferencia por edad no se vive como amenaza sino como estatus: se presentan como ''la generación que lo ve'' y hacen de traductores para sus abuelos.'
    origen:
    - medios/h3/3
    - oftalmologa/h3/1
    - adolescente/h3/2
  - id: h3-04
    texto: 'Las sociedades de oftalmología fijan a mediodía que no se recambiará ninguna lente intraocular para recuperar los colores nuevos, por el riesgo quirúrgico frente a un beneficio que nadie sabe si es permanente. Los operados con lente con filtro pasan de la pregunta a la queja, con un discurso de agravio (''a nosotros nos lo han quitado''), y alguna clínica privada extranjera insinúa en redes que podría hacerlo. Los pacientes con cataratas leves empiezan a pedir que se aplace su cirugía para no perder el color nuevo, lo que resta actividad a las clínicas a corto plazo. Alcon y Carl Zeiss Meditec viven una sesión volátil sin dirección clara: el mercado no compra una ola de recambios.'
    origen:
    - oftalmologa/h3/2
    - economista/h3/3
  - id: h3-05
    texto: 'El cristal corriente no protege: el vidrio de ventana deja pasar buena parte del UV-A y solo el laminado de los parabrisas lo corta casi del todo. En aulas, oficinas y autobuses junto a la ventana sigue el deslumbramiento, así que se bajan persianas, se enciende la luz artificial a mediodía y la gente se aparta hacia pasillos, sótanos y el centro de los edificios. Los colegios que metieron el recreo dentro ven a los alumnos amontonarse en las ventanas y los profesores bajan las persianas. En el coche el parabrisas protege pero las ventanillas laterales no, y el consejo de tráfico pasa a ser ventanillas subidas y gafas UV400 también dentro del vehículo; motoristas, ciclistas y repartidores son los más expuestos.'
    origen:
    - disruptor/h3/2
    - oftalmologa/h3/3
    - adolescente/h3/5
  - id: h3-06
    texto: 'El canal UV-A vuelve visible la piel. En los adultos aparece un moteado de manchas y daño solar acumulado que antes no se veía; como los mayores apenas perciben el color nuevo, se enteran porque se lo dicen hijos y nietos, y las consultas a dermatología y farmacia pasan de los ojos a la pregunta de si esas manchas son cáncer. La moda de la cara lavada se parte por edad: los adolescentes la mantienen y muchos adultos vuelven a la crema o al maquillaje. Además la crema solar se ve oscura y deja ver dónde falta, de modo que los divulgadores ganan un argumento que no depende de su autoridad, la gente revisa orejas, cuello y párpados y empiezan las quejas contra cremas y maquillajes con SPF que apenas se oscurecen. La protección solar pasa a ser comprobable por el consumidor.'
    origen:
    - disruptor/h3/1
    - medios/h3/4
    - disruptor/h3/4
  - id: h3-07
    texto: 'La primera acción coercitiva de los gobiernos europeos va contra el fraude y no contra el fenómeno: Consumo y las autoridades de vigilancia del mercado anuncian controles a gafas sin marcado CE ni filtro real y requerimientos a los marketplaces, y las policías avisan de dominios y apps fraudulentos. Los marketplaces retiran en bloque anuncios dudosos y Google y las plataformas publicitarias aplican sus políticas de eventos sensibles. El fraude se desplaza al contenido orgánico, las tiendas dentro de las redes y Telegram. La oferta se estrecha por dos lados: la retirada elimina anuncios sin que haya inventario homologado que los sustituya, y las empresas con plantillas al aire libre piden gafas de protección laboral en bloque, por la obligación de prevención de riesgos, a distribuidores de EPI que reservan existencias para sus clientes con contrato. El precio de las gafas que quedan sube en lugar de bajar.'
    origen:
    - politico/h3/2
    - economista/h3/5
    - medios/h3/5
    - economista/h3/1
  - id: h3-08
    texto: Las primeras imágenes que 'muestran' el fenómeno salen de fotógrafos con cámaras convertidas y filtros UV, astrónomos aficionados y laboratorios, que publican fotos UV-A en falso color y se viralizan justo al amanecer en Norteamérica. Sirven como primera prueba visual para quien aún no ha visto el sol, pero cada imagen usa un falso color distinto y ninguno coincide con lo que la gente ve, así que se abre un debate sobre cuál es el color 'verdadero' y las cuentas escépticas las presentan como montajes.
    origen:
    - disruptor/h3/3
  - id: h3-09
    texto: La OMS publica una declaración formal que desautoriza los comunicados falsos con su logotipo, dice que no tiene constancia de daño ocular permanente y que vigila el fenómeno con los Estados, pero no convoca el comité de emergencias del Reglamento Sanitario Internacional ni declara una emergencia de salud pública de importancia internacional, porque no hay enfermedad ni propagación.
    origen:
    - politico/h3/5
  - id: h3-10
    texto: Los partidos de la oposición en España y otros países europeos piden la comparecencia urgente del jefe de Gobierno y del ministro de Defensa sobre qué se sabía y quién evaluó la hipótesis de un ataque. Los partidos grandes piden transparencia sin respaldar teorías, mientras formaciones y figuras populistas amplifican en redes la idea de que ópticas y gobiernos 'lo sabían'. El asunto entra en la agenda parlamentaria.
    origen:
    - politico/h3/4
  tensiones_abiertas:
  - Queda por ver si el contraargumento de los ancianos operados sin filtro frena la teoría del cambio dirigido o si las redes conspirativas lo absorben como una pieza más.
  - Queda por ver si el agravio de los operados con lente con filtro encuentra salida en clínicas extranjeras que ofrezcan el recambio y qué responden las autoridades sanitarias.
  - Queda por ver qué ocurre en la apertura de Wall Street, a las 15:30 de Madrid, ahora que Norteamérica ha visto el fenómeno, y si el ajuste sigue en las opciones o pasa al contado.
  - Queda por ver si quitarse las gafas y la crema para ver el color nuevo produce un aumento visible de consultas por fatiga visual, cefaleas o quemaduras, sobre todo entre adolescentes y en las regiones con UV alto.
  - Queda por ver si la visión UV-A deja a la vista marcas antiguas en la piel, como moratones o lesiones, y qué efecto tendría en colegios, servicios sociales y atención a la violencia. Sigue sin base suficiente para establecerlo.
  - Queda por ver qué materiales filtran el fenómeno (cristales, gafas graduadas, lentillas, plásticos) y si esa confusión alimenta nuevos bulos o un mercado de láminas y recubrimientos.
  - Queda por ver cuándo y cómo comparecen los jefes de Gobierno y los ministros de Defensa, y si dicen algo más sobre las evaluaciones secretas.
  contradicciones_resueltas:
  - entre:
    - politico/h3/1
    - medios/h3/2
    decision: La rueda de prensa sí incluye la explicación de la edad y las lentes intraoculares, pero lo que circula son los cortes sobre defensa y sobre la crema, así que la explicación oficial apenas llega.
    motivo: 'El mecanismo del político es más sólido: el guion de las sociedades científicas ya estaba probado (h2-01) y la petición sobre las lentes es coherente con la posición de oftalmologa/h3/2. El argumento de medios sobre la circulación de cortes es plausible y se conserva, pero su afirmación de que la intervención omite la edad no tiene dato.'
  - entre:
    - disruptor/h3/4
    - economista/h2/3
    decision: 'Se matiza h2-08: el golpe a la cosmética solar no es uniforme. La crema visible pasa a ser también una prueba de eficacia y caen sobre todo los productos que no la superan a simple vista.'
    motivo: El disruptor aporta un mecanismo con dato sobre la crema oscura en UV como verificación de cobertura, que añade una consecuencia nueva sin anular la caída sectorial ya establecida.
  - entre:
    - medios/h3/4
    - disruptor/h3/1
    - adolescente/h2/4
    decision: 'Se matiza h2-05: la cara lavada se mantiene entre adolescentes pero muchos adultos vuelven a la crema o al maquillaje.'
    motivo: Medios y disruptor aportan mecanismo y dato sobre el daño solar acumulado visible en UV, que depende de la edad. No contradice la tendencia adolescente, la limita.
  - entre:
    - disruptor/h3/2
    - oftalmologa/h3/3
    decision: 'Se matiza h2-04: los espacios cerrados protegen por el techo opaco y la distancia a la ventana, no por el cristal, y el coche solo protege por el parabrisas.'
    motivo: Ambas afirmaciones tienen confianza alta y datos de transmisión UV-A coherentes entre sí (vidrio común y ventanillas laterales frente al parabrisas laminado).
  - entre:
    - economista/h3/3
    - oftalmologa/h3/2
    decision: No hay negocio inmediato de recambio de lentes; el efecto a corto plazo es de aplazamientos y agravio.
    motivo: Ambos coinciden en que explantar una lente no se va a ofrecer por riesgo clínico, lo que cierra la puerta abierta en h2-02 sobre si se podía cambiar la lente.
  descartadas:
  - id: economista/h3/2
    motivo: Tiene mecanismo y dato, pero es un efecto sectorial y regional sobre el reparto a domicilio que no cambia el rumbo de otras áreas. Con el límite de diez hechos cede ante efectos de más alcance.
  - id: economista/h3/4
    motivo: Tiene confianza baja y no aporta dato. Queda recogido en la tensión sobre la apertura de Wall Street.
  - id: oftalmologa/h3/4
    motivo: Concreta la prueba casera de h2-01 sin añadir una consecuencia nueva para otras áreas y no aporta dato. La confusión sobre materiales queda como tensión abierta.
  - id: oftalmologa/h3/5
    motivo: Es un cambio de protocolo clínico local y de detalle, sin dato, que no altera el rumbo de otras áreas.
  - id: adolescente/h3/3
    motivo: Es un efecto escolar de detalle sin dato. Queda recogido en la tensión sobre la exposición y las consultas por fatiga y cefaleas.
  - id: adolescente/h3/4
    motivo: Tiene confianza baja y no aporta dato. La posible visibilidad de marcas antiguas en la piel sigue como tensión abierta.
  - id: disruptor/h3/5
    motivo: Tiene confianza baja, no aporta dato sobre la transmisión UV-A de las cubiertas y es un efecto local. La confusión sobre materiales queda como tensión abierta.
  metricas:
    alarma_social: 3
    respuesta_gobiernos: comunicacion
    impacto_economico: 2
    adaptacion: 2

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h5
  afirmaciones:
  - texto: Entre las 13:00 y las 15:00, los instaladores de lámina solar para ventanas en España y el resto de Europa reciben una avalancha de peticiones de presupuesto de oficinas, colegios concertados y privados, clínicas y comercios con escaparate. Las agendas de instalación se llenan para semanas, el precio del servicio sube y los rollos de lámina para colocar uno mismo se agotan en las grandes superficies de bricolaje y en la venta en línea. En el preapertura de Wall Street, los fabricantes cotizados de lámina (3M, Eastman con su marca LLumar) suben.
    mecanismo: 'El cristal corriente deja pasar el UV-A (h3-05) y la solución que se ha improvisado, bajar persianas y encender la luz, sacrifica el espacio más caro del edificio, el que da a fachada. Para quien gestiona un edificio, la lámina anti-UV es la forma más barata y rápida de recuperar esas mesas y aulas sin obra: no hay que cambiar ventanas, se pega sobre el vidrio existente y bloquea casi todo el UV-A. El cuello de botella no es el material sino la mano de obra: hay pocos instaladores especializados y no se forman en una tarde, así que el ajuste llega por precio y por plazo, igual que con las gafas. El que no consigue instalador compra el rollo para hacerlo él mismo, y ese canal minorista, pequeño y sin reposición rápida, se vacía primero. El mercado estadounidense, que abre con cinco horas de ventaja informativa sobre Europa, tiene ya en la mesa un producto concreto con fabricantes cotizados a los que asignarle la demanda.'
    dato: Las láminas para ventana con el sello de la Skin Cancer Foundation deben demostrar que bloquean el 99 % o más del UV-A y el UV-B solar; el vidrio corriente filtra casi todo el UV-B pero deja pasar el UV-A.
    fuente: https://skincancer.org/windowfilm
    confianza: media
    areas_afectadas:
    - mercados
    - consumo
    - vivienda_y_edificios
    - educacion
    - empleo
    id: economista/h5/1
  - texto: 'Por la tarde, Beiersdorf y L''Oréal recuperan buena parte de lo que perdieron en la segunda hora, y dentro del sector se abre una dispersión: suben los fabricantes de filtros UV-A (dsm-firmenich, BASF) y las marcas de protección solar de farmacia con filtros de amplio espectro, mientras que las marcas baratas y los maquillajes con SPF señalados en redes por ''no oscurecerse'' pierden ventas en el lineal.'
    mecanismo: 'Corrijo mi propia lectura de economista/h2/3 y coincido con disruptor/h3/4. En la segunda hora el mercado descontó un coste estético: nadie querría llevar una mancha oscura en la cara. Pero al hacerse visible, la crema solar deja de ser un bien de confianza, cuya eficacia el consumidor no puede comprobar, y pasa a ser un bien que se verifica a simple vista. Eso no hunde la categoría: la ordena por calidad. La demanda se desplaza hacia los productos que demuestran protección UV-A en el espejo y en los ojos de los hijos (h3-06), y a la vez los adultos que descubren su daño solar vuelven a la crema. Los filtros UV-A eficaces salen de un puñado de proveedores químicos con moléculas patentadas y procesos de aprobación larguísimos, así que el analista ve en ellos el cuello de botella de la reformulación y les asigna el poder de precio, no a las marcas.'
    dato: La FDA autorizó en Estados Unidos el primer filtro UV nuevo en 27 años, una molécula de BASF y dsm-firmenich, lo que ilustra lo concentrado y lento que es el mercado de filtros.
    fuente: https://www.perfumerflavorist.com/home/news/22968559/basf-and-dsmfirmenich-score-major-win-as-fda-clears-first-new-uv-filter-in-27-years
    confianza: media
    areas_afectadas:
    - mercados
    - consumo
    - salud
    - cosmetica
    id: economista/h5/2
  - texto: 'A las 15:00 de Madrid, en el preapertura de Wall Street, los valores estadounidenses no se mueven como un bloque sino copiando el mapa sectorial que Europa trazó por la mañana: suben los minoristas de óptica y los fabricantes de equipos de protección individual y de lámina, las aerolíneas bajan poco y los valores de cosmética solar llegan ya con la lectura corregida. Los índices abren con una corrección moderada y sin la sobrerreacción inicial que tuvo Europa.'
    mecanismo: 'Discrepo de la idea de que Estados Unidos vaya a repetir el susto europeo al ver el sol (medios/h3/1, h3-02). Cuando abre Nueva York, los analistas de las mesas americanas llevan cinco horas viendo cómo cotizaba Europa sector por sector, con notas de sus colegas de Londres ya escritas. El primer impulso del inversor es trasladar ese guion a los equivalentes estadounidenses, que es más rápido que analizar desde cero, y la experiencia europea ya ha mostrado lo que sobró: el hundimiento general no llegó, la volatilidad se pagó en opciones (economista/h2/1) y la cosmética solar se ha dado la vuelta. Ver el fenómeno con los propios ojos convence de que es real, pero no añade información sobre su coste económico, que ya está estimado en Europa.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados
    - finanzas
    id: economista/h5/3
  - texto: 'Las aseguradoras de salud privadas en España y las cadenas de dermatología ven saturadas sus aplicaciones de cita para dermatología, y la teledermatología por fotos no sirve para filtrar: los médicos no pueden ver en la foto lo que el paciente ve en su piel, así que derivan a consulta presencial. Las listas de espera se alargan de golpe y la farmacia se convierte en el primer filtro, con consultas largas que no siempre acaban en venta.'
    mecanismo: 'Es un choque de demanda sobre una oferta fija: el número de dermatólogos no cambia en una tarde y las preguntas por manchas que podrían ser cáncer (h3-06) llegan a la vez en todo el país. La teledermatología, que las aseguradoras promocionan precisamente para descongestionar consultas, depende de la foto del móvil, y el móvil lleva filtros que cortan el UV-A (h1-06): la mancha que alarma al nieto no aparece en la imagen. El médico, por prudencia y responsabilidad, no puede descartar a distancia algo que no ve, así que el canal barato se cierra y toda la demanda va al canal caro y escaso. El ajuste se hace por espera y no por precio, porque las primas y los copagos están fijados de antemano.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - seguros
    - consumo
    id: economista/h5/4
  - texto: La luz eléctrica encendida a mediodía en oficinas, aulas y comercios aparece en la curva de demanda de Red Eléctrica como un repunte visible respecto a un martes normal de noviembre, pero no mueve el precio de la electricidad en España ni pone en riesgo el suministro.
    mecanismo: Discrepo de que el consumo anómalo de luz (disruptor/h3/2) tenga coste económico relevante. La iluminación es una fracción pequeña de la demanda eléctrica y el repunte cae justo en las horas centrales del día, cuando la solar fotovoltaica cubre buena parte del sistema y el precio mayorista español suele estar en mínimos, a veces cero. La generación solar no se ve afectada porque el fenómeno está en los ojos y no en la radiación. El sistema absorbe el pico con la energía más barata de la jornada, de modo que el efecto se ve en el gráfico y no en la factura.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - energia
    - mercados
    id: economista/h5/5
  reacciona_a:
  - disruptor/h3/4
  - disruptor/h3/2
  - medios/h3/1
- agente: politico
  tramo: h5
  afirmaciones:
  - texto: 'Entre las 13:00 y las 15:00 el Gobierno español no espera a que la Mesa del Congreso tramite las peticiones de la oposición: el Ministerio de Defensa registra una solicitud de comparecencia a petición propia, sin fecha cerrada, y ofrece informar de las evaluaciones de seguridad a puerta cerrada en la comisión que controla los gastos reservados (la llamada Comisión de Secretos Oficiales). Los portavoces de los partidos grandes aceptan el formato; las formaciones populistas que no tienen asiento en esa comisión lo denuncian en redes como ''más secreto''.'
    mecanismo: 'Pedir la comparecencia a petición propia es la forma clásica de quitarle la iniciativa a la oposición: el Gobierno controla el calendario y el formato en lugar de que se lo impongan. La comisión a puerta cerrada resuelve el dilema de h3-01, porque permite compartir las evaluaciones con los partidos con aspiración de gobierno sin desclasificarlas ni contradecir a la OTAN, y los convierte en corresponsables del silencio. El coste es que la sesión secreta confirma, otra vez, que hay algo que no se cuenta, y quien queda fuera de la sala gana el argumento ante su audiencia.'
    dato: La ministra de Defensa ya ha comparecido ante la Comisión de Secretos Oficiales del Congreso, que sesiona a puerta cerrada, citada por la presidencia de la Cámara.
    fuente: https://www.democrata.es/politica/congreso-y-senado/armengol-cita-a-robles-ante-la-comision-de-secretos-el-dia-6-y-deja-fuera-a-la-directora-del-cni/
    confianza: media
    areas_afectadas:
    - politica
    - defensa
    - parlamento
    - desinformacion
    id: politico/h5/1
  - texto: 'La Comisión Europea convoca por videoconferencia el Comité de Seguridad Sanitaria con los Estados miembros, y de esa reunión sale el primer mensaje común europeo: una pauta de comunicación de riesgo compartida (gafas UV400 con marcado CE, no recambiar lentes intraoculares, el cristal corriente no protege, crema solar) que cada ministerio adapta y difunde. No hay medidas comunes vinculantes ni cierre de nada.'
    mecanismo: 'El IPCR en modo de intercambio de información (h2) no produce mensajes para el público, y cada ministerio de Sanidad ha improvisado el suyo. El Reglamento europeo de amenazas transfronterizas graves para la salud incluye las amenazas de origen desconocido, así que la Comisión tiene base para convocar el Comité sin decir qué es el fenómeno ni declarar emergencia, igual que la OMS en h3-09. Coordinar la comunicación es la herramienta más barata y menos arriesgada de Bruselas, y responde a un problema visible: mensajes nacionales que se contradicen en las mismas redes.'
    dato: El Reglamento (UE) 2022/2371 se aplica a las amenazas transfronterizas graves para la salud de origen biológico, químico, medioambiental o desconocido, y el Comité de Seguridad Sanitaria coordina la comunicación de riesgos entre Estados.
    fuente: https://eur-lex.europa.eu/eli/reg/2022/2371/oj
    confianza: media
    areas_afectadas:
    - union-europea
    - sanidad
    - comunicacion-publica
    id: politico/h5/2
  - texto: 'Ante las clínicas extranjeras que insinúan que harán el recambio de lente, el Ministerio de Sanidad y los colegios de médicos emiten una advertencia contra el ''turismo quirúrgico'' para recuperar los colores nuevos, pero no anuncian ninguna prohibición. El agravio de los operados con lente con filtro se convierte en una petición organizada: aparecen las primeras recogidas de firmas y asociaciones de pacientes que exigen una ''solución'' a la sanidad pública.'
    mecanismo: El Gobierno no puede impedir que un ciudadano europeo se opere en otro país pagándolo de su bolsillo, porque la libre prestación de servicios y la normativa de asistencia sanitaria transfronteriza lo amparan, y la publicidad que se hace desde fuera en redes queda fuera del alcance práctico de las autoridades españolas. Lo único que le queda es advertir. Al negarse el sistema público y las sociedades científicas (h3-04, oftalmologa/h3/2), el colectivo agraviado busca la vía política, que es la de la petición y la asociación, y los partidos empiezan a medir si les conviene recogerla.
    dato: La Directiva 2011/24/UE reconoce el derecho de los pacientes a recibir asistencia sanitaria en otro Estado miembro.
    fuente: https://eur-lex.europa.eu/eli/dir/2011/24/oj
    confianza: media
    areas_afectadas:
    - sanidad
    - politica
    - pacientes
    - oftalmologia
    id: politico/h5/3
  - texto: 'Los sindicatos piden al Ministerio de Trabajo que aplique a los trabajadores al aire libre la obligación de adaptar o reducir la jornada que ya existe para el calor extremo. Trabajo responde con una nota de criterio para la Inspección: el deslumbramiento debe entrar en la evaluación de riesgos y el empresario debe dar gafas homologadas, pero no hay paralización obligatoria de la actividad. Sindicatos y patronal del reparto y la construcción chocan por primera vez por el fenómeno.'
    mecanismo: 'La obligación de adaptar la jornada por calor está ligada a los avisos meteorológicos oficiales, y aquí no hay aviso que lo active, así que el Gobierno no tiene una norma que estirar sin legislar de urgencia sobre un fenómeno que nadie sabe si durará. La nota de criterio es la herramienta intermedia: da cobertura a la Inspección y confirma la lógica de la prevención (economista/h3/1) sin parar la economía. Para los sindicatos los repartidores y los trabajadores de obra son el grupo más expuesto (economista/h3/2, oftalmologa/h3/3), y pedir la paralización es una reivindicación con apoyo social y sin coste para ellos.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - trabajo
    - sindicatos
    - prevencion-riesgos
    - reparto
    id: politico/h5/4
  - texto: 'En Estados Unidos, con la costa este ya en hora de oficina, los líderes de los comités de inteligencia del Congreso de ambos partidos piden públicamente un informe clasificado sobre la evaluación del fenómeno, y la Casa Blanca acepta darlo. El debate estadounidense sigue el mismo camino que el europeo: no se discute si existe, sino qué sabían las agencias.'
    mecanismo: 'Tras h3-03 el escepticismo federal ya no es defendible, así que el incentivo político pasa a la pregunta de la ocultación que la frase ''no hay indicios de acción hostil'' ha abierto en todas partes (h2-04). Pedir un informe clasificado es la jugada de menor riesgo para un legislador: muestra control sin comprometerse con una causa, y el Ejecutivo tiene la costumbre y la obligación de informar a los comités de inteligencia. Aceptarlo rápido es la forma de que la sesión sea a puerta cerrada y no un espectáculo televisado.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - politica
    - defensa
    - inteligencia
    - estados-unidos
    id: politico/h5/5
  reacciona_a:
  - oftalmologa/h3/2
  - economista/h3/1
  - economista/h3/2
- agente: medios
  tramo: h5
  afirmaciones:
  - texto: 'A las 15:00 de Madrid los telediarios de sobremesa en España abren con el fenómeno y, por primera vez, la explicación de la edad llega a quien más la necesita: con infografía del cristalino, el testimonio de un nonagenario operado de cataratas que ve el color mejor que su nieto y el caso de Monet. Es el primer momento del día en que el mensaje sanitario le gana el espacio al corte de la rueda de prensa entre el público mayor, y muchos abuelos dejan de leer la diferencia por edad como algo dirigido contra ellos y pasan a preguntar a sus nietos qué ven.'
    mecanismo: 'La rueda de prensa no llegó (h3-01) porque se consumió en cortes de vídeo corto, un canal joven. El telediario de las 15:00 es el formato con más audiencia de la franja de mediodía, la ven sobre todo personas mayores en casa, y tiene lo que el corte no tiene: dos o tres minutos de pieza montada con gráfico, que es justo lo que necesita una explicación óptica. Las redacciones han tenido tres horas para conseguir el personaje que resuelve el relato, el anciano operado (oftalmologa/h3/1), que es televisivo porque invierte la expectativa. Así el contraargumento a la teoría del cambio dirigido llega por la tele a los mismos mayores a los que la teoría llegaba por WhatsApp.'
    dato: En noviembre de 2025 Antena 3 Noticias 1 tuvo un 24% de cuota media en la sobremesa entre semana y el Telediario 1 de TVE un 15,3%.
    fuente: https://www.formulatv.com/noticias/antena-3-noticias-lidera-noviembre-telediario-135747/
    confianza: media
    areas_afectadas:
    - medios
    - salud
    - opinion_publica
    - familias
    id: medios/h5/1
  - texto: 'Las redes conspirativas no se quedan sin argumento con el caso de los ancianos operados: lo absorben. Entre las 13:00 y las 15:00 circula en Telegram y en canales de vídeo la versión de que los filtros UV de las lentes intraoculares se introdujeron en los ochenta ''porque ya lo sabían'', y que a millones de operados ''les pusieron un tapón'' para que no vieran lo que llegaría. El agravio de los operados con filtro encuentra así un culpable con nombre (las farmacéuticas y los fabricantes de lentes) y se cruza con el bulo de que las ópticas ''lo sabían''.'
    mecanismo: 'Discrepo en parte de oftalmologa/h3/1: el dato histórico que desmonta la selección por edad trae dentro una fecha, y una fecha es materia prima para una conspiración. Un marco conspirativo maduro no se refuta con un contraejemplo; lo reinterpreta como prueba de que el plan es anterior. El relato ya tenía beneficiarios (las ópticas, h3-03) y ahora gana una cronología de cuarenta años y unas víctimas reales, los operados con filtro, que tienen una pérdida verdadera y una negativa de las sociedades científicas a corregirla (h3-04). El agravio legítimo da credibilidad emocional a la parte inventada.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - desinformacion
    - salud
    - sanidad_privada
    - industria_optica
    id: medios/h5/2
  - texto: 'A partir de las marcas en la piel que se comentan en institutos (adolescente/h3/4) se viraliza el bulo de que la visión ultravioleta ''ve a través de la ropa''. Hay chicas que dejan de ir al gimnasio o se niegan a quitarse la sudadera, padres que preguntan en los grupos del colegio si es verdad, y los verificadores tienen que desmentir algo que es al revés: el tejido corta el UV-A más que la luz visible y lo único que se ve distinto es la piel descubierta.'
    mecanismo: 'Cada vez que aparece un sentido o un sensor nuevo, el primer bulo de privacidad es el de los rayos X. Pasó en 2020 con la cámara de filtro de color del OnePlus 8 Pro, que usaba infrarrojo y veía a través de algunos plásticos, y aunque no atravesaba la ropa la idea corrió tanto que la marca desactivó la función. Aquí hay una semilla real: en el canal nuevo se ven manchas y marcas que antes no se veían, así que el salto de ''se ven cosas ocultas en la piel'' a ''se ve lo que hay debajo de la ropa'' es corto para quien no conoce la física. Además encaja en la conversación que ya existía entre adolescentes sobre quién ve qué del cuerpo del otro, y el miedo a la exposición viaja más rápido que la explicación de que la ropa protege.'
    dato: En mayo de 2020 OnePlus desactivó por software el filtro Photochrom de la cámara del OnePlus 8 Pro, que usaba infrarrojo y podía ver a través de plásticos finos, tras la polémica de privacidad; las pruebas mostraron que no atravesaba la ropa.
    fuente: https://www.engadget.com/one-plus-disable-see-through-filter-8-pro-114502178.html
    confianza: media
    areas_afectadas:
    - desinformacion
    - educacion
    - privacidad
    - adolescentes
    id: medios/h5/3
  - texto: 'YouTube, TikTok y los buscadores ponen paneles informativos sobre las búsquedas de los nombres virales del color, con enlace a la declaración de la OMS y a las autoridades sanitarias de cada país, y los verificadores por fin tienen una fuente oficial que citar. El efecto es desigual: en las redes abiertas el contenido de los divulgadores gana posición, pero en los canales conspirativos el panel se presenta como prueba de censura y el tráfico se desplaza aún más hacia Telegram y plataformas alternativas.'
    mecanismo: Las plataformas ya tienen la herramienta, los paneles de información que usaron con la COVID y con noticias de última hora, pero necesitan una fuente reconocida a la que enlazar. Hasta la hora 3 no la había; la declaración de la OMS (h3-09) y las notas de los ministerios se la dan, y activar un panel es un cambio de configuración que se hace en horas. Pero el panel actúa sobre la búsqueda y la recomendación, no sobre la mensajería, y para una comunidad que ya cree en la ocultación (h3-03) una etiqueta oficial encima de su vídeo es la confirmación de que alguien intenta tapar algo.
    dato: YouTube muestra paneles de información de fuentes autorizadas junto a resultados de búsqueda y vídeos sobre temas propensos a la desinformación y sobre noticias en desarrollo.
    fuente: https://www.youtube.com/intl/ALL_ie/howyoutubeworks/product-features/news-information/
    confianza: alta
    areas_afectadas:
    - plataformas
    - desinformacion
    - verificacion
    - salud
    id: medios/h5/4
  - texto: 'En Asia oriental, donde a las 15:00 de Madrid son las 22:00 o las 23:00 y el sol se puso antes del suceso, la mayoría aún no ha visto el color nuevo con sus ojos, y la conversación nocturna la ocupa la luz negra: linternas UV de detectar billetes y manchas, lámparas de uñas y luces de discoteca se convierten en la forma casera de verlo, con directos de madrugada, agotamiento de linternas UV en las tiendas en línea y los primeros avisos sanitarios contra mirar directamente los LED ultravioleta.'
    mecanismo: 'Es la misma brecha de credibilidad que vivió Norteamérica antes del amanecer (h3-02), pero con una diferencia: tras cinco horas de vídeos y testimonios nadie allí lo descarta como histeria, todos quieren comprobarlo ya y faltan horas para que salga el sol. Las fuentes domésticas de UV-A existen en millones de casas y comercios, y quien ha visto los testimonios deduce que si el color nuevo es ultravioleta, la luz negra debería mostrarlo. La prueba funciona, así que se viraliza como la de quitarse las gafas. Pero una linterna UV apuntada a los ojos concentra mucha más radiación que el cielo, y la curiosidad de mirarla de frente es la que obliga a los sanitarios a salir con un aviso nuevo.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - asia
    - comercio_electronico
    - salud
    - redes_sociales
    id: medios/h5/5
  reacciona_a:
  - oftalmologa/h3/1
  - adolescente/h3/4
- agente: oftalmologa
  tramo: h5
  afirmaciones:
  - texto: 'Entre las 13:00 y las 15:00 los niños y adolescentes describen el color nuevo como algo que ''no se enfoca'': bordes con halo violáceo alrededor de ramas, cables, letras blancas sobre fondo de cielo y siluetas a contraluz. Las quejas de dolor de cabeza y ojos cansados en colegios se concentran en quienes miran por la ventana o leen junto a ella, y optometristas y oftalmólogos empiezan a explicar en los medios que el color nuevo se ve desenfocado por la propia óptica del ojo y que no es señal de lesión.'
    mecanismo: 'El ojo tiene aberración cromática longitudinal: cuanto más corta es la longitud de onda, más por delante de la retina enfoca. El UV-A queda todavía más desenfocado que el azul, así que en un ojo con cristalino transparente la imagen del canal nuevo llega siempre borrosa respecto a la visible, como una franja de color alrededor de los contornos con mucho contraste. El sistema de acomodación intenta enfocar dos imágenes que no coinciden y no lo consigue, que es el mecanismo clásico de la fatiga visual y la cefalea. Los niños, que más UV-A reciben en la retina, son los que más lo sufren, y se suma a los que se quitan las gafas para ver el color (adolescente/h3/3).'
    dato: La aberración cromática longitudinal del ojo humano es de unas dos dioptrías en el espectro visible y aumenta hacia las longitudes de onda cortas.
    fuente: https://ophthalmologytimes.com/view/what-role-does-chromatic-aberration-play-iols
    confianza: media
    areas_afectadas:
    - salud
    - educacion
    - comunicacion_sanitaria
    id: oftalmologa/h5/1
  - texto: 'Las personas mayores con cristalino propio, que casi no ven el color nuevo, sí empiezan a quejarse de que al aire libre lo ven todo ''como con niebla'' o ''con un velo'', sobre todo con sol bajo de tarde. Los oftalmólogos lo explican como un efecto de su propio cristalino, y esto matiza el relato de que los mayores ''no notan nada'': notan el fenómeno como pérdida de contraste, no como color.'
    mecanismo: 'El cristalino envejecido absorbe casi todo el UV-A antes de que llegue a la retina, por eso los mayores ven poco el color nuevo (h2-02). Pero esa energía absorbida no desaparece: los cromóforos del cristalino emiten fluorescencia azul verdosa dentro del ojo, que se reparte por la retina como una luz difusa que tapa el contraste de la imagen. La fluorescencia del cristalino crece con la edad y ya estaba descrita como fuente de deslumbramiento por velo. Ahora el UV-A no se percibe solo como color, sino también a través de ese velo, de modo que el mayor sufre la molestia sin la recompensa del color nuevo, y eso refuerza su sensación de agravio frente a los nietos.'
    dato: La fluorescencia del cristalino humano inducida por luz UV cercana y azul aumenta con la edad y produce luz difusa intraocular que interfiere con la función visual.
    fuente: https://proceedings.spiedigitallibrary.org/journals/journal-of-biomedical-optics/volume-10/issue-4/044021/Near-UV-blue-light-induced-fluorescence-in-the-human-lens/10.1117/1.1990163.full
    confianza: media
    areas_afectadas:
    - salud
    - mayores
    - comunicacion_sanitaria
    id: oftalmologa/h5/2
  - texto: 'En interiores aparecen fuentes artificiales de UV-A que antes nadie veía: las lámparas de uñas de los salones de manicura, los matainsectos eléctricos de bares, cocinas y carnicerías, los detectores de billetes, las luces negras de locales y las camas de bronceado se ven ahora como focos intensos de color nuevo. Las manicuristas son el primer colectivo que se queja de deslumbramiento en el puesto de trabajo, y muchos negocios apagan los matainsectos y las lámparas de detectar billetes a media tarde.'
    mecanismo: 'Esos aparatos emiten justo en la banda que ahora se percibe: las lámparas de uñas LED y UV curan el gel con picos entre 365 y 405 nanómetros, los matainsectos y detectores usan tubos de luz negra en torno a 365, y las camas solares emiten sobre todo UV-A. Antes eran casi invisibles porque su luz caía fuera del espectro visible; ahora son, en un interior en penumbra con las persianas bajadas (h3-05), la fuente de UV-A más intensa de la sala, a poca distancia de los ojos. La manicurista mira la lámpara de cerca durante horas, sin la protección del sol del exterior, y el empresario apaga lo que molesta al cliente porque es lo más barato.'
    dato: Las lámparas para curar gel de uñas trabajan con longitudes de onda de 365, 395 y 405 nanómetros.
    fuente: https://purespadirect.com/blogs/pure-spa-direct-blog/selecting-the-correct-light-spectrum-for-curing-led-builder-gels-why-365nm-395nm-and-405nm-matter-for-perfect-wrinkle-free-nails
    confianza: media
    areas_afectadas:
    - trabajo
    - prevencion_riesgos
    - comercio
    - hosteleria
    id: oftalmologa/h5/3
  - texto: Las sociedades de oftalmología y los servicios de urgencias avisan a media tarde de que esta noche y mañana pueden llegar casos de queratitis por ultravioleta (ojos rojos, dolor intenso, sensación de arena, lagrimeo) en quienes han mirado al cielo o al sol sin gafas durante el día en zonas de UV alto o con nieve. Insisten en que es una quemadura superficial de la córnea, dolorosa pero que cura en uno o dos días, y en que no la causa el fenómeno sino haber mirado al sol sin protección.
    mecanismo: 'La percepción del UV-A no daña el ojo (supuesto del mundo), pero la curiosidad sí cambia la conducta: la gente mira al cielo y al sol para ver el color nuevo y se quita las gafas (h3-01, adolescente/h3/3). En las regiones con mucho sol, y en montaña con nieve, eso supone también exposición a UV-B, que es la que quema la córnea. La queratitis por ultravioleta no da síntomas en el momento sino entre seis y doce horas después, así que las exposiciones del mediodía en el Golfo, el sur de Asia o el hemisferio sur se convertirán en consultas de urgencia por la noche. Avisar antes evita que esos casos se lean como prueba de que el fenómeno sí daña los ojos y desmientan el mensaje de la OMS (h3-09).'
    dato: Los síntomas de la fotoqueratitis aparecen típicamente entre 6 y 12 horas después de la exposición y suelen resolverse en 24 a 72 horas.
    fuente: https://www.college-optometrists.org/Clinical-guidance/Clinical-Management-Guidelines/Photokeratitis_Ultraviolet_UV_Burn_ArcEye_SnowBlin
    confianza: media
    areas_afectadas:
    - salud
    - urgencias
    - comunicacion_sanitaria
    - desinformacion
    id: oftalmologa/h5/4
  - texto: Pediatras, médicos forenses y servicios de protección a la infancia piden a profesores y familias que no saquen conclusiones de las marcas que ahora se ven en la piel. En el canal nuevo pueden aparecer moratones curados hace semanas o meses, pero también manchas de pigmento, cicatrices y eccemas que se ven igual de oscuros, y una marca en el color nuevo no prueba ni descarta un maltrato.
    mecanismo: 'La fotografía forense con UV reflejado se usa desde hace décadas porque muestra moratones y mordeduras que ya no se ven en luz visible, ya que la piel alterada y la melanina absorben más UV que la sana. Lo que vieron los adolescentes en h3 (adolescente/h3/4) tiene esa base. Pero esa misma técnica tiene muchos falsos positivos y se interpreta en contexto, con protocolo y por profesionales: el pigmento, la cicatriz o la irritación dan la misma imagen oscura. Cuando millones de personas pasan a ver eso a simple vista en colegios y casas, las instituciones de infancia tienen que adelantarse a dos riesgos a la vez, la acusación infundada y la marca real ignorada, y la respuesta más barata y rápida es una nota que encauce las sospechas hacia los circuitos ya existentes en lugar de al chisme o a la denuncia directa.'
    dato: La fotografía con ultravioleta reflejado permite documentar moratones desvanecidos o no visibles a simple vista, y se usa en forense para lesiones en niños.
    fuente: https://www.crime-scene-investigator.net/uvchildphoto.html
    confianza: baja
    areas_afectadas:
    - infancia
    - educacion
    - servicios_sociales
    - violencia
    - salud
    id: oftalmologa/h5/5
  reacciona_a:
  - adolescente/h3/3
  - adolescente/h3/4
- agente: adolescente
  tramo: h5
  afirmaciones:
  - texto: 'A las 14:30, al salir del instituto, la puerta se convierte en un atasco: casi nadie quiere cruzar el patio y la calle a pleno sol, nos quedamos en el vestíbulo esperando a que vengan a por nosotros o salimos en grupo directos a la boca de metro más cercana, aunque normalmente fuéramos andando. El metro, que va bajo tierra, se llena de gente de mi edad haciendo trayectos de dos paradas.'
    mecanismo: Llevamos toda la mañana dentro con persianas bajadas y la última vez que salimos al sol nos lloraban los ojos, así que salir es lo que más miedo nos da del día, aunque no lo digamos. Muchas no tenemos gafas de sol buenas y nuestras madres nos han dicho que no vayamos sin ellas. El metro es el único sitio que conocemos que está tapado del todo y nos acerca a casa sin pasar tiempo en la calle, y si vas en grupo te da menos vergüenza parecer que tienes miedo.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - transporte
    - vida_cotidiana
    id: adolescente/h5/1
  - texto: 'En la comida en casa, entre las 14:30 y las 15:00, le decimos a nuestras madres y padres cómo se les ven las manchas de la cara junto a la ventana, y en TikTok aparece un formato nuevo: grabar la reacción del padre o la madre cuando le describes su cara ''en el color nuevo''. Unos vídeos son de risa y otros acaban con la madre llorando o pidiendo cita en el dermatólogo, y entre nosotras se discute si eso está bien o es cruel.'
    mecanismo: Somos las únicas en casa que vemos bien las manchas y ellos no pueden comprobarlo en el espejo, así que lo que decimos va a misa. Eso nos da un poder que no tenemos casi nunca en casa, y lo que nos da poder lo convertimos en contenido. La comida es el primer momento del día en que estamos frente a frente con ellos y con luz de ventana. Pero como la reacción de los adultos es de preocupación de verdad, a algunas nos sienta mal haber hecho la gracia y empieza el debate.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - familia
    - redes_sociales
    - salud
    id: adolescente/h5/2
  - texto: Después de comer, varias del grupo decimos en el chat que tenemos dolor de cabeza y los ojos cansados o rojos, pero lo contamos de broma ('me ha reventado el color'), y alguna madre nos da un ibuprofeno o nos manda a echarnos la siesta con la persiana bajada. Nadie lo relaciona en serio con haber estado mirando por la ventana o haberse quitado las gafas.
    mecanismo: 'Llevamos cinco horas forzando la vista: pegadas a las ventanas, mirando al sol a escondidas y los de gafas quitándoselas. El cansancio llega cuando paramos y nos sentamos a comer. Como lo de protegerse ya es un meme y quejarse es quedar como miedica, lo contamos en tono de broma, y así los padres lo ven como un dolor de cabeza normal y no como algo que haya que mirar.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - familia
    id: adolescente/h5/3
  - texto: 'Las fotos en falso color que circulan desde Estados Unidos nos llegan por la tarde y entre la gente de mi edad se convierten en un juego de puntuar: ''esta se parece'', ''esta no tiene nada que ver''. Salen tutoriales de cómo editar una foto con filtros para que se parezca más al color de verdad, y gana la versión que hace la gente que más sigo, no la de los fotógrafos.'
    mecanismo: Nosotras somos las que mejor lo vemos, así que sentimos que tenemos derecho a decir cuál foto acierta y cuál no, y eso encaja con lo de ser 'la generación que lo ve'. Como ninguna foto coincide, el reto de acercarse con filtros de edición es divertido y fácil de hacer con el móvil. Y en mi grupo siempre se acaba quedando la versión que sube alguien conocido, igual que pasó con las palabras para el color.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes_sociales
    - cultura
    - medios
    id: adolescente/h5/4
  - texto: Por la tarde mi madre intenta comprarme unas gafas de sol homologadas para mañana y no encuentra en las ópticas del barrio o las que hay son caras; yo le digo que no las quiero porque con ellas no se ve el color y en clase nadie las va a llevar. En el grupo se acuerda, medio en serio, que mañana nadie lleve gafas oscuras al instituto.
    mecanismo: Las gafas buenas se han acabado o han subido de precio, así que a mi madre le cuesta más conseguirlas y se agobia. Para mí ponérmelas significa quedarme sin lo que todo el mundo comenta y parecer la que hace caso a los adultos, que es justo de lo que nos reímos con el meme de la rueda de prensa. Si lo acordamos en grupo, nadie se queda como la rara, y la decisión pasa a ser del grupo y no de cada casa.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - consumo
    - familia
    - educacion
    - salud
    id: adolescente/h5/5
  reacciona_a:
  - disruptor/h3/1
  - disruptor/h3/3
- agente: disruptor
  tramo: h5
  afirmaciones:
  - texto: 'En Asia oriental y Oceanía, donde lleva horas siendo de noche, la desaparición de los colores nuevos al ponerse el sol se lee como ''ya se ha ido'', y ese rumor llega a Europa por la tarde. La respuesta no la dan las autoridades sino un aparato barato: las linternas ultravioleta de 365 y 395 nm que se venden para detectar orina de mascotas, escorpiones o billetes falsos. Entre las horas 3 y 5 se agotan en tiendas de conveniencia y plataformas de Japón, Corea, China y Australia, y encenderlas cada noche se convierte en la ''prueba de permanencia'' casera, con vídeos de gente que comprueba antes de dormir si todavía lo ve.'
    mecanismo: 'El supuesto central del mundo es que nadie sabe si el cambio es permanente, y la noche quita el único estímulo natural: sin sol no hay UV-A y el ojo no tiene con qué comprobar si la capacidad sigue ahí. Eso convierte cada anochecer en una incertidumbre nueva, y el primer anochecer lo vive Asia-Pacífico mientras Europa y América aún tienen sol. La linterna UV es el único objeto doméstico que emite justo la banda que ahora se percibe, cuesta pocos euros, ya está en el inventario de bazares y marketplaces, y no depende de la homologación que ha estrechado la oferta de gafas (h3-07). Repite la lógica de la prueba de quitarse las gafas: una comprobación que cada uno hace con sus propios ojos sin fiarse de nadie. Efecto secundario: las de 395 nm emiten sobre todo violeta visible y casi no ''demuestran'' nada, así que aparece otra disputa sobre qué linterna sirve.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - consumo
    - redes_sociales
    - informacion
    - comercio_electronico
    id: disruptor/h5/1
  - texto: En cocinas de hostelería, obradores, industrias alimentarias, supermercados y hospitales, los mata-insectos eléctricos de tubo ultravioleta pasan a ser las lámparas más llamativas y molestas del local. Los trabajadores los apagan, los tapan o los desenchufan, y los responsables de calidad descubren a media tarde que han perdido sin decidirlo una de las medidas de control de plagas que exigen sus planes de seguridad alimentaria.
    mecanismo: Los mata-insectos de cocina e industria funcionan con tubos que emiten UV-A centrado en 365 nm, la banda que atrae a las moscas y que hasta el martes el ojo humano apenas percibía como un tenue brillo violeta. Ahora esa misma emisión se ve como una fuente intensa del color nuevo, a la altura de la vista y en espacios cerrados donde el personal pasa ocho horas, justo cuando ya hay fatiga visual por la mañana en exteriores. Apagarlo es la solución inmediata y nadie la registra como incidencia porque parece un gesto de comodidad, pero el aparato forma parte del programa de control de plagas que inspeccionan sanidad y las auditorías de cliente. El conflicto no lo resuelve una norma nueva sino el responsable de calidad de cada empresa, que tendrá que elegir entre la queja del personal y el control de plagas.
    dato: Los tubos de recambio para mata-insectos profesionales se comercializan con emisión a 365 nm, en el UV-A.
    fuente: https://uk.rs-online.com/web/p/fly-killer-lights/4730840
    confianza: media
    areas_afectadas:
    - hosteleria
    - industria_alimentaria
    - sanidad
    - trabajo
    id: disruptor/h5/2
  - texto: 'Las cabinas de rayos UVA y las lámparas de manicura de gel se convierten en las fuentes de luz más deslumbrantes que la gente ha visto de cerca. En los centros de bronceado de Europa por la tarde los clientes cancelan o salen de la cabina antes de tiempo, y en los salones de uñas, abiertos a esa hora, clientas y manicuristas apartan la vista de la lámpara de curado. El argumento sanitario contra las cabinas, que llevaba años perdiendo frente a la estética, gana una prueba directa: el cliente ve cuánta radiación recibe.'
    mecanismo: 'Las camas de bronceado emiten sobre todo UV-A, con mucha más intensidad por centímetro cuadrado que el sol de noviembre en Europa, y las lámparas de curado de gel trabajan entre 365 y 405 nm a pocos centímetros de la cara de quien las mira. Lo que antes era una luz azulada inofensiva en apariencia ahora se percibe tal como es. Es el mismo giro que h3-06 dio a la crema solar: el riesgo deja de depender de la autoridad del dermatólogo y pasa a ser visible para el consumidor. Las gafas de cabina, que muchos usuarios se saltaban, pasan a ser imprescindibles por pura molestia y no por prevención del cáncer, y los dermatólogos, que ya están recibiendo consultas por manchas (h3-06), tienen una imagen fácil para pedir que no se use la cabina mientras dure el fenómeno.'
    dato: Las camas de bronceado emiten radiación predominantemente UV-A, con una pequeña fracción de UV-B.
    fuente: https://www.sciencelearn.org.nz/resources/1333-the-problem-with-sunbeds
    confianza: media
    areas_afectadas:
    - estetica
    - salud
    - consumo
    - comercio
    id: disruptor/h5/3
  - texto: En las conversaciones cara a cara junto a una ventana o en la calle, las coronas, carillas y empastes estéticos se ven distintos de los dientes naturales en el color nuevo, como dientes más oscuros o de otro tono en mitad de la sonrisa. Lo notan sobre todo los jóvenes al mirar a adultos, y por la tarde llegan las primeras llamadas a clínicas dentales de pacientes que preguntan si su carilla 'está mal' o si se puede cambiar, mientras los dentistas no pueden prometer nada porque los materiales nunca se diseñaron pensando en ese canal.
    mecanismo: 'El esmalte y la dentina responden al UV de una forma característica, por eso a la luz negra los dientes naturales se ven brillantes y muchas restauraciones se ven apagadas u oscuras; los fabricantes de porcelana añaden agentes fluorescentes precisamente para imitarlo, y no todas las restauraciones los llevan ni responden igual. Hasta ahora esa diferencia solo aparecía en discotecas con luz negra; con la percepción del UV-A a la luz del día pasa a verse en cualquier conversación con sol. Como en h3-01, el que ve el defecto es el interlocutor joven y no el propio portador, que si es mayor apenas percibe el canal nuevo. Es una variante del efecto piel: el UV-A deja a la vista lo que la estética había resuelto solo para la luz visible.'
    dato: Las porcelanas dentales llevan aditivos fluorescentes para imitar la respuesta de los dientes naturales a la luz ultravioleta, y sin ellos las restauraciones se ven oscuras bajo luz negra.
    fuente: https://www.dentalcare.com/en-us/ce-courses/ce690/optical-properties-of-teeth
    confianza: baja
    areas_afectadas:
    - salud
    - estetica
    - relaciones_sociales
    id: disruptor/h5/4
  reacciona_a: []

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
