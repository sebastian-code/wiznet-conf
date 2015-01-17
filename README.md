# WIZ1x0SR Series Configuration Tool

Desde hace un tiempo, y por razones de negocios, y algo de gusto personal, uso la tarjeta conversora de protocolo Serial-Ethernet WIZ110SR de WIZNET, un equipo bastante interesante, y con potencial para muchas cosas, pero que en este instante solo me sirve para el proyecto que estoy adelantando y que es la razon por la cual llegue a este hardware.

WIZNET pone a disposicion del publico una herramienta de configuracion, la cual esta diseñada para correr unicamente en Windows. Como soy usario Linux, obviamente he pasado todos los problemas del mundo tratando de configurar estos equipos, mas cuando debo hacerlo en los lugares donde se hacen las instalaciones, siempre buscando prestado un equipo Windows para poder hacer el trabajo, claro que podria tener uno propio, pero no vale la pena tener un equipo que solo voy a prender una vez cada dos meses.

Buscando, encontre un proyecto en Python, creado por Laurent Coustet, Zehome en GitHub, y quien en el repositorio publico puso a disposicion el script base que permite manejar por terminal, la comunicacion con fines de configuracion mediante conexion ethernet, con cualquier tarjeta WIZnet WIZ1000, WIZ110SR / WIZ1x0SR.

Actualmente el script es compatible con Linux, *BSD y Windows y si quieren mas informacion sobre el script original, pueden encontrarlo en el enlace https://github.com/zehome/wiznetconfigurator.

Haciendo las pruebas con el sistema, realmente la libreria es muy util, pero puede resultar engorrosa de utilizar, sobre todo para usuarios noveles, por lo que considero que avanzar en la construccion de una interfaz grafica puede resultar util, a parte que la implementacion no es del todo mi gusto.

# Mis pretensiones.

La idea es avanzar, a mi ritmo que es muy lento, en construir una interfaz grafica, mejorar la calidad del script para terminar de implementar todas las instrucciones del equipo, aunque usare el script de Zehome como inspiracion, realmente pienso modificarlo mucho para ajustarse un poco mas a mi estilo y, adicionalmente buscare reducir el alcance especificamente a equipos WIZnet WIZ110SR, como una idea complementaria tal vez crear instaladores para facilitar su despliegue en todas las plataformas.

Quizas haya mas posibilidades de crear codigo y compartirlo, eso esta por verse.

# Licenciamiento.

Por ahora soy novel en el tema de licenciamiento, pero tengo la intencion de liberarlo para uso publico, de la misma forma que WIZnet ha liberado el codigo de su herramienta de configuracion. Pero basicamente puede usarse como se les antoje, y el credito por la obra nunca estara de mas.