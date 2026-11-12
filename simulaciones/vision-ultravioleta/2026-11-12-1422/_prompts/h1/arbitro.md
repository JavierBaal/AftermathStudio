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
Hora 1 (PT1H desde el suceso)
Estado del mundo anterior:
Primer tramo.

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h1
  afirmaciones:
  - texto: En la primera hora, las bolsas europeas (las únicas grandes plazas abiertas a las 10:00 de Madrid) no se desploman. Lo que hay es una ráfaga de interrupciones por volatilidad en valores concretos y diferenciales de compraventa más anchos, sin cierre general del mercado.
    mecanismo: El suceso no destruye ningún flujo de caja de forma inmediata y los operadores trabajan en interiores, donde casi no llega UV-A, así que siguen funcionando con normalidad. Los algoritmos que leen titulares reaccionan en segundos y empujan precios fuera de los corredores de cada valor. Eso activa subastas de al menos dos minutos valor a valor, no una suspensión del mercado. Los creadores de mercado ensanchan los diferenciales porque no saben valorar el riesgo de un fenómeno sin causa ni duración conocidas. Tokio ya ha cerrado y Wall Street abre a las 15:30 de Madrid, así que en Europa se forma el precio en solitario y con poca liquidez transfronteriza.
    dato: En Xetra, si un precio sale del corredor estático o dinámico, la negociación continua pasa a una subasta de al menos dos minutos que termina en un momento aleatorio. El valor no queda suspendido.
    fuente: https://www.deutsche-boerse.com/dbg-en/media/news-stories/explainers/financial-market-know-how/explainer-protection
    confianza: media
    areas_afectadas:
    - mercados_financieros
    - bolsas_europeas
    - liquidez
    id: economista/h1/1
  - texto: EssilorLuxottica y otros cotizados de óptica y gafas de sol suben con fuerza en París y Milán durante la primera hora, mientras que el resto del Eurostoxx se mueve de lado o baja ligeramente.
    mecanismo: 'Es la única lectura evidente del suceso: si hay deslumbramiento, harán falta filtros UV. El dinero rápido (fondos sistemáticos, minoristas, opciones de compra) se concentra en el líder del sector. Un líder con una cuota de mercado alta y su propia red de tiendas absorbe la mayor parte de esa narrativa. Es una subida especulativa: nadie sabe aún si el fenómeno es permanente ni si las gafas actuales filtran lo que ahora molesta.'
    dato: EssilorLuxottica controla en torno al 25 % del mercado mundial de gafas, según Euromonitor, con 26.500 millones de euros de ingresos en 2024.
    fuente: https://fortune.com/europe/2025/06/04/essilorluxottica-ray-ban-oakley-med-tech-vision/
    confianza: media
    areas_afectadas:
    - mercados_financieros
    - optica
    - consumo
    id: economista/h1/2
  - texto: 'El golpe a la productividad en la primera hora es geográficamente desigual. En la Europa de noviembre apenas se nota, porque es media mañana y el sol está bajo. Se concentra en el trabajo al aire libre de las franjas de mediodía y primera tarde con más radiación: Golfo Pérsico, África subsahariana y sur de Asia.'
    mecanismo: La fatiga visual depende de cuánto UV-A llega al ojo, y eso depende de la latitud, la estación y la hora solar. A las 09:00 UTC es mediodía o primera tarde en Oriente Medio, el este de África y la India, que tienen una radiación alta y mucha mano de obra al aire libre en construcción, agricultura y logística. En España, en noviembre, el índice UV ronda 3-4 como máximo. América está de noche y Asia oriental, en su tarde. El sector afectado en esa hora es sobre todo el informal, que no figura en las estadísticas inmediatas.
    dato: 'Índice UV de Madrid en noviembre: alrededor de 4 (máximo mensual); en los meses de invierno, en torno a 3-4.'
    fuente: https://nomadseason.com/uv-index/spain/madrid/madrid.html
    confianza: media
    areas_afectadas:
    - empleo
    - productividad
    - construccion
    - agricultura
    - economias_emergentes
    id: economista/h1/3
  - texto: En las tiendas físicas abiertas (ópticas, gasolineras, grandes superficies) y en el comercio electrónico se dispara la compra de gafas de sol. En las zonas soleadas que están a mediodía, las existencias de gama baja se agotan localmente en una o dos horas, pero esa hora no hay escasez sistémica.
    mecanismo: El incentivo individual es inmediato y el producto es barato, así que se compra por precaución aunque haya dudas sobre si sirve. El inventario de tienda está dimensionado para la demanda de temporada, que en el hemisferio norte en noviembre es baja. Por eso los primeros que compran vacían los expositores, mientras que los almacenes regionales y los centros de distribución aún tienen stock. La escasez real dependerá de la reposición desde las fábricas de Asia, que no se nota en una hora.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - consumo
    - comercio_minorista
    - cadena_de_suministro
    id: economista/h1/4
  - texto: Los futuros de los índices estadounidenses y los activos refugio (bonos alemanes, franco suizo, oro) se mueven con moderación. No hay una huida masiva hacia la seguridad, porque el mercado trata el suceso como un choque raro, de dirección incierta, y no como recesivo.
    mecanismo: 'Para que haya una huida masiva hacia los refugios hace falta un mecanismo que reduzca la demanda agregada o el crédito, y en la primera hora nadie lo ve: la gente sigue viendo y en interiores trabaja con normalidad. Las mesas institucionales recortan exposición bruta por incertidumbre, sin cambiar de sentido sus posiciones, y esperan a que la apertura de Nueva York confirme o desmienta. El riesgo mayor que valoran los analistas es si cambia la demanda de iluminación, pantallas, pinturas y textiles, y eso aún no tiene precio.'
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - mercados_financieros
    - renta_fija
    - divisas
    - materias_primas
    id: economista/h1/5
  reacciona_a: []
- agente: politico
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora la respuesta oficial es asimétrica por husos horarios: hablan Europa, África y Oriente Medio; Asia oriental reacciona a medias, y en América no hay más que avisos internos, porque sus gobiernos se están despertando.'
    mecanismo: 'Las 10:00 de Madrid son las 09:00 UTC: las 04:00 en Washington, de madrugada en todo el continente americano, y anochecer en Pekín y Tokio. Con poca gente en el mar o en exteriores, los gobiernos americanos no tienen urgencia que justifique despertar a un portavoz para hablar de algo que no entienden. Además, el deslumbramiento solo crea problemas donde es de día, así que la presión inmediata se concentra en Europa y África. El primer marco político mundial lo fijan, por tanto, gobiernos europeos y africanos, no Washington ni Pekín.'
    dato: Momento cero a las 09:00 UTC; Washington en UTC-5 en noviembre.
    fuente: ''
    confianza: alta
    areas_afectadas:
    - gobiernos
    - comunicacion_publica
    - geopolitica
    id: politico/h1/1
  - texto: Los gobiernos con luz diurna usan el deslumbramiento como su única palanca operativa. Antes de una hora, las autoridades de tráfico y protección civil piden reducir la conducción y se refuerza la vigilancia en carreteras, sin que nadie se pronuncie sobre el fenómeno en sí.
    mecanismo: Un gobierno sin causa ni pronóstico necesita una acción que pueda anunciar y que no le comprometa. El deslumbramiento en exteriores es un riesgo conocido, con protocolos de tráfico y protección civil ya escritos y responsables claros. Así el ministro aparece gestionando sin tener que explicar lo inexplicable. Si sube la siniestralidad vial del mediodía, la medida queda justificada de inmediato.
    dato: Los análisis de la NHTSA identifican el deslumbramiento solar como factor de visibilidad en accidentes de tráfico.
    fuente: https://www.fcsm.gov/assets/files/docs/2005FCSM_Choi_Singh_IVA.pdf
    confianza: media
    areas_afectadas:
    - trafico
    - proteccion_civil
    - comunicacion_publica
    id: politico/h1/2
  - texto: En España se convoca de urgencia el Consejo de Seguridad Nacional o su comité de situación, pero no se declara ninguna situación de interés para la Seguridad Nacional en esta primera hora.
    mecanismo: La Ley 36/2015 da un cauce de coordinación interministerial ya probado con la COVID y los apagones. Activarlo es barato y protege políticamente al Gobierno. Declarar formalmente una situación de interés, en cambio, exige un real decreto y concretar medidas y recursos. No hay daño medible que lo justifique y el Gobierno no quiere fijar una calificación que tendría que corregir si el fenómeno resulta inocuo.
    dato: La Ley 36/2015 regula el Consejo de Seguridad Nacional y la declaración de situación de interés para la Seguridad Nacional mediante real decreto.
    fuente: https://www.boe.es/buscar/pdf/2015/BOE-A-2015-10389-consolidado.pdf
    confianza: media
    areas_afectadas:
    - gobierno_espana
    - seguridad_nacional
    - coordinacion_interministerial
    id: politico/h1/3
  - texto: La OMS emite una nota breve de que está vigilando la situación, pero ni convoca formalmente el Comité de Emergencias del RSI ni declara una emergencia de salud pública de importancia internacional.
    mecanismo: 'El procedimiento del Reglamento Sanitario Internacional exige que los Estados notifiquen el evento, una evaluación y reunir a un comité de expertos, lo que lleva días. Además, el fenómeno no encaja en sus criterios: no se propaga, no hay agente ni contagio, no hay muertos y no cabe restringir viajes o comercio. La OMS no quiere estrenar sus atribuciones de 2024 con algo que quizá no sea un problema sanitario.'
    dato: El artículo 12 del RSI (2005) prevé que el Director General consulte al Comité de Emergencias antes de determinar una emergencia de salud pública de importancia internacional.
    fuente: https://apps.who.int/gb/wgihr/pdf_files/wgihr2/A_WGIHR2_Reference_document-sp.pdf
    confianza: media
    areas_afectadas:
    - organismos_internacionales
    - salud_publica
    id: politico/h1/4
  - texto: Los servicios de inteligencia y defensa de las grandes potencias abren en privado la hipótesis de un ataque, pero ningún gobierno acusa públicamente a otro en esta primera hora.
    mecanismo: Cualquier alteración masiva e inexplicada obliga por protocolo a descartar la autoría hostil, y los mandos se ponen en alerta. Pero el efecto es simultáneo y alcanza a todos, incluidas las poblaciones y los ejércitos de los posibles culpables. Así se queda sin sentido la lógica atacante-víctima, y acusar sin pruebas expondría al gobierno que lo haga a un ridículo diplomático. La sospecha va por canales internos, no por declaraciones.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - defensa
    - inteligencia
    - geopolitica
    id: politico/h1/5
  reacciona_a: []
- agente: medios
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora el fenómeno se vuelve viral precisamente porque no se puede grabar: millones de vídeos y fotos de móvil no muestran nada distinto, y el formato dominante pasa a ser el testimonio hablado y el texto (gente intentando describir colores que no tienen nombre), no la imagen.'
    mecanismo: 'Los sensores de los móviles llevan filtros que cortan el ultravioleta y su procesado está calibrado para la visión humana anterior, así que la prueba visual que las redes necesitan para validar un suceso no existe. La frustración de ''lo estoy viendo y la cámara no lo coge'' se convierte en contenido en sí mismo y alimenta a la vez dos relatos opuestos: ''es real y no lo podemos enseñar'' y ''es una alucinación colectiva''.'
    dato: Los sensores de cámara de consumo incorporan filtros que bloquean el UV y no registran el UV-A tal como ahora lo percibe el ojo.
    fuente: https://www.uniquephoto.com/community/qa/can-a-smartphone-camera-capture-uv-fluorescence-around-340-350-nm
    confianza: alta
    areas_afectadas:
    - redes sociales
    - medios audiovisuales
    - verificación
    id: medios/h1/1
  - texto: 'La narrativa de la primera hora es europea y africana: la viven a plena luz de la mañana, mientras que en América es de madrugada y en Asia oriental ya ha anochecido, y allí muchos no notan nada todavía y responden con escepticismo a lo que llega desde Europa.'
    mecanismo: A las 10:00 de Madrid son en torno a las 4:00 en Nueva York y las 18:00 en Tokio; sin luz solar apenas hay UV-A ambiente, así que la experiencia diferencial depende de la hora local. El primer ciclo de contenido se genera en husos con sol, y en los husos a oscuras el suceso llega primero como rumor ajeno, lo que siembra la sospecha de montaje o de histeria mediática regional.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes sociales
    - geopolítica informativa
    - confianza institucional
    id: medios/h1/2
  - texto: Antes de que acabe la hora circulan varias explicaciones falsas con gran alcance (antenas 5G, fumigaciones, una tormenta solar ocultada, un experimento militar o farmacéutico), y superan en difusión a los mensajes de prudencia de oftalmólogos y autoridades.
    mecanismo: Hay un vacío explicativo total, ya que nadie conoce la causa, y las cuentas conspirativas tienen marcos narrativos previos que solo necesitan recolocar. Lo falso y novedoso se comparte más y más rápido que lo verificado, y un '¿todavía no sabemos nada?' oficial no compite con una historia completa.
    dato: En Twitter, las noticias falsas tenían un 70% más de probabilidad de ser retuiteadas y las verdaderas tardaban unas seis veces más en llegar a 1.500 personas.
    fuente: https://news.mit.edu/2018/study-twitter-false-news-travels-faster-true-stories-0308
    confianza: alta
    areas_afectadas:
    - desinformación
    - salud pública
    - plataformas
    id: medios/h1/3
  - texto: 'Surge una ola de contenido de descubrimiento que deriva en el bulo de ''lo que nos ocultaban'': gente mostrando marcas en billetes, envases, documentos, ropa o paredes que antes no veía, interpretadas como mensajes secretos o vigilancia.'
    mecanismo: Muchos objetos cotidianos llevan tintas, blanqueadores ópticos o tratamientos que solo se distinguen en ultravioleta y que tienen razones técnicas banales (seguridad antifalsificación, detergentes, protectores solares). Sin ese contexto, el hallazgo repentino de patrones invisibles encaja perfecto con el esquema conspirativo y es fácil de contar sin necesidad de imagen.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - desinformación
    - consumo
    - banca
    - seguridad documental
    id: medios/h1/4
  - texto: 'Los medios tradicionales europeos abren especiales en directo en menos de una hora pero sin material propio: rellenan con tertulias, oftalmólogos y lectura de redes, y amplifican sin querer los bulos al citarlos para desmentirlos.'
    mecanismo: Un suceso global sin imagen ni fuente oficial deja a la televisión sin su recurso principal; la presión por emitir hace que las redes pasen a ser la fuente, y el desmentido en directo repite el contenido falso ante una audiencia mayor que la original. Los verificadores no tienen todavía nada con que contrastar, porque ningún organismo ha publicado nada.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios de comunicación
    - verificación
    - comunicación institucional
    id: medios/h1/5
  reacciona_a: []
- agente: oftalmologa
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora, las personas afáquicas o con lentes intraoculares que dejan pasar UV son las únicas que pueden describir con criterio lo que todos ven: para ellas no es un color del todo nuevo, sino una versión más intensa del blanco azulado o violáceo que ya percibían. Las consultas de oftalmología y los medios empiezan a buscarlas como informantes de referencia.'
    mecanismo: El cristalino natural absorbe casi todo el UV antes de que llegue a la retina; sin él, el UV llega a los conos (sobre todo a los S, más sensibles a esas longitudes) y se percibe como blanquecino azulado o violeta. Esa experiencia previa es el único marco de comparación disponible para describir el fenómeno en tiempo real.
    dato: En ojos afáquicos o con implantes que transmiten UV, longitudes de onda de hasta unos 315 nm llegan a la retina y se perciben como azul o violeta blanquecino; los conos S son los más sensibles al UV.
    fuente: https://2020mag.com/article/uv-vision-seeing-invisible-ultraviolet
    confianza: media
    areas_afectadas:
    - salud
    - medios
    - ciencia
    id: oftalmologa/h1/1
  - texto: Los objetos que destacan en UV se ven con un halo o borde ligeramente desenfocado respecto a su contorno visible, y mucha gente lo interpreta en la primera hora como un problema de vista y no como un color nuevo.
    mecanismo: 'Aberración cromática longitudinal: el ojo refracta más las longitudes de onda cortas, así que el UV-A enfoca por delante de la retina cuando el ojo enfoca el visible. El sistema de acomodación está calibrado para el visible y no corrige ese desfase, de modo que la capa UV de la imagen llega algo borrosa.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - vida_cotidiana
    id: oftalmologa/h1/2
  - texto: Quien lleva gafas graduadas con filtro UV o gafas de sol UV400 apenas ve los colores nuevos mientras las lleva puestas; quitárselas y ponérselas se convierte en el gesto para comprobar qué es UV y qué no, y las gafas UV400 pasan a ser el alivio inmediato del deslumbramiento en exteriores.
    mecanismo: Los filtros UV400 bloquean la radiación por debajo de 400 nm, que es justo la banda UV-A que ahora estimula la retina. Al cortarla, devuelven la visión al estado anterior y eliminan la fuente del deslumbramiento, sin afectar al visible.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - salud
    - consumo
    - vida_cotidiana
    id: oftalmologa/h1/3
  - texto: Dentro de casas y oficinas con iluminación LED el cambio es casi imperceptible; donde se nota es al mirar por la ventana o salir a la calle. En coches el parabrisas atenúa buena parte del efecto, mientras que las ventanillas laterales lo dejan pasar más.
    mecanismo: Las lámparas LED blancas emiten muy poca radiación por debajo de 400 nm, así que en interiores casi no hay UV-A que ver. El vidrio común de ventana deja pasar gran parte del UV-A, y el parabrisas laminado lleva una lámina intermedia que lo absorbe en mayor proporción que el vidrio templado de las ventanillas.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - vida_cotidiana
    - transporte
    - trabajo
    id: oftalmologa/h1/4
  - texto: 'La intensidad de los colores nuevos varía con la edad: niños y jóvenes los describen más vivos y las personas mayores, más apagados. Las primeras comparaciones entre generaciones dentro de una misma familia generan desconcierto.'
    mecanismo: El cristalino amarillea y se opacifica con los años, lo que aumenta su absorción de longitudes de onda cortas. Aunque ahora todos perciben UV-A, la cantidad que llega a la retina depende de lo transparente que sea cada cristalino, que es máxima en la infancia.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - familia
    - vida_cotidiana
    id: oftalmologa/h1/5
  reacciona_a: []
- agente: adolescente
  tramo: h1
  afirmaciones:
  - texto: 'A las 10 estoy en clase de mates y la clase se para sola: nadie atiende y la profe acaba dejando que miremos por la ventana o que salgamos al patio un rato, aunque nadie le ha dicho que lo haga.'
    mecanismo: Le pasa a ella igual que a nosotros, así que no tiene a nadie por encima que le diga que es normal. Treinta adolescentes gritando que ven colores raros es imposible de controlar, y dejarnos mirar es la forma más rápida de que nos calmemos. En el patio además da el sol y ahí es donde más se nota.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - vida_cotidiana
    id: adolescente/h1/1
  - texto: En mi insti el móvil está prohibido en clase, pero en menos de diez minutos todo el mundo lo ha sacado y nadie nos lo quita; lo primero que hacemos es escribir a casa y al grupo de clase.
    mecanismo: Ante algo que no entiendes, lo primero es saber si a tu familia y a tus amigos les pasa lo mismo. Los profes también están mirando sus móviles, así que no tienen autoridad para quitárnoslos, y los padres empiezan a escribir preguntando si estamos bien.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - educacion
    - redes_sociales
    - familia
    id: adolescente/h1/2
  - texto: En la primera hora lo que más se sube a TikTok e Instagram son vídeos de gente apuntando con el móvil a cosas, y la gente se frustra porque en la pantalla no sale lo que ven sus ojos; los comentarios se llenan de que si es falso o si es que la cámara no lo coge.
    mecanismo: 'Lo natural es grabarlo para compartirlo, pero la cámara del móvil está hecha para enseñar los colores de siempre, así que el vídeo sale normal. Eso genera la primera tendencia: vídeos de reacción con la cara de la gente y no de lo que ve, porque la cara es lo único que sí se puede enseñar.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes_sociales
    - tecnologia
    id: adolescente/h1/3
  - texto: 'En mi grupo de amigas lo que más se comenta no es el cielo, sino cómo nos vemos las unas a las otras: que si se te ven manchas en la cara, que si el pelo o el maquillaje se ven distintos. Varias se van al baño a mirarse al espejo y alguna no quiere volver a clase.'
    mecanismo: A mi edad lo primero que te importa es cómo te ven los demás. Si de repente hay un color nuevo en la piel o en la ropa que antes nadie veía, todas nos fijamos en lo que puede dejarnos en ridículo antes que en cualquier otra cosa, y con la luz del baño puedes comprobarlo sin que te miren.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud_mental
    - imagen_personal
    - relaciones_sociales
    id: adolescente/h1/4
  - texto: A los que les molesta mucho la luz al salir al patio se les ve entrecerrando los ojos o pidiendo gafas de sol prestadas, y en una hora ya hay quien dice que el que tiene gafas de sol es el que mejor se lo está pasando, y el que no tiene se queda dentro.
    mecanismo: Fuera, con sol, deslumbra y cansa la vista, así que quien tiene gafas puede quedarse mirando más rato. Eso convierte unas gafas en algo que se presta, se pide y marca quién está en el centro del grupo y quién se queda fuera, que es lo que más me preocupa a mí.
    dato: ''
    fuente: ''
    confianza: baja
    areas_afectadas:
    - vida_cotidiana
    - relaciones_sociales
    - salud
    id: adolescente/h1/5
  reacciona_a: []
- agente: disruptor
  tramo: h1
  afirmaciones:
  - texto: En la primera hora, millones de personas con gafas graduadas de policarbonato, alto índice o tratamiento UV400 apenas notan el cambio en su visión central y solo lo perciben por los bordes de la montura. Eso genera testimonios contradictorios (unos dicen que no ven nada y otros describen colores nuevos), y el primer truco que se hace viral no es ponerse gafas de sol, sino quitarse las gafas de ver.
    mecanismo: El fenómeno solo existe si llega luz UV-A a la retina. Gran parte de las lentes oftálmicas modernas filtran casi todo el UV por el material o por un recubrimiento, así que funcionan como un interruptor que apaga la nueva percepción en el centro del campo visual. La experiencia depende de la óptica que lleve cada uno, la gente compara relatos incompatibles y la confusión inicial no viene de la ignorancia, sino de una diferencia física real entre observadores.
    dato: Las lentes de policarbonato bloquean el 100 % de la radiación UV de forma intrínseca, sin necesidad de recubrimiento.
    fuente: https://www.allaboutvision.com/en-gb/eyeglasses/polycarbonate-lenses/
    confianza: alta
    areas_afectadas:
    - salud
    - informacion
    - redes_sociales
    - optica
    id: disruptor/h1/1
  - texto: En la hora 1, casi todo el continente americano y buena parte de quienes trabajan en interiores en Europa no ven nada nuevo. En América es de noche (las 4:00 en Nueva York y la 1:00 en Los Ángeles) y la iluminación LED no emite UV-A. Su primer contacto con el suceso son los vídeos y mensajes que llegan de Europa, África, Oriente Medio y la India, y eso alimenta en las redes de EE. UU. la tesis de que es un bulo o una campaña coordinada hasta que amanece.
    mecanismo: 'Por la noche no hay fuente de UV-A natural, porque la luz de la luna es luz solar reflejada muy débil, y los LED blancos de uso general emiten UV despreciable. Sin estímulo no hay percepción. La asimetría horaria convierte un suceso simultáneo en uno escalonado: primero se vive en las zonas iluminadas por el sol y el resto lo recibe como relato de segunda mano, sin poder comprobarlo, en el momento de máxima credulidad o desconfianza. Las oficinas europeas con LED y lejos de las ventanas reproducen el mismo efecto a pequeña escala.'
    dato: Los LED blancos de iluminación general no emiten cantidades relevantes de radiación ultravioleta.
    fuente: https://www.icnirp.org/en/applications/led/led.html
    confianza: alta
    areas_afectadas:
    - informacion
    - desinformacion
    - geopolitica_mediatica
    - trabajo
    id: disruptor/h1/2
  - texto: 'En las zonas de día (Europa, África, Oriente Medio, la India), los conductores ven un mundo partido: a través del parabrisas el paisaje parece casi normal, pero por las ventanillas laterales aparecen los colores UV y el deslumbramiento. Los incidentes de tráfico de la primera hora se concentran en cambios de carril, incorporaciones y giros (cuando el conductor mira de lado), no en la conducción en línea recta. Al mismo tiempo, muchos descubren que el coche parado es un refugio contra la fatiga visual.'
    mecanismo: Los parabrisas son de vidrio laminado, cuya lámina intermedia absorbe casi todo el UV-A. Las ventanillas laterales suelen ser de vidrio templado y dejan pasar bastante más. La fatiga y el deslumbramiento solo aparecen cuando el conductor gira la cabeza, justo en las maniobras que más atención exigen. Además, el contraste brusco entre la vista frontal y la lateral obliga a readaptarse en cada mirada.
    dato: En un estudio de 29 vehículos, los parabrisas bloquearon de media el 96 % del UV-A y las ventanillas del conductor solo el 71 %.
    fuente: https://safetyandhealthmagazine.com/articles/14075-vehicle-side-windows-offer-little-protection-from-suns-rays-study
    confianza: media
    areas_afectadas:
    - trafico
    - seguridad_vial
    - seguros
    - automocion
    id: disruptor/h1/3
  - texto: Los talleres de mantenimiento aeronáutico e industrial de Europa, que a las 10:00 están en plena jornada, suspenden las inspecciones por líquidos penetrantes fluorescentes y partículas magnéticas. Se retrasa la puesta en servicio de piezas de motor y de estructuras que estaban pendientes de liberación.
    mecanismo: 'Estos ensayos se hacen en cabinas oscuras iluminadas con lámparas UV-A de 365 nm, con un supuesto implícito: el inspector no ve la luz UV-A y solo ve la fluorescencia visible de las grietas sobre un fondo negro. Ahora el inspector percibe la luz reflejada por toda la pieza y por la cabina, el contraste se hunde y el método deja de cumplir las condiciones con las que se validó. Ningún responsable de calidad firmará una liberación con un procedimiento cuya premisa física ha cambiado, así que el efecto no es pánico, sino una parada normativa silenciosa.'
    dato: La inspección fluorescente usa lámparas UV-A con el pico de intensidad en 365 nm y exige limitar la luz visible ambiental en la cabina.
    fuente: https://magnaflux.com/Magnaflux/Resources/Blog/NDT-UV-LED-FAQ
    confianza: media
    areas_afectadas:
    - aviacion
    - industria
    - calidad
    - normativa
    - cadena_de_suministro
    id: disruptor/h1/4
  - texto: En la India y Oriente Medio, donde a esa hora es primera hora de la tarde con mucho sol, la gente empieza a ver la crema solar en la piel de los demás como manchas o máscaras oscuras. También ve que la ropa blanca lavada con detergentes con blanqueantes ópticos no se parece a la blanca sin tratar. En la primera hora circulan imágenes de caras con parches irregulares de protector solar y aparecen dudas sobre si la crema funciona o si mancha.
    mecanismo: Los filtros solares químicos y minerales funcionan precisamente absorbiendo o reflejando el UV. En una visión que incluye el UV-A, una zona con protector se ve claramente distinta de la piel desprotegida, y se nota cada zona mal extendida. Los blanqueantes ópticos absorben UV-A y lo reemiten en azul, de modo que su aspecto cambia con el nuevo canal de color. Algo que hasta ahora era invisible por diseño pasa a ser visible y a juzgarse por estética.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - cosmetica
    - consumo
    - salud_dermatologica
    - redes_sociales
    id: disruptor/h1/5
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
  metricas:
    alarma_social: valor
    respuesta_gobiernos: valor
    impacto_economico: valor
    adaptacion: valor
