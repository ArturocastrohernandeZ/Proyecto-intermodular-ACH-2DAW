Pilates Life — Guía de estilo
Web de reservas de clases de pilates. Marca: Pilates Life.

Diseño editable: https://www.figma.com/design/EE83xUkPeH8q9os5aLa51l?node-id=3-2
Dirección visual
Serenidad, claridad y movimiento. Tonos naturales, espacio en blanco y formas suaves. La jerarquía destaca fecha, hora y plazas para reservar con confianza.
01. Tipografía
Uso	Fuente	Tamaño / interlineado	Ejemplo
H1	Lora Regular	40 / 52 px	Encuentra tu equilibrio
H2	Lora Medium	28 / 38 px	Elige tu próxima clase
H3	DM Sans SemiBold	20 / 28 px	Pilates Reformer
Cuerpo	DM Sans Regular	16 / 24 px	Reserva tu plaza y dedica un momento a cuidarte.
Secundario	DM Sans Regular	14 / 20 px	50 minutos · Nivel iniciación
Botones	DM Sans SemiBold	15 / 22 px	Reservar clase


Un H1 por pantalla. Etiquetas siempre visibles y texto alineado a la izquierda. Cuerpo principal mínimo de 16 px.
02. Paleta de colores
Color	HEX	Uso
Verde bosque	#31594D	Acción principal
Verde profundo	#244338	Hover
Salvia suave	#DFE8DE	Fondos suaves
Terracota	#A9573F	Acento editorial
Verde disponible	#2E614A	Disponibilidad y confirmación
Ámbar	#875815	Últimas plazas
Rojo	#A93636	Error y clase completa
Texto principal	#24332E	Lectura principal
Texto secundario	#5F6B63	Ayuda y metadatos
Fondo crema	#F7F5EE	Fondo general
Blanco	#FFFFFF	Tarjetas y texto sobre verde
Borde	#CFD8CF	Contornos de campos y tarjetas
Deshabilitado	#E7EBE5	Fondo de controles bloqueados
Texto deshabilitado	#66726A	Texto de controles bloqueados


Los estados llevan una etiqueta textual; el color nunca es la única señal. Fondos semánticos: disponible #EAF3EB, aviso #FBF0D8 y error #FBECEC.
03. Botones
230 × 52 px, radio 12 px y relleno horizontal 24 px.
Estado	Fondo	Texto
Active / Activo	#31594D	#FFFFFF
Hover	#244338	#FFFFFF
Disabled / Deshabilitado	#E7EBE5	#66726A


Acción principal: «Reservar clase». Confirmación: «Confirmar reserva». Deshabilitar cuando faltan selecciones obligatorias o la clase está completa. Añadir contorno visible de 2 px al recibir foco con teclado. En móvil, ocupar el ancho disponible.
04. Campos de texto
Altura 52 px, radio 12 px y relleno horizontal 16 px. La etiqueta permanece visible.
Estado	Apariencia	Ejemplo
Empty Label / Vacío	Fondo blanco, borde #CFD8CF de 1 px	Nombre completo / Introduce tu nombre
Focus Label / Enfocado	Borde #31594D de 2 px	Nombre completo / María García
Disabled Label / Bloqueado	Fondo #E7EBE5, texto #66726A	Código de reserva / PL-2048


Mostrar la validación junto al campo. Ejemplo de error: «Introduce un correo válido, como nombre@ejemplo.com». No utilizar el placeholder como única etiqueta.
05. Ejemplo de reserva
Datos ilustrativos del diseño:
Hora	Clase	Detalle	Estado
09:00	Pilates suelo	50 min · Iniciación · Laura	Disponible
10:30	Pilates Reformer	50 min · Todos los niveles · Ana	Últimas plazas
18:00	Pilates suave	50 min · Iniciación · Marta	Completa


Selección: miércoles 18 de noviembre de 2026, Pilates Reformer de 10:30 a 11:20, profesora Ana, sala Reformer. Quedan 2 de 8 plazas. Precio ilustrativo: 18 €.

La selección usa un borde verde y un resumen con clase, fecha, hora, profesora, disponibilidad y precio. Una clase completa impide reservar; puede ofrecerse lista de espera. Tras confirmar, mostrar: «Tu plaza está reservada. Te esperamos el miércoles a las 10:30».
Composición y adaptación
- Escala de espaciado: 8, 16, 24, 32, 48 y 64 px.
- Radio de tarjetas: 20 px; portada: 28 px.
- Escritorio: calendario y clases junto al resumen.
- Móvil: una columna, márgenes de 16 px y resumen debajo de las clases.
- Área interactiva mínima: 44 × 44 px.
El archivo de Figma incluye 52 variables, 6 estilos tipográficos y 3 familias de componentes con 9 variantes en total: botón, campo y disponibilidad.