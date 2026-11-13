Eres el evaluador de una simulación de escenarios de Aftermath Studio. No pronosticas ni consolidas: mides el estado del mundo con unas escalas definidas.

## El mundo
Suceso: Todos los seres humanos desarrollan a la vez la capacidad de ver el espectro ultravioleta.
Momento cero: Martes, 10:00 hora de Madrid, simultáneo en todo el planeta. Alcance: global.
Supuestos (son hechos del mundo; no los discutas ni los expliques):
- El cambio es instantáneo y afecta a todas las personas, incluidos recién nacidos
- Se percibe el ultravioleta cercano (UV-A) como colores nuevos, sin perder la visión normal
- Los primeros días hay deslumbramiento y fatiga visual en exteriores con mucho sol; remite en unas dos semanas y no deja daño ocular permanente
- Nadie conoce la causa y nadie sabe si es permanente
Fuera de alcance: Explicar la causa del fenómeno; Efectos en animales

## Tramo que evalúas
Hora 3 (PT3H desde el suceso)
Estado del mundo al cierre de este tramo:
estado_del_mundo:
  tramo: h3
  resumen: 'En la tercera hora amanece en la costa este de Estados Unidos y los matinales lo emiten en directo, pero la primera luz, pobre en ultravioleta, deja un velo débil que alimenta la versión de que a ellos les llega distinto; sin voz de la Casa Blanca, el agitador convierte el amanecer franja a franja en prueba de un despliegue planificado. En España Sanidad completa su mensaje con una nota conjunta con oftalmólogos y dermatólogos (gafas con marcado CE, protector aunque se vea oscuro porque eso es que protege), Trabajo recuerda el derecho a interrumpir la actividad ante riesgo grave sin dictar parada y el Banco de España, con el BCE, confirma que los billetes son válidos, mientras la AEMET no puede emitir un aviso por ultravioleta que active el permiso retribuido y la oposición lleva el choque al Congreso. El efecto cruzado más fuerte es que el canal nuevo revela lo que la piel escondía: el daño solar acumulado en la cara de los mayores da a los dermatólogos una prueba visible contra
    el abandono del protector, que los adolescentes solo esquivan en la cara, y los moratones antiguos ya curados empiezan a llegar como sospechas a protección de menores y violencia de género, con detecciones reales y falsos positivos. A la vez, las lámparas UV usadas en casa abren un riesgo de lesión con síntomas retardados que la sociedad oftalmológica intenta atribuir de antemano a la lámpara, mientras titulares y agitador mezclan esos heridos con el fenómeno.'
  hechos_establecidos:
  - id: h3-01
    texto: 'Amanece en la costa este de Estados Unidos (en Nueva York el sol sale hacia las 6:40 a mediados de noviembre, según sunrise-sunset.org) y los magacines matinales de las grandes cadenas abren con corresponsales en exteriores contando en directo la primera luz, un formato que une amanecer y aparición y refuerza la lectura de una ola que llega franja a franja. Con el sol en el horizonte llega muy poco ultravioleta, así que los primeros testimonios hablan de un velo débil frente a los relatos europeos de mediodía, y eso alimenta la versión de que a ellos les llega más flojo o les han hecho otra cosa, hasta que el sol sube. La Casa Blanca no hace declaración propia y deja hablar a las agencias sanitarias con un mensaje de mínimos; varios gobernadores salen antes con mensajes contradictorios. El agitador no rectifica: activa la mitad de su marco preparada para este caso, retransmite amaneceres enviados por seguidores ciudad a ciudad como prueba de un despliegue escalonado y llega antes
      que los medios locales a la audiencia hispanohablante, sobre todo en México y Centroamérica, donde aún es de noche.'
    origen:
    - medios/h3/1
    - disruptor/h3/4
    - agitador/h3/1
    - politico/h3/5
  - id: h3-02
    texto: 'Sanidad amplía su mensaje sin convocar otro Interterritorial: publica una nota conjunta con la sociedad oftalmológica y la de dermatología que remite a la guía oftalmológica, recomienda gafas de sol con marcado CE y mantiene el protector solar aunque se vea oscuro, sin decir cuánto dura el fenómeno. La nota incorpora la explicación física que propone la sociedad oftalmológica: crema, maquillaje con filtro y lentes UV400 se ven oscuros porque absorben el ultravioleta, es decir, porque protegen. La comunidad de la oposición que se había desmarcado acusa al Ministerio de llegar tarde y copiarla, y otras comunidades de su color se suman a la crítica en lugar de a una recomendación propia.'
    origen:
    - politico/h3/1
    - oftalmologa/h3/3
  - id: h3-03
    texto: 'Con el sol cerca del mediodía en Europa, la gente empieza a ver en la cara de otros el daño solar acumulado que antes era invisible (pecas subsuperficiales, léntigos, manchas de sol), intenso en mayores y en quien trabaja al aire libre, como ya mostraba la fotografía ultravioleta. Como los jóvenes son quienes mejor perciben el canal nuevo, son hijos y nietos los que ven a sus mayores llenos de manchas. Los dermatólogos lo convierten en su mejor argumento contra el abandono del protector y surge una corriente contraria al rechazo, con farmacias y consultas recibiendo a gente asustada por manchas antiguas. El rechazo se parte pero no desaparece: la explicación corrige el miedo antes que la vergüenza, y muchas adolescentes obedecen en casa y se quitan la crema de la cara con toallitas en el portal, aplicándola solo en brazos y nuca y llevando gorra, de modo que la cara se queda sin protección justo con más sol.'
    origen:
    - disruptor/h3/1
    - adolescente/h3/3
    - oftalmologa/h3/3
  - id: h3-04
    texto: Docentes, pediatras, sanitarios de urgencias y compañeros de trabajo empiezan a ver en la piel de otras personas moratones antiguos ya curados a simple vista, como los que revela la fotografía ultravioleta forense meses después de la lesión. Llegan las primeras consultas a servicios de protección de menores y a líneas de violencia de género, mezcladas con falsos positivos por manchas de nacimiento, lunares o pigmentación normal y con familias señaladas sin motivo, porque los profesionales obligados a comunicar sospechas ven algo nuevo sin ningún criterio para interpretarlo. Quien tapaba un golpe con maquillaje queda más expuesto, porque la base con filtro se ve oscura justo encima de la zona oculta.
    origen:
    - disruptor/h3/2
  - id: h3-05
    texto: 'La discusión sobre quién paga las horas no trabajadas al aire libre se concreta en una pugna sobre el aviso oficial. Tras la DANA, el Estatuto de los Trabajadores prevé un permiso retribuido cuando una autoridad limita la movilidad o hay riesgo grave por un fenómeno adverso, garantizado al menos los cuatro primeros días y sin ERTE por fuerza mayor hasta pasados esos días (arts. 37.3 g y 47.6 ET), así que los sindicatos quieren un aviso y las patronales prefieren protocolos voluntarios. Los sindicatos piden a la AEMET un aviso que active la adaptación de jornada, pero la radiación ultravioleta no figura entre los fenómenos de Meteoalerta y no puede emitirlo. El Ministerio de Trabajo no dicta parada: recuerda vía Inspección que las empresas deben evaluar el riesgo de deslumbramiento y que, ante riesgo grave e inminente, el trabajador puede interrumpir la actividad (art. 21 de la Ley de Prevención de Riesgos Laborales), y convoca a sindicatos y patronales; unos lo leen como puerta
      para parar obras y reparto, otros como coste trasladado sin norma. Entretanto el índice UV, único dato oficial sobre ultravioleta, se consulta al revés en redes, como pronóstico de dónde y cuándo se verán mejor los colores.'
    origen:
    - economista/h3/1
    - disruptor/h3/3
    - politico/h3/2
  - id: h3-06
    texto: 'Antes de que hable ningún banco central, los medios publican piezas de servicio sobre cómo distinguir un billete auténtico con los ojos nuevos, basadas en la guía pública del BCE (el papel auténtico no brilla y las fibras aparecen en rojo, azul y verde bajo luz UV); son de lo más compartido de la hora y reducen rechazos donde llegan, pero convierten a cualquier cajero en verificador sin formación, con discusiones por billetes gastados o lavados, y la guía describe lo que se ve con lámpara, no con la percepción humana del UV-A solar. Después el Banco de España, coordinado con el BCE, emite una nota breve: todos los billetes siguen siendo de curso legal y lo que se ve son elementos de seguridad que ya existían. El Gobierno la reenvía como mensaje de normalidad, pero parte del pequeño comercio y la hostelería empieza a pedir pago con tarjeta para evitar la duda.'
    origen:
    - medios/h3/3
    - politico/h3/3
    - economista/h3/2
  - id: h3-07
    texto: 'Con las lámparas agotadas en tiendas, adolescentes y familias sacan las lámparas de uñas y las linternas de luz negra que ya tenían en casa para ver los colores en interiores, y entre los jóvenes circulan juegos de alumbrarse la cara, los dientes o los ojos, donde aguantar más da estatus. La sociedad oftalmológica añade a su guía un aviso anticipado: quien se haya iluminado los ojos con lámparas germicidas, de bronceado o mal etiquetadas puede notar horas después dolor intenso, lagrimeo, ojo rojo y sensación de arena, y eso sí es una lesión, fotoqueratitis, que debe ir a urgencias (los síntomas suelen aparecer entre 30 minutos y 12 horas después, según la Academia Americana de Oftalmología). Lo hace para atribuir de antemano a la lámpara, y no al fenómeno, los casos que llegarán por la tarde y la noche.'
    origen:
    - adolescente/h3/1
    - oftalmologa/h3/1
  - id: h3-08
    texto: 'Los pocos casos de lesión real por mirar al sol o por lámparas UV pasan a abrir titulares como los primeros heridos del fenómeno, por encima de la ola mucho mayor de deslumbramiento sin lesión, y el rótulo corto pierde la distinción entre molestia y daño evitable, aunque da a los medios un consejo concreto con fuente que repetir: no mirar al sol ni a lámparas UV. El agitador se cubre diciendo en directo que no hay que mirar al sol, pero presenta a esos pacientes como víctimas del fenómeno y no de la exposición, los suma a sus seguidores que dicen haber perdido vista y borra así la frontera que la sociedad oftalmológica intenta trazar.'
    origen:
    - medios/h3/2
    - agitador/h3/4
  - id: h3-09
    texto: 'La disparidad por edad reordena la autoridad sobre el fenómeno. En casas y aulas los niños y adolescentes pasan a ser quienes explican cómo es, en vídeos de hijos describiendo a padres y abuelos lo que ven, y como ningún adulto puede comprobarlo, algunos exageran o inventan colores, mezclando lo verdadero con lo inventado. El agitador adopta la exclusión de los mayores como segundo tema estrella después del protector: plantea en forma de preguntas por qué a los operados de cataratas les pusieron una lente que bloquea el ultravioleta y quién decidió que no vieran, dando la vuelta a un diseño protector, y parte de su audiencia, sobre todo hijos de mayores, llama a clínicas preguntando por el recambio de lente justo cuando la sociedad oftalmológica lo desaconseja.'
    origen:
    - adolescente/h3/2
    - agitador/h3/2
  - id: h3-10
    texto: 'La oposición lleva el choque al Congreso: registra una solicitud de comparecencia urgente del presidente en el Pleno y pide alterar el orden del día de esta semana. El Gobierno ofrece la comparecencia de la ministra de Sanidad en comisión y la del presidente más adelante, cuando haya información técnica, y sus socios parlamentarios aceptan esa fórmula, que en la Junta de Portavoces le permite ganar días.'
    origen:
    - politico/h3/4
  tensiones_abiertas:
  - Si los casos de fotoqueratitis y de mancha central que lleguen por la tarde y la noche se leen como daño de las lámparas o como daño retardado del propio fenómeno, sobre todo si coinciden con el directo largo del agitador.
  - Si al subir el sol en Norteamérica la experiencia se iguala y el rumor de que a ellos les llega distinto muere, cuándo habla la Casa Blanca y cómo amanecen México y Centroamérica con el marco del agitador ya instalado.
  - Si algún organismo publica criterios para que docentes y sanitarios distingan moratones antiguos de pigmentación normal antes de que las notificaciones y los falsos positivos saturen protección de menores y las líneas de violencia de género.
  - Si la mesa de diálogo social o una instrucción de Trabajo resuelve quién paga las horas no trabajadas, o si se pide reformar el sistema de avisos para incluir el ultravioleta.
  - Si alguna clínica privada anuncia valoraciones o recambio de lente intraocular para ganar visión UV y si los colegios de médicos actúan sobre esa publicidad.
  - Si la preferencia por tarjeta en comercios se extiende tras la nota del Banco de España y el BCE o se frena.
  - Si el abandono del protector pesa en el hemisferio sur, donde coincide con primavera avanzada y pico de compra, y si las marcas de cosmética solar empiezan a cotizar ese riesgo.
  - Si la comparecencia de la ministra en comisión desactiva la presión parlamentaria o la oposición logra alterar el orden del día del Pleno.
  - Si algún gobierno atribuye el fenómeno a una acción hostil y obliga a otras cancillerías a responder.
  contradicciones_resueltas:
  - entre:
    - politico/h3/1
    - oftalmologa/h3/3
    - agitador/h3/3
    decision: Prevalece que Sanidad publica una nota conjunta con oftalmólogos y dermatólogos que incluye gafas con marcado CE y protector solar; el argumento del agitador de que no hay pauta única ni nada oficial sobre el protector queda superado en esta hora, y su explotación del desacuerdo se reduce a la crítica de las comunidades de la oposición.
    motivo: 'El mecanismo del político es más sólido y lo respalda la propuesta de mensaje conjunto de la sociedad oftalmológica: con dos sociedades científicas por escrito el Ministerio puede avanzar sin rectificar. La afirmación del agitador parte de un hueco (Sanidad callada sobre el protector) que la nota cierra.'
  - entre:
    - medios/h3/1
    - disruptor/h3/4
    - politico/h3/5
    decision: 'Se mantienen juntas: el amanecer en directo confirma que el fenómeno llega a Estados Unidos y refuerza la lectura de la ola, pero la primera luz da la experiencia más débil y alimenta la versión de que allí llega distinto, en ausencia de voz federal.'
    motivo: 'No se excluyen: medios describe el formato de la cobertura y disruptor aporta un mecanismo físico sólido sobre la poca radiación UV con el sol en el horizonte; ambos efectos favorecen el marco del agitador, que no depende de que el rumor sea cierto.'
  - entre:
    - medios/h3/3
    - politico/h3/3
    - economista/h3/2
    decision: 'Se ordenan en secuencia: primero las piezas de servicio de los medios basadas en la guía pública del BCE, después la nota del Banco de España coordinada con el BCE, y en paralelo comercios que empiezan a pedir tarjeta.'
    motivo: Los medios llenan con fuente citable el hueco mientras los bancos centrales deciden qué decir; la nota llega después y no enseña a distinguir billetes en caja, lo que explica que la preferencia por tarjeta no se frene.
  - entre:
    - oftalmologa/h3/1
    - medios/h3/2
    - agitador/h3/4
    decision: 'Se mantienen las tres y la atribución de los casos de lesión queda como tensión abierta: la sociedad se anticipa atribuyendo la fotoqueratitis a las lámparas, mientras titulares y agitador mezclan heridos con el fenómeno.'
    motivo: Describen actores con incentivos distintos que actúan a la vez; no se puede decidir en esta hora qué lectura prevalece porque los casos con síntomas retardados aún no han llegado.
  descartadas:
  - id: economista/h3/3
    motivo: Lectura de analistas basada en inferencia y sin dato; su contenido sobre el hemisferio sur queda como tensión abierta y supera el límite de hechos.
  - id: economista/h3/4
    motivo: Amplía h2-10 y repite el patrón de h2-07 en otro producto sin consecuencia nueva suficiente; supera el límite de hechos.
  - id: economista/h3/5
    motivo: Repite en Estados Unidos la dispersión por calidad ya establecida en h2-07 y la quietud de los futuros de h2-01 sin consecuencia nueva.
  - id: politico/h3/5
    motivo: Recogida dentro de h3-01, combinada con medios/h3/1, disruptor/h3/4 y agitador/h3/1.
  - id: medios/h3/4
    motivo: Parte de seguidores grabando en urgencias, premisa que procede de agitador/h2/5, descartada en el tramo anterior y ausente del canon.
  - id: medios/h3/5
    motivo: Confianza baja, especulación y sin dato; la cuestión de las clínicas privadas sigue como tensión abierta.
  - id: oftalmologa/h3/2
    motivo: Efecto de detalle por nubosidad y nieve que amplía h2-07 y la guía oftalmológica sin cambiar el rumbo del mundo; supera el límite de hechos.
  - id: oftalmologa/h3/4
    motivo: Recomendación específica para niños que concreta la guía ya establecida (h2-03) y la disparidad por edad (h2-08) sin consecuencia nueva suficiente; supera el límite de hechos.
  - id: oftalmologa/h3/5
    motivo: Confianza baja, especulación y sin dato; las clínicas privadas quedan como tensión abierta.
  - id: adolescente/h3/4
    motivo: Especulación sin dato sobre la difusión fragmentada del directo de la tarde, que aún no ha ocurrido.
  - id: adolescente/h3/5
    motivo: Confianza baja, especulación y sin dato; efecto local de centros educativos.
  - id: agitador/h3/3
    motivo: Su premisa, que Sanidad no ha dicho nada sobre el protector ni hay pauta común, queda superada por la nota conjunta de h3-02.
  - id: agitador/h3/5
    motivo: Repite y amplía h2-04 (escaparate moderado en la plataforma grande y migración a canales propios) sin consecuencia nueva.
  - id: disruptor/h3/5
    motivo: Confianza baja, especulación y sin dato; el riesgo de lesión por lámparas de bronceado ya entra a través de h3-07.

Tu evaluación del tramo anterior, como referencia:
evaluacion:
  tramo: h2
  metricas:
    - id: alarma_social
      valor: 3
      justificacion: "Los cambios de conducta visibles se multiplican y diversifican en parte de la población: compra masiva de linternas y lámparas UV, abandono del protector solar y de las gafas con filtro entre jóvenes, escasez y reventa de gafas, rechazo de billetes y llamadas a bancos centrales y primeros casos de lesión real en urgencias. No llega a 4 porque no hay servicios colapsados, acaparamiento de bienes esenciales ni protestas en varios países, y el rumor geográfico se reformula sin generar miedo."
      apoyos: [h2-06, h2-07, h2-09, h2-10]
    - id: confianza_institucional
      valor: 3
      justificacion: "Ya existe una versión oficial concreta (mensaje mínimo de Sanidad, Comité de Situación, recomendaciones de la DGT, guía práctica de la sociedad oftalmológica) que las plataformas y verificadores usan como referencia, así que deja de ser un vacío. Pero convive con una sospecha amplia: una comunidad se desmarca, el agitador capitaliza la moderación como censura, los jóvenes rechazan la protección y los desmentidos llegan a mucha menos gente que los bulos. No es 4 porque no hay evidencia de que la mayoría siga las indicaciones oficiales, que además callan sobre gafas."
      apoyos: [h2-02, h2-03, h2-04, h2-05, h2-06]
    - id: relatos_en_competencia
      valor: 3
      justificacion: "El relato técnico y oficial convive con el del agitador, que tiene canales propios, audiencia que migra y se amplía a la América hispanohablante, y un marco inmune a los hechos; además circulan imágenes reales de archivo y fotos UV en falso color que alimentan versiones incompatibles. No es 4 porque los medios generalistas no recogen ambos relatos como equivalentes: rotulan el archivo, citan los testimonios del sur contra el rumor geográfico y se apoyan en los oftalmólogos; el choque de pruebas se da sobre todo en redes."
      apoyos: [h2-01, h2-04, h2-05, h2-06]
    - id: respuesta_gobiernos
      valor: comunicacion
      justificacion: "Los gobiernos pasan a coordinar (Sistema de Seguridad Nacional, Interterritorial, Comité de Seguridad Sanitaria europeo) pero solo emiten mensajes y recomendaciones, incluida la de la DGT; no hay orden sobre trabajo al aire libre ni estado de alarma o emergencia. Para llegar a medidas sectoriales faltaría una decisión obligatoria, por ejemplo activar el protocolo de trabajo al aire libre o restricciones de tráfico."
      apoyos: [h2-02]
    - id: impacto_economico
      valor: 3
      justificacion: "Hay disrupción en varios sectores a la vez: trabajo al aire libre parado según cada empresa con conflicto sobre las horas, mercado de gafas desordenado con escasez en línea y reventa sin garantía, compras masivas de lámparas UV y fricción en el pago con efectivo en la zona euro. Sigue en el límite inferior porque los índices, incluidos los futuros estadounidenses, están estables; no es 4 porque no hay crisis de mercado ni intervención de bancos centrales o gobiernos."
      apoyos: [h2-01, h2-02, h2-07, h2-09, h2-10]
    - id: adaptacion
      valor: 3
      justificacion: "Ya hay pautas claras con respaldo técnico (guía oftalmológica, mensaje de Sanidad, recomendaciones de la DGT) y parte de la población las aplica y las refina, pasando a gafas con filtro certificado, monturas envolventes y gorras. Está en el límite inferior porque otra parte, sobre todo jóvenes y seguidores del agitador, rechaza la protección y algunos se exponen con lámparas o mirando al sol; para llegar a 4 haría falta que la mayoría hubiera ajustado su rutina, lo que no ocurre en América, que aún no ha amanecido en su mayor parte."
      apoyos: [h2-02, h2-03, h2-06, h2-07, h2-10]

## Métricas y niveles

### alarma_social: Nivel de alarma social (escala)
- 1: Curiosidad; la vida sigue igual
- 2: Inquietud; conversación y búsquedas, sin cambios de conducta
- 3: Preocupación; cambios de conducta visibles en parte de la población (compras, quedarse en casa)
- 4: Miedo extendido; acaparamiento, servicios colapsados o protestas en varios países
- 5: Pánico; desórdenes, violencia o huidas masivas

### confianza_institucional: Confianza en la explicación y las indicaciones oficiales (escala)
- 1: La mayoría desconfía abiertamente; las versiones alternativas dominan
- 2: La versión oficial es minoritaria fuera de los medios tradicionales
- 3: Dividida: la versión oficial convive con una sospecha amplia
- 4: La mayoría sigue las indicaciones oficiales, con reservas
- 5: Confianza alta; las instituciones marcan el relato

### relatos_en_competencia: Grado de enfrentamiento entre relatos sobre lo que está pasando (escala)
- 1: Un relato dominante, compartido por instituciones, medios y público
- 2: Relato dominante; versiones alternativas marginales, sin canales ni audiencia propios
- 3: El relato oficial y uno alternativo conviven; el alternativo tiene audiencia y canales propios
- 4: Relatos enfrentados con cifras o pruebas incompatibles; los medios generalistas recogen los dos
- 5: Fractura: grupos amplios viven en relatos incompatibles y desconfían de cualquier fuente del otro

### respuesta_gobiernos: Respuesta dominante de los gobiernos (categorica)
- ninguna: Silencio oficial
- comunicacion: Mensajes y recomendaciones, sin medidas
- medidas_sectoriales: Medidas concretas en sectores (transporte, colegios, trabajo) sin estado excepcional
- emergencia: Declaración formal de emergencia o alerta nacional
- medidas_excepcionales: Restricción de derechos: confinamientos, toques de queda o censura

### impacto_economico: Impacto económico agregado (escala)
- 1: Sin efecto apreciable
- 2: Movimientos sectoriales; índices estables
- 3: Caídas generales de índices o disrupción en varios sectores
- 4: Crisis de mercado; intervención de bancos centrales o gobiernos
- 5: Parálisis económica

### adaptacion: Grado de normalización del cambio (escala)
- 1: Nadie sabe qué hacer
- 2: Primeras pautas, poco seguidas
- 3: Pautas claras y adoptadas por parte de la población
- 4: La mayoría ha ajustado su rutina
- 5: Normalizado

## Tu tarea
1. Para cada métrica, elige el nivel cuya descripción se ajusta mejor a los hechos establecidos, no a las tensiones ni a lo que podría pasar.
2. Si el mundo está entre dos niveles, elige el más cercano según los hechos, no el inferior ni el superior por prudencia, y di en la justificación qué falta para alcanzar el siguiente.
3. Justifica cada valor en una o dos frases: por qué este nivel y no el contiguo. Cita en apoyos los ids de los hechos que lo sostienen.
4. Mide el mundo en su conjunto. Si hay diferencias claras entre regiones, dilo en la justificación.

## Formato de respuesta
Solo este YAML (comillas dobles en los textos):

evaluacion:
  tramo: h3
  metricas:
    - id: alarma_social
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: confianza_institucional
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: relatos_en_competencia
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: respuesta_gobiernos
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: impacto_economico
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
    - id: adaptacion
      valor: ...
      justificacion: "..."
      apoyos: [ids de hechos]
