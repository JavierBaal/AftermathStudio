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
Hora 2 (PT2H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h1
  resumen: 'En la primera hora el suceso se vive de forma escalonada aunque sea simultáneo: solo lo perciben con claridad quienes están al aire libre o junto a ventanas en zonas con luz solar (Europa, África, Oriente Medio, India), mientras que en América es de noche, en Asia oriental ya ha anochecido y en interiores con LED apenas se nota. Como las cámaras de los móviles no registran el UV-A, el fenómeno se cuenta con testimonios y caras de reacción, lo que alimenta a la vez el escepticismo (sobre todo en EE. UU.) y una oleada de bulos sobre la causa y sobre marcas ocultas que ahora se ven en billetes, ropa o piel. Las gafas con filtro UV (UV400, policarbonato) funcionan como interruptor que apaga la nueva percepción y alivia el deslumbramiento, lo que dispara la compra de gafas de sol y la subida especulativa de EssilorLuxottica, en unos mercados europeos tensos pero sin desplome. Los gobiernos con luz diurna actúan solo sobre el deslumbramiento (tráfico, protección civil) y la coordinación
    interna, sin pronunciarse sobre el fenómeno; la OMS vigila sin declarar emergencia y la hipótesis de ataque se queda en canales reservados.'
  hechos_establecidos:
  - id: h1-01
    texto: 'La experiencia del suceso depende de la luz solar local: a las 09:00 UTC lo viven a plena luz Europa, África, Oriente Medio y la India; en América es de madrugada y en Asia oriental ya ha anochecido, de modo que allí la mayoría no ve nada nuevo y recibe el suceso como relato de segunda mano, con escepticismo y sospecha de montaje o histeria regional, especialmente en las redes de EE. UU.'
    origen:
    - politico/h1/1
    - medios/h1/2
    - disruptor/h1/2
  - id: h1-02
    texto: En interiores iluminados con LED el cambio es casi imperceptible, porque esas lámparas apenas emiten UV-A; se nota al mirar por una ventana o al salir a la calle. Oficinas, mesas de operaciones y aulas lejos de las ventanas funcionan casi con normalidad.
    origen:
    - oftalmologa/h1/4
    - disruptor/h1/2
    - economista/h1/1
  - id: h1-03
    texto: 'Las cámaras de los móviles no registran el UV-A tal como ahora lo percibe el ojo: los vídeos salen normales, no hay prueba visual del fenómeno y el contenido viral dominante son testimonios hablados, textos que intentan describir colores sin nombre y vídeos de reacción centrados en las caras; los comentarios se llenan de acusaciones de falsedad.'
    origen:
    - medios/h1/1
    - adolescente/h1/3
  - id: h1-04
    texto: Las lentes con filtro UV (gafas de sol UV400 y muchas gafas graduadas de policarbonato, alto índice o con tratamiento UV) apagan la nueva percepción en el centro del campo visual y eliminan el deslumbramiento; quienes las llevan solo notan el cambio por los bordes de la montura. Esto genera testimonios contradictorios entre observadores, y el gesto de quitarse y ponerse las gafas (de ver o de sol) se vuelve viral como forma de comprobar qué es UV.
    origen:
    - oftalmologa/h1/3
    - disruptor/h1/1
  - id: h1-05
    texto: En las zonas con sol se dispara la compra de gafas de sol en tiendas físicas y comercio electrónico; en las zonas que están a mediodía se agotan localmente las existencias de gama baja en una o dos horas, pero no hay escasez sistémica porque los almacenes regionales aún tienen stock. Entre adolescentes, tener gafas de sol empieza a marcar quién puede quedarse fuera mirando y quién se queda dentro.
    origen:
    - economista/h1/4
    - adolescente/h1/5
  - id: h1-06
    texto: 'Las bolsas europeas, principales plazas abiertas a esa hora junto a algunas de India y el Golfo, no se desploman: hay interrupciones por volatilidad valor a valor (subastas de al menos dos minutos), diferenciales más anchos y formación de precio con poca liquidez transfronteriza a la espera de la apertura de Wall Street a las 15:30 de Madrid.'
    origen:
    - economista/h1/1
  - id: h1-07
    texto: EssilorLuxottica y otros cotizados de óptica y gafas de sol suben con fuerza en París y Milán en una subida especulativa, mientras el resto del Eurostoxx se mueve de lado o baja ligeramente.
    origen:
    - economista/h1/2
  - id: h1-08
    texto: 'Futuros estadounidenses y activos refugio (bono alemán, franco suizo, oro) se mueven con moderación: no hay huida masiva hacia la seguridad, las mesas institucionales reducen exposición bruta y esperan a Nueva York.'
    origen:
    - economista/h1/5
  - id: h1-09
    texto: 'El golpe a la productividad es geográficamente desigual: en la Europa de noviembre, con sol bajo, el deslumbramiento es leve; se concentra en el trabajo al aire libre de las zonas a mediodía o primera tarde con alta radiación (Golfo Pérsico, África subsahariana, sur de Asia), sobre todo en el sector informal.'
    origen:
    - economista/h1/3
  - id: h1-10
    texto: Los parabrisas laminados bloquean casi todo el UV-A y las ventanillas laterales mucho menos, así que los conductores ven un paisaje casi normal al frente y colores UV con deslumbramiento por los lados; los incidentes de la primera hora se concentran en cambios de carril, incorporaciones y giros, y el coche parado se descubre como refugio contra la fatiga visual.
    origen:
    - disruptor/h1/3
    - oftalmologa/h1/4
  - id: h1-11
    texto: 'Los gobiernos con luz diurna actúan solo sobre el deslumbramiento: autoridades de tráfico y protección civil piden reducir la conducción y refuerzan la vigilancia en carreteras, sin pronunciarse sobre el fenómeno en sí.'
    origen:
    - politico/h1/2
  - id: h1-12
    texto: En España se convoca de urgencia el Consejo de Seguridad Nacional o su comité de situación, sin declarar ninguna situación de interés para la Seguridad Nacional.
    origen:
    - politico/h1/3
  - id: h1-13
    texto: La OMS emite una nota breve de que vigila la situación, sin convocar el Comité de Emergencias del RSI ni declarar una emergencia de salud pública de importancia internacional.
    origen:
    - politico/h1/4
  - id: h1-14
    texto: Los servicios de inteligencia y defensa de las grandes potencias abren en privado la hipótesis de un ataque y elevan la alerta, pero ningún gobierno acusa públicamente a otro.
    origen:
    - politico/h1/5
  - id: h1-15
    texto: Antes de que acabe la hora circulan con gran alcance explicaciones falsas (antenas 5G, fumigaciones, tormenta solar ocultada, experimento militar o farmacéutico) que superan en difusión a los mensajes de prudencia de oftalmólogos y autoridades.
    origen:
    - medios/h1/3
  - id: h1-16
    texto: 'Surge una ola de descubrimientos que se cuenta de palabra: marcas antes invisibles en billetes, documentos, envases, ropa y paredes (tintas de seguridad, blanqueantes ópticos), la ropa blanca lavada con blanqueantes distinta de la no tratada y, donde hay sol fuerte (India, Oriente Medio), el protector solar visible como parches o máscaras en la piel. Parte se interpreta como mensajes ocultos o vigilancia y aparecen dudas sobre si la crema solar funciona o mancha.'
    origen:
    - medios/h1/4
    - disruptor/h1/5
  - id: h1-17
    texto: Las televisiones europeas abren especiales en directo sin material propio, con tertulias, oftalmólogos y lectura de redes, y amplifican los bulos al citarlos para desmentirlos.
    origen:
    - medios/h1/5
  - id: h1-18
    texto: Los objetos que destacan en UV se ven con un halo o borde ligeramente desenfocado por aberración cromática, y mucha gente lo interpreta como un problema de vista y no como un color nuevo.
    origen:
    - oftalmologa/h1/2
  - id: h1-19
    texto: 'La intensidad de los colores nuevos varía con la edad por la transparencia del cristalino: niños y jóvenes los ven más vivos y los mayores más apagados, lo que desconcierta en las comparaciones familiares.'
    origen:
    - oftalmologa/h1/5
  - id: h1-20
    texto: 'En los colegios e institutos españoles las clases se paran solas: el profesorado deja mirar por la ventana o salir al patio sin instrucciones, el móvil sale en todas partes pese a la prohibición y lo primero es escribir a la familia y al grupo de clase, mientras los padres preguntan si sus hijos están bien.'
    origen:
    - adolescente/h1/1
    - adolescente/h1/2
  - id: h1-21
    texto: 'Entre adolescentes la preocupación inmediata es la propia imagen: cómo se ven piel, pelo y maquillaje con los colores nuevos. La comprobación en el espejo del baño, con luz LED interior, no muestra el efecto, de modo que la duda no se resuelve en interiores.'
    origen:
    - adolescente/h1/4
    - oftalmologa/h1/4
  - id: h1-22
    texto: Los talleres europeos de mantenimiento aeronáutico e industrial suspenden las inspecciones por líquidos penetrantes fluorescentes y partículas magnéticas, porque el inspector ahora percibe la luz UV-A de 365 nm y el contraste del método se hunde; se retrasa la liberación de piezas de motor y estructuras pendientes.
    origen:
    - disruptor/h1/4
  - id: h1-23
    texto: Las personas afáquicas o con lentes intraoculares que dejan pasar UV empiezan a ser buscadas por consultas y medios como informantes de referencia, porque tenían experiencia previa de percibir UV como un blanco azulado o violáceo.
    origen:
    - oftalmologa/h1/1
  tensiones_abiertas:
  - Si la experiencia previa de los afáquicos coincide realmente con los colores nuevos que percibe el resto o solo es un parecido parcial; su valor como informantes depende de ello.
  - 'Si la subida de EssilorLuxottica y la compra de gafas de sol se sostienen: el filtro UV400 alivia de forma física, pero el mercado no sabe si el fenómeno es permanente ni si la gente preferirá ver el UV a bloquearlo.'
  - 'Qué ocurre cuando amanezca en América: si la experiencia directa disuelve el escepticismo estadounidense o si el marco de bulo o campaña coordinada ya fijado en la primera hora persiste.'
  - Si el aumento de incidentes de tráfico en maniobras laterales es medible y empuja a pasar de la recomendación a medidas obligatorias.
  - Cuánto dura la parada de ensayos fluorescentes en aviación e industria y si los reguladores validan un procedimiento alternativo antes de que afecte a la operación de flotas.
  contradicciones_resueltas:
  - entre:
    - disruptor/h1/5
    - medios/h1/1
    decision: 'Se acepta que el protector solar y los blanqueantes ópticos se ven distintos, pero se corrige que circulen imágenes de caras con parches: lo que circula son descripciones y testimonios.'
    motivo: Las cámaras de los móviles no registran el UV-A (dato verificable de medios/h1/1, confianza alta), así que no puede haber imágenes que muestren el efecto.
  - entre:
    - adolescente/h1/4
    - oftalmologa/h1/4
    decision: Se mantiene la preocupación por la propia imagen, pero el espejo del baño no permite comprobarla.
    motivo: La iluminación LED interior casi no emite UV-A; el mecanismo de oftalmologa/h1/4 y el dato de disruptor/h1/2 son más sólidos.
  - entre:
    - oftalmologa/h1/3
    - disruptor/h1/1
    decision: 'Se combinan: el gesto viral es quitarse y ponerse cualquier lente con filtro UV, tanto gafas de sol como graduadas.'
    motivo: Ambas descansan en el mismo mecanismo físico de filtrado por debajo de 400 nm y no se excluyen.
  - entre:
    - economista/h1/2
    - oftalmologa/h1/3
    decision: Se mantiene la subida como especulativa, pero en el canon queda establecido que las gafas UV400 sí bloquean lo que ahora molesta.
    motivo: La duda del mercado es de información de los inversores en la primera hora, no del mecanismo físico, que está bien fundado.
  - entre:
    - economista/h1/1
    - politico/h1/1
    decision: 'Se matiza que las bolsas europeas son las principales plazas abiertas, no las únicas: Tokio, Shanghái y Hong Kong ya han cerrado, pero India y el Golfo siguen en sesión.'
    motivo: Corrección horaria verificable a las 09:00 UTC; no altera el resto de la afirmación.
  descartadas: []
  metricas:
    alarma_social: 3
    respuesta_gobiernos: comunicacion
    impacto_economico: 2
    adaptacion: 2

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora la subida de EssilorLuxottica se frena y devuelve parte de lo ganado: las primeras notas de análisis de los bancos señalan que el grueso de la demanda nueva va a gafas de sol baratas sin marca, no a las líneas de margen alto del grupo, y la ganancia se reparte hacia distribuidores y cadenas de óptica de gran volumen.'
    mecanismo: 'La primera hora fue una compra por narrativa en el líder del sector. En la segunda, los analistas hacen la cuenta de la demanda incremental: buena parte de la población con gafas graduadas ya filtra UV con el material o el tratamiento de la lente, así que no necesita comprar nada, y quien compra por el deslumbramiento busca la gafa más barata disponible ya, no una marca de lujo. Ese volumen lo capturan fabricantes sin marca y el canal de gran consumo, que apenas cotizan. Además nadie sabe si el fenómeno es permanente ni si la gente preferirá ver el UV a bloquearlo, lo que impide subir las previsiones de beneficio. Sin revisión de beneficios, los fondos rápidos toman ganancias.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados financieros
    - sector óptico
    - comercio minorista
    id: economista/h2/1
  - texto: Entre las 11:00 y las 12:00 de Madrid, con las fábricas chinas a primera hora de la noche, distribuidores europeos, de Oriente Medio y de la India lanzan pedidos urgentes de gafas de sol básicas y lentes UV400 a los polos productores chinos (Danyang, Xiamen, Wenzhou). Los proveedores en plataformas mayoristas suben precios de oferta y acortan la validez de sus presupuestos, y algunos anuncian turnos extra para el día siguiente.
    mecanismo: 'Las existencias de tienda se agotaron en la primera hora y los almacenes regionales están dimensionados para la temporada baja del hemisferio norte. Los compras de cadenas y distribuidores no esperan a saber si el fenómeno dura: el coste de quedarse sin producto es mayor que el de sobrestock de un artículo barato y no perecedero. La capacidad está muy concentrada en China, así que la reposición pasa por allí, y el proveedor con pedidos simultáneos de varios continentes tiene poder de precio inmediato. El cuello de botella real no es fabricar monturas simples, sino lentes con filtro certificado y transporte aéreo, que tardará días.'
    dato: Danyang produce más de 400 millones de lentes al año, en torno al 45 % de la producción mundial de lentes para gafas, y más de 100 millones de monturas.
    fuente: https://investinchina.chinadaily.com.cn/s/202203/16/WS6231abc0498e6a12c1225a79/city-of-glasses-plays-crucial-role-in-global-eyewear-market.html
    confianza: media
    areas_afectadas:
    - cadenas de suministro
    - comercio internacional
    - sector óptico
    - precios
    id: economista/h2/2
  - texto: MTU Aero Engines, Safran y Lufthansa (por su división de mantenimiento) se quedan por debajo del índice en Fráncfort y París durante la segunda hora, cuando las mesas conectan la parada de los ensayos fluorescentes en talleres con una capacidad de mantenimiento de motores que ya estaba al límite.
    mecanismo: 'La suspensión de inspecciones por líquidos penetrantes y partículas magnéticas no es pánico, es un cuello de botella regulatorio con efecto acumulativo: cada día sin liberar piezas alarga las visitas a taller y deja aviones en tierra. El mercado ya conocía lo caro que es eso por las revisiones de los motores GTF, que obligaron a parar aviones y costaron cientos de millones a los talleres y fabricantes. Los analistas aplican esa plantilla: ingresos de mantenimiento retrasados, penalizaciones contractuales y aerolíneas con menos aviones disponibles. La caída es moderada porque se supone que el regulador validará un procedimiento alternativo, pero nadie sabe cuándo.'
    dato: MTU estimó un impacto de alrededor de 1.000 millones de euros por el problema del motor PW1100G, que ya tensionaba la capacidad de los talleres de motores.
    fuente: https://www.flightglobal.com/aerospace/mtu-expects-1bn-impact-from-pw1100g-issue-but-maintains-faith-in-geared-fan-outlook/154933.article
    confianza: media
    areas_afectadas:
    - aviación
    - mercados financieros
    - mantenimiento industrial
    - transporte aéreo
    id: economista/h2/3
  - texto: 'En la segunda hora la volatilidad implícita europea (VSTOXX y opciones sobre índices) sube bastante más de lo que bajan los índices: el mercado compra protección en lugar de vender acciones, y el precio de las coberturas se encarece sin que haya desplome al contado.'
    mecanismo: 'Las mesas institucionales ya recortaron exposición en la primera hora y no tienen motivo para seguir vendiendo, porque no ven ningún flujo de caja destruido. Lo que tienen es un riesgo sin dirección y sin duración conocida antes de un acontecimiento binario: la apertura de Nueva York y el amanecer en América, que dirá si el fenómeno se confirma allí. Ante incertidumbre de ese tipo, el instrumento racional es la opción, que limita pérdidas sin renunciar a la posición. Los creadores de mercado, que venden esas opciones, suben su precio para cubrirse, y la volatilidad implícita se separa del movimiento del índice.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados financieros
    - derivados
    id: economista/h2/4
  - texto: Las cosméticas con peso en protección solar y maquillaje (Beiersdorf, L'Oréal) bajan ligeramente en la segunda hora, más por relato que por cifras, mientras los minoristas de cosmética reciben consultas sobre si la crema solar sigue protegiendo y cómo se ve el maquillaje con los colores nuevos.
    mecanismo: La crema solar y muchos maquillajes llevan filtros y pigmentos (dióxido de titanio, óxido de zinc) que absorben o reflejan UV-A, justo lo que ahora se ve como manchas o máscaras. El riesgo para el inversor no es que dejen de proteger, sino que el consumidor deje de usarlos por estética, y ese riesgo es nuevo y no tiene precio. El efecto en ventas reales es pequeño en la Europa de noviembre, que es temporada baja de protección solar, y por eso la caída es leve y no una venta masiva; la respuesta de las marcas, que tendrán que reformular o explicar, tardará semanas.
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - mercados financieros
    - cosmética
    - consumo
    id: economista/h2/5
  reacciona_a:
  - disruptor/h1/1
  - disruptor/h1/4
  - disruptor/h1/5
  - adolescente/h1/4
- agente: politico
  tramo: h2
  afirmaciones:
  - texto: En la segunda hora la presidencia del Consejo de la UE activa el dispositivo IPCR en modo de intercambio de información, y no en activación plena. Se abre una plataforma web con informes nacionales sobre tráfico, sanidad y aviación, y el Centro de Coordinación de la Respuesta a Emergencias de la Comisión empieza a publicar un informe de situación. No hay reunión de líderes ni una declaración política común.
    mecanismo: 'El IPCR tiene varios niveles, y el de intercambio de información puede activarlo la presidencia sin consenso de los Estados ni sin calificar el suceso. Es la opción barata, del mismo tipo que el Consejo de Seguridad Nacional español de la hora 1: coordina sin comprometerse. La activación plena llevaría a mesas redondas que acaban en conclusiones, y ningún gobierno quiere firmar un texto sobre algo cuya causa y duración desconoce. Además, la presión operativa que justifica coordinar es transfronteriza: deslumbramiento en carreteras, ensayos fluorescentes parados en talleres aeronáuticos y bulos que cruzan fronteras.'
    dato: El IPCR tiene un modo de seguimiento, un modo de intercambio de información y un modo de activación plena; la presidencia decide el nivel.
    fuente: https://www.consilium.europa.eu/en/policies/ipcr-response-to-crises
    confianza: media
    areas_afectadas:
    - union_europea
    - coordinacion_intergubernamental
    - proteccion_civil
    id: politico/h2/1
  - texto: En EE. UU. sigue siendo de noche a las 05:00 de Washington. La Casa Blanca reúne en la Sala de Situación al equipo de seguridad nacional y a asesores científicos, pero decide no emitir ninguna declaración pública hasta que amanezca en la costa este. Solo se filtra a la prensa que el presidente ha sido informado.
    mecanismo: Hablar antes de que la propia población pueda comprobarlo es arriesgado en los dos sentidos. Si confirma el fenómeno, el presidente avala lo que las redes estadounidenses están tratando como bulo europeo. Si lo minimiza, queda en ridículo al cabo de una o dos horas, cuando salga el sol. Esperar al amanecer convierte la primera declaración en un relato compartido con los votantes ('lo estamos viendo todos'), y la filtración de que ha sido informado cubre el riesgo de que parezca que el Gobierno estaba dormido. En paralelo, la hipótesis de ataque sigue abierta por canales reservados, y eso también aconseja no hablar.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - estados_unidos
    - comunicacion_institucional
    - seguridad_nacional
    id: politico/h2/2
  - texto: 'En España las consejerías de Educación de varias comunidades autónomas mandan antes del mediodía instrucciones a los centros: recreos en interior o a la sombra, ninguna salida al exterior y aviso a las familias de que no hace falta recoger a los alumnos. El Ministerio de Educación no da ninguna orden propia y se limita a pedir coordinación en la Conferencia Sectorial.'
    mecanismo: La gestión ordinaria de los centros es competencia autonómica, y las consejerías ya tienen protocolos de este tipo para olas de calor y episodios de contaminación, que solo hay que adaptar. La presión inmediata viene de las familias, que escriben a los colegios y a los grupos de clase preguntando si los hijos están bien, y de un profesorado que en la primera hora ha actuado sin instrucciones. Para un consejero, mandar una circular es la acción visible y sin coste que demuestra que gestiona. Mandar a los niños a casa, en cambio, desataría una salida masiva de padres a la calle y a la carretera justo en las horas de más deslumbramiento.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - comunidades_autonomas
    - familias
    id: politico/h2/3
  - texto: El Banco Central Europeo y el Banco de España, y con ellos otros bancos centrales con luz diurna, publican antes de que acabe la hora 2 una nota técnica que explica las marcas fluorescentes de los billetes como medida de seguridad conocida desde hace décadas. Es la primera explicación oficial que desmonta un bulo concreto, aunque sigan sin decir nada sobre el fenómeno en sí.
    mecanismo: 'El bulo de las marcas ocultas en billetes ataca directamente la confianza en el dinero, que es lo que un banco central protege antes que nada. Desmentirlo cuesta poco: las características UV de los billetes ya están descritas públicamente en los folletos para cajeros, así que la nota se apoya en material existente y no obliga a opinar sobre la causa del suceso. Es una respuesta oficial que sí compite con los bulos, porque ofrece una historia completa y verificable en lugar de un ''no sabemos''.'
    dato: El BCE describe en sus materiales para profesionales del efectivo los elementos de los billetes en euros que se iluminan bajo luz ultravioleta.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/cashier_brochure_new_20.de.pdf
    confianza: alta
    areas_afectadas:
    - bancos_centrales
    - desinformacion
    - confianza_monetaria
    id: politico/h2/4
  - texto: La Comisión Europea contacta de forma informal con las grandes plataformas para pedirles que destaquen información de autoridades sanitarias y que frenen la difusión de los bulos más virales, pero no activa el mecanismo de respuesta a crisis del artículo 36 de la Ley de Servicios Digitales.
    mecanismo: El artículo 36 exige una recomendación previa de la Junta Europea de Servicios Digitales y una decisión formal de la Comisión, y eso no cabe en dos horas. Además, aplicarlo por primera vez a un suceso sin víctimas ni amenaza identificada expondría a la Comisión a la acusación de censurar a ciudadanos que solo describen lo que ven, justo cuando la mitad de los bulos se mezclan con descubrimientos reales, como las tintas de seguridad o los blanqueantes ópticos. La vía informal da a la Comisión algo que anunciar y deja a las plataformas decidir qué retiran.
    dato: El artículo 36 de la Ley de Servicios Digitales prevé que la Comisión, a recomendación de la Junta, pueda exigir medidas a plataformas muy grandes en situación de crisis.
    fuente: https://dsa-observatory.eu/2023/02/21/the-dsas-crisis-approach-crisis-response-mechanism-and-crisis-protocols/
    confianza: media
    areas_afectadas:
    - union_europea
    - plataformas_digitales
    - desinformacion
    id: politico/h2/5
  reacciona_a:
  - medios/h1/3
  - medios/h1/4
  - adolescente/h1/2
- agente: medios
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora el vacío de imagen se rellena con fotografía ultravioleta en falso color: fotos de flores, caras con protector solar y billetes hechas con cámaras convertidas a espectro completo por aficionados y laboratorios se vuelven virales con el rótulo ''esto es lo que vemos ahora'', mezcladas con filtros y montajes generados con IA. Quienes están al sol responden en masa que ''no se parece'', y la discusión pasa de ''¿es real?'' a ''¿cuál es la imagen buena?''.'
    mecanismo: Existe un nicho previo de fotografía UV con cámaras a las que se retira el filtro de corte y se pone un filtro de paso UV; su material está archivado y listo para recircular. Pero esas cámaras traducen el UV a colores visibles arbitrarios (falso color), mientras que el ojo lo percibe ahora como un color sin nombre. La plataforma premia la primera imagen que llena el hueco, no la fiel, y la contradicción entre imagen y experiencia directa genera más conversación, no menos.
    dato: Empresas como LifePixel ofrecen conversiones comerciales de cámaras mirrorless para fotografía ultravioleta.
    fuente: https://www.lifepixel.com/shop/our-services/ultraviolet-camera-conversion/sony-mirrorless-uv-camera-conversion
    confianza: media
    areas_afectadas:
    - redes sociales
    - desinformación
    - fotografía
    - verificación
    id: medios/h2/1
  - texto: 'En EE. UU., aún de noche (las 5:00 en Nueva York), nace la contraprueba casera que empieza a romper el escepticismo antes del amanecer: encender una luz negra, una lámpara de uñas de gel, un matamosquitos o la luz de un acuario. Los noctámbulos que lo prueban publican ''acabo de encender mi lámpara de uñas y lo veo'', y el hilo de bulo o campaña coordinada se parte en dos bandos dentro de la propia audiencia estadounidense.'
    mecanismo: El escepticismo de la hora 1 se basaba en no tener estímulo UV-A de noche y en interiores con LED. Pero muchos hogares tienen fuentes de UV-A cercano por otros motivos (curado de esmalte, fiestas, insectos, acuarios). Cuando un testimonio europeo menciona que se ve al encender una luz negra, la prueba se vuelve replicable en casa sin esperar al sol, y una prueba que cada uno puede hacer pesa más que cualquier vídeo.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes sociales
    - escepticismo EE. UU.
    - comercio minorista
    - cosmética
    id: medios/h2/2
  - texto: 'Los verificadores europeos publican sus primeros desmentidos con base documental sobre las marcas en billetes: las fibras y elementos fluorescentes del euro son una medida de seguridad pública y documentada por el BCE. El bulo de ''lo que nos ocultaban'' no muere, sino que se desplaza a lo que no tiene ficha técnica a mano: etiquetas de ropa, documentos de identidad, marcas en paredes y fachadas, y la piel.'
    mecanismo: 'Por primera vez desde el suceso hay algo verificable: los bancos centrales llevan años publicando guías con lo que se ve bajo luz UV. Los verificadores priorizan lo que pueden contrastar en minutos y el desmentido funciona en ese punto concreto. Pero lo falso y novedoso se difunde más rápido que lo verificado, así que la narrativa conspirativa abandona el terreno perdido y se muda a objetos sin documentación pública, donde el desmentido tardará horas o días.'
    dato: La guía del BCE indica que bajo luz ultravioleta aparecen fibras y elementos fluorescentes en los billetes en euros. Según el estudio de Vosoughi, Roy y Aral (Science, 2018), las noticias falsas tienen un 70 % más de probabilidades de ser retuiteadas que las verdaderas.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/quick_guide_specimen_en.pdf ; https://mitsloan.mit.edu/press/false-news-spreads-widely-and-easily
    confianza: alta
    areas_afectadas:
    - verificación
    - desinformación
    - bancos centrales
    - medios tradicionales
    id: medios/h2/3
  - texto: 'Las televisiones convierten a los afáquicos en el formato estrella de la segunda hora, y con ellos aparece la figura del falso vidente: personas que dicen ''yo siempre lo he visto'' (influencers espirituales, supuestos ''niños índigo'' o ''semillas estelares'', vendedores de terapias) sin haber pasado por una cirugía de cristalino, y que ganan audiencia contando el fenómeno como un despertar.'
    mecanismo: Los afáquicos dan a la televisión lo que no tiene, que es una autoridad con historia personal. Pero la condición no se verifica en directo y la producción no tiene tiempo de comprobarla. El marco de 'algunos ya lo veían' es justo el que necesitan las comunidades esotéricas, que tienen audiencias propias y un relato preparado (evolución, ascensión), y que se cuelan por la misma puerta que abrieron los informantes legítimos.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios tradicionales
    - desinformación
    - salud
    - comunidades esotéricas
    id: medios/h2/4
  - texto: Se hace viral la captura de pantalla de chatbots de IA respondiendo que 'los humanos no pueden ver el ultravioleta', y se usa en EE. UU. como prueba de que el fenómeno es falso, mientras en Europa circula como prueba de que 'la IA nos oculta la verdad'.
    mecanismo: 'Mucha gente consulta primero a un asistente de IA en vez de a un buscador. Los modelos responden con su conocimiento de entrenamiento (la visión humana termina en torno a 400 nm) y, sin fuentes de última hora que les contradigan, desmienten con seguridad lo que el usuario vive. Una captura de una máquina que contradice tus ojos sirve a los dos bandos: al escéptico como argumento de autoridad y al conspirativo como prueba de censura.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes sociales
    - inteligencia artificial
    - escepticismo EE. UU.
    - desinformación
    id: medios/h2/5
  reacciona_a:
  - oftalmologa/h1/1
  - disruptor/h1/2
- agente: oftalmologa
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora los afáquicos consultados por medios y consultas dan un relato que solo coincide a medias con el del resto: confirman la banda y el blanco violáceo de fondo, pero muchos dicen que ahora ven además matices que antes no tenían, y otros que para ellos el cambio apenas existe. Su papel pasa de testigos que ya lo sabían a grupo de control, y su valor como informantes baja en los medios aunque sube en la investigación clínica.'
    mecanismo: 'Antes del suceso, el afáquico percibía el UV solo a través de la cola de sensibilidad de sus conos de siempre, sobre todo los S, así que lo veía como un blanco azulado o violeta dentro de su espacio de color habitual y sin un tono nuevo. El suceso añade la percepción del UV-A como colores nuevos, que es otra cosa: un canal cromático, no solo más luz llegando a los mismos conos. Por eso el afáquico reconoce dónde está el UV pero no puede describir el color nuevo mejor que nadie. Los que tenían el ojo afáquico en un solo lado comparan los dos ojos y dan el relato más útil.'
    dato: Sin cristalino, la sensibilidad visual se extiende hasta unos 300 nm y el UV se describe como blanco azulado o violáceo; se cita el caso de Monet tras su operación de cataratas.
    fuente: https://en.wikipedia.org/wiki/Aphakia ; https://www.healio.com/news/optometry/20230518/blog-the-link-between-uv-light-iols-and-claude-monets-water-lilies
    confianza: media
    areas_afectadas:
    - salud
    - medios
    - ciencia
    id: oftalmologa/h2/1
  - texto: 'Se invierte en parte el gradiente por edad de la primera hora: los mayores operados de cataratas con lente intraocular moderna apenas ven los colores nuevos, menos que sus coetáneos sin operar con cristalino aún claro, y las consultas de oftalmología reciben llamadas de operados que creen que la operación les ha quitado algo o que la lente está mal.'
    mecanismo: Desde los años ochenta prácticamente todas las lentes intraoculares llevan un cromóforo que absorbe el UV, y muchas además filtran el azul. Funcionan como unas gafas UV400 dentro del ojo y no se pueden quitar. En España se hacen cientos de miles de operaciones de cataratas al año, así que hay millones de personas mayores con el interruptor apagado de forma permanente. Solo los portadores de lentes antiguas o de modelos sin filtro (una minoría) quedan en el grupo de los que sí ven, lo que explica por qué algunos operados ven y otros no.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - salud
    - sanidad_publica
    - mayores
    id: oftalmologa/h2/2
  - texto: 'Las sociedades de oftalmología y los colegios de ópticos emiten en esta hora el primer aviso práctico concreto: las gafas de sol baratas compradas a toda prisa sin marcado CE o sin filtro UV400 no apagan el UV ni alivian el deslumbramiento, y pueden empeorarlo. El aviso se centra en comprobar la etiqueta, no en la causa del fenómeno.'
    mecanismo: 'El tinte oscuro y el filtro UV son cosas independientes: una lente puede oscurecer el visible y dejar pasar el UV-A. Si oscurece, la pupila se dilata algo y entra más UV-A por el centro del campo visual, justo lo contrario de lo que se busca. Con los expositores de gama baja vaciándose y gente comprando en bazares y gasolineras, la queja de que me he comprado gafas y sigo viendo lo raro y me molesta llega a las ópticas en la primera hora. Es el único consejo que un profesional puede dar con seguridad sin saber nada de la causa, así que es el primero que sale.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - consumo
    - comercio
    id: oftalmologa/h2/3
  - texto: 'El gesto viral de quitarse las gafas de ver para comprobar el UV produce resultados distintos según la graduación: los hipermétropes sin corregir describen los bordes UV más nítidos que el resto, y los miopes los ven aún más emborronados. Esto alimenta testimonios contradictorios y la sospecha de que el fenómeno es un trastorno de enfoque.'
    mecanismo: Por aberración cromática longitudinal, el UV-A enfoca por delante de la retina cuando el ojo enfoca el visible. En un miope sin corrección la imagen visible ya cae por delante, así que la capa UV queda aún más desenfocada. En un hipermétrope la imagen visible cae por detrás y el desplazamiento del UV hacia delante la acerca a la retina, de modo que esa capa sale relativamente más nítida. Al quitarse las gafas cada uno ve una combinación distinta de desenfoque visible y UV, y lo atribuye al fenómeno.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - redes_sociales
    id: oftalmologa/h2/4
  - texto: 'Las urgencias oftalmológicas de las zonas con sol registran en la segunda hora un pico de consultas por halos, visión borrosa y fatiga, casi todas sin patología, y los hospitales empiezan a hacer triaje telefónico y a publicar criterios de cuándo acudir: dolor intenso, pérdida de visión en un ojo, cortina o destellos.'
    mecanismo: 'El halo por aberración cromática y la fatiga en exteriores se parecen a síntomas reales de urgencia (desprendimiento de retina, glaucoma agudo, uveítis), y la gente no puede distinguirlos. Como el canon dice que el deslumbramiento remite sin daño, la tarea clínica es separar lo poco que coincide por azar con una patología real del ruido del fenómeno. La forma más barata de hacerlo es fijar los signos de alarma clásicos que el fenómeno no produce: dolor intenso, pérdida brusca de visión, síntomas en un solo ojo.'
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - salud
    - sanidad_publica
    id: oftalmologa/h2/5
  reacciona_a:
  - economista/h1/4
- agente: adolescente
  tramo: h2
  afirmaciones:
  - texto: 'En el recreo de las once y media mis amigas y yo salimos al patio con espejitos de bolso y con la pantalla del móvil apagada para mirarnos la cara al sol, y cuando eso no basta nos usamos las unas a las otras de espejo: ''dime de verdad cómo se me ve''. Así es como descubrimos que la crema con color y algunos correctores se ven como manchas raras y que el iluminador de alguna brilla muchísimo.'
    mecanismo: En el baño con la luz de siempre no se ve nada, así que la duda de cómo nos vemos sigue sin resolverse. La única forma de comprobarlo es salir donde da el sol. Un espejo pequeño fuera sí devuelve parte de esos colores, pero como no te fías, acabas preguntando a una amiga, y eso hace que la opinión de las demás sobre tu cara pese todavía más que antes.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - adolescencia
    - imagen_personal
    - cosmetica
    - salud_mental
    id: adolescente/h2/1
  - texto: 'En una hora las gafas de sol pasan de ser lo que todo el mundo quería a ser casi de pringados dentro de mi grupo: lo que se lleva es aguantar sin ellas y decir lo que ves, y quien se las pone mucho rato es ''el que no se entera''. Las gafas se quedan para los que lo pasan mal con la luz, que se ponen y se quitan como para comprobar algo.'
    mecanismo: Ya se sabe que con las gafas de sol los colores nuevos desaparecen. Si lo que todos comentan es lo que ve cada uno, llevar gafas te deja fuera de la conversación. Entre nosotros lo que cuenta es poder decir 'yo lo he visto', así que aguantar el deslumbramiento se vuelve una forma de demostrar que estás dentro, aunque luego te duelan los ojos.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - adolescencia
    - consumo
    - gafas_de_sol
    - salud_visual
    id: adolescente/h2/2
  - texto: 'En el patio se empieza a señalar la ropa: las zapatillas blancas nuevas, las camisetas recién lavadas y las etiquetas o logos que antes no se veían destacan muchísimo, y sale un ranking de quién ''brilla'' y quién no. Hay risas, pero también alguna se agobia porque se le nota una mancha o un remiendo que antes no se veía.'
    mecanismo: Lo que se lava con detergente con blanqueante y algunas tintas de las marcas se ven distintas con los colores nuevos, y cada uno lleva ropa lavada de forma diferente en su casa. Eso convierte algo que no controlas, el detergente de tu madre o lo vieja que es tu ropa, en algo que todos pueden ver y comentar, y en clase cualquier diferencia visible acaba siendo motivo de broma.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - adolescencia
    - textil
    - convivencia_escolar
    - desigualdad
    id: adolescente/h2/3
  - texto: Antes del recreo llega un aviso por la aplicación del instituto y por megafonía diciendo que el recreo será dentro o en el porche 'por precaución por el deslumbramiento'. Mucha gente sale igual, se pega a las ventanas del pasillo o se escapa al patio, y los profes de guardia no lo impiden mucho.
    mecanismo: La dirección no tiene instrucciones de la Consejería y le llegan mensajes de padres preocupados. Lo único que puede decir sin comprometerse es lo de la luz, igual que hace tráfico. Pero los profes también quieren mirar y nadie les ha explicado por qué es peligroso, así que la norma se cumple a medias y los que más se juntan son los que quieren seguir mirando.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - adolescencia
    - familias
    - gestion_publica
    id: adolescente/h2/4
  - texto: En el grupo de familia y en el de clase empiezan a circular audios de 'una prima que es enfermera' diciendo que si miras mucho rato te quedas ciega o que esto se queda para siempre. Mi madre me pide que no salga, mi abuela dice que ella casi no ve nada raro y no se cree lo que le cuento, y yo me siento entre asustada y sin que me crean.
    mecanismo: Nadie oficial ha explicado nada y un audio con voz de alguien de confianza llega antes que cualquier aviso. En casa además cada uno ve el color con distinta fuerza según la edad, así que cuando le digo a mi abuela lo vivo que lo veo piensa que exagero. Eso me empuja a confiar más en lo que dicen mis amigos y las redes que en mi familia, justo cuando más miedo da.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - desinformacion
    - familias
    - adolescencia
    - salud_mental
    id: adolescente/h2/5
  reacciona_a: []
- agente: disruptor
  tramo: h2
  afirmaciones:
  - texto: 'En la hora 2 los primeros americanos que viven el suceso en directo no son estadounidenses, sino brasileños, uruguayos y argentinos de la costa atlántica, que van a trabajar a las 7:00 con el sol ya alto. Su testimonio en portugués y español entra en las redes latinas de EE. UU. y el marco de bulo europeo se resquebraja antes de que amanezca en Nueva York: el escepticismo deja de ser americano y pasa a ser solo del norte.'
    mecanismo: A las 10:00 UTC son las 7:00 en São Paulo y Buenos Aires (UTC-3), y en noviembre, casi en el solsticio austral, allí amanece hacia las 5:15, mientras que en Nueva York son las 5:00 y aún es de noche. Hay radiación creciente justo en la hora punta del transporte, con millones de personas en la calle, en autobuses y en motos sin parabrisas. Las diásporas brasileña y latina en EE. UU. reciben esos mensajes de familiares directos, un canal de confianza que los vídeos europeos de desconocidos no tenían. Un testigo cercano y en tu idioma desactiva la sospecha de histeria regional europea que se fijó en la primera hora.
    dato: 'Amanecer en São Paulo el 12 de noviembre de 2026: 5:14 hora de Brasilia (UTC-3).'
    fuente: https://sunrise-sunset.org/br/moema
    confianza: alta
    areas_afectadas:
    - medios
    - redes sociales
    - geopolitica
    - America Latina
    - Estados Unidos
    id: disruptor/h2/1
  - texto: 'Se rompe la idea de que el interior es un refugio: en cocinas de bares, obradores, carnicerías, panaderías, salones de uñas, discotecas y cajas de comercios, el problema no es la ventana sino aparatos que emiten UV-A a propósito. Los mataínsectos eléctricos de 365 nm y las lámparas de curado de gel se ven como focos intensos de un color nuevo, y el personal los apaga o los tapa. Así, en plena mañana, la hostelería y la alimentación se quedan sin su control de insectos obligatorio.'
    mecanismo: Los mataínsectos de lámpara actínica se instalan en zonas donde se manipulan alimentos precisamente porque el UV-A atrae a los insectos y el ojo humano apenas lo veía, así que podían estar encendidos todo el día sin molestar. Ahora son la fuente de UV-A más intensa del local, a la altura de la vista y en espacios iluminados con LED donde no hay nada que compita con ellos. Lo mismo ocurre con las lámparas de uñas, las de comprobar billetes y la luz negra de ocio. El apagado es una decisión individual e inmediata del trabajador, y nadie piensa en ese momento que el plan de control de plagas del APPCC daba por hecho que esa luz no molestaba a nadie.
    dato: Las lámparas comerciales para mataínsectos tienen un pico de emisión en 365 nm (UV-A) y se recomiendan para zonas donde se sirven, preparan o consumen alimentos.
    fuente: https://uk.rs-online.com/web/p/fly-killer-lights/4730840
    confianza: media
    areas_afectadas:
    - hosteleria
    - seguridad alimentaria
    - comercio
    - trabajo en interiores
    id: disruptor/h2/2
  - texto: 'En los mercados y comercios a pleno sol de la India, Oriente Medio, África y el sur de Europa, cualquiera puede distinguir a simple vista el papel de los billetes, y los vendedores empiezan a rechazar los que se ven raros. Lo que se dispara no es la detección de falsos, sino los falsos positivos: billetes auténticos que pasaron por la lavadora o estuvieron en contacto con papel o ropa tratada con blanqueantes ópticos se ven como el papel de oficina y se tratan como sospechosos.'
    mecanismo: El papel de los billetes de seguridad, como el del euro, se fabrica sin blanqueantes ópticos para que bajo UV no brille, mientras que el papel comercial y los tejidos lavados con detergente sí los llevan. Hasta ahora esa diferencia solo la veían las lámparas de las cajas; ahora la ve cualquiera a la luz del sol. Pero la gente no sabe qué aspecto debe tener un billete legítimo en el nuevo canal, y los billetes sucios o lavados han absorbido blanqueantes. Esto entra en el marco de lo que nos ocultaban (h1-16) y provoca discusiones en el pago en efectivo, sobre todo en la economía informal, que vive del billete pequeño y gastado.
    dato: La guía del BCE indica que bajo luz ultravioleta el papel del billete en euros no brilla y que las fibras incrustadas aparecen en rojo, azul y verde.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/Quick_Guide_EN_Specimen.pdf
    confianza: media
    areas_afectadas:
    - efectivo
    - comercio minorista
    - economia informal
    - bancos centrales
    - bulos
    id: disruptor/h2/3
  - texto: 'En la hora 2 aparecen las primeras imágenes del fenómeno, hechas por una comunidad marginal de fotógrafos ultravioleta, astrofotógrafos y peritos forenses con cámaras de espectro completo y filtros de paso UV. Pero no resuelven la falta de pruebas: como son imágenes en falso color, cada una asigna al UV un tono distinto, nadie que las ve las reconoce como lo que percibe y se convierten en munición para los dos bandos.'
    mecanismo: Un sensor de silicio sin el filtro interno que corta el UV y el infrarrojo sí registra UV-A, pero lo traduce a los canales RGB según la sensibilidad residual de su matriz de Bayer y un balance de blancos arbitrario, de modo que el color final es una convención del fotógrafo. Estos usuarios ya existían y tienen el equipo en casa, así que son los únicos capaces de responder a la frustración de que la cámara no lo coge (h1-03). Cuando una imagen pinta el cielo de magenta y otra de amarillo, los escépticos lo leen como manipulación y los creyentes como prueba. La falta de pruebas pasa a ser una guerra sobre qué color es el verdadero.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios
    - redes sociales
    - verificacion
    - fotografia
    - ciencia
    id: disruptor/h2/4
  - texto: Quienes en zonas de mucho sol (Golfo, sur de Asia, África oriental) buscan alivio a la sombra de árboles, toldos o soportales descubren que el deslumbramiento apenas baja, porque el cielo entero brilla en el nuevo color. El alivio no lo da la sombra, sino un techo o un cristal. Se produce un desplazamiento masivo e improvisado de trabajadores al aire libre hacia interiores, porches cerrados, vehículos y centros comerciales, que aún no figura en las cifras de productividad.
    mecanismo: La dispersión de Rayleigh crece mucho al acortarse la longitud de onda, así que el cielo dispersa el UV-A con mucha más fuerza que el visible y una gran parte del UV que llega al suelo es difusa, no directa. Una sombra tapa el disco solar pero no la bóveda celeste, al contrario de lo que la gente espera por su experiencia con el visible. Eso amplía el refugio del coche parado (h1-10) a cualquier espacio con techo y vidrio laminado o LED, y convierte los centros comerciales con aire acondicionado y luz artificial del Golfo y la India en refugios espontáneos del mediodía.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - trabajo al aire libre
    - sector informal
    - comercio
    - espacio publico
    - salud laboral
    id: disruptor/h2/5
  reacciona_a:
  - medios/h1/2
  - medios/h1/1
  - oftalmologa/h1/4

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
  metricas:
    alarma_social: valor
    respuesta_gobiernos: valor
    impacto_economico: valor
    adaptacion: valor
