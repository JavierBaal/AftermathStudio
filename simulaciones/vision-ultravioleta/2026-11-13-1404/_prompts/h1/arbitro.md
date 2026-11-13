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
  - texto: Durante la primera hora no hay un desplome generalizado de la renta variable europea, pero sí paradas técnicas en valores concretos (óptica, gafas, pantallas, cámaras) por movimientos bruscos en ambas direcciones.
    mecanismo: 'Las bolsas europeas llevan una hora abiertas cuando ocurre el suceso y son el único gran mercado de contado operando: Asia ya ha cerrado y Wall Street está en preapertura. No hay daño físico a fábricas, puertos ni balances, así que no existe un shock de flujos de caja que justifique vender índices enteros. La incertidumbre se concentra en sectores cuya demanda depende de la vista y la luz. Los mecanismos de protección de Euronext congelan durante unos minutos los valores que se mueven demasiado rápido. Eso frena las cascadas de órdenes automáticas, aunque genera titulares de que se suspende la cotización que algunos medios presentan como pánico.'
    dato: En Euronext, los valores del CAC 40 y otros índices de referencia entran en periodo de reserva de al menos 3 minutos si el precio se mueve un 3 % frente a la última operación, y un 8 % frente al precio de apertura.
    fuente: https://www.euronext.com/en/for-investors/market-quality/trading-safeguards
    confianza: media
    evidencia: dato
    areas_afectadas:
    - mercados financieros
    - bolsa
    id: economista/h1/1
  - texto: 'Las acciones de los fabricantes de gafas de sol se convierten en el primer termómetro del suceso: el mercado anticipa un pico de demanda a corto plazo y, a la vez, duda sobre si la categoría cambia para siempre.'
    mecanismo: 'El deslumbramiento en exteriores soleados crea una necesidad inmediata de protección, y la oferta de gafas de sol está muy concentrada en pocos grupos. Para un operador, el razonamiento rápido es comprar porque las ventas se dispararán. El razonamiento lento es más incierto: si las lentes actuales no filtran bien lo que ahora se percibe, o si el deslumbramiento remite en dos semanas, el pico se queda en transitorio y puede seguirle un periodo de existencias sobrantes. Esa pugna entre ambos razonamientos genera volatilidad en lugar de una tendencia clara.'
    dato: EssilorLuxottica facturó 26.500 millones de euros en 2024, y las gafas de sol supusieron el 23 % de sus ingresos.
    fuente: https://moodiedavittreport.com/essilorluxottica-records-solid-revenue-and-profits-growth-in-2024-despite-industry-headwinds/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - mercados financieros
    - consumo
    - comercio minorista
    id: economista/h1/2
  - texto: En la franja del planeta donde es de día (Europa, África y Oriente Medio) se agotan en horas las existencias de gafas de sol en farmacias, ópticas y gasolineras, y en los mercados en línea aparecen reventas a precios inflados.
    mecanismo: La demanda se multiplica de golpe y de forma simultánea, mientras que la reposición depende de cadenas de suministro con fabricación concentrada en Asia y plazos de semanas. Las tiendas físicas no suben precios en una hora, así que se vacían por cola. Los revendedores y los vendedores oportunistas de plataformas en línea, en cambio, sí ajustan el precio al instante. En América todavía es de noche y la demanda allí llegará con el amanecer, lo que da a los revendedores varias horas para acaparar.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - comercio minorista
    - cadenas de suministro
    id: economista/h1/3
  - texto: La productividad de los trabajos al aire libre cae en las zonas soleadas durante esta primera hora (construcción, agricultura, reparto, transporte por carretera), pero sería un error leerlo ya como un dato de empleo o de recesión.
    mecanismo: 'El deslumbramiento y la fatiga visual obligan a parar o a ir más despacio por pura seguridad, sobre todo en la conducción y en el trabajo en altura. Las empresas de logística y las aseguradoras tienen incentivos para frenar actividad antes de que haya accidentes. Es una pérdida de horas, no de puestos de trabajo: el efecto es temporal y no está en ninguna estadística oficial. Quien hable en esta hora de destrucción de empleo está extrapolando sin datos.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - empleo
    - logística
    - transporte
    - productividad
    id: economista/h1/4
  - texto: Algunos operadores minoristas y algoritmos que leen titulares compran valores por asociación de nombre o de palabra clave (empresas con UV o visión en el nombre, fabricantes de protección solar), con subidas que no tienen nada que ver con su negocio real.
    mecanismo: Los sistemas que operan leyendo noticias y los inversores particulares reaccionan a palabras clave antes de analizar el negocio. Ya ha ocurrido en otros episodios que se compraran títulos equivocados por un nombre parecido. Con un suceso sin precedentes y sin datos de impacto, el ruido de palabras clave domina la primera hora. Estas subidas deberían deshacerse cuando lleguen análisis más serios, y dejarán pérdidas a quien entró tarde.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - mercados financieros
    - inversores minoristas
    id: economista/h1/5
  reacciona_a: []
- agente: politico
  tramo: h1
  afirmaciones:
  - texto: En España el suceso pilla al Gobierno con el Consejo de Ministros ordinario convocado esa misma mañana de martes; antes de las 11:00 Moncloa suspende el orden del día previsto y lo convierte en reunión de seguimiento, y la rueda de prensa posterior se retrasa sin hora fija.
    mecanismo: El Consejo de Ministros se reúne de forma ordinaria los martes por la mañana, así que los ministros ya están juntos o de camino. Cancelar la reunión daría imagen de descontrol, y mantener la rueda de prensa habitual sin nada que decir sería peor. La salida que protege la legitimidad es reconvertir la sesión y aplazar la comparecencia hasta tener algo respaldado por los técnicos.
    dato: El Consejo de Ministros celebra habitualmente sus reuniones ordinarias los martes.
    fuente: https://www.lamoncloa.gob.es/consejodeministros/Paginas/funciones/index.aspx
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - gobierno
    - comunicacion_institucional
    id: politico/h1/1
  - texto: En la primera hora ningún gobierno con instituciones sanitarias funcionales declara un estado de excepción o alarma; lo que sale son comunicados de 'calma, estamos evaluando' firmados por ministerios de Sanidad, sin medidas obligatorias.
    mecanismo: Las medidas excepcionales exigen base legal y respaldo técnico. En España la Ley Orgánica 4/1981 permite el estado de alarma por crisis sanitarias como epidemias, pero aquí no hay contagio, ni enfermos graves, ni nada que restringir con fundamento; ningún técnico puede firmar todavía que haya un riesgo que justifique limitar derechos. Declarar algo ahora y tener que rectificar después es la peor jugada en legitimidad, así que el incentivo es comunicar sin decretar.
    dato: El artículo 4 de la Ley Orgánica 4/1981 prevé el estado de alarma ante crisis sanitarias, tales como epidemias y situaciones de contaminación graves.
    fuente: https://www.boe.es/eli/es/lo/1981/06/01/4
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - gobierno
    - derecho
    - sanidad
    id: politico/h1/2
  - texto: La OMS no convoca todavía su Comité de Emergencias del Reglamento Sanitario Internacional en la primera hora; se limita a una nota de que está recabando información de los Estados miembros, y varios gobiernos se escudan en esa espera para no pronunciarse.
    mecanismo: 'El mecanismo del RSI se activa a partir de notificaciones de los Estados y de una evaluación de riesgo, y el Director General convoca el comité tras esa evaluación, no en minutos. Un fenómeno simultáneo en todo el planeta no tiene país de origen que notifique primero. A los gobiernos les conviene que haya una autoridad internacional ''evaluando'': les da una razón respetable para no comprometerse con nada que luego tengan que rectificar.'
    dato: Conforme al Reglamento Sanitario Internacional, el Director General de la OMS convoca un Comité de Emergencias para asesorar sobre si un evento constituye una emergencia de salud pública de importancia internacional.
    fuente: https://paho.org/sites/default/files/2021-03/labs-reg-sanitario2005.pdf
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - organismos_internacionales
    - sanidad
    - diplomacia
    id: politico/h1/3
  - texto: 'La oposición en España rompe el silencio institucional antes que el Gobierno: en la primera hora algún portavoz exige en redes una comparecencia inmediata del presidente y critica que ''el Gobierno no dice nada'', y algún político autonómico o local se adelanta con una recomendación propia (no salir al sol, gafas de sol) sin base técnica.'
    mecanismo: La oposición gana con cada silencio del Gobierno y no tiene la restricción de decir solo lo que respaldan los técnicos, así que puede moverse antes. Los presidentes autonómicos y alcaldes compiten por visibilidad y tienen competencias en protección civil y salud pública; recomendar gafas de sol al ver gente deslumbrada en la calle es barato y parece responsable, aunque luego choque con lo que diga Sanidad.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - politica
    - comunicacion_institucional
    - administracion_autonomica
    id: politico/h1/4
  - texto: Algún gobierno, previsiblemente uno con poco control institucional sobre sus técnicos, aprovecha la primera hora para atribuir el fenómeno a una acción hostil o lo presenta como señal favorable a su régimen, y eso obliga a otras cancillerías a decidir si responden o lo ignoran.
    mecanismo: Sin causa conocida, el vacío explicativo es una oportunidad para quien no rinde cuentas ante un cuerpo técnico independiente. Culpar a un enemigo exterior cohesiona a la población y adelanta el relato antes que los demás. Las democracias no pueden contestarlo con una explicación alternativa porque nadie la tiene, así que la respuesta probable es una desmentida genérica y tardía, lo que deja el primer relato internacional en manos del que exageró.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - diplomacia
    - desinformacion
    - politica_internacional
    id: politico/h1/5
  reacciona_a: []
- agente: medios
  tramo: h1
  afirmaciones:
  - texto: En la primera hora el relato global lo fijan Europa, África y Oriente Medio, que están a plena luz de la mañana o del mediodía; Asia oriental lo vive al atardecer y con menos efecto, y América está casi entera dormida, con las redacciones estadounidenses en turno de noche y plantilla mínima. América despertará dentro de unas horas ante un relato ya formado por otros, con titulares y bulos traducidos en lugar de experiencia propia.
    mecanismo: Las 10:00 de Madrid son de madrugada en América y de tarde-noche en Asia oriental. El fenómeno se nota sobre todo con luz solar, que lleva ultravioleta, así que solo quien está de día al sol tiene algo llamativo que contar y grabar. Quien lo cuenta primero fija el encuadre, y quien despierta después lo recibe ya interpretado.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - medios
    - redes_sociales
    - opinion_publica
    - geopolitica_informativa
    id: medios/h1/1
  - texto: 'El primer formato viral no son imágenes de los colores nuevos sino quejas de que la cámara no los capta: millones de personas intentan grabar lo que ven y el móvil muestra lo de siempre. Esa frustración se vuelve meme (la cámara no ve lo que yo veo) y, a la vez, abre un vacío que se llena con montajes y filtros falsos que presumen de enseñar cómo se ve el ultravioleta y que se comparten como si fueran reales.'
    mecanismo: 'Las cámaras de los móviles se diseñan para reproducir el espectro visible humano anterior, así que no hay forma rápida de documentar lo nuevo. Cuando la experiencia no se puede probar con imagen, la demanda de contenido visual la cubre quien inventa: creadores que buscan audiencia aplican filtros de color y los presentan como capturas auténticas.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - desinformacion
    - tecnologia_consumo
    id: medios/h1/2
  - texto: 'Los bulos sanitarios corren más que cualquier mensaje oficial: cadenas de WhatsApp y vídeos cortos que dicen que la gente se está quedando ciega, que hay que encerrarse a oscuras o que ciertos remedios caseros protegen los ojos. El deslumbramiento real en exteriores sirve de prueba aparente, y el desmentido llega tarde porque ningún organismo sanitario tiene todavía nada que decir.'
    mecanismo: Lo falso y novedoso se comparte más y más rápido que lo verdadero, y aquí todo es novedoso. El deslumbramiento y la fatiga visual existen y cada persona los nota en sí misma, lo que da credibilidad a la versión exagerada. Las autoridades sanitarias no publican sin conocimiento y en la primera hora no lo tienen, así que el hueco lo ocupan los mensajes alarmistas.
    dato: En Twitter, las noticias falsas tenían un 70% más de probabilidad de ser retuiteadas que las verdaderas, y las verdaderas tardaban unas seis veces más en llegar a 1.500 personas; las respuestas a lo falso mostraban más sorpresa y asco.
    fuente: https://news.mit.edu/2018/study-twitter-false-news-travels-faster-true-stories-0308
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - salud_publica
    - desinformacion
    - redes_sociales
    - servicios_de_urgencias
    id: medios/h1/3
  - texto: Los medios serios abren directos en minutos, porque cada periodista es testigo y fuente de primera mano, pero no tienen expertos que expliquen nada. Llenan el directo con oftalmólogos que hablan de la fatiga visual, físicos que explican qué es el ultravioleta y llamadas a agencias espaciales y meteorológicas. La pregunta de si ha pasado algo con el Sol se convierte en el titular de la hora porque es la hipótesis que el público entiende, aunque nadie la confirme.
    mecanismo: La regla de al menos una fuente se cumple sin esfuerzo cuando la propia redacción ve el fenómeno, y la presión por ser el primero empuja a publicar ya. Sin causa conocida, el medio busca al experto disponible más cercano al tema y formula preguntas en vez de afirmaciones. La asociación popular entre ultravioleta y Sol hace que esa pregunta enganche más que cualquier otra.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - ciencia
    - opinion_publica
    id: medios/h1/4
  - texto: 'Entre los jóvenes el relato lo construyen creadores e influencers, no los medios, y las plataformas apenas moderan en esta primera hora: sus normas contra la desinformación sanitaria se apoyan en lo que dicen las autoridades, que aún callan. Solo retiran lo más claramente dañino, como retos de mirar al sol para entrenar la vista nueva, mientras ya aparecen anuncios oportunistas de gafas y gotas que prometen proteger del ultravioleta.'
    mecanismo: Una parte grande de los jóvenes se informa sobre todo en redes y vídeo, donde el creador que reacciona en directo gana audiencia a cualquier redacción. Las políticas de moderación necesitan un consenso oficial contra el que comparar, y sin él solo actúan sobre daños evidentes. El miedo al deslumbramiento crea demanda inmediata que vendedores y estafadores aprovechan antes de que nadie la regule.
    dato: Un 44% de los jóvenes de 18 a 24 años en el mundo dice que las redes sociales o de vídeo son su principal fuente de noticias, frente al 20% de los mayores de 55; el 58% teme no distinguir lo real de lo falso en internet.
    fuente: https://www.journalism.co.uk/ten-talking-points-from-the-reuters-institute-digital-news-report-2025/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - plataformas
    - juventud
    - desinformacion
    - consumo
    - fraude
    id: medios/h1/5
  reacciona_a: []
- agente: oftalmologa
  tramo: h1
  afirmaciones:
  - texto: 'En la primera hora la sociedad oftalmológica difunde un comunicado que ancla el fenómeno en un precedente clínico: las personas sin cristalino (afáquicas) o con lentes intraoculares que dejan pasar el ultravioleta ya veían UV cercano antes del martes, y lo describían como un azul o violeta blanquecino. Esto da a los clínicos un marco descriptivo inmediato y a la sociedad la posición de referencia.'
    mecanismo: En el ojo normal el cristalino filtra casi todo el ultravioleta antes de que llegue a la retina; cuando falta, los fotorreceptores reciben UV y responden. Los conos azules son los más sensibles al UV, de ahí el tono azul-violeta, y cuando los tres tipos de cono lo absorben a la vez la sensación tiende al blanco. Una sociedad científica que quiere ser la voz del fenómeno usa el único dato clínico previo que existe para hablar primero y con base.
    dato: Afáquicos y portadores de lentes intraoculares transmisoras de UV pueden percibir UV hasta unos 315 nm; el UV se percibe como azul blanquecino o violeta blanquecino según la longitud de onda; los conos azules son los más sensibles al UV.
    fuente: https://2020mag.com/article/uv-vision-seeing-invisible-ultraviolet
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - salud
    - ciencia
    - comunicacion
    id: oftalmologa/h1/1
  - texto: 'Los relatos de lo que se ve no coinciden entre personas: unas describen colores intensos y otras apenas un velo azulado. Esa disparidad alimenta en la primera hora autodiagnósticos erróneos (gente que cree que ve mal o que su visión se está dañando) y llamadas a consultas y urgencias oftalmológicas.'
    mecanismo: La sensibilidad al UV varía mucho de un individuo a otro, de modo que el mismo estímulo produce percepciones de intensidad muy distinta. Sin un patrón de referencia, quien percibe menos o más que su entorno interpreta la diferencia como un problema propio.
    dato: En un estudio con 42 participantes, todos detectaron un pico UV aislado hacia 315 nm, pero la variación individual de sensibilidad superó un factor de 30 y los hombres resultaron más sensibles que las mujeres.
    fuente: https://2020mag.com/article/uv-vision-seeing-invisible-ultraviolet
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - sanidad_publica
    - vida_cotidiana
    id: oftalmologa/h1/2
  - texto: El cambio se nota sobre todo en exteriores y junto a ventanas; en interiores con iluminación LED las oficinas, casas y comercios se ven casi igual que antes. Durante la primera hora, la gente sale a la calle o se asoma a las ventanas para comprobar lo que ocurre, y ahí es donde se concentran el deslumbramiento y las primeras consultas.
    mecanismo: Para ver un color UV tiene que haber luz UV-A que ilumine la escena. La luz solar contiene UV-A y el vidrio común de ventana bloquea sobre todo el UV-B pero deja pasar parte del UV-A, mientras que las lámparas LED blancas de uso general emiten muy poco ultravioleta. Por eso el fenómeno se percibe de forma desigual según el sitio en que se esté.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - vida_cotidiana
    - trabajo
    - salud
    id: oftalmologa/h1/3
  - texto: 'Aparecen diferencias visuales llamativas en objetos corrientes: la piel con protector solar se ve oscura o con manchas, la ropa lavada con detergentes con blanqueante óptico destaca con un brillo nuevo y muchas flores muestran patrones que antes no se veían. Estos ejemplos se difunden en redes como pruebas caseras del fenómeno.'
    mecanismo: Los filtros solares funcionan absorbiendo UV, de modo que bajo visión UV reflejan poco y se ven oscuros. Los blanqueantes ópticos absorben UV y reemiten luz, por lo que su aspecto cambia cuando el ojo también capta el UV que reflejan o absorben. Muchas flores tienen pigmentos que reflejan o absorben UV de forma distinta al resto del pétalo y forman patrones que hasta ahora solo se veían con cámaras UV.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - vida_cotidiana
    - cosmetica
    - redes_sociales
    id: oftalmologa/h1/4
  - texto: 'Algunos profesionales y comercios se adelantan a la evidencia: en la primera hora circulan recomendaciones contradictorias, desde quien aconseja no salir a la calle hasta quien anuncia gafas que bloquean UV como solución o, al contrario, como algo que hay que quitarse para no perder la nueva visión. La sociedad oftalmológica pierde terreno ahí si tarda en publicar una guía práctica.'
    mecanismo: Ante un fenómeno sin causa conocida y con molestias reales en exteriores, la demanda de consejo inmediato es alta y la evidencia clínica todavía no existe. Quien responde primero ocupa el espacio aunque no tenga base, y quien vende filtros UV tiene incentivo para presentarlos como la respuesta. Las gafas con filtro UV sí reducirían la luz UV que llega al ojo y, con ella, la percepción de los colores nuevos y parte del deslumbramiento, lo que hace que el mensaje comercial sea plausible a primera vista.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - salud
    - comercio
    - comunicacion
    id: oftalmologa/h1/5
  reacciona_a: []
- agente: adolescente
  tramo: h1
  afirmaciones:
  - texto: 'En mi instituto la clase de las diez se para del todo: nadie atiende y los profes no consiguen recuperar el control durante la primera hora, porque a ellos también les pasa.'
    mecanismo: Es un martes en mitad de la mañana, estamos todos juntos en el aula y el cambio nos pilla a la vez a alumnos y profesores. Si el profe también está viendo colores raros, no tiene autoridad para decirnos que nos calmemos, y la norma de no sacar el móvil deja de cumplirse porque todos queremos comprobar si es cosa nuestra o de todo el mundo.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - convivencia
    id: adolescente/h1/1
  - texto: 'Mis amigas y yo intentamos sacar fotos y vídeos de los colores nuevos para subirlos, y descubrimos enseguida que en la pantalla no salen: eso nos frustra y a la vez convierte el tema en algo que solo se puede contar, no enseñar.'
    mecanismo: Lo primero que hago cuando me pasa algo fuerte es grabarlo para las redes. Pero la cámara y la pantalla del móvil están hechas para los colores de antes, así que lo que veo con mis ojos no aparece en el vídeo. Como no se puede enseñar, lo que se comparte son reacciones, caras, gritos y descripciones exageradas.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes_sociales
    - tecnologia
    id: adolescente/h1/2
  - texto: 'En menos de una hora en los grupos de clase y en TikTok ya circulan audios y vídeos de gente que se inventa cosas: que es por el 5G, que si miras al sol te quedas ciega o que el instituto va a cerrar. Algunos de mi clase se lo creen y lo reenvían.'
    mecanismo: Nadie sabe la causa ni si es permanente, así que hay un hueco que llena el que hable primero y más alto. En mi edad compartir algo antes que nadie da estatus, aunque sea mentira, y los chicos que buscan seguidores exageran a propósito porque eso da visitas.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: especulacion
    areas_afectadas:
    - desinformacion
    - redes_sociales
    - salud_publica
    id: adolescente/h1/3
  - texto: Los que salen al patio o están en Educación Física en la calle vuelven quejándose de que les molesta la luz y les duele la vista; el instituto acaba metiendo a todo el mundo dentro y algunos padres empiezan a escribir para venir a recoger a sus hijos.
    mecanismo: Fuera, con sol, hay deslumbramiento y cansancio en los ojos. Los profesores no saben si es peligroso, así que lo más fácil para ellos es no dejar salir a nadie. Mis padres, que también lo están viendo en el trabajo, se asustan y escriben al grupo de familias, y como yo dependo de lo que ellos decidan, a algunos nos sacan del instituto y a otros no.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - educacion
    - salud
    - familias
    id: adolescente/h1/4
  - texto: 'Dentro de mi grupo empieza una competición por quién ve más o mejor: hay quien dice que ve colores en la piel, en el pelo o en la ropa de los demás, y eso se convierte rápido en motivo de comentarios sobre el físico de cada uno.'
    mecanismo: Estamos todo el día pendientes de cómo nos ven los demás. Si de repente se ven cosas nuevas en la cara, la ropa o el maquillaje, la gente se pone a mirarse y a comparar, y los más populares deciden qué queda bien y qué es raro. Quien quiere encajar repite lo que dicen ellos aunque no lo vea igual.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - convivencia
    - salud_mental
    - imagen_corporal
    id: adolescente/h1/5
  reacciona_a: []
- agente: agitador
  tramo: h1
  afirmaciones:
  - texto: En los primeros 20 minutos, el agitador abre un directo en sus canales propios de mensajería y en una plataforma grande, sin guion, grabando el cielo y objetos cotidianos con colores nuevos y pidiendo a sus seguidores que envíen vídeos. Se convierte en uno de los primeros nodos de agregación de testimonios en su idioma antes de que haya ninguna comparecencia oficial.
    mecanismo: En un vacío informativo gana quien llega antes, y el agitador no necesita verificar ni coordinar con nadie, mientras gobiernos y organismos sanitarios tardan en convocar comités y redactar comunicados. Recoger vídeos de su audiencia le da contenido gratis y hace que sus seguidores sientan que participan.
    dato: Las noticias falsas en Twitter llegaban a 1.500 personas unas seis veces más rápido que las verdaderas, sobre todo por la novedad y porque generaban sorpresa.
    fuente: https://www.science.org/doi/10.1126/science.aap9559
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - informacion
    - redes_sociales
    - confianza_institucional
    id: agitador/h1/1
  - texto: 'Hacia la media hora, el agitador pasa del asombro a la sospecha: plantea en directo, como preguntas abiertas, que alguien tenía que saberlo y que el silencio oficial es deliberado, y señala de forma difusa a gobiernos, laboratorios y grandes tecnológicas sin acusar a nadie con nombre propio.'
    mecanismo: Su modelo de negocio premia la historia de culpables, pero hablar con preguntas y sin nombres concretos le permite sostener la credibilidad ante su audiencia y reducir el riesgo de que la plataforma lo sancione por desinformación o difamación. Como nadie conoce la causa, ninguna autoridad puede desmentirle en la primera hora.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - confianza_institucional
    - informacion
    - politica
    id: agitador/h1/2
  - texto: El agitador traslada el grueso de su conversación a sus canales propios de mensajería y deja en la plataforma grande una versión más contenida, porque prevé moderación. Sus canales propios ganan suscriptores de forma visible durante la hora y reciben un pico de donaciones.
    mecanismo: Las grandes plataformas tienen políticas contra la desinformación médica dañina; un fenómeno que afecta a la visión de todo el mundo entra en ese terreno y la moderación puede activarse rápido. Los canales propios no tienen ese freno, y los seguidores que temen perder el acceso al directo se mudan allí. El miedo y la sensación de exclusiva empujan la donación.
    dato: YouTube prohíbe el contenido que contradice la orientación de las autoridades sanitarias locales o de la OMS sobre afecciones y sustancias concretas cuando supone riesgo de daño grave.
    fuente: https://support.google.com/youtube/answer/13813322
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - plataformas
    - redes_sociales
    - economia_creadores
    id: agitador/h1/3
  - texto: Entre los vídeos que reenvía el agitador se cuelan testimonios de deslumbramiento y molestias en exteriores con mucho sol que él presenta como daño, sin distinguir fatiga visual de lesión. Una parte de su audiencia se encierra, se tapa los ojos o llama a urgencias oftalmológicas y centros de salud por síntomas que remitirían solos.
    mecanismo: El deslumbramiento es real y cualquiera lo puede comprobar al salir a la calle a media mañana, lo que da verosimilitud inmediata al relato del agitador. Como en la primera hora no hay ninguna fuente oficial que diga que remite y no deja daño, el testimonio en primera persona pesa más que cualquier matiz y convierte una molestia transitoria en alarma sanitaria.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - sanidad
    - informacion
    - comportamiento_publico
    id: agitador/h1/4
  - texto: Al final de la hora, el agitador anuncia un directo largo para la tarde y promete exponer lo que no cuentan, con lo que fija una cita que obliga a otros creadores y a medios a reaccionar a su marco. Algunos medios recogen sus clips como muestra de la reacción en redes y le dan alcance fuera de su burbuja.
    mecanismo: Programar un evento retiene a la audiencia mientras dura la incertidumbre y le asegura la siguiente ola de atención. Los medios generalistas, desbordados y sin explicación que dar, recurren a contenido viral para llenar la cobertura en directo, y al citarlo, aunque sea para criticarlo, amplifican su relato.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - medios
    - informacion
    - politica
    id: agitador/h1/5
  reacciona_a: []
- agente: disruptor
  tramo: h1
  afirmaciones:
  - texto: En la primera hora, quien conduce de día en Europa, África y Oriente Medio ve el parabrisas como un filtro oscuro y teñido mientras las ventanillas laterales dejan pasar la luz nueva. Ese contraste, sumado al deslumbramiento lateral, provoca maniobras bruscas y paradas en arcén, y en ciudad aparece una oleada de alcances leves.
    mecanismo: El vidrio laminado del parabrisas absorbe casi todo el UV-A y el vidrio templado de las laterales mucho menos. Con visión UV, el conductor percibe de golpe dos ventanas de color y brillo distintos en el mismo campo visual. El sol de media mañana entra por los laterales y deslumbra justo en la zona de visión periférica que se usa para cambiar de carril. Muchos frenan para entender qué les pasa en los ojos.
    dato: Los parabrisas bloquearon de media el 96 % del UV-A y las ventanillas laterales el 71 % (Boxer Wachler, JAMA Ophthalmology, 2016).
    fuente: https://safetyandhealthmagazine.com/articles/14075-vehicle-side-windows-offer-little-protection-from-suns-rays-study
    confianza: media
    evidencia: dato
    areas_afectadas:
    - trafico
    - seguridad_vial
    - seguros
    id: disruptor/h1/1
  - texto: 'Quien lleva protector solar o maquillaje con filtro aparece a ojos de los demás con la cara oscurecida a manchas. Durante la primera hora esto se toma como síntoma: hay gente que acude a farmacias y urgencias por manchas en la piel que en realidad son crema mal extendida.'
    mecanismo: Los filtros solares están hechos para absorber UV-A, así que en UV la zona tratada refleja poco y se ve oscura, y las zonas con poca crema se ven claras. Nadie tiene todavía un marco para interpretar lo que ve en la cara de otro, y un suceso corporal inexplicable lleva a asociar cualquier cambio visible con enfermedad. Muchas cremas hidratantes y bases de maquillaje llevan filtro, así que afecta a mucha gente que no cree llevar protector.
    dato: Con fotografía UV, la piel con protector solar aparece oscura o negra porque el producto absorbe el ultravioleta.
    fuente: https://gizmodo.com/the-best-way-to-apply-sunscreen-on-your-face-revealed-1828666401
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - cosmetica
    - percepcion_social
    id: disruptor/h1/2
  - texto: En América es de madrugada en la primera hora, y casi nadie allí puede comprobar el fenómeno con sus propios ojos. Se conoce por noticias de Europa, África y Asia, y circula el rumor de que el cambio no afecta al continente americano o que llega en una ola que avanza hacia el oeste. Las pocas confirmaciones locales salen de discotecas con luz negra, mataderos de insectos y lámparas de uñas.
    mecanismo: Sin sol no hay UV-A ambiental, así que la nueva capacidad no tiene nada que percibir y la gente que despierta y mira a su alrededor no nota diferencia. Las únicas fuentes de UV-A a esa hora son artificiales y minoritarias. La ausencia de experiencia propia, sumada a noticias de otros continentes, alimenta una explicación geográfica falsa que solo se desmiente al amanecer. A las 10:00 de Madrid son las 4:00 en Nueva York.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - informacion
    - desinformacion
    - geopolitica
    id: disruptor/h1/3
  - texto: 'Durante la primera hora, la gente con gafas de sol descubre a simple vista si sus lentes filtran de verdad el ultravioleta. Las gafas baratas sin filtro UV quedan en evidencia y empiezan las primeras quejas públicas contra marcas y vendedores. Los usuarios de gafas graduadas de policarbonato ven el mundo dividido: sin colores nuevos a través de la lente y con ellos por los bordes.'
    mecanismo: Una lente con filtro UV400 absorbe el UV-A y se percibe como opaca o teñida en el canal nuevo, y una lente sin filtro deja pasar los colores nuevos. Quien se pone gafas para aliviar el deslumbramiento comprueba al instante si funcionan. Es la primera vez que el consumidor puede verificar sin instrumentos una promesa de etiqueta. El policarbonato absorbe el UV por la naturaleza del material, lo que crea una frontera visible entre la lente y la visión periférica.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - consumo
    - optica
    - regulacion
    id: disruptor/h1/4
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
