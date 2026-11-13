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
  resumen: 'En la segunda hora el rumor de que América queda fuera empieza a caer desde Brasil y el Cono Sur, donde ya es de día, aunque se reformula como una ola que llega con el amanecer y el agitador lo aprovecha para captar audiencia hispanohablante americana; los futuros estadounidenses, quietos, tampoco ponen precio a ninguna diferencia geográfica. Las instituciones pasan del silencio a la coordinación sin medidas obligatorias (Comité de Situación, Interterritorial con mensaje mínimo, recomendaciones de la DGT, Comité de Seguridad Sanitaria europeo), y la sociedad oftalmológica publica la primera guía práctica, que se convierte en la referencia contra la que plataformas y verificadores empiezan a actuar con medidas blandas, lo que el agitador exhibe como censura. El efecto cruzado más fuerte es el rechazo de la protección: el protector solar y el maquillaje con filtro se ven como manchas oscuras y las gafas con filtro restan colores nuevos, así que jóvenes y seguidores del agitador
    se quitan ambos justo con más sol, mientras dermatólogos y oftalmólogos compiten por la voz sanitaria y el mercado de gafas se separa por calidad de filtro. El canal nuevo empieza además a tocar áreas inesperadas: billetes en euros que se ven distintos, compra masiva de lámparas UV con primeros casos de lesión real, y una disparidad de percepción por edad y por lentes intraoculares que deja a parte de los mayores fuera.'
  hechos_establecidos:
  - id: h2-01
    texto: 'El rumor de que el fenómeno no afecta a América empieza a caer desde el sur: en Brasil y el Cono Sur ya es de día (en São Paulo son las 7:00 y hay sol desde poco después de las 5:00) y medios matinales y usuarios publican los primeros testimonios americanos en primera persona, que las redacciones estadounidenses en turno de noche citan como prueba. El rumor no desaparece, se reformula como una ola que llega con el amanecer franja a franja. Los futuros sobre índices estadounidenses, que cotizan casi todo el día, apenas se mueven y no ponen precio a ninguna diferencia geográfica. El agitador reorienta su emisión a la audiencia hispanohablante de América que despierta con un marco en el que cualquier resultado le da la razón (si lo ven, era algo planificado y escalonado; si lo ven distinto, a ellos les han hecho otra cosa) y llega antes que la cobertura local.'
    origen:
    - medios/h2/1
    - economista/h2/1
    - agitador/h2/3
  - id: h2-02
    texto: 'Los gobiernos pasan a coordinar sin restringir derechos. En España Moncloa activa el Sistema de Seguridad Nacional y convoca el Comité de Situación en lugar del estado de alarma; Sanidad reúne por vía telemática el Consejo Interterritorial y pacta un mensaje único de mínimos (no mirar al sol, el deslumbramiento por ahora no se asocia a lesión, urgencias solo ante síntomas concretos), sin decir que remite ni nada sobre gafas, y al menos una comunidad gobernada por la oposición se desmarca con su propia recomendación. La primera medida operativa la da la DGT con recomendaciones en paneles y redes (reducir velocidad, no parar en el arcén, cuidado con el deslumbramiento lateral), que el Gobierno exhibe como prueba de que actúa. No hay orden pública sobre el trabajo al aire libre: el protocolo de calor que obliga a adaptar horarios solo se activa con aviso meteorológico oficial, así que cada empresa decide si para o sigue y empieza la discusión entre sindicatos y patronales sobre
      quién paga las horas no trabajadas. En Bruselas la Comisión convoca el Comité de Seguridad Sanitaria sin declarar emergencia, y varios gobiernos europeos lo usan para esperar una posición común antes de recomendar nada sobre protección ocular.'
    origen:
    - politico/h2/1
    - politico/h2/2
    - politico/h2/3
    - politico/h2/4
    - economista/h2/5
  - id: h2-03
    texto: 'La sociedad oftalmológica publica una guía práctica breve para urgencias, farmacias y público: el deslumbramiento y la fatiga visual no son lesión; a urgencias solo con signos de alarma clásicos (dolor intenso, ojo rojo, pérdida brusca de visión, mancha fija); las gafas con filtro UV400 alivian y quitárselas no hace perder la capacidad nueva; ningún colirio filtra el ultravioleta; no hay que mirar al sol. Llega después de que los medios generalistas titularan su comunicado descriptivo como si fuera una guía y lo usaran para avalar recomendaciones contradictorias que no había dado, lo que la obligó a precisar qué decía. Es la única referencia técnica sobre gafas, porque el mensaje oficial de Sanidad no dice nada de ellas.'
    origen:
    - oftalmologa/h2/1
    - medios/h2/3
  - id: h2-04
    texto: 'Con el mensaje mínimo de Sanidad y la guía oftalmológica ya hay una referencia contra la que moderar, y las plataformas grandes actúan con medidas blandas, sin retiradas: etiquetan o limitan el alcance de clips del agitador que presentan el deslumbramiento como daño ocular. El agitador exhibe la etiqueta en sus canales propios como prueba de que le censuran, pide a su audiencia que le siga allí y que done para el directo de la tarde, y mantiene una versión moderada en la plataforma grande para seguir captando.'
    origen:
    - agitador/h2/4
  - id: h2-05
    texto: El hueco visual no se cierra con imágenes reales sino que se enreda más. Circula material auténtico de archivo grabado con cámaras ultravioleta, como el vídeo viral de 2014 de caras con protector oscurecidas o fotos de flores con patrones UV, que los medios publican con rótulo de archivo pero que en redes pierde el contexto y se comparte como imágenes del martes. A la vez aparecen las primeras fotos UV reales de aficionados, laboratorios forenses y astrofotógrafos con cámaras modificadas, que se muestran en falso color, no coinciden con lo que la gente ve y parte del público toma por montajes. Las unidades de verificación desmienten los bulos de ceguera y 5G apoyándose en los oftalmólogos, pero no pueden refutar los montajes de colores nuevos más que diciendo que ninguna cámara lo capta, y esos desmentidos llegan a mucha menos gente que el bulo.
    origen:
    - medios/h2/2
    - disruptor/h2/1
    - medios/h2/4
  - id: h2-06
    texto: Se extiende el rechazo de la protección por imagen y por desafío. Muchas personas, sobre todo adolescentes y jóvenes, se lavan la cara o dejan de usar protector solar, maquillaje y cremas con filtro porque a ojos ajenos se ven manchadas, y algunas evitan salir o hacerse fotos. El agitador convierte las manchas del protector en su tema estrella, mezclándolas en forma de preguntas con el discurso previo contra los filtros solares, y además anima a quitarse las gafas con filtro en exteriores presentándolas como algo que impide ver lo que hay que ver. Entre los jóvenes se forma un bando que prescinde de gafas buenas para no perderse los colores frente a otro que las presume. El resultado es menos protección justo en las horas de más sol, más deslumbramiento que llega a urgencias y una nueva voz sanitaria, la de los dermatólogos, que advierte del riesgo para la piel y compite con la de los oftalmólogos.
    origen:
    - adolescente/h2/3
    - disruptor/h2/3
    - agitador/h2/1
    - agitador/h2/2
    - adolescente/h2/4
  - id: h2-07
    texto: 'El mercado de gafas pasa de la volatilidad en bloque a la dispersión por calidad: las marcas con filtro certificado y distribución propia se leen como ganadoras y el producto barato sin filtro como existencias difíciles de vender. Las grandes plataformas de venta en línea activan sus políticas contra precios abusivos con avisos genéricos, muchos vendedores legítimos retiran también su stock, la escasez en línea empeora y la reventa se va a aplicaciones de segunda mano, mensajería y redes, sin garantía de filtro. Al mismo tiempo, quien ya lleva gafas con filtro sigue viendo colores nuevos y deslumbrándose por los laterales y por reflejo en la cara interna de la lente, lo interpreta como que sus gafas no funcionan, presenta quejas injustas y desplaza la demanda hacia monturas envolventes y gorras con visera.'
    origen:
    - economista/h2/3
    - economista/h2/2
    - oftalmologa/h2/4
  - id: h2-08
    texto: 'La disparidad de percepción toma un patrón por edad y por cirugía: niños y jóvenes describen los colores nuevos más intensos y muchos mayores apenas un velo azulado, porque el cristalino amarillea y absorbe más onda corta con los años. Los operados de cataratas con lente intraocular que bloquea el UV, que son la mayoría, los ven muy débiles o no los ven en el ojo operado. En familias y aulas los adultos dudan de lo que cuentan los niños, parte de los mayores se siente excluida y llama preguntando si puede cambiarse la lente, y la sociedad oftalmológica desaconseja cualquier cirugía para ganar visión UV.'
    origen:
    - oftalmologa/h2/2
    - oftalmologa/h2/3
  - id: h2-09
    texto: En comercios de la zona euro con luz natural, cajeros y clientes ven en los billetes dibujos de fibras y tintas de seguridad que antes no percibían, y los impresos en papel corriente con blanqueantes no se parecen a los auténticos, cuyo papel no brilla bajo UV. Hay rechazos de billetes buenos que parecen raros, algún billete falso detectado sin máquina y llamadas a los bancos centrales preguntando si el dinero sigue siendo válido.
    origen:
    - disruptor/h2/2
  - id: h2-10
    texto: 'Arranca una segunda ola de compra, no de gafas sino de linternas UV, lámparas de luz negra y de uñas para ver el fenómeno en interiores con LED, y en América, aún de noche, para comprobarlo antes del amanecer; se agotan en tiendas en línea y bazares. Con ellas y con retos de mirar al sol llegan a urgencias los primeros casos de visión borrosa o mancha central por exposición directa: son pocos frente a la ola de deslumbramiento, pero son los únicos con riesgo de lesión real, y la sociedad oftalmológica los usa para separar molestia transitoria de daño evitable.'
    origen:
    - disruptor/h2/4
    - oftalmologa/h2/5
  tensiones_abiertas:
  - Si Sanidad y el Interterritorial asumen la guía oftalmológica, incluida la recomendación sobre gafas UV400, o siguen en el mensaje de mínimos, y si la comunidad que se desmarcó arrastra a otras.
  - Si los dermatólogos o las autoridades sanitarias sacan una pauta sobre protector solar que frene el abandono, y si las marcas de cosmética solar pasan a cotizar un riesgo de rechazo estético del producto.
  - 'Cómo amanece Norteamérica: si el Gobierno federal se pronuncia antes del amanecer o deja que lo haga la luz, y si la audiencia recibe el relato ya interpretado por el agitador.'
  - Qué ocurre en el directo largo de la tarde del agitador, y si la migración a sus canales propios crece con cada etiqueta de las plataformas.
  - Si algún banco central o el BCE emite un aviso sobre la apariencia de los billetes antes de que los rechazos se extiendan.
  - Si aparecen clínicas privadas que ofrezcan recambio de lente intraocular para ganar visión UV.
  - Quién paga las horas no trabajadas al aire libre y si algún organismo emite un aviso que active los protocolos existentes.
  - Si algún gobierno atribuye el fenómeno a una acción hostil y obliga a otras cancillerías a responder.
  contradicciones_resueltas:
  - entre:
    - agitador/h2/4
    - politico/h2/2
    decision: Prevalece que el mensaje oficial español no dice que el deslumbramiento remita; la moderación blanda de las plataformas se apoya en ese mensaje mínimo (no se asocia a lesión) y en la guía oftalmológica, no en un anuncio oficial de transitoriedad.
    motivo: 'El mecanismo del político es más sólido: ningún gobierno afirma lo que sus técnicos no respaldan. Para etiquetar clips que confunden molestia con lesión basta con la referencia mínima que sí existe.'
  - entre:
    - medios/h2/3
    - oftalmologa/h2/1
    decision: 'Ambas se mantienen en secuencia: primero los medios presentan el comunicado descriptivo como guía y le atribuyen recomendaciones ajenas; después la sociedad publica una guía práctica real que precisa lo que dice.'
    motivo: La presión mediática que describe medios es precisamente el incentivo que explica por qué la sociedad publica la guía en esta hora.
  - entre:
    - oftalmologa/h2/1
    - agitador/h2/2
    - politico/h2/2
    decision: La única referencia técnica sobre gafas es la guía oftalmológica (UV400 alivia y no quita la capacidad); el mensaje oficial calla sobre gafas y el agitador llena ese silencio animando a quitárselas.
    motivo: 'No se excluyen: describen actores distintos, y el silencio oficial sobre gafas es el mecanismo que deja espacio a la consigna del agitador.'
  - entre:
    - agitador/h2/3
    - medios/h2/1
    decision: El rumor geográfico se debilita con los testimonios del sur pero no muere; el marco del agitador sobrevive porque no depende de que el rumor sea cierto.
    motivo: Medios aporta dato verificable sobre la luz en São Paulo y un mecanismo de reformulación del rumor que es compatible con la apuesta sin riesgo del agitador.
  descartadas:
  - id: economista/h2/4
    motivo: Confianza baja, especulación y sin dato; el abandono del protector ya entra por otras afirmaciones y el efecto bursátil queda como tensión abierta.
  - id: politico/h2/5
    motivo: Confianza baja, especulación y sin dato; la reacción federal estadounidense queda como tensión abierta.
  - id: medios/h2/5
    motivo: Confianza baja, especulación y sin dato; la idea de medidas blandas sin retiradas se recoge a través de agitador/h2/4.
  - id: agitador/h2/5
    motivo: Confianza baja, especulación y sin dato; los invitados y la grabación en urgencias quedan pendientes del directo de la tarde.
  - id: disruptor/h2/5
    motivo: Confianza baja y sin dato; detalle por tipo de cristal que amplía h1-04 sin consecuencia nueva suficientemente sólida.
  - id: adolescente/h2/1
    motivo: Efecto local de un centro que amplía h1-10 sin cambiar el rumbo del mundo; supera el límite de hechos.
  - id: adolescente/h2/2
    motivo: Moda local y especulativa de mensajes con crema; detalle de convivencia sin consecuencia para otras áreas.
  - id: adolescente/h2/5
    motivo: Especulación que repite hechos ya establecidos (montajes virales en h1-07 y directo del agitador en h1-09) sin consecuencia nueva.

Intervenciones de este tramo (todas, con sus ids):
- agente: economista
  tramo: h3
  afirmaciones:
  - texto: La discusión sobre quién paga las horas no trabajadas al aire libre se concreta en una pugna sobre si alguna autoridad debe emitir un aviso. Los sindicatos piden que Gobierno o comunidades recomienden formalmente no desplazarse o no trabajar al sol en las horas centrales, porque eso activaría el permiso retribuido por fenómeno adverso; las patronales prefieren recomendaciones genéricas y protocolos voluntarios, porque ese aviso cargaría a la empresa el salario de los primeros días sin poder acudir aún a un ERTE.
    mecanismo: 'Tras la DANA, el Estatuto de los Trabajadores incorporó un permiso retribuido para cuando una autoridad limita la movilidad o existe riesgo grave por un fenómeno adverso, garantizado al menos los cuatro primeros días, y el ERTE por fuerza mayor no puede aplicarse hasta pasados esos días. El texto deja indeterminado si una simple recomendación basta, así que cualquier aviso oficial se convierte en el interruptor de quién paga. Eso da a cada parte un incentivo claro: los sindicatos quieren el aviso y las patronales que no llegue, y el Gobierno, que hasta ahora solo ha recomendado vía DGT, tiene un motivo económico adicional para no emitirlo mientras no haya criterio técnico.'
    dato: Permiso retribuido del art. 37.3 g) ET, garantizado al menos los 4 primeros días; ERTE por fuerza mayor no aplicable hasta pasados esos 4 días (art. 47.6 ET); obligación de negociar protocolos ante fenómenos meteorológicos adversos (art. 85.1 ET).
    fuente: https://www.cuatrecasas.com/es/spain/laboral/art/medidas-laborales-empresas-cambio-climatico
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - empleo
    - relaciones_laborales
    - politica
    id: economista/h3/1
  - texto: 'Los rechazos de billetes empujan a parte del pequeño comercio y la hostelería de la zona euro a pedir pago con tarjeta o a poner carteles de preferencia por tarjeta. El BCE o los bancos centrales nacionales responden antes del cierre del tramo con un mensaje breve: los billetes siguen siendo de curso legal y lo que se ve son elementos de seguridad que ya estaban documentados.'
    mecanismo: 'El efectivo sigue siendo el medio más usado en número de compras en tienda, así que la duda del cajero se repite muchas veces por hora y el coste de equivocarse (aceptar un falso o perder una venta) lo asume el comercio. Pasar a tarjeta elimina la duda al instante. Para el banco central, la respuesta es barata y segura: no tiene que explicar el fenómeno, solo remitir a sus guías públicas de elementos de seguridad, que ya describen fibras y tintas visibles bajo luz ultravioleta. Su incentivo es cortar cualquier idea de que el dinero ha dejado de valer antes de que llegue a las colas de los cajeros automáticos.'
    dato: En 2024 el efectivo se usó en el 52% de las transacciones en punto de venta de la zona euro y en el 39% de su valor.
    fuente: https://www.ecb.europa.eu/press/pr/date/2024/html/ecb.pr241219~172b929461.en.html
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sistema_financiero
    - comercio
    - consumo
    id: economista/h3/2
  - texto: El abandono del protector solar se mueve poco en las ventas europeas de cosmética solar a corto plazo, porque en noviembre es temporada baja en el hemisferio norte; donde sí pesa es en el hemisferio sur, ahora en primavera avanzada y con sol fuerte, como Brasil, Argentina o Australia. Los analistas que no se suman al pánico separan ese riesgo geográfico y estacional del ruido del día.
    mecanismo: El consumo de protector solar en Europa se concentra en primavera y verano, así que dejar de usarlo un martes de noviembre resta poco a la facturación del trimestre; el riesgo real para las marcas es que el rechazo estético persista hasta la próxima campaña. En cambio, donde ahora empieza el verano el abandono coincide con el pico de compra y de exposición, y ahí sí afecta a ventas y a salud. Es una lectura que un economista puede defender en público sin apostar a un desplome que luego no ocurra.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados_financieros
    - consumo
    - salud
    id: economista/h3/3
  - texto: 'La escasez de linternas y lámparas UV no se resuelve en días: el pedido masivo llega a proveedores mayoristas de Asia ya por la tarde allí, que suben precios y aplazan entregas, mientras las plataformas de venta en línea empiezan a añadir avisos de seguridad a estos productos tras los primeros casos de lesión, con el mismo efecto que en las gafas: más reventa en canales sin control.'
    mecanismo: Son productos baratos de fabricación concentrada en Asia y distribuidos en Europa y América por importadores con inventario corto. Cuando la demanda se dispara a la vez en dos continentes, el cuello de botella no es fabricar el LED sino el transporte y los plazos, de modo que el precio sube en origen y la reposición tarda. Las plataformas, que ya actuaron con las gafas, tienen ahora un incentivo de seguridad de producto además del reputacional, y sus avisos genéricos vuelven a expulsar oferta legítima hacia la segunda mano y la mensajería.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - cadenas_de_suministro
    - comercio_electronico
    - salud
    id: economista/h3/4
  - texto: 'Con la preapertura de Nueva York ya en marcha, los valores estadounidenses de óptica, gafas y venta de lámparas reproducen la dispersión vista en Europa por calidad de filtro y canal de venta, pero sin arrastrar a los índices: los futuros siguen sin pricear un golpe agregado.'
    mecanismo: La negociación previa a la apertura en Estados Unidos empieza horas antes de la sesión de contado, y es donde los operadores estadounidenses, que han visto la reacción europea durante toda la mañana, pueden expresar la misma lectura en valores sueltos. Como ya disponen del patrón europeo, no repiten la volatilidad indiscriminada de la primera hora sino que separan ganadores y perdedores desde el principio. Al no haber daño físico ni interrupción de producción, no hay razón para vender índices enteros.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - mercados_financieros
    id: economista/h3/5
  reacciona_a:
  - disruptor/h2/2
  - disruptor/h2/3
  - disruptor/h2/4
- agente: politico
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora Sanidad amplía su mensaje sin convocar otro Interterritorial: publica en su web una nota conjunta con la sociedad oftalmológica y la de dermatología que remite a la guía oftalmológica, recomienda gafas de sol con marcado CE e indica que el protector solar sigue recomendado aunque se vea oscuro. No dice cuánto dura el fenómeno. La comunidad de la oposición que se desmarcó acusa al Ministerio de llegar tarde y copiar lo que ella ya decía, y otras comunidades de su mismo color se suman a esa crítica en lugar de a su recomendación propia.'
    mecanismo: 'El Ministerio no puede afirmar lo que sus técnicos no respaldan, pero ahora ya hay dos sociedades científicas que lo respaldan por escrito, y una nota conjunta le permite avanzar sin que parezca que rectifica el mensaje de mínimos: lo completa con autoridad prestada. Recomendar gafas con marcado CE no exige ninguna base legal nueva, porque es la regla de conformidad que ya se aplica a las gafas de sol, y le sirve para frenar la compra en reventa sin garantía. Mantener el protector solar es lo que piden los dermatólogos ante el abandono por imagen, y es el punto donde el silencio oficial le cuesta más en titulares. A la oposición le rinde más criticar el retraso que defender una recomendación propia que el Ministerio acaba de absorber.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - politica
    - comunicacion
    - consumo
    id: politico/h3/1
  - texto: 'El Ministerio de Trabajo no dicta ninguna orden de parada para el trabajo al aire libre, pero emite un recordatorio de la Inspección de Trabajo: las empresas deben evaluar el riesgo de deslumbramiento en su plan de prevención y, si hay un riesgo grave e inminente, el trabajador puede interrumpir la actividad. Convoca a sindicatos y patronales para hablar de las horas no trabajadas. Los sindicatos lo leen como una puerta para parar obras y reparto; las patronales, como una forma de pasarles el coste sin norma.'
    mecanismo: El Gobierno necesita dar respuesta a la discusión sobre quién paga sin aprobar nada que luego tenga que rectificar, y la Ley de Prevención de Riesgos Laborales ya contiene el derecho a interrumpir la actividad ante riesgo grave e inminente. Recordarlo no requiere decreto ni aviso meteorológico, que es lo que activaría el protocolo de calor y que ningún organismo puede emitir por deslumbramiento. El efecto real es trasladar la decisión a cada centro de trabajo con más respaldo para el trabajador, lo que contenta a los sindicatos, y dejar abierto el coste, que se discute en una mesa de diálogo social que da imagen de gestión.
    dato: El artículo 21 de la Ley 31/1995 de Prevención de Riesgos Laborales obliga al empresario a informar y adoptar medidas ante un riesgo grave e inminente y reconoce al trabajador el derecho a interrumpir su actividad y abandonar el lugar de trabajo si es necesario.
    fuente: https://iberley.es/legislacion/articulo-21-ley-prevencion-riesgos-laborales
    confianza: media
    evidencia: dato
    areas_afectadas:
    - trabajo
    - economia
    - politica
    id: politico/h3/2
  - texto: 'El Banco de España, coordinado con el BCE, emite una nota breve: todos los billetes en euros siguen siendo de curso legal, los dibujos que ahora se ven con luz natural son elementos de seguridad que ya existían y el comercio debe comprobar los billetes con el método habitual. El Gobierno la reenvía como otro mensaje de normalidad, pero no evita que algunos comercios empiecen a pedir pago con tarjeta.'
    mecanismo: 'Un banco central pierde más con una duda sobre la validez del dinero que con cualquier otro rumor, y aquí puede hablar sin que nadie le contradiga: los rasgos visibles bajo ultravioleta están descritos en su material público para cajeros. No necesita saber la causa del fenómeno para afirmar que el billete no ha cambiado. Para el Gobierno es un aval técnico gratuito. En la tienda, sin embargo, una nota no enseña a nadie a distinguir el billete auténtico raro del falso, y para el comerciante es más sencillo evitar el efectivo.'
    dato: El BCE describe en su material para profesionales del efectivo que, bajo luz ultravioleta, el papel del billete auténtico no brilla y aparecen fibras e imágenes con tintas fluorescentes.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/quick_guide_specimen_es.pdf
    confianza: media
    evidencia: dato
    areas_afectadas:
    - economia
    - finanzas
    - comercio
    - comunicacion
    id: politico/h3/3
  - texto: 'La oposición en España traslada el choque al Congreso: registra una solicitud de comparecencia urgente del presidente en el Pleno y pide que se altere el orden del día de esta misma semana. El Gobierno responde ofreciendo la comparecencia de la ministra de Sanidad en comisión y la del presidente más adelante, cuando haya información técnica, y sus socios parlamentarios aceptan esa fórmula.'
    mecanismo: 'Para la oposición cada hora sin comparecencia es un error que puede exhibir, y el Parlamento es el único escenario donde puede obligar al presidente a responder en directo. Al presidente le conviene no salir hasta poder decir algo que no tenga que corregir, y una ministra en comisión hace de cortafuegos: concentra el desgaste en un área técnica y no en el jefe del Gobierno. La alteración del orden del día depende de la Junta de Portavoces y de la mayoría, así que el Gobierno puede ganar días si sus socios no tienen interés en un pleno de desgaste.'
    dato: La Junta de Portavoces del Congreso, presidida por la Presidencia de la Cámara, participa en la fijación del orden del día del Pleno.
    fuente: https://www.congreso.es/es/junta-de-portavoces
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - instituciones
    id: politico/h3/4
  - texto: Con el amanecer ya llegando a la costa este de Estados Unidos y el rumor geográfico cayendo desde Brasil, la Casa Blanca no hace declaración propia y deja que hablen el Departamento de Salud y los CDC con un mensaje sanitario de mínimos parecido al europeo. Varios gobernadores salen antes que Washington con mensajes contradictorios, y la falta de una voz federal en la primera hora de luz deja que buena parte de la audiencia hispanohablante reciba primero el marco del agitador.
    mecanismo: 'El Gobierno federal ya no tiene que desmentir el rumor: lo desmiente la luz y lo han desmentido los testimonios del sur, así que la opción que menos riesgo tiene es no comprometer al presidente y delegar en las agencias sanitarias, igual que hicieron los gobiernos europeos con la OMS y el Comité de Seguridad Sanitaria. La salud pública está muy descentralizada en Estados Unidos y los gobernadores compiten por visibilidad sin la misma restricción técnica que una agencia federal. Ese reparto deja un hueco de minutos u horas que el agitador, que ya emite en español para quien despierta, ocupa antes que cualquier comunicado en inglés.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - politica
    - internacional
    - sanidad
    - comunicacion
    id: politico/h3/5
  reacciona_a:
  - agitador/h2/3
  - economista/h2/5
  - disruptor/h2/2
  - disruptor/h2/3
- agente: medios
  tramo: h3
  afirmaciones:
  - texto: En la tercera hora amanece en la costa este de Estados Unidos y los magacines matinales de las grandes cadenas, que arrancan a las 7:00, abren con corresponsales en exteriores contando en directo lo que ven con la primera luz. Esa emisión fija el relato estadounidense y lo hace con el formato del amanecer en directo, que confirma visualmente la idea de la ola que llega franja a franja aunque solo avance la luz. En México y Centroamérica aún es de noche, así que la audiencia hispanohablante del continente sigue sin experiencia propia y recibiendo el marco del agitador.
    mecanismo: 'A las 13:00 de Madrid (12:00 UTC) son las 7:00 en Nueva York, y a mediados de noviembre allí sale el sol hacia las 6:40, de modo que los programas matinales coinciden con los primeros minutos de luz. Para una cadena, que el fenómeno llegue en directo durante su franja de máxima audiencia matinal es la noticia que llevaba tres horas contando de segunda mano: lo emite como un acontecimiento en vivo, con plano del sol saliendo y testimonio del presentador. El formato, sin pretenderlo, refuerza la lectura geográfica de la ola, porque une en la misma imagen amanecer y aparición. En Ciudad de México son las 6:00 y amanece más tarde, así que allí el hueco sigue ocupado por emisiones en español desde fuera.'
    dato: 'Salida del sol en Nueva York el 15 de noviembre de 2026: 6:42 hora local (EST).'
    fuente: https://sunrise-sunset.org/us/10012
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - medios
    - opinion_publica
    - politica_internacional
    - desinformacion
    id: medios/h3/1
  - texto: 'Los pocos casos de lesión real por mirar al sol o por lámparas UV pasan a abrir titulares como los primeros heridos del fenómeno, por encima de la ola mucho mayor de deslumbramiento sin lesión. La cobertura mezcla ambas cosas en el mismo rótulo y hace que el público perciba más daño del que hay, aunque a la vez da a los medios por fin un consejo concreto y con fuente que repetir: no mirar al sol ni a lámparas UV.'
    mecanismo: Un caso clínico con hospital, diagnóstico y paciente es justo lo que la regla de la fuente permite publicar, y una lesión ocular tiene más valor de noticia que una molestia transitoria. Las redacciones llevan tres horas sin poder enseñar el fenómeno ni explicar su causa, y un herido es contenido verificable y emocional a la vez. La sociedad oftalmológica usa esos casos para separar molestia de daño evitable, pero el titular corto se queda con la palabra lesión y pierde la distinción, que el agitador recoge como confirmación de su relato de daño ocular.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - medios
    - sanidad
    - desinformacion
    - opinion_publica
    id: medios/h3/2
  - texto: Antes de que el BCE o los bancos centrales nacionales digan nada, los medios publican piezas de servicio sobre cómo distinguir un billete auténtico con los ojos nuevos, basadas en la guía pública de seguridad de los billetes en euros. Son de lo más compartido de la hora porque es la primera utilidad práctica del fenómeno, y reducen rechazos de billetes buenos donde llegan, pero también convierten a cualquier cajero en verificador sin formación y generan discusiones en comercios por billetes gastados o lavados que no coinciden con la foto.
    mecanismo: 'El BCE ya describe en material público cómo se ve un billete bajo luz UV: el papel no brilla y las fibras aparecen en rojo, azul y verde, con otros elementos en verde y amarillo. Eso es una fuente institucional citable sin necesidad de declaración nueva, y los medios la usan para llenar el hueco que dejan los bancos centrales mientras deciden qué decir. Pero esa guía describe lo que se ve con lámpara UV, no con la percepción humana del UV-A solar, que además varía con la edad y la luz del local, así que la comparación en caja no es tan clara como sugiere la pieza.'
    dato: Según la guía rápida del BCE, bajo luz UV el papel del billete no brilla y las fibras incrustadas aparecen en rojo, azul y verde.
    fuente: https://www.ecb.europa.eu/euro/pdf/material/Quick_Guide_EN_Specimen.pdf
    confianza: media
    evidencia: dato
    areas_afectadas:
    - medios
    - economia
    - comercio
    - banca
    id: medios/h3/3
  - texto: Los vídeos de seguidores del agitador grabando en urgencias se convierten en noticia para los medios serios, que los cubren como historia de saturación sanitaria con fuentes hospitalarias y colegios profesionales. Al hacerlo citan al agitador y su directo de la tarde, lo que le da una difusión que no tenía fuera de sus canales; algunas redacciones optan por no nombrarle, pero la mayoría lo nombra porque la competencia ya lo ha hecho.
    mecanismo: 'La grabación en un centro sanitario genera un conflicto concreto con fuentes oficiales dispuestas a hablar (gerencias, colegios de médicos, sindicatos sanitarios), así que cumple la regla de la fuente y permite contar la historia desde el lado de los sanitarios. Pero explicar por qué graban obliga a explicar quién se lo pide. Es el patrón descrito como amplificación: cubrir a un manipulador para criticarlo blanquea su mensaje y le lleva audiencia. La decisión de silenciarlo no se sostiene cuando la primera cabecera lo nombra, porque las demás compiten por la misma búsqueda.'
    dato: El informe The Oxygen of Amplification describe cómo la cobertura periodística de manipuladores, incluso crítica, amplifica y da credibilidad a sus mensajes.
    fuente: https://datasociety.net/output/oxygen-of-amplification
    confianza: media
    evidencia: dato
    areas_afectadas:
    - medios
    - sanidad
    - desinformacion
    - opinion_publica
    id: medios/h3/4
  - texto: Las piezas de interés humano sobre mayores y operados de cataratas que no ven los colores nuevos se multiplican en la preparación de los informativos de mediodía, y en ellas aparecen portavoces de clínicas oftalmológicas privadas como expertos. No ofrecen todavía recambio de lente, pero la cobertura instala la pregunta de si se puede operar y da a esas clínicas visibilidad gratuita antes de que exista una oferta.
    mecanismo: Un abuelo que no ve lo que ve su nieto es un personaje con el que se identifica toda la audiencia y que no exige explicar la causa, ideal para los informativos de las 14:00 y 15:00 que se montan en esta hora. La sociedad oftalmológica ya ha dicho que desaconseja la cirugía, pero las redacciones buscan más voces y los departamentos de comunicación de las clínicas privadas ofrecen cirujanos disponibles al momento. El cirujano dice que hay que esperar, pero el rótulo plantea la operación como posibilidad, y eso alimenta las llamadas a consultas.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - medios
    - sanidad
    - opinion_publica
    id: medios/h3/5
  reacciona_a:
  - politico/h2/5
  - oftalmologa/h2/5
  - disruptor/h2/2
  - agitador/h2/5
  - oftalmologa/h2/3
- agente: oftalmologa
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora la sociedad oftalmológica añade a su guía un aviso anticipado sobre las lámparas compradas en la segunda hora: quien se haya iluminado los ojos con lámparas germicidas, de bronceado o mal etiquetadas puede notar horas después dolor intenso, lagrimeo, ojo rojo y sensación de arena, y eso sí es una lesión (fotoqueratitis) que debe ir a urgencias. Lo hace antes de que lleguen los casos porque sabe que aparecerán por la tarde y la noche, desconectados en el tiempo de la exposición.'
    mecanismo: 'La fotoqueratitis es una quemadura de la superficie del ojo con latencia: los síntomas no salen al mirar la lámpara sino después, cuando la persona ya no relaciona el dolor con lo que hizo. En los bazares y tiendas en línea se venden mezcladas linternas UV-A, lámparas de uñas y lámparas germicidas UV-C, y el comprador no distingue entre ellas. Si la sociedad no lo explica antes, esos casos llegarán por la tarde, coincidiendo con el directo del agitador, y se leerán como daño retardado del propio fenómeno. Anticiparse le permite atribuirlos a la lámpara y no al suceso, y conservar la autoridad de su guía, que ya dijo que el deslumbramiento no es lesión.'
    dato: Los síntomas de la fotoqueratitis suelen aparecer entre 30 minutos y 12 horas después de la exposición; entre las causas figuran las lámparas germicidas o de laboratorio, las camas y lámparas de bronceado y la soldadura.
    fuente: https://eyewiki.aao.org/Photokeratitis
    confianza: alta
    evidencia: dato
    areas_afectadas:
    - sanidad
    - urgencias
    - comercio
    - desinformacion
    id: oftalmologa/h3/1
  - texto: Con el sol cerca de su punto más alto en España, la sociedad precisa que las nubes finas y la sombra abierta no eliminan el ultravioleta y que la nieve lo multiplica. En zonas nubladas mucha gente cree que el fenómeno se ha apagado o se queda en terrazas a la sombra pensando que no se deslumbra, y en montaña y estaciones con nieve aparecen los deslumbramientos más fuertes del día.
    mecanismo: El UV-A atraviesa la nubosidad ligera y llega dispersado desde todo el cielo, así que en un día gris los colores nuevos se ven más difusos pero siguen ahí, y el brillo llega de todas partes y no solo del sol. La gente usa el cielo nublado como señal de que no hay riesgo, igual que hace con las quemaduras solares. La nieve fresca refleja buena parte del ultravioleta desde abajo, por donde ni gorra ni visera protegen, de modo que montañeros, trabajadores de alta montaña y quien esté en zonas nevadas sufren el deslumbramiento más intenso. La sociedad lo incorpora porque es física conocida, encaja con lo que ya dijo de las gafas envolventes y le permite contestar a la lectura de que el fenómeno se apaga sin entrar en su duración.
    dato: La OMS advierte que las nubes finas pueden reducir poco el UV e incluso aumentarlo por dispersión, que la sombra abierta no impide quemarse en días de UV alto, y que la nieve fresca puede reflejar hasta el 80 % del UV frente a menos del 10 % de hierba, suelo o agua.
    fuente: https://www.who.int/uv/faq/whatisuv/en/index2.html
    confianza: media
    evidencia: dato
    areas_afectadas:
    - sanidad
    - trabajo_al_aire_libre
    - turismo_montana
    - percepcion_publica
    id: oftalmologa/h3/2
  - texto: 'La sociedad oftalmológica tiende la mano a los dermatólogos y propone un mensaje conjunto con una explicación física de las manchas: si la crema o el maquillaje se ven oscuros es porque absorben el ultravioleta, es decir, porque están protegiendo. Busca convertir la mancha en la prueba de que el filtro funciona, igual que la lente oscura de unas gafas UV400, y quitarle al agitador su tema estrella.'
    mecanismo: 'La sociedad pierde autoridad si la voz sanitaria se parte entre ojo y piel, y gana si es ella la que explica el mecanismo óptico común a gafas y crema: un filtro absorbe el UV-A y por eso, en el canal nuevo, se ve oscuro. Esa explicación es física básica, no requiere conocer la causa del fenómeno y responde directamente a la interpretación del agitador, que da la vuelta a un hecho real. El límite es que la explicación corrige el miedo pero no la vergüenza: a un adolescente le importa más cómo le ven que saber que la mancha protege, de modo que el abandono del protector se frena en adultos antes que en jóvenes. Discrepo de la idea implícita en agitador/h2/1 de que nadie puede corregirle en la hora: el hecho físico que usa es justamente el que la oftalmología puede explicar.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - dermatologia
    - cosmetica
    - desinformacion
    - jovenes
    id: oftalmologa/h3/3
  - texto: 'La sociedad emite una recomendación específica para niños: gorra con visera y gafas con filtro UV400 en el recreo y en exteriores durante los primeros días, sin miedo a que pierdan los colores nuevos. Choca con colegios e institutos que han soltado a los alumnos a la calle y con el bando juvenil que se quita las gafas, y aumentan las consultas pediátricas por deslumbramiento.'
    mecanismo: 'El cristalino infantil es más transparente a la onda corta y la pupila es mayor, así que los niños son los que reciben más UV-A en la retina: por eso ven los colores más intensos (ya en el canon) y por la misma razón son los que más se deslumbran. La sociedad tiene base clínica previa para tratarlos como grupo prioritario, porque la protección ocular infantil ya se recomendaba antes del martes. A la vez, los niños son los menos capaces de dejar de mirar algo fascinante, y los centros que mandaron a casa a los alumnos los han puesto al sol en las horas centrales, como describe adolescente/h2/1.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - sanidad
    - educacion
    - familias
    - pediatria
    id: oftalmologa/h3/4
  - texto: Aparecen los primeros mensajes de clínicas privadas, sobre todo de cirugía refractiva y de cristalino, que responden a las llamadas de mayores operados de cataratas con citas de valoración para estudiar la lente, sin anunciar todavía el recambio de forma explícita. La sociedad oftalmológica sale a desautorizarlo en público y pide a los colegios de médicos vigilancia de la publicidad sanitaria.
    mecanismo: 'La demanda ya está en el canon: mayores que se sienten excluidos y llaman preguntando si pueden cambiarse la lente. Las clínicas privadas de cristalino tienen agenda, márgenes y un mercado de cirugía electiva ya montado, y ofrecer una valoración no compromete a nada ni exige afirmar que el recambio funcione. Para la sociedad es una amenaza directa a su autoridad: si una clínica con oftalmólogos colegiados vende esperanza, el público no distingue entre la sociedad y el gremio. Su incentivo es marcar distancia pronto, recordando que el recambio de lente intraocular es una cirugía con riesgos reales, sin indicación médica, y que nadie sabe si el fenómeno durará.'
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - sanidad_privada
    - mayores
    - regulacion_publicidad
    - etica_medica
    id: oftalmologa/h3/5
  reacciona_a:
  - agitador/h2/1
  - disruptor/h2/3
  - disruptor/h2/4
  - adolescente/h2/1
  - agitador/h2/5
- agente: adolescente
  tramo: h3
  afirmaciones:
  - texto: Entre las doce y la una, en mi casa y en las de mis amigas sacamos las lámparas de uñas de nuestras madres o hermanas y las linternas de luz negra de las fiestas para seguir viendo los colores dentro. Hacemos juegos de alumbrarnos la cara, los dientes o los ojos unos a otros, y alguno se queda viendo raro un rato y lo cuenta como si fuera un logro.
    mecanismo: Dentro de casa, con la luz normal, no se ve casi nada, y a mi edad no puedes estar todo el rato en la calle porque tus padres o el instituto no te dejan. La lámpara de uñas ya está en el baño, no hay que comprar nada. Como en las tiendas se han agotado, quien tiene una se convierte en el sitio donde quedar. Y como el reto de mirar al sol ya circula, alumbrarse los ojos de cerca parece más seguro aunque no lo es, y aguantar más que los demás da estatus en el grupo.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - jovenes
    - consumo
    - redes_sociales
    id: adolescente/h3/1
  - texto: 'Como los adultos ven los colores mucho más flojos, en mi clase y en casa los chavales pasamos a ser los que explican cómo es: hacemos vídeos de explicarle a mi madre o a mi abuelo lo que estoy viendo, y en clase algunos profes nos preguntan a nosotros. Eso nos da una autoridad que nunca habíamos tenido, y algunos la usan para exagerar o inventarse cosas porque nadie mayor puede comprobarlo.'
    mecanismo: Ya se sabe que los mayores, y sobre todo los abuelos operados de cataratas, ven solo un velo. Si eres tú quien lo ve mejor, eres tú quien cuenta cómo es, y en un tema que no se puede grabar el que mejor lo cuenta gana. Los vídeos de hijo explicando a padre que no entiende funcionan muy bien en redes porque son graciosos y tiernos a la vez. Pero como el adulto no puede comparar, nadie te pilla si añades colores o cosas que no ves, y eso mezcla lo verdadero con lo inventado.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - familias
    - educacion
    - redes_sociales
    - desinformacion
    id: adolescente/h3/2
  - texto: 'En casa empieza la pelea por la crema: mi madre me obliga a ponérmela antes de salir y yo me la quito en el portal o en el ascensor con toallitas. Entre nosotras se pasa el truco de llevar crema en la mochila para ponérsela solo en los brazos o la nuca, donde no se nota en la cara, y llevar gorra.'
    mecanismo: Dependo de mis padres y ellos han oído a los dermatólogos en la tele, pero lo que me importa es lo que digan de mi cara mis amigas, que me van a ver en diez minutos. El daño del sol es para dentro de años y la mancha se ve ahora. Así que obedezco donde me ven mis padres y desobedezco donde me ven los demás. La gorra y la crema en sitios que no son la cara es la forma de no pelearme con nadie, aunque la cara se queda sin nada justo con más sol.
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - salud
    - familias
    - jovenes
    - cosmetica
    id: adolescente/h3/3
  - texto: El directo de la tarde del agitador nos llega sobre todo a trozos, en vídeos de otros tiktokers que se ríen de él o le contestan, no porque le sigamos. Pero al compartirlos para reírnos, sus frases sobre que las gafas te quitan lo que hay que ver o que la crema esconde algo se quedan, y alguno de clase las repite en serio.
    mecanismo: A mi edad casi nadie se pone a ver un directo de horas de un señor, pero sí los cortes de treinta segundos con reacciones, que es lo que sale en la página principal. Compartirlo para burlarte te hace quedar bien en el grupo, pero el corte lleva su frase entera y sin explicación al lado. Como encima coincide con algo que tú ves, como la cara manchada de crema, la frase suena menos loca de lo que parecía, y a quien ya prefería no llevar gafas le da una excusa.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: especulacion
    areas_afectadas:
    - redes_sociales
    - desinformacion
    - jovenes
    id: adolescente/h3/4
  - texto: A la hora de salida algunos institutos dejan a los alumnos dentro un rato más o les piden que esperen en el vestíbulo hasta que pase lo peor del sol, pero sin orden oficial cada centro hace una cosa distinta y los padres se quejan en el grupo de familias de que en el instituto de al lado lo hacen de otra forma.
    mecanismo: El instituto no puede cambiar el horario por su cuenta y nadie de Educación ni de Sanidad le ha dicho nada concreto, solo que no hay que mirar al sol. Así que cada director decide con lo que tiene, igual que las empresas con los trabajadores de la calle. Las familias comparan en los grupos de WhatsApp lo que hace cada centro y cualquier diferencia se lee como que en el tuyo lo hacen mal, lo que mete más presión al instituto y a la consejería.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - educacion
    - familias
    - instituciones
    id: adolescente/h3/5
  reacciona_a:
  - disruptor/h2/4
  - oftalmologa/h2/2
  - disruptor/h2/3
  - agitador/h2/2
- agente: agitador
  tramo: h3
  afirmaciones:
  - texto: 'Cuando amanece en Colombia, Venezuela, Perú y la costa este de Estados Unidos y la gente confirma con sus ojos el fenómeno, el agitador no rectifica nada: activa la mitad del marco que dejó preparado en la hora 2 y presenta la llegada franja a franja como prueba de que fue algo escalonado y planificado. Retransmite en directo amaneceres enviados por seguidores americanos, ciudad a ciudad, y convierte el amanecer en un formato de seguimiento que retiene a la audiencia hispanohablante recién captada mientras los medios locales aún arrancan sus matinales.'
    mecanismo: 'El agitador formuló en la hora 2 una apuesta en la que cualquier resultado le da la razón, así que el desmentido geográfico que trae el sol no le cuesta credibilidad ante su audiencia. El mapa de franja solar, que ya circula como formato que confirma la ola, le da una narrativa visual sin necesidad de imágenes del fenómeno: lo que avanza es la luz, pero él lo cuenta como un despliegue. Llegar antes que las redacciones locales le permite que el público que despierta reciba primero su interpretación y no la del comunicado federal mínimo.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - comunicacion
    - redes_sociales
    - america
    - confianza_institucional
    id: agitador/h3/1
  - texto: 'El agitador adopta la disparidad por edad y por lente intraocular como segundo tema estrella después del protector solar: plantea en forma de preguntas por qué a millones de operados de cataratas les pusieron una lente que bloquea el ultravioleta y quién decidió que los mayores no vieran. Parte de su audiencia mayor, y sobre todo hijos de mayores, llama a clínicas preguntando por el recambio de lente, lo que crea demanda visible para que alguna clínica privada se anuncie, justo cuando la sociedad oftalmológica la desaconseja.'
    mecanismo: 'Repite el patrón que le funcionó con la crema: un hecho físico real y comprobable (las lentes intraoculares bloquean el UV desde hace décadas por diseño protector) al que solo le cambia la interpretación, de protección a privación. La exclusión de los mayores es un agravio emocional que no requiere imagen y amplía su audiencia más allá de los jóvenes. Que la sociedad oftalmológica desaconseje la cirugía le sirve para presentarla otra vez como parte interesada que quita algo, y el villano vuelve a ser industrial y difuso, sin nombres propios, lo que limita su riesgo de sanción.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - mayores
    - sanidad_privada
    - redes_sociales
    id: agitador/h3/2
  - texto: 'Ante la aparición de una voz dermatológica que advierte contra quitarse el protector, el agitador no la discute de frente: la enfrenta con la de los oftalmólogos y muestra en directo recortes de ambas como prueba de que ni los expertos se ponen de acuerdo. Usa también el mensaje de mínimos de Sanidad, que calla sobre gafas, y la comunidad autónoma que se desmarcó para sostener que no hay una versión oficial en la que confiar.'
    mecanismo: 'Cada nueva voz sanitaria que entra sin coordinarse con las demás añade una contradicción aparente aunque las recomendaciones sean compatibles (proteger la piel y proteger los ojos no se excluyen). Para quien vive de la desconfianza, exhibir la falta de una pauta única es más rentable que rebatir una pauta concreta, porque no le obliga a afirmar nada falsable. El hueco existe de verdad: Sanidad no ha asumido la guía oftalmológica ni ha dicho nada del protector, y una comunidad ya ha roto el consenso.'
    dato: ''
    fuente: ''
    confianza: alta
    evidencia: inferencia
    areas_afectadas:
    - salud
    - comunicacion
    - confianza_institucional
    - cosmetica
    id: agitador/h3/3
  - texto: 'Cuando llegan a urgencias los primeros casos de mancha central por mirar al sol o a lámparas UV, el agitador se cubre: dice en directo que no hay que mirar al sol, pero presenta a esos pacientes como víctimas del fenómeno y no de la exposición directa, y los suma a su lista de seguidores que dicen haber perdido vista. Así borra la frontera que la sociedad oftalmológica intenta trazar entre molestia transitoria y daño evitable.'
    mecanismo: Los casos de retinopatía solar son el único daño real del tramo y amenazan con convertirse en una advertencia concreta que normalice el resto. Al agitador le conviene a la vez no aparecer como responsable de los retos, porque eso sí le expondría a retiradas y a pérdida de credibilidad, y no dejar que el daño se atribuya a una conducta evitable, porque entonces el fenómeno queda explicado. Mezclar los casos reales con los testimonios de deslumbramiento le da una cifra de afectados que crece sin tener que inventarla.
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - salud
    - urgencias
    - redes_sociales
    id: agitador/h3/4
  - texto: 'El agitador separa definitivamente audiencia y cobro: en la plataforma grande deja solo piezas de asombro que no chocan con la pauta sanitaria y sirven de escaparate, y traslada a sus canales propios de mensajería el contenido de sospecha, la convocatoria del directo de la tarde y la petición de donaciones. Sus canales propios crecen con cada etiqueta, pero con un público más pequeño y más fiel que el de la plataforma grande.'
    mecanismo: Las etiquetas y la limitación de alcance de la hora 2 le muestran que la plataforma grande ya tiene una referencia contra la que moderar, y la desmonetización le golpearía justo cuando más donaciones recibe. La investigación sobre figuras expulsadas que migran a Telegram describe este movimiento hacia canales alternativos, donde el creador conserva la relación directa con su núcleo aunque pierda alcance general. Mantener el escaparate moderado le asegura seguir captando nuevos seguidores, que después deriva a donde controla la conversación y el pago.
    dato: Rogers (2020) estudia la migración a Telegram y redes alternativas de celebridades de internet expulsadas de las plataformas grandes.
    fuente: https://voxpol.eu/?p=18226
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - redes_sociales
    - plataformas
    - moderacion
    - economia_creadores
    id: agitador/h3/5
  reacciona_a:
  - oftalmologa/h2/3
  - oftalmologa/h2/5
  - disruptor/h2/3
  - medios/h2/1
  - politico/h2/5
- agente: disruptor
  tramo: h3
  afirmaciones:
  - texto: 'En la tercera hora, con el sol cerca del mediodía en Europa, la gente empieza a ver en la cara de los demás el daño solar acumulado que antes era invisible: pecas bajo la piel, léntigos y manchas de sol que aparecen intensas en mayores, en trabajadores del campo y la obra y en quien ha tomado mucho el sol. Como los jóvenes son los que mejor perciben los colores nuevos, son hijos y nietos quienes ven a padres y abuelos llenos de manchas. Los dermatólogos convierten esa imagen en su mejor argumento contra el abandono del protector: lo que se ve en la cara del abuelo es lo que deja el sol sin crema. Aparece una corriente contraria al rechazo del protector, mientras farmacias y consultas reciben a gente asustada por manchas que llevan años ahí.'
    mecanismo: 'La melanina absorbe con fuerza el UV-A, así que las acumulaciones de pigmento que deja la exposición solar, aunque estén por debajo de la superficie y no se vean con luz visible, contrastan mucho en el canal ultravioleta. Es exactamente lo que mostraba el vídeo viral de 2014 que ya circula en redes, pero ahora se ve sin cámara y en la cara de personas conocidas. La disparidad por edad del canon hace que lo vean sobre todo los jóvenes mirando a los mayores, que apenas pueden comprobarlo en sí mismos. El relato del agitador sobre el protector se apoya en que la crema se ve oscura; la piel dañada también se ve oscura, a manchas y sin crema, y eso da a los dermatólogos una prueba visible que hasta ahora no tenían. El efecto no anula el rechazo estético, pero lo parte: quien ve la cara de sus mayores tiene un motivo concreto para seguir usando protector.'
    dato: La fotografía ultravioleta muestra daño solar bajo la superficie que no se ve a simple vista, como pecas subsuperficiales, léntigos solares y manchas de la edad; el vídeo How the sun sees you de 2014 lo popularizó.
    fuente: https://www.smithsonianmag.com/smart-news/ultraviolet-camera-reveals-secret-price-sunbathing-180952363/
    confianza: media
    evidencia: dato
    areas_afectadas:
    - salud
    - dermatologia
    - cosmetica
    - familias
    - comunicacion_sanitaria
    id: disruptor/h3/1
  - texto: 'Profesores, pediatras, sanitarios de urgencias y compañeros de trabajo empiezan a ver en la piel de otras personas moratones antiguos que ya se habían curado a simple vista. En la tercera hora llegan las primeras consultas a servicios de protección de menores y a líneas de violencia de género, junto a falsos positivos: manchas de nacimiento, lunares o pigmentación normal tomadas por golpes, y familias señaladas sin motivo. Quien tapaba un golpe con maquillaje queda más expuesto, porque la base con filtro se ve oscura justo encima de la zona que quería ocultar.'
    mecanismo: 'La fotografía ultravioleta reflejada se usa en medicina forense precisamente porque revela moratones y mordeduras cuando ya no se ven: los cambios de pigmento que deja la lesión en la epidermis absorben UV-A durante meses. Ahora cualquiera que mire con luz natural percibe esas marcas. Los profesionales con obligación de comunicar sospechas de maltrato, como docentes y sanitarios, ven algo nuevo sin ningún criterio para interpretarlo, y en la duda los protocolos empujan a notificar. Como no existe una guía sobre qué es un moratón antiguo y qué es pigmentación, se mezclan detecciones reales con alarmas falsas, y el maquillaje con filtro, que ya se ve a manchas, señala la zona tapada en lugar de esconderla.'
    dato: La fotografía ultravioleta reflejada muestra moratones o mordeduras que ya no son visibles; la literatura recoge resultados al menos 5 meses después de la lesión.
    fuente: https://www.crime-scene-investigator.net/uvchildphoto.html
    confianza: media
    evidencia: dato
    areas_afectadas:
    - proteccion_menores
    - violencia_de_genero
    - educacion
    - sanidad
    - justicia
    id: disruptor/h3/2
  - texto: 'La discusión sobre quién paga las horas no trabajadas al aire libre choca con un obstáculo técnico: los sindicatos piden a la AEMET un aviso que active los protocolos de adaptación de jornada, y la AEMET responde que la radiación ultravioleta no está entre los fenómenos de su sistema de avisos, así que no puede emitir uno. A la vez, su índice UV, que solo es informativo, se empieza a usar al revés: en redes y en grupos se consulta como un pronóstico de dónde y cuándo se verán mejor los colores nuevos, y un índice alto pasa a significar salir a mirar en lugar de protegerse.'
    mecanismo: La norma que obliga a adaptar o reducir la jornada al aire libre se dispara cuando la AEMET o el órgano autonómico emite un aviso naranja o rojo, pero el plan de avisos solo cubre lluvia, nieve, viento, tormentas, temperaturas, fenómenos costeros, polvo, niebla, galernas, deshielos y aludes. El índice UV se publica como predicción aparte, sin niveles de aviso. Sin ese fenómeno en la lista, el único gatillo legal existente no puede activarse, la decisión sigue en cada empresa y la presión se traslada a pedir una reforma o una instrucción del Ministerio de Trabajo. Mientras, el índice UV es el único dato oficial que habla de ultravioleta y la gente lo reinterpreta según su nuevo interés.
    dato: Meteoalerta emite avisos para lluvia, nieve, viento, tormentas, temperaturas máximas y mínimas, fenómenos costeros, polvo en suspensión, galernas, rissagues, niebla, deshielos y aludes; la radiación ultravioleta figura como predicción aparte. La adaptación obligatoria de condiciones se activa cuando se emite aviso de fenómenos de nivel naranja o rojo.
    fuente: https://www.aemet.es/en/eltiempo/prediccion/avisos/ayuda ; https://www.garrigues.com/es_ES/noticia/altas-temperaturas-obligaran-empresas-adoptar-medidas-preventivas-proteger-trabajadores
    confianza: media
    evidencia: dato
    areas_afectadas:
    - trabajo
    - relaciones_laborales
    - meteorologia
    - comunicacion_publica
    id: disruptor/h3/3
  - texto: 'Al final de la tercera hora amanece en la costa este de Estados Unidos y los primeros testimonios en persona dicen que se ve poco: un velo débil, no los colores intensos que cuentan desde Europa. En lugar de cerrar el rumor geográfico, ese primer amanecer lo alimenta en la versión que el agitador ya había preparado, la de que a ellos les han hecho otra cosa o les llega más flojo, hasta que el sol sube y el efecto se iguala horas después.'
    mecanismo: 'Con el sol en el horizonte la luz atraviesa mucha más atmósfera y llega muy poco ultravioleta, así que el primer rato de luz en Nueva York o Washington da la experiencia más débil del fenómeno. La gente que madruga para comprobarlo compara con relatos europeos escritos cerca del mediodía y concluye que hay una diferencia. Coincide además con la hora en que el agitador ya tiene audiencia americana despierta y con un marco en el que cualquier diferencia le da la razón, mientras el comunicado federal mínimo solo dice que el fenómeno es global. Discrepo de que el amanecer desmienta por sí solo el rumor: el primer amanecer lo desmiente mal, porque llega con la luz más pobre en ultravioleta del día.'
    dato: ''
    fuente: ''
    confianza: media
    evidencia: inferencia
    areas_afectadas:
    - desinformacion
    - medios
    - politica_estados_unidos
    - opinion_publica
    id: disruptor/h3/4
  - texto: 'Los solarios y centros de uñas con lámparas UV se convierten en salas para ver el fenómeno en interiores: reciben reservas y gente que entra sin intención de broncearse, y algunos clientes se quitan las gafas protectoras dentro de la cabina para ver los colores. Llegan a urgencias los primeros casos de ojos irritados y dolorosos horas después de una sesión, que se confunden con el deslumbramiento transitorio.'
    mecanismo: La segunda ola de compra de lámparas ha agotado el producto doméstico, y el solario es el único lugar abierto al público con una fuente de UV-A potente y sin depender del sol, útil también en edificios y casas donde el LED no deja ver nada. Para el negocio es una demanda inesperada en noviembre, temporada baja, y tiene incentivo para aceptarla. Las gafas protectoras que se exigen en la cabina quitan justo lo que el cliente ha venido a ver. Una exposición ocular cercana y sin protección a una lámpara de bronceado puede inflamar la córnea con síntomas que aparecen horas después, y como llegan mezclados con la ola de deslumbramiento, el triaje tarda en separarlos.
    dato: ''
    fuente: ''
    confianza: baja
    evidencia: especulacion
    areas_afectadas:
    - salud
    - comercio
    - urgencias
    - regulacion_sanitaria
    id: disruptor/h3/5
  reacciona_a:
  - economista/h2/4
  - agitador/h2/1
  - economista/h2/5
  - medios/h2/1
  - agitador/h2/3
  - politico/h2/5

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
