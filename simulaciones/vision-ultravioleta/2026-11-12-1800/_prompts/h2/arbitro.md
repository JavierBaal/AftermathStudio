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
Hora 2 (PT2H desde el suceso)
Estado del mundo anterior:
estado_del_mundo:
  tramo: h1
  resumen: 'En la primera hora el cambio se vive de forma desigual según la luz: dentro de edificios y tras el cristal apenas se nota, al sol molesta, las gafas UV400 devuelven la visión de antes y en América, donde es de noche, llega como noticia. La experiencia no se puede fotografiar ni mostrar en pantalla, así que circula por mensajería privada como testimonio, sin imágenes, y el vacío lo llenan falsos avisos sanitarios, imágenes recicladas y el rumor de que hay gente a la que no le ha afectado, porque quienes llevan lentes con filtro UV no ven los colores nuevos en el centro de la vista. Los gobiernos callan y recogen datos, las únicas decisiones públicas son avisos de reguladores de transporte, y defensa abre evaluaciones secretas por si fuera un ataque. Los mercados no se hunden: pierden liquidez y el dinero se concentra en apuestas de relato fácil como las ópticas, mientras la crema solar, que ahora se ve como manchas oscuras en la cara, empuja a la gente a quitársela justo cuando
    hay deslumbramiento.'
  hechos_establecidos:
  - id: h1-01
    texto: El impacto físico depende de la luz solar local. En interiores y tras el vidrio común o con iluminación LED el cambio casi no se nota. Al salir al sol aparecen el deslumbramiento y el lagrimeo, la gente vuelve a entrar o busca la sombra, y las gafas de sol UV400 devuelven la visión de antes. El golpe físico es mayor donde es pleno día con UV alto (África austral y oriental, Oriente Medio, sur de Asia), donde se agotan las primeras existencias de gafas de sol en farmacias, ópticas y puestos callejeros. En América, que está de noche, el suceso llega primero como noticia y no como molestia.
    origen:
    - oftalmologa/h1/3
    - economista/h1/3
    - adolescente/h1/3
    - politico/h1/3
    - medios/h1/4
  - id: h1-02
    texto: Muchas personas con gafas graduadas o de sol con filtro UV, o con lentillas que bloquean el UV, no ven los colores nuevos en el centro de la vista, solo en la periferia o al quitárselas. Durante la primera hora muchas creen que el fenómeno no les ha afectado y en redes se extienden mensajes de 'yo no lo veo' que alimentan el rumor de que el cambio es parcial o selectivo.
    origen:
    - disruptor/h1/1
  - id: h1-03
    texto: Ningún gobierno declara la emergencia formal. Se activan las salas de crisis existentes (en España, el Departamento de Seguridad Nacional) solo para recoger información, sin que comparezca el jefe de Gobierno. La OMS y la UE se limitan a contactos informales entre puntos focales, sin comité de emergencia ni Consejo extraordinario. Los gobiernos de América, donde es de noche, responden con declaraciones de calma, y eso descoordina el mensaje internacional.
    origen:
    - politico/h1/1
    - politico/h1/4
    - politico/h1/3
  - id: h1-04
    texto: 'La primera decisión pública concreta la toman los reguladores sectoriales de transporte: autoridades aéreas y de tráfico emiten avisos de precaución por el deslumbramiento y algunos operadores retienen o ralentizan salidas. En carretera aparece además una distracción propia: el parabrisas bloquea casi todo el UV-A y las ventanillas laterales no, así que el conductor ve los colores nuevos a los lados y no al frente, y eso provoca giros de cabeza, frenazos y paradas para comparar.'
    origen:
    - politico/h1/2
    - disruptor/h1/2
  - id: h1-05
    texto: Los servicios de inteligencia y defensa de las grandes potencias abren evaluaciones urgentes y secretas para descartar un ataque y medir el efecto sobre la vigilancia, el camuflaje y la señalización militar, que ahora quedan expuestos a la vista UV-A.
    origen:
    - politico/h1/5
  - id: h1-06
    texto: El relato nace en la mensajería privada (WhatsApp, Telegram, grupos familiares y de clase) antes que en los medios. Ninguna cámara ni pantalla de consumo puede captar ni mostrar los colores nuevos, así que las fotos salen normales y la gente publica que 'la foto no lo pilla'. La demanda de pruebas se llena con imágenes UV antiguas recicladas y con filtros de falso color, y crece la desconfianza hacia la imagen grabada como prueba. Hacia el final de la hora los medios tradicionales entran en directo con testimonios y expertos que reconocen no saber nada.
    origen:
    - medios/h1/1
    - medios/h1/2
    - disruptor/h1/4
    - adolescente/h1/2
    - medios/h1/4
  - id: h1-07
    texto: Los primeros bulos con tracción son falsos avisos sanitarios con apariencia oficial ('te quemas la retina', 'tápale los ojos al bebé', supuestos comunicados de la OMS o de Sanidad). A la vez, las urgencias oftalmológicas y los teléfonos de información sanitaria reciben un primer pico de consultas por fotofobia y miedo a una lesión, y las exploraciones salen normales, lo que desconcierta más de lo que tranquiliza.
    origen:
    - medios/h1/3
    - oftalmologa/h1/4
  - id: h1-08
    texto: Empieza una disputa por el vocabulario. Las primeras descripciones hablan de un blanco azulado o violáceo que brilla en el cielo, las nubes y las superficies blancas al sol, y son vagas y contradictorias. En cada lengua surgen en paralelo nombres nuevos para el color, y los que impulsan las cuentas con más alcance empiezan a fijarse como término común.
    origen:
    - medios/h1/5
    - adolescente/h1/4
    - oftalmologa/h1/1
  - id: h1-09
    texto: La crema solar y el maquillaje con filtro UV se ven como manchas oscuras, casi negras, con huecos claros donde no llegó el producto, y la piel muestra manchas antes invisibles. Allí donde es de día, esto provoca vergüenza social y comparaciones, sobre todo entre adolescentes, y lleva a mucha gente a lavarse la cara y quedarse sin protección justo cuando hay deslumbramiento al aire libre.
    origen:
    - disruptor/h1/3
    - adolescente/h1/5
  - id: h1-10
    texto: 'Los índices europeos no se hunden. El ajuste llega por la liquidez: los diferenciales se amplían, el libro de órdenes pierde profundidad y el volumen se concentra en unos pocos valores, con Nueva York cerrada y Tokio ya cerrada. EssilorLuxottica es el valor europeo que más sube y sufre al menos una interrupción por volatilidad en Euronext París, arrastrando a ópticas y fabricantes de filtros. Es un impulso de relato que los análisis fríos ya ven como un adelanto de demanda y no como un aumento permanente.'
    origen:
    - economista/h1/1
    - economista/h1/2
  tensiones_abiertas:
  - No está claro cuánto deslumbramiento hay en Europa en noviembre. El economista apoya con datos de AEMET (índice UV máximo de 2 en Madrid) que la molestia allí es escasa, mientras que la adolescente, el político y el disruptor describen deslumbramiento y efectos en el tráfico en España y Europa. El índice UV mide sobre todo UV-B, y el UV-A varía menos con la estación, así que no basta para zanjar la cuestión.
  - Queda por ver si el rumor de 'yo no lo veo' entre quienes llevan lentes con filtro UV se aclara pronto o se suma a los bulos sanitarios y alimenta teorías de un cambio selectivo.
  - Queda por ver si quitarse las gafas de sol y la crema por estética o curiosidad choca con la necesidad de protegerse del deslumbramiento, y cómo responden las autoridades sanitarias.
  - Queda por ver si las evaluaciones secretas de defensa se filtran y cómo cambiaría eso el silencio de los gobiernos.
  contradicciones_resueltas:
  - entre:
    - economista/h1/3
    - adolescente/h1/3
    - politico/h1/2
    - disruptor/h1/2
    decision: Se establece que el impacto físico es mayor en las regiones con UV alto y que en Europa existe pero es más suave. Su intensidad exacta en Europa queda como tensión abierta.
    motivo: El economista aporta un dato verificable, pero mide índice UV (sobre todo UV-B) y no UV-A. Los demás describen mecanismos plausibles sin dato. Ninguna parte se impone del todo.
  - entre:
    - disruptor/h1/4
    - medios/h1/2
    - adolescente/h1/2
    decision: Se combinan en un solo hecho sobre la imposibilidad de documentar el fenómeno.
    motivo: 'Las tres describen la misma limitación técnica de cámaras y pantallas con consecuencias complementarias: falsificaciones, frustración y desconfianza en la imagen.'
  descartadas:
  - id: economista/h1/4
    motivo: Tiene confianza baja y no aporta dato. Es un efecto sectorial que de momento no cambia el rumbo.
  - id: oftalmologa/h1/5
    motivo: Tiene confianza baja y no aporta dato. Además, el bulo sobre bebés ya está recogido en h1-07.
  - id: oftalmologa/h1/2
    motivo: Es un efecto de detalle clínico que solo concreta cómo se describe el fenómeno (h1-08) y no añade una consecuencia nueva para otras áreas.
  - id: adolescente/h1/1
    motivo: Es un efecto local en el aula, plausible pero de detalle. El impacto en la comunicación ya está recogido en h1-06.
  - id: disruptor/h1/5
    motivo: Las marcas fluorescentes ya emiten luz visible bajo una lámpara UV, así que la visión UV-A no las revela sin fuente UV de forma tan clara como se afirma. No aporta dato y, con el límite de diez hechos, cede ante efectos de más alcance. Puede volver en un tramo posterior con mecanismo más preciso.
  metricas:
    alarma_social: 3
    respuesta_gobiernos: comunicacion
    impacto_economico: 2
    adaptacion: 1

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h2
  afirmaciones:
  - texto: Entre las 11:00 y las 12:00, el ajuste en los mercados europeos pasa del contado a las opciones. El VSTOXX y la volatilidad implícita de las opciones sobre índices suben con mucha más fuerza de lo que caen el Euro Stoxx 50 o el Ibex, que siguen sin desplomarse. Los gestores compran protección en lugar de vender cartera.
    mecanismo: 'Vender en un mercado con poca profundidad y diferenciales amplios (h1-10) sale caro y fija pérdidas por un riesgo que nadie sabe cuantificar. Comprar puts o coberturas cuesta una prima conocida y mantiene la cartera, así que es la respuesta racional cuando la incertidumbre no tiene signo: el fenómeno puede ser neutro, malo para algunos sectores o permanente, y nadie lo sabe. Los creadores de mercado que venden esa protección la encarecen, y la volatilidad implícita recoge la incertidumbre mientras el precio de las acciones apenas se mueve.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados financieros
    - derivados
    - gestión de activos
    id: economista/h2/1
  - texto: Las aerolíneas europeas cotizadas (IAG, Air France-KLM, Lufthansa, Ryanair) son el primer sector que cae de forma clara en la segunda hora. La caída es moderada y no se convierte en desplome, porque los analistas leen pronto que el coste es de retrasos operativos y no de indemnizaciones.
    mecanismo: 'Las retenciones y ralentizaciones de salidas ordenadas por los reguladores de transporte (h1-04) se propagan en cascada: aviones y tripulaciones fuera de posición, slots perdidos y conexiones rotas durante todo el día, y eso es un coste directo fácil de modelizar. Pero el Reglamento europeo 261/2004 exime a las aerolíneas de pagar compensaciones cuando la causa son circunstancias extraordinarias, y una decisión de un regulador ante un fenómeno global encaja en ese supuesto. Sin el pasivo de las indemnizaciones, el daño se queda en un mal día de operaciones y no en un agujero en las cuentas.'
    dato: El Reglamento (CE) 261/2004 exime a las compañías de pagar compensación cuando la incidencia se debe a circunstancias extraordinarias que no podrían haberse evitado aunque se hubieran tomado todas las medidas razonables.
    fuente: https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32004R0261
    confianza: media
    areas_afectadas:
    - mercados financieros
    - transporte aéreo
    - turismo
    id: economista/h2/2
  - texto: 'Los valores de cosmética con mucho peso de la protección solar, como Beiersdorf (Nivea Sun) y en menor medida L''Oréal, bajan en Xetra y Euronext en la segunda hora. Es el reverso del impulso de las ópticas: el mercado descuenta que nadie querrá llevar en la cara un producto que se ve como una mancha negra.'
    mecanismo: 'El relato de la crema que mancha (h1-09) es tan fácil de leer como el de las gafas de sol y los mismos algoritmos de titulares lo operan en sentido contrario. El problema de fondo es estructural y no de formulación: un filtro solar protege precisamente porque absorbe o dispersa el ultravioleta, así que cualquier crema que funcione se verá oscura en el canal UV-A. Desde el escepticismo, el golpe en ventas a corto plazo es menor de lo que sugiere el precio, porque en noviembre la temporada de solares en el hemisferio norte está parada y el grueso de la demanda está ahora en el verano austral (Latinoamérica, Sudáfrica, Australia). Lo que de verdad cotiza es una opción sobre la permanencia del fenómeno, que nadie puede valorar todavía.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - mercados financieros
    - cosmética
    - consumo
    id: economista/h2/3
  - texto: En Europa, donde el deslumbramiento de noviembre es moderado, la compra de gafas de sol se mueve por miedo y no por molestia física. En la segunda hora suben con fuerza las búsquedas y pedidos en línea de gafas UV400 infantiles y de protecciones para bebés, y en los marketplaces aparecen vendedores externos que suben precios y prometen plazos que no podrán cumplir.
    mecanismo: Esto encaja con la tensión abierta sobre el deslumbramiento en Europa. Con el sol bajo de noviembre llega menos ultravioleta total y una parte menor es UV-B, pero el UV-A es la mayor parte de la radiación y no desaparece, así que hay molestia en exteriores, aunque menor que en el Golfo o la India. Lo que dispara la compra es la combinación de los bulos sanitarios ('tápale los ojos al bebé', h1-07) con la observación real de que los lactantes sufren más el deslumbramiento (oftalmologa/h1/5). Los padres compran como seguro y no como respuesta a lo que sienten ellos, y lo hacen desde el móvil porque están en interiores. El inventario de gafas infantiles homologadas es pequeño y está en almacenes de temporada baja, así que se agota antes que el de adultos y aparecen precios abusivos.
    dato: La radiación solar ultravioleta que llega a la superficie es mayoritariamente UV-A (normalmente más del 95%); cuanto más alto está el sol, mayor es la proporción de UV-B.
    fuente: https://irishskin.ie/seasonal-uv-changes-and-protecting-our-skin/
    confianza: media
    areas_afectadas:
    - consumo
    - comercio electrónico
    - distribución
    - sanidad
    id: economista/h2/4
  - texto: En comercios y bancos no hay un rechazo al efectivo por la pérdida del secreto de las marcas UV. Al contrario, en la segunda hora empiezan a circular por mensajería avisos de cajeros y comerciantes que dicen distinguir billetes falsos a simple vista junto a la ventana, y algunos detectan falsificaciones que llevaban en caja.
    mecanismo: 'Discrepo en parte de disruptor/h1/5. La marca UV pierde su valor como secreto, pero en el billete en euros nunca fue un secreto: es una comprobación pública que antes exigía una lámpara. El papel auténtico es mate bajo ultravioleta y solo brillan las fibras, la bandera y algunos elementos impresos. El papel corriente y muchas tintas comerciales llevan blanqueantes ópticos que reaccionan al UV. Si todo el mundo ve ahora el UV-A con luz natural, la comprobación que hacía la máquina la puede hacer cualquiera junto a una ventana o en la calle. A corto plazo eso endurece la detección de falsificaciones en el punto de venta, en lugar de debilitarla. El riesgo real para el sistema antifraude llega más tarde, cuando los falsificadores puedan ajustar sus tintas mirando ellos mismos el resultado.'
    dato: Según el Bundesbank, bajo luz ultravioleta el papel de un billete auténtico de 20 euros (primera serie) es mate, las fibras incrustadas brillan en verde, rojo y azul, y la bandera europea brilla en amarillo o verde.
    fuente: https://www.bundesbank.de/content/755326
    confianza: baja
    areas_afectadas:
    - medios de pago
    - comercio minorista
    - banca
    - seguridad antifraude
    id: economista/h2/5
  reacciona_a:
  - disruptor/h1/5
  - oftalmologa/h1/5
- agente: politico
  tramo: h2
  afirmaciones:
  - texto: 'En España, la primera aparición pública del Gobierno no es del presidente, sino de la ministra portavoz en la rueda de prensa posterior al Consejo de Ministros del martes, entre las 12:00 y las 13:00. Allí el Consejo se reconvierte en reunión de seguimiento y la portavoz lee un mensaje breve: no hay indicios de daño ocular, se pide no difundir avisos sin fuente oficial y se remite a Sanidad y a Interior para los detalles.'
    mecanismo: 'El suceso coincide con el día y la hora en que el Consejo de Ministros se reúne en Moncloa, así que los ministros ya están juntos y no hace falta convocar nada extraordinario. La rueda de prensa posterior es un acto de agenda fija: suspenderla sería más alarmante que celebrarla. Usar a la portavoz y no al presidente protege la legitimidad del jefe de Gobierno, que no compromete su figura ante algo sin causa, y permite responder a los bulos sanitarios con tono oficial sin declarar una emergencia que luego habría que justificar.'
    dato: El Consejo de Ministros se celebra habitualmente los martes en Moncloa y va seguido de una rueda de prensa con la ministra portavoz.
    fuente: https://www.lamoncloa.gob.es/consejodeministros/resumenes/Paginas/2026/210726-rueda-prensa-ministros.aspx
    confianza: media
    areas_afectadas:
    - gobierno
    - comunicacion_institucional
    - medios
    - salud
    id: politico/h2/1
  - texto: 'Los ministerios de Sanidad europeos y las agencias de protección civil publican en la segunda hora los primeros desmentidos formales de los falsos avisos sanitarios, con una recomendación práctica de tres puntos: gafas de sol con filtro UV400 al aire libre, no retirar la crema solar por estética y no tapar los ojos a los bebés en interiores. Es una comunicación técnica, firmada por el organismo y no por un político.'
    mecanismo: 'Los bulos usan logos copiados de la OMS y de los ministerios, y eso convierte el silencio en un coste directo para la institución suplantada: cada hora sin desmentido es una hora en que su marca respalda algo falso. Sanidad es además el único departamento con competencia clara sobre un síntoma (la fotofobia) aunque no la tenga sobre la causa. El canal técnico permite actuar sin que un ministro tenga que explicar lo que nadie sabe, y la recomendación de no quitarse la crema responde a la vergüenza social que ya ha llevado a mucha gente a lavarse la cara.'
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - salud
    - comunicacion_institucional
    - desinformacion
    id: politico/h2/2
  - texto: La presidencia rotatoria del Consejo de la UE activa el mecanismo de respuesta política integrada a las crisis (IPCR) en su modo de intercambio de información, no en activación plena. Se abre un informe conjunto de situación con aportaciones de los Estados y de la Comisión, pero no se convoca Consejo extraordinario ni se adoptan medidas comunes.
    mecanismo: 'El modo de intercambio de información es el escalón intermedio del IPCR y puede activarlo la presidencia sin el acuerdo político que exige la activación plena. Da a los gobiernos una forma de parecer coordinados ante la prensa sin comprometerse a nada, y resuelve el problema de la primera hora, cuando nadie sabía a qué ministerio asignar el asunto: el informe obliga a cada Estado a nombrar un punto de contacto. Escalar más necesitaría una amenaza concreta que justifique decisiones comunes, y no la hay.'
    dato: 'El IPCR funciona en tres modos: seguimiento, intercambio de información y activación plena.'
    fuente: https://www.consilium.europa.eu/en/policies/ipcr-response-to-crises
    confianza: media
    areas_afectadas:
    - union_europea
    - coordinacion_internacional
    - gobierno
    id: politico/h2/3
  - texto: Ante preguntas de periodistas, portavoces de defensa de varias potencias y de la OTAN declaran que no hay indicios de acción hostil, sin decir quién lo ha evaluado ni cómo. La frase confirma de forma implícita que se ha estudiado la hipótesis de un ataque, y en redes se lee como prueba de que los gobiernos sabían más de lo que decían.
    mecanismo: 'En cuanto los medios entran en directo, la pregunta de si es un ataque llega a todas las oficinas de prensa de defensa, que no pueden negarse a responder sin alimentar sospechas. La fórmula estándar de no hay indicios es la menos costosa, pero solo tiene sentido si alguien ha mirado, así que revela parcialmente las evaluaciones secretas. El problema de legitimidad se invierte: el secreto que protegía de alarmar ahora alimenta el relato de ocultación, sobre todo en los grupos de mensajería donde ya circula la idea de un cambio selectivo.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - defensa
    - comunicacion_institucional
    - desinformacion
    - confianza_institucional
    id: politico/h2/4
  - texto: 'La descoordinación internacional se desplaza: en Brasil, Argentina y el resto del Cono Sur amanece con sol de primavera en plena entrada a colegios y trabajos, y sus gobiernos pasan de las declaraciones de calma a decisiones operativas (avisos de tráfico, recreos a cubierto, retrasos en obras al aire libre). Estados Unidos y Canadá siguen de noche y su Gobierno federal mantiene el mensaje de calma, de modo que en el mismo continente conviven dos posturas.'
    mecanismo: 'A las 12:00 de Madrid son las 8:00 en Buenos Aires y Brasilia, con el sol ya alto en noviembre en el hemisferio sur, mientras que en Nueva York son las 6:00 y aún no ha salido el sol. La presión operativa llega con la luz y no con la noticia: cuando la población sale a la calle y aparecen deslumbramientos en la hora punta, los gobiernos locales y regionales actúan por responsabilidad legal, igual que los reguladores europeos en la primera hora. Cada gobierno responde a su propio reloj solar, y eso impide un mensaje común en la OEA o en el G20.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - gobierno
    - transporte
    - educacion
    - coordinacion_internacional
    id: politico/h2/5
  reacciona_a:
  - medios/h1/3
  - disruptor/h1/3
  - oftalmologa/h1/5
  - disruptor/h1/1
- agente: medios
  tramo: h2
  afirmaciones:
  - texto: 'En la segunda hora el rumor de ''yo no lo veo'' se desactiva en buena parte gracias a una prueba casera que se vuelve viral: ''quítate las gafas y mira al cielo por una ventana abierta''. Sin embargo, la aclaración genera un bulo derivado: que las gafas con filtro UV ''protegen'' del fenómeno, o que los ópticos y fabricantes ''lo sabían''. Esto se mezcla con la subida de EssilorLuxottica que ya circula en titulares.'
    mecanismo: A diferencia del color nuevo, que no se puede fotografiar, esta prueba la puede repetir cualquiera en diez segundos, así que se difunde como instrucción y no como imagen, que es el formato que mejor funciona cuando la prueba es imposible. Al confirmar que la lente cambia lo que se ve, la gente pasa de 'el cambio es selectivo' a 'el filtro me salva', una explicación más sencilla y con un culpable o un remedio a mano. La noticia bursátil de las ópticas, que ya está en el canon, le da al bulo un supuesto beneficiario y lo convierte en sospecha de lucro.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - desinformacion
    - salud
    - consumo
    - redes_sociales
    id: medios/h2/1
  - texto: Los verificadores (Maldita, Newtral, EFE Verifica y sus equivalentes en la red IFCN) publican los primeros desmentidos de los falsos comunicados de la OMS y de Sanidad, pero sin una fuente oficial que citar. Se apoyan en sociedades científicas de oftalmología y en urgencias que dicen que las exploraciones salen normales. El desmentido llega con un 'no hay pruebas de daño, pero nadie sabe la causa' que los grupos de mensajería leen como una confirmación a medias.
    mecanismo: 'Un verificador necesita una fuente con autoridad para cerrar un bulo y los gobiernos callan (h1-03), así que se recurre a la siguiente fuente con autoridad disponible: los colectivos médicos. Además, el desmentido viaja peor que el bulo por la misma vía. En la mensajería privada, el límite de reenvío y la etiqueta de ''reenviado muchas veces'' frenan las cadenas largas, pero el bulo ya circuló durante la primera hora y el desmentido entra tarde y con menos carga emocional. La honestidad sobre lo que no se sabe, que sería lo correcto, deja un hueco que el miedo rellena.'
    dato: Tras limitar en 2020 el reenvío de mensajes muy reenviados a un chat cada vez, WhatsApp informó de una caída del 70 % en ese tipo de mensajes.
    fuente: https://techcrunch.com/2020/04/27/whatsapps-new-limit-cuts-virality-of-highly-forwarded-messages-by-70
    confianza: media
    areas_afectadas:
    - desinformacion
    - salud
    - medios
    - verificacion
    id: medios/h2/2
  - texto: En Norteamérica, donde siguen a oscuras (entre las 5:00 y las 6:00 en la costa este), los primeros informativos matinales y los comentaristas de redes reciben el suceso como una noticia de Europa sin pruebas visuales y una parte lo enmarca como 'histeria colectiva' o sugestión. Así se abre una brecha transatlántica de credibilidad que dura hasta que allí sale el sol.
    mecanismo: Quien no lo ha sentido en su cuerpo solo tiene relatos y fotos que salen normales (h1-06), así que el escepticismo es el marco más barato y además da audiencia porque lleva la contraria. De noche y con iluminación interior apenas hay UV-A, así que el espectador estadounidense no puede comprobarlo por sí mismo. Las declaraciones de calma de los gobiernos americanos (h1-03) refuerzan ese marco. Cuando amanezca, el escepticismo se volverá contra quienes lo defendieron, pero en esta hora domina el formato de debate entre 'lo veo' y 'es sugestión'.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - medios
    - politica_internacional
    - redes_sociales
    - confianza_publica
    id: medios/h2/3
  - texto: 'Aparece la primera ola de fraude oportunista que explota la prueba imposible: aplicaciones y filtros que dicen ''mostrar el color nuevo en tu pantalla'', webs de venta de ''gafas para potenciar la visión UV'' o ''gafas antiultravioleta certificadas'' y dominios recién registrados con los nombres del color que se están haciendo virales.'
    mecanismo: 'La demanda de ''enséñamelo'' que ningún dispositivo puede cubrir (h1-06) es un mercado ideal para la estafa, porque el comprador no puede comprobar la promesa. La disputa por el vocabulario (h1-08) da palabras clave con un volumen de búsqueda que crece de golpe, y registrar un dominio o subir una app con esos términos cuesta minutos. Es el mismo patrón que en cualquier suceso global con búsquedas masivas: los estafadores registran dominios con el término de moda en las primeras horas.'
    dato: Al principio de la pandemia de 2020 se registraron miles de dominios nuevos relacionados con el coronavirus, y una parte se identificó como maliciosa o sospechosa.
    fuente: https://www.scmagazine.com/news/sc-stats-coronavirus-spurring-thousands-of-new-domains-many-malicious
    confianza: alta
    areas_afectadas:
    - fraude
    - consumo
    - ciberseguridad
    - desinformacion
    id: medios/h2/4
  - texto: Los primeros mensajes de salud que consiguen difusión masiva no vienen de los gobiernos sino de dermatólogos, oftalmólogos y divulgadores sanitarios con muchos seguidores, que piden no quitarse la crema solar ni las gafas de sol por estética. El mensaje choca con la tendencia de lavarse la cara y la convierte en una guerra cultural incipiente entre 'proteger' y 'ver'.
    mecanismo: 'Ante el silencio oficial (h1-03), la autoridad sanitaria la ocupan los perfiles que ya tienen audiencia y credibilidad en redes y que pueden publicar sin esperar a nadie. La vergüenza por las manchas de crema (h1-09) es un comportamiento visible y fácil de corregir con un consejo, así que es un tema perfecto para un vídeo corto. Pero el consejo pide renunciar justo a lo que hace atractivo el fenómeno, ver los colores nuevos y no salir ''manchado'', y eso polariza: los adolescentes y los curiosos responden con contenido a favor de quitarse las gafas para ''vivirlo''.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - redes_sociales
    - adolescentes
    - comunicacion_publica
    id: medios/h2/5
  reacciona_a:
  - disruptor/h1/1
  - disruptor/h1/3
  - economista/h1/1
  - politico/h1/3
- agente: oftalmologa
  tramo: h2
  afirmaciones:
  - texto: En la segunda hora queda claro que en Europa sí hay deslumbramiento en noviembre, aunque el índice UV sea bajo. Molesta más en la calle, al conducir hacia el sol y en superficies claras o mojadas que mirando al cielo a mediodía, y los oftalmólogos lo explican en los medios como un problema de ángulo y no de cantidad de sol.
    mecanismo: El índice UV mide la radiación que cae sobre una superficie horizontal y pesa sobre todo el UV-B. Al ojo, que mira en horizontal y queda protegido por la ceja cuando el sol está alto, le llega la luz directa sobre todo cuando el sol está bajo. En noviembre, entre las 11:00 y las 12:00 en Madrid, el sol está a unos 30 grados sobre el horizonte, justo en la franja en la que entra de frente en el campo visual. A eso se suma que el UV-A varía menos con la estación que el UV-B. Por eso el índice UV de 2 que cita el economista no permite deducir que la molestia sea escasa.
    dato: En invierno, con el sol a 30 grados en su punto más alto, el índice UV fue 1 a mediodía, pero el índice UV ocular con el maniquí de cara al sol rondó 4 y superó al índice UV durante todo el día. La exposición ocular máxima se dio con el sol a unos 40 grados (medición de UV-B en Japón).
    fuente: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8185396/
    confianza: media
    areas_afectadas:
    - salud
    - transporte
    - comunicacion
    id: oftalmologa/h2/1
  - texto: A media mañana se ve que la intensidad de los colores nuevos depende de la edad. Niños y adolescentes los describen vivos y molestos, los adultos de mediana edad, más tenues, y muchas personas mayores casi no los notan en el centro de la vista. En grupos familiares y redes la comparación entre abuelos y nietos se suma al rumor de que el cambio es selectivo.
    mecanismo: El cambio afecta a la percepción, pero el UV-A tiene que atravesar el cristalino para llegar a la retina. El cristalino infantil es casi transparente al UV, y con los años amarillea y absorbe cada vez más. A los operados de cataratas con lente intraocular moderna con filtro UV les pasa lo mismo que a quienes llevan gafas UV400. Es el mismo filtro óptico que el de las gafas, solo que dentro del ojo, y por eso no se puede corregir quitándose nada.
    dato: El cristalino transmite más del 75 % de la radiación UV en menores de 10 años y en torno al 10 % en mayores de 25.
    fuente: https://zeiss.com/vision-care/int/better-vision/health-prevention/why-kids-glasses-should-offer-the-best-uv-protection.html
    confianza: media
    areas_afectadas:
    - salud
    - sociedad
    - comunicacion
    - desinformacion
    id: oftalmologa/h2/2
  - texto: 'Las sociedades científicas de oftalmología y optometría son las primeras instituciones que difunden una explicación técnica del ''yo no lo veo'', antes que cualquier gobierno. Proponen una prueba casera: mirar un cielo luminoso o una pared blanca al sol con las gafas o lentillas puestas y luego sin ellas. La prueba se viraliza y frena la parte del rumor que atribuía el fenómeno a una diferencia entre personas.'
    mecanismo: 'La sociedad científica no necesita conocer la causa para explicar por qué un filtro UV400 corta lo que ahora ve el ojo, porque es óptica de manual. Además, sus portavoces tienen un incentivo para hablar: reducir las urgencias por miedo a una lesión que vieron en la primera hora. Los gobiernos siguen sin asignar el asunto a nadie, así que el primer mensaje con autoridad sale de colegios profesionales y no de Sanidad. La prueba funciona porque cada persona la comprueba por sí misma en diez segundos, y eso convence más que cualquier comunicado en una crisis donde ninguna imagen sirve como prueba.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - comunicacion
    - desinformacion
    - instituciones
    id: oftalmologa/h2/3
  - texto: En las zonas con UV alto donde se han agotado las gafas homologadas, se venden gafas de sol baratas, muy oscuras y sin filtro UV real. Quien las usa nota más deslumbramiento y fatiga que sin ellas, y empiezan las primeras quejas de que las gafas no sirven, que se suman a la confusión sobre qué protege.
    mecanismo: 'Un cristal tintado sin filtro UV reduce la luz visible, así que la pupila se dilata para compensar. Como el cristal deja pasar el UV-A, entra en el ojo más UV-A que sin gafas. Cuando la demanda supera a las existencias, el mercado informal llena el hueco con producto sin certificar, y el comprador no puede distinguirlo a simple vista. Ahora el usuario nota la diferencia con su propio ojo: unas gafas UV400 de verdad le devuelven la visión de antes y unas falsas no.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - consumo
    - comercio_informal
    id: oftalmologa/h2/4
  - texto: Las consultas cambian en la segunda hora. Bajan las llamadas por miedo a quemarse la retina y suben las de dolor de cabeza, ojos cansados y crisis de migraña en quienes han pasado un rato al aire libre o junto a ventanas soleadas. Los oftalmólogos derivan parte de ellas a atención primaria y neurología.
    mecanismo: Cuando alguien se deslumbra de forma sostenida, entrecierra los ojos, contrae la musculatura de la frente y activa las vías del trigémino que intervienen en la fotofobia, y eso produce cefalea al cabo de una o dos horas. Las personas con migraña tienen esas vías sensibilizadas y la luz intensa es uno de sus desencadenantes conocidos. Que las exploraciones de la primera hora salieran normales y empiece a circular una explicación técnica reduce el miedo a la lesión, mientras que la molestia acumulada crece con el tiempo de exposición.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - sanidad_publica
    - trabajo
    id: oftalmologa/h2/5
  reacciona_a:
  - economista/h1/3
  - disruptor/h1/1
- agente: adolescente
  tramo: h2
  afirmaciones:
  - texto: 'En clase descubrimos que los de gafas sí lo ven: alguien se las quita, flipa, y en diez minutos todos los que llevan gafas o lentillas se las están quitando y poniendo para comparar. Lo de ''yo no lo veo'' pasa de ser un bulo a ser una broma del grupo, y a los de gafas les pedimos que nos digan ''qué se pierden'' con las gafas puestas.'
    mecanismo: En un aula hay treinta personas juntas mirando lo mismo y alguien con gafas siempre acaba quitándoselas para frotarse los ojos o probar. En cuanto uno lo cuenta en voz alta, el resto lo repite porque nadie quiere ser el único que no lo ve. Por eso entre nosotros el rumor se deshace rápido, aunque en el grupo de la familia y en redes de mayores siga circulando, porque allí nadie está al lado para probar.
    dato: ''
    fuente: ''
    confianza: alta
    areas_afectadas:
    - educacion
    - redes_sociales
    - salud_visual
    - bulos
    id: adolescente/h2/1
  - texto: 'En el grupo de WhatsApp de la familia mi madre y mi tía reenvían el falso aviso de ''te quemas la retina'' y me escriben que no salga al patio sin gafas. Nosotras nos reímos de ellas en el grupo de clase, pero varias acabamos haciéndoles caso a medias: no salimos al siguiente recreo ''por si acaso'', aunque digamos que es una tontería.'
    mecanismo: Los adultos de mi familia confían en lo que parece oficial y lo reenvían sin comprobar, y yo no tengo forma de demostrar que es falso porque nadie de verdad ha dicho nada. Burlarme de los bulos me hace quedar bien con mi grupo, pero el lagrimeo del primer recreo fue real y nadie quiere arriesgarse sola, así que obedecemos sin reconocerlo.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - familia
    - bulos
    - salud_publica
    - redes_sociales
    id: adolescente/h2/2
  - texto: El instituto manda un mensaje a las familias por la aplicación del centro diciendo que el recreo y Educación Física se hacen dentro 'como precaución'. Algunos padres vienen a recoger a sus hijos antes de tiempo y en clase se nota quién se ha ido, y los que nos quedamos lo comentamos con un poco de envidia y un poco de miedo.
    mecanismo: 'La dirección no tiene instrucciones de nadie y no quiere que le pase nada a un alumno mientras está a su cargo, así que hace lo mismo que todo el mundo cuando no sabe: proteger dentro. El mensaje oficial, aunque sea solo de precaución, a muchos padres les confirma que hay peligro, y como ya han leído los avisos falsos, algunos deciden llevarse a sus hijos a casa.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - educacion
    - familia
    - salud_publica
    id: adolescente/h2/3
  - texto: 'En TikTok y en los stories la conversación sobre la cara cambia de vergüenza a reto: salen vídeos en los que alguien describe con palabras cómo se le ve la cara ''en el color nuevo'' y pide que los demás digan si ''sale bien'' o ''sale mal''. Ir con la cara lavada, sin crema ni maquillaje, empieza a verse como lo normal y lo que mola, y la que sigue con crema queda como la rara.'
    mecanismo: Como las fotos no lo pillan, la única manera de participar es contarlo y que te lo confirmen los que te ven en persona, así que se vuelve un juego de opinión. Cuando unas cuantas chicas populares se lavan la cara y lo enseñan como algo natural, el resto lo copia para no quedarse fuera, y la protección solar pasa a ser un tema de imagen, no de salud.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - redes_sociales
    - imagen_personal
    - salud_publica
    - cosmetica
    id: adolescente/h2/4
  - texto: En cuanto la tele y las cuentas de mayores empiezan a usar una de las palabras nuevas para el color, a nosotras nos empieza a dar vergüenza usarla y nos pasamos a otra, más de broma, que solo usa la gente de nuestra edad.
    mecanismo: Si la palabra la dicen los presentadores o mis padres, deja de ser nuestra y suena a viejo. Tener una palabra propia sirve para saber quién está dentro del grupo, y lo hemos hecho siempre con las expresiones de moda, así que lo mismo pasa con el nombre del color en cuestión de horas.
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - lenguaje
    - redes_sociales
    - cultura_juvenil
    - medios
    id: adolescente/h2/5
  reacciona_a:
  - disruptor/h1/1
  - medios/h1/3
  - medios/h1/5
  - disruptor/h1/3
- agente: disruptor
  tramo: h2
  afirmaciones:
  - texto: 'Durante la segunda hora, cuando ya circula que quitarse las gafas basta para ver los colores nuevos, aparece el primer grupo de verdad excluido: los operados de cataratas con lente intraocular moderna con filtro UV. Se quitan las gafas y siguen sin ver nada en ninguna parte del campo visual. Sus testimonios dan al rumor de ''yo no lo veo'' una base real, y las consultas de oftalmología empiezan a recibir la pregunta de si se puede cambiar la lente.'
    mecanismo: 'Casi todas las lentes intraoculares que se implantan desde hace décadas llevan un cromóforo que absorbe el ultravioleta, para sustituir la función protectora del cristalino natural que se extrae. Al contrario que unas gafas, esa lente no se puede quitar: el UV-A nunca llega a la retina, de modo que la capacidad nueva existe pero no tiene luz que procesar. Es lo inverso de lo que la oftalmóloga señaló en la hora 1 (afáquicos e implantes antiguos sin filtro, que ya veían el tinte): con las lentes nuevas, la cirugía de cataratas pasa de ser una ventaja a ser una barrera. Como se trata sobre todo de personas mayores, el desmentido de ''basta con quitarse las gafas'' no les sirve, y su experiencia, verdadera, se mezcla con los bulos de cambio selectivo.'
    dato: ''
    fuente: ''
    confianza: media
    areas_afectadas:
    - salud
    - informacion
    - sociedad
    id: disruptor/h2/1
  - texto: 'En los chats familiares se impone una brecha generacional en la intensidad: niños y jóvenes describen colores vivos y deslumbramiento fuerte, mientras abuelos y padres mayores dicen ver ''un poco de brillo'' o casi nada. La primera explicación popular no es óptica sino de edad, del tipo ''el cambio afecta más a los jóvenes'', y alimenta teorías sobre un fenómeno dirigido a las generaciones nuevas.'
    mecanismo: El cristalino humano amarillea con la edad y absorbe cada vez más ultravioleta y luz de onda corta antes de que llegue a la retina, así que la cantidad de UV-A que recibe un adulto mayor es mucho menor que la de un adolescente o un niño. La capacidad de percibir es la misma para todos, pero la señal que llega no. Como cada familia compara en tiempo real a tres generaciones por mensajería, la diferencia se hace visible al instante, y sin explicación médica pública se lee como una propiedad del fenómeno y no del ojo.
    dato: El cristalino empieza a amarillear hacia los 10 años a medida que absorbe UV, y a los 60 años la luz que llega a los fotorreceptores es solo un tercio de la que llega a los 20.
    fuente: https://2020mag.com/article/color-changes-as-the-eyes-age
    confianza: media
    areas_afectadas:
    - sociedad
    - informacion
    - salud
    id: disruptor/h2/2
  - texto: 'La sombra no funciona como refugio. Quien se refugia bajo árboles, toldos o soportales sigue viendo un cielo deslumbrante y nota que el alivio es parcial. En la segunda hora, en las regiones con UV alto, la gente abandona la sombra al aire libre y se concentra en espacios cerrados con techo y cristal: centros comerciales, estaciones de metro, mezquitas, oficinas y vehículos aparcados con el motor en marcha. Se vacían terrazas, mercados al aire libre y paradas de autobús descubiertas.'
    mecanismo: Discrepo de que buscar la sombra resuelva el problema (oftalmologa/h1/3 y hecho h1-01). Por la dispersión de Rayleigh, que crece mucho al acortarse la longitud de onda, una parte muy grande del UV-A llega de todo el cielo y no solo del disco solar. Por eso una sombra que tapa el sol pero deja ver el cielo apenas reduce la radiación que entra en el ojo, y además el cielo entero pasa a ser la superficie más brillante del campo visual. Solo un techo completo o el vidrio bloquean ese UV difuso. La conducta se reorganiza hacia los interiores, no hacia la sombra, y eso desplaza la gente a pocos espacios cerrados.
    dato: En un estudio en parques con el sol alto y cielo despejado, las zonas a la sombra de estructuras construidas recibieron de media unas 3 dosis eritemáticas estándar frente a unas 5 al sol, una reducción de alrededor del 40 %.
    fuente: https://www.arpansa.gov.au/built-shades-parks-protect-us-ultraviolet-radiation
    confianza: media
    areas_afectadas:
    - salud
    - movilidad
    - comercio
    - espacio_publico
    id: disruptor/h2/3
  - texto: En América, todavía de noche o al amanecer, las compañías eléctricas y los teléfonos de emergencia reciben avisos de 'chispas', 'fuego' o 'luz morada' en líneas de alta tensión, aisladores y subestaciones, sobre todo donde hay humedad o niebla. Algunas compañías mandan cuadrillas a revisar líneas que funcionan con normalidad.
    mecanismo: Las líneas y equipos de alta tensión producen descargas de efecto corona que emiten sobre todo en el ultravioleta, de forma tenue y continua. Hasta ahora solo se veían con cámaras especiales y, de hecho, esas cámaras funcionaban mejor de noche porque de día el UV solar tapa la señal. Con la vista UV-A, en la oscuridad el resplandor se vuelve visible para cualquiera que pase cerca. Quien no sabe que la corona es normal lo interpreta como una avería o un incendio, y la norma de responder a cada aviso eléctrico obliga a revisar.
    dato: Según un responsable de EPRI, la detección de corona por UV solo funcionaba de noche porque la luz solar en las bandas UV-A y UV-B enmascaraba la débil señal de la descarga.
    fuente: https://www.laserfocusworld.com/optics/article/16555562/uv-detectors-camera-detects-power-line-corona-in-daytime
    confianza: baja
    areas_afectadas:
    - energia
    - emergencias
    - infraestructuras
    id: disruptor/h2/4
  - texto: En lugares con luz solar intensa, profesores, compañeros de trabajo y familiares empiezan a ver en otras personas moratones antiguos y marcas de mordiscos o dedos que ya no se veían a simple vista. En la segunda hora aparecen las primeras preguntas incómodas en colegios, centros de trabajo y consultas, y algunas llamadas a servicios sociales y líneas de atención a la violencia, mezcladas con falsas alarmas por manchas de pigmentación normales.
    mecanismo: La medicina forense usa la fotografía ultravioleta reflejada porque las alteraciones de la piel que deja una lesión siguen absorbiendo UV cuando el moratón ya ha desaparecido para la vista normal. Con la percepción UV-A, ese contraste deja de necesitar una cámara y lo ve cualquiera a la luz del día. Lo que la víctima o el agresor daban por borrado vuelve a estar a la vista de terceros. Como nadie sabe todavía distinguir una marca de lesión de una mancha solar o de pigmento en el canal UV, la detección real llega junto con sospechas injustas.
    dato: La fotografía UV reflejada puede revelar moratones y marcas de mordisco después de que dejen de ser visibles, en algunos casos al menos 5 meses después de la lesión, según la literatura citada.
    fuente: https://www.crime-scene-investigator.net/uvchildphoto.html
    confianza: baja
    areas_afectadas:
    - proteccion_infancia
    - violencia
    - sanidad
    - educacion
    id: disruptor/h2/5
  reacciona_a:
  - oftalmologa/h1/2
  - oftalmologa/h1/3

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
