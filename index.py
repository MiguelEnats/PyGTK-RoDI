#-*-encodinf:utf-8-*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
from scripts import notes, sensors, moves, moods

music = notes.music()
action = sensors.sensors()
move = moves.moves()
mood = moods.moods()

#Creamos una lista para utilizarla al momento de saber si sonar la nota o no
play_yes = [0]

class app:
	#Función que se ejecutará si o si al comienzo
	def __init__(self):
		#Creamos la ventana con sus respectivas propiedades
		ventana = Gtk.Window()
		ventana.maximize()
		ventana.set_default_size(640, 480)
		ventana.set_resizable(True)
		ventana.set_title("RoDI")
		ventana.set_icon_from_file("images/logo_rodi_2.jpg")
		ventana.connect("destroy", Gtk.main_quit)

		#Creamos los botones del menú principal
		btn_main_rodi = Gtk.Button("RoDI")
		btn_main_info = Gtk.Button("Acerca de")
		btn_main_actions = Gtk.Button("Acciones")
		btn_main_salir = Gtk.Button("Salir")

		#Conectamos los botones a los métodos correspondientes
		btn_main_rodi.connect("clicked", self.view_rodi, ventana)
		btn_main_info.connect("clicked", self.view_info, ventana)
		btn_main_actions.connect("clicked", self.view_actions, ventana)
		btn_main_salir.connect("clicked", self.message_exit, ventana)

		#Creamos los tooltips para los botones del menú principal
		btn_main_rodi.set_tooltip_text("Historia y versiones de RoDI")
		btn_main_info.set_tooltip_text("Información del programa")
		btn_main_actions.set_tooltip_text("Una lista de acciones posibles con el RoDI")
		btn_main_salir.set_tooltip_text("Clic para salir del programa")

		#Creamos la caja contenedora de los botones principales
		caja_principal = Gtk.VBox()
		caja_p_arriba = Gtk.HBox(homogeneous = True)
		caja_p_abajo = Gtk.HBox(homogeneous = True)

		#Creamos una variable con una imagen para poder mostrarla como título
		image_rodi = Gtk.Image()
		image_rodi.set_from_file("images/title_rodi.png")

		#Empaquetamos todo en la caja para poder mostrar
		caja_principal.pack_start(image_rodi, True, True, 10)
		caja_principal.pack_start(caja_p_arriba, True, True, 25)
		caja_principal.pack_start(caja_p_abajo, True, True, 25)

		#Agregamos en las cajas secundarias los botones
		caja_p_arriba.pack_start(btn_main_rodi, True, True, 75)
		caja_p_arriba.pack_start(btn_main_info, True, True, 75)
		caja_p_abajo.pack_start(btn_main_actions, True, True, 75)
		caja_p_abajo.pack_start(btn_main_salir, True, True, 75)

		#Creamos la caja principal donde estará la caja que se mostrará en la pantalla
		caja_p = Gtk.HBox(homogeneous = True)

		#Empaquetamos la caja
		caja_p.pack_start(caja_principal, True, True, 100)

		#Adherimos la caja principal a la ventana y la mostramos para poder visualizar lo que contiene
		ventana.add(caja_p)
		ventana.show_all()

	#Creamos el cuadro de diálogo que se mostrará al presionar el botón de salir
	def message_exit(self, widget, ventana):
		dialog_exit = Gtk.Dialog()
		dialog_exit.set_title("¡Atención!")
		dialog_exit.set_modal(True)
		dialog_exit.set_transient_for(ventana)
		dialog_exit.set_border_width(5)
		dialog_exit.set_resizable(False)
		
		#Creamos las cajas, los botones y el texto que se mostrará en el cuadro de diálogo
		vbox_main = Gtk.VBox(spacing = 5)
		hbox_option = Gtk.HBox(homogeneous = True, spacing = 5)
		button_yes = Gtk.Button("Si")
		button_cancel = Gtk.Button("Cancelar")
		label_dialog = Gtk.Label("¿Estás seguro que desea salir?")
		
		#Conectamos los botones a los eventos correspondientes
		button_yes.connect("clicked", self.exit)
		button_cancel.connect("clicked", self.close_box, dialog_exit)
		
		#Empaquetamos todo en las cajas y la caja al cuadro
		hbox_option.pack_start(button_yes, True, True, 5)
		hbox_option.pack_start(button_cancel, True, True, 5)
		vbox_main.pack_start(label_dialog, True, True, 5)
		vbox_main.pack_start(hbox_option, True, True, 5)
		box_message = dialog_exit.get_content_area()
		box_message.add(vbox_main)

		#Mostramos el cuadro
		dialog_exit.show_all()

	#Método que se activará si se hace clic en el botón 'Ver RoDI'
	def view_rodi(self, widget, ventana):
		#Creamos la ventana donde se mostrará los elementos
		dialog_rodi = Gtk.Dialog()
		dialog_rodi.set_title("RoDI")
		dialog_rodi.set_border_width(5)
		dialog_rodi.set_transient_for(ventana)
		dialog_rodi.set_modal(True)
		dialog_rodi.set_resizable(False)
		dialog_rodi.set_default_size(640, 480)

		#Creamos el contenedor donde estarán todos los elementos
		notebook_rodi = Gtk.Notebook()
		notebook_rodi.set_scrollable(True)
		
		#Botones que estarán en las páginas para poder pasar uno a otro
		button_next = Gtk.Button("Siguiente")
		button_back = Gtk.Button("Anterior")
		button_close = Gtk.Button("Cerrar")
		
		#Tooltips de los botones
		button_next.set_tooltip_text("Clic para pasar a la siguiente página")
		button_back.set_tooltip_text("Clic para regresar a la página anterior")
		
		#Conectamos los botones a sus respectivas señales
		button_next.connect("clicked", self.next_page, notebook_rodi)
		button_back.connect("clicked", self.back_page, notebook_rodi)
		button_close.connect("clicked", self.close_box, dialog_rodi)
		
		#Creamos todas las páginas que utilizaremos
		page_1_rodi = Gtk.VBox()
		page_2_history = Gtk.VBox()
		page_3_parts = Gtk.VBox()
		page_4_moods = Gtk.VBox()
		
		#Contenedor de los botones
		buttons_page = Gtk.HBox(homogeneous = True, spacing = 5)
		
		#Agregamos los botones a las cajas
		buttons_page.pack_start(button_back, True, True, 10)
		buttons_page.pack_start(button_next, True, True, 10)
		buttons_page.pack_start(button_close, True, True, 10)
		
		#Creamos las imágenes para las diferentes páginas
		image_1 = Gtk.Image()
		
		#Ahora le damos la imagen a cada objeto
		image_1.set_from_file("images/img_rodi_0.jpg")

		#Creamos el título y el cuerpo del contenido
		label_1_cite = Gtk.Label()
		label_1_title_1 = Gtk.Label()
		label_1_title_2 = Gtk.Label()
		label_1_body_1 = Gtk.Label()
		label_1_body_2 = Gtk.Label()

		label_1_cite.set_markup("""<i><b>RoDI</b> (Robot Didáctico Inalámbrico) es un robot pequeño, inalámbrico, de bajo costo y
fácil de usar para enseñar a los niños y también adultos</i>\n""")
		label_1_cite.set_justify(Gtk.Justification.CENTER)
		label_1_title_1.set_markup("<span font_family=\"Arial\"><big><b>Construyendo una educación diferente, libre y accesible</b></big></span>")
		label_1_body_1.set_markup("""\n<i>Robot Didáctico Inalámbrico</i> con hardware y software libre, multiplataforma, multilenguaje y
divertido para la construcción del pensamiento computacional y lateral para niños, niñas,
jóvenes y adultos.""")
		label_1_body_1.set_justify(Gtk.Justification.CENTER)		
		label_1_title_2.set_markup("\n<span font_family=\'Arial\'><b><big>Fácil de usar, Divertido de aprender</big></b></span>\n")
		label_1_body_2.set_markup("""RoDI es ideal para que todos aprendan, de forma práctica y entretenida, a resolver
problemas mediante el pensamiento computacional. Cuenta con el respaldo de una
<i>plataforma web como Turtle Blocks</i>\n""")
		label_1_body_2.set_justify(Gtk.Justification.CENTER)
		labels_1 = (label_1_cite, label_1_title_1, label_1_body_1, label_1_title_2, label_1_body_2)

		#Para la segunda página
		label_2_title = Gtk.Label()
		label_2_body = Gtk.Label()

		label_2_title.set_markup("<span font_family=\'Arial\'><b><big>Pequeña Historia</big></b></span>")
		label_2_body.set_markup("""<b>RoDI</b> nace con el deseo de acercar aún más la tecnología hacia los niños o personas de
escasos recuros, tiene el deseo de facilitar el aprendizaje básico de robótica,
programación y sobre todo desarrollar el pensamiento lógico de la persona que lo utilice,
no hay barreras para el RoDI, y no solo es para los niños, también puede ayudar a los jóvenes,
y también a las personas adultas, es una herramienta para el aprendizaje interactivo, es decir,
mientras más juegas con el robot más aprenderás sobre él... es como una
<b>puerta hacia el aprendizaje</b> y lo mejor de este pequeño robot es que
es libre, es decir, el software (programa) y el hardware (el robot en sí) están disponibles
para todo público, lo puede utilizar, estudiar y si lo desea, 
también lo puede mejorar.
\nY como lo dijo un gran pensador: \n<i><b>El cambio está a tu alcance, es tu decisión tomarlo.</b></i>""")
		label_2_body.set_justify(Gtk.Justification.CENTER)

		labels_2 = (label_2_title, label_2_body)

		#Para la página número 3
		label_3_title = Gtk.Label()
		label_3_body = Gtk.Label()

		label_3_title.set_markup("<span font_family=\'Arial\'><big><b>RoDI Actual</b></big></span>")

		label_3_body.set_markup("""<i>Imagen actual del RoDI</i>
En esta versión el robot tiene un <b>buzzer</b> que es capaz de reproducir notas musicales,
Tiene un <b>sensor de ultrasonido</b> capaz de medir la distancia de un objeto
que tiene al frente, un <b>LED RGB</b> que es capaz de emitir todos los colores posibles,
un <b>led</b> normal capaz de prender y apagarse, un <b>sensor lumimico</b> que
mide la intensidad de la luz que hay en el ambiente, dos <b>sensores seguidor de línea</b>
que se puede utilizar para convertirlo en un seguidor de línea (están abajo),
también dos <b>motores servos</b> que se utilizan para hacer girar las ruedas del robot
Y para establecer conexión con el RoDI está el <b>módulo wifi</b> que se utiliza
para pasarle las instrucciones que realizará el robot, también se podría hacer
que se volviera "<b>autónomo</b>", es decir, que se maneje solo esquivando
cualquier obstáculo
""")
		label_3_body.set_justify(Gtk.Justification.CENTER)

		labels_3 = (label_3_title, image_1, label_3_body)

		#Página número 4
		label_4_title = Gtk.Label()
		label_4_mod1 = Gtk.Label()
		label_4_mod2 = Gtk.Label()

		label_4_title.set_markup("<span font_family=\'Arial\'><big><b>Modos</b></big></span>")
		label_4_mod1.set_markup("""<span font_family='Arial'><b>Seguidor de Línea</b></span>
El <b>modo seguidor</b> es para poder activar el modo de competencia de Seguidores de línea,
es decir, se debe crear una pista blanca con líneas de color negras
para poder utilizar este modo de forma correcta. Lo que hace en este modo es
seguir la línea de color negra hasta que gire el número de curvas ingresadas,
solo se puede salir de este modo al cumplirse los giros necesarios.\n
Este modo lo puede encontrar en la parte de "Acciones/Modos"
""")
		label_4_mod2.set_markup("""<span font_family='Arial'><b>Sumo</b></span>
El <b>modo sumo</b> es para poder utilizar el rodi de forma de un luchador, eso no quiere
decir que el RoDI posea armamentos ni nada por el estilo. El sumo hace referencia
a las competencias de mini sumo, donde los robots deben sacarse uno al otro de un
pequeño ring (dojo), la competencia es 1 vs 1, aunque aveces se realiza un
'Battle Royale' o todos vs todos. Para poder utilizar de forma correcta este modo debe
leer las especificaciones del dojo para las batallas de sumo robot, pero <b>NO es recomendable
activar este modo</b> ya que haciendolo podría dañar el robot y eso es perjudicial
para usted o para su contrincante... Si lo activa es bajo su propia responsabilidad...
Para poder desactivar este modo debe reiniciar el robot ya que no hay quien
lo pare al estar en este modo.\n
Este modo NO está disponible, pero lo puede encontrar en el script moods
""")
		labels_4 = (label_4_title, label_4_mod1, label_4_mod2)

		#Empaquetamos todo en las cajas
		for i in range(len(labels_1)):
			self.pack_elements(page_1_rodi, labels_1[i], 2)

		for i in range(len(labels_2)):
			self.pack_elements(page_2_history, labels_2[i], 2)

		for i in range(len(labels_3)):
			self.pack_elements(page_3_parts, labels_3[i], 2)

		for i in range(len(labels_4)):
			labels_4[i].set_justify(Gtk.Justification.CENTER)
			self.pack_elements(page_4_moods, labels_4[i], 2)

		#Ahora colocamos todas las páginas al cuadro
		notebook_rodi.append_page(page_1_rodi, Gtk.Label("RoDI"))
		notebook_rodi.append_page(page_2_history, Gtk.Label("Futuro"))
		notebook_rodi.append_page(page_3_parts, Gtk.Label("Partes"))
		notebook_rodi.append_page(page_4_moods, Gtk.Label("Modos"))

		#Agregamos el contenedor al cuadro de diálogo y creamos otra caja vertical para contener todas las opciones e información
		vbox_main = Gtk.VBox(spacing = 5)
		vbox_main.pack_start(notebook_rodi, True, True, 5)
		vbox_main.pack_start(buttons_page, True, True, 10)
		box_rodi = dialog_rodi.get_content_area()
		box_rodi.add(vbox_main)
		
		#Mostramos el cuadro
		dialog_rodi.show_all()

	#Método que se activará si se hace clic en el botón 'Acerca de'
	def view_info(self, widget, ventana):
		dialog_about = Gtk.AboutDialog()
		dialog_about.set_modal(True)
		dialog_about.set_transient_for(ventana)

		#Ponemos una imagen para el logo del cuadro de diálogo
		image_logo = Pixbuf.new_from_file("images/logo_rodi.png")
		dialog_about.set_logo(image_logo)
		
		#Rellenamos los espacios de la parte de créditos
		dialog_about.set_artists(["Miguel Benítez"])
		dialog_about.set_authors(["Miguel Benítez"])
		list_person = ["Equipo RoDI","Gary Servín", "Martín Abente", "Mauro Gavilán", "Patricia Escauriza", "Manuel Kaufmann - RoDI-Py"]
		dialog_about.add_credit_section("Créditos", list_person)
		dialog_about.set_documenters(["Miguel Benítez"])
		dialog_about.set_program_name("RoDI")
		dialog_about.set_comments("Programa realizado con la finalidad de utilizar todas las funciones del RoDI")
		dialog_about.set_version("1.0")
		dialog_about.set_website_label("Página Oficial de RoDI")
		dialog_about.set_website("http://www.rodibot.com")

		#Mostramos el cuadro de información
		dialog_about.show()
	
	#Método para ver las opciones disponibles con el RoDI
	def view_actions(self, widget, ventana):
		dialog_action = Gtk.Dialog()
		dialog_action.set_title("Elige una acción")
		dialog_action.set_border_width(5)
		dialog_action.set_modal(True)
		dialog_action.set_transient_for(ventana)
		dialog_action.set_resizable(False)

		vbox_buttons = Gtk.VBox(homogeneous = True, spacing = 5)
		hbox_1 = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_2 = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_3 = Gtk.HBox(homogeneous = True, spacing = 2)

		button_sounds = Gtk.Button("Sonidos/Canciones")
		button_sensors = Gtk.Button("Sensores y LEDS")
		button_moves = Gtk.Button("Movimientos Básicos")
		button_moods = Gtk.Button("Modos")
		button_close = Gtk.Button("Cerrar")

		button_sounds.connect("clicked", self.view_songs, dialog_action)
		button_sensors.connect("clicked", self.view_sensors_leds, dialog_action)
		button_moves.connect("clicked", self.view_moves, dialog_action, ventana)
		button_moods.connect("clicked", self.view_moods, dialog_action)
		button_close.connect("clicked", self.close_box, dialog_action)

		hbox_1.pack_start(button_sounds, True, True, 5)
		hbox_1.pack_start(button_sensors, True, True, 5)
		hbox_2.pack_start(button_moves, True, True, 5)
		hbox_2.pack_start(button_moods, True, True, 5)
		hbox_3.pack_start(button_close, True, True, 5)
		cajas = (hbox_1, hbox_2, hbox_3)

		for i in range(len(cajas)):
			self.pack_elements(vbox_buttons, cajas[i], 5)

		#Mostramos el cuadro y esperamos a que realice una acción
		box_action = dialog_action.get_content_area()
		box_action.add(vbox_buttons)

		dialog_action.show_all()
		
	#Empieza las funciones para las canciones

	#Método que se activará si se hace clic en el botón 'Sonidos/Canciones'
	def view_songs(self, widget, ventana):
		dialog_song = Gtk.Dialog()
		dialog_song.set_title("Elige una acción")
		dialog_song.set_border_width(5)
		dialog_song.set_modal(True)
		dialog_song.set_transient_for(ventana)
		dialog_song.set_resizable(False)
		dialog_song.add_buttons("Reproducir canciones", 0, "Crear canciones", 1, "Cerrar", 2)

		#Mostramos el cuadro y esperamos a que realice una acción y la agarramos en la variable response_song
		response_song = dialog_song.run()
		if response_song == 0:
			dialog_song.destroy()
			self.play_songs(ventana)
		elif response_song == 1:
			dialog_song.destroy()
			self.create_song(ventana)
		else:
			self.close_box(dialog_song, dialog_song)

	#Método para seleccionar los sonidos creados
	def play_songs(self, ventana):
		dialog_play = Gtk.FileChooserDialog("Elige una canción", ventana, Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))
		
		#Le pasamos la ruta de donde buscará las canciones
		dialog_play.set_current_folder("../Rodi-PyGtk/songs")

		#Mostramos el cuadro de selección
		response_play = dialog_play.run()
		
		#Esperamos la respuesta o acción del usuario para saber qué hacer
		if response_play == Gtk.ResponseType.CANCEL:
			#Acción para cerrar el cuadro
			self.close_box(response_play, dialog_play)
		else:
			#Acción para abrir el archivo
			name_archivo = dialog_play.get_filename()
			self.close_box(response_play, dialog_play)
			self.select_play(response_play, ventana, name_archivo)

	#Métódo para mostrar un cuadro de diálogo para elegir si reproducir o no la canción seleccionada
	def select_play(self, widget, parent, archive):
		#Lo único que se hace acá es agarrar el nombre del archivo y ponerle como título al cuadro
		longitud = len(archive) - 1
		name = str
		name_file = str
		while longitud >= 0:
			if archive[longitud] == "/":
				name = archive[(longitud+1):]
				break
			longitud -= 1
		longitud = len(name) - 1
		while longitud >= 0:
			if name[longitud] == ".":
				name_file = name[:(longitud)]
				break
			longitud -= 1

		#Acá empezamos a crear el cuadro que se mostrará después de seleccionar una canción
		dialog_playing = Gtk.Dialog()
		dialog_playing.set_title("Canción " + name_file)
		dialog_playing.set_default_size(320, 130)
		dialog_playing.set_resizable(False)
		dialog_playing.set_modal(True)
		dialog_playing.set_transient_for(parent)

		#Ahora crearemos un spinner para que gire mientras suene la canción y dos botones
		label_text = Gtk.Label()
		spinner_play = Gtk.Spinner()
		spinner_play.start()
		button_close = Gtk.Button("Cerrar canción")
		button_play = Gtk.Button("Reproducir")
		button_other = Gtk.Button("Elegir otra canción")
		hbox_buttons = Gtk.HBox(homogeneous = True, spacing = 5)
		vbox_play = Gtk.VBox(spacing = 5)

		#Ahora llamamos a la función para que reproduzca la canción
		state, text_return = music.play_archive(archive, name_file)
		label_text.set_text(text_return)
		#music.play_song() Tengo que descomentar esta línea

		#Función para reproducir de nuevo la canción
		def play_again(self):
			music.play_song()
			music.delete_all()

		def close_song(self):
			music.delete_all()
			dialog_playing.destroy()

		#Ahora conectaremos los botones a las señales correspondientes
		button_close.connect("clicked", close_song)
		button_other.connect("clicked", self.error_archive, parent, dialog_playing)
		if state:
			#Si el archivo es una canción entonces tendrá la opción de reproducir de nuevo o elegir otra
			hbox_buttons.pack_start(button_other, True, True, 5)
			hbox_buttons.pack_start(button_play, True, True, 5)
			button_play.connect("clicked", play_again)
		else:
			#Si el archivo no es una canción, entonces le mostrará un mensaje de error y la opción de elegir otro archivo o salir
			label_text.set_text("Error en el archivo, no se puede reproducir, elija otro archivo")
			hbox_buttons.pack_start(button_other, True, True, 5)

		#Ahora empaquetamos todo en las cajas correspondientes
		hbox_buttons.pack_start(button_close, True, True, 5)
		vbox_play.pack_start(label_text, True, True, 5)
		vbox_play.pack_start(spinner_play, True, True, 5)
		vbox_play.pack_start(hbox_buttons, True, True, 5)
		
		#Agregamos la caja principal al cuadro
		box_play = dialog_playing.get_content_area()
		box_play.add(vbox_play)
		
		#Mostramos el cuadro de diálogo
		dialog_playing.show_all()

	#Función si el archivo no es sonido
	def error_archive(self, widget, parent, dialog):
		self.close_box(widget, dialog)
		self.play_songs(parent)
	
	#Método para crear sonidos
	def create_song(self, ventana):
		#Creamos el contenedor principal
		dialog_create = Gtk.Dialog()
		dialog_create.set_title("Crea tus propias canciones")
		dialog_create.set_resizable(False)
		dialog_create.set_modal(True)
		dialog_create.set_transient_for(ventana)

		#Creamos la caja donde estarán todas las opciones disponibles
		hbox_songs = Gtk.HBox(spacing = 5)
		vbox_notes_1 = Gtk.VBox(homogeneous = True, spacing = 5)
		vbox_notes_2 = Gtk.VBox(homogeneous = True, spacing = 5)
		vbox_notes_3 = Gtk.VBox(spacing = 5)
		vbox_option = Gtk.VBox(homogeneous = True, spacing = 10)

		#Creamos las cajas para las notas musicales
		vbox_0 = Gtk.VBox()
		hbox_0_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_0_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_1 = Gtk.VBox()
		hbox_1_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_1_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_2 = Gtk.VBox()
		hbox_2_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_2_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_3 = Gtk.VBox()
		hbox_3_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_3_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_4 = Gtk.VBox()
		hbox_4_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_4_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_5 = Gtk.VBox()
		hbox_5_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_5_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_6 = Gtk.VBox()
		hbox_6_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_6_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_7 = Gtk.VBox()
		hbox_7_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_7_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_8 = Gtk.VBox()
		hbox_8_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_8_notes_2 = Gtk.HBox(homogeneous = True)
		vbox_9 = Gtk.VBox()
		hbox_9_notes_1 = Gtk.HBox(homogeneous = True)
		hbox_9_notes_2 = Gtk.HBox(homogeneous = True)

		#Ponemos en una tupla las cajas para poder usarlas en los ciclos
		box_box = (vbox_0, vbox_1, vbox_2, vbox_3, vbox_4, vbox_5, vbox_6, vbox_7, vbox_8, vbox_9)
		
		#Lo mismo acá
		box_notes_0 = (hbox_0_notes_1, hbox_1_notes_1, hbox_2_notes_1, hbox_3_notes_1, hbox_4_notes_1, hbox_5_notes_1, hbox_6_notes_1,
			hbox_7_notes_1, hbox_8_notes_1, hbox_9_notes_1)
		
		#Y acá también
		box_notes_1 = (hbox_0_notes_2, hbox_1_notes_2, hbox_2_notes_2, hbox_3_notes_2,  hbox_4_notes_2,  hbox_5_notes_2, hbox_6_notes_2,
			 hbox_7_notes_2, hbox_8_notes_2, hbox_9_notes_2)

		#Creamos los botones para las diferentes notas según su octava
		#Octava 0
		button_note_do_0 = Gtk.Button("Do  0")
		button_note_do_s_0 = Gtk.Button("Do#  0")
		button_note_re_0 = Gtk.Button("Re  0")
		button_note_re_s_0 = Gtk.Button("Re#  0")
		button_note_mi_0 = Gtk.Button("Mi  0")
		button_note_fa_0 = Gtk.Button("Fa  0")
		button_note_fa_s_0 = Gtk.Button("Fa#  0")
		button_note_sol_0 = Gtk.Button("Sol  0")
		button_note_sol_s_0 = Gtk.Button("Sol#  0")
		button_note_la_0 = Gtk.Button("La  0")
		button_note_la_s_0 = Gtk.Button("La#  0")
		button_note_si_0 = Gtk.Button("Si  0")
		
		#Las ponemos en diferentes tuplas
		notes_0_1 = (button_note_do_0, button_note_do_s_0, button_note_re_0, button_note_re_s_0, button_note_mi_0, button_note_fa_0)
		notes_0_2 = (button_note_fa_s_0, button_note_sol_0, button_note_sol_s_0, button_note_la_0, button_note_la_s_0, button_note_si_0)
		
		#Octava 1
		button_note_do_1 = Gtk.Button("Do  1")
		button_note_do_s_1 = Gtk.Button("Do#  1")
		button_note_re_1 = Gtk.Button("Re  1")
		button_note_re_s_1 = Gtk.Button("Re#  1")
		button_note_mi_1 = Gtk.Button("Mi  1")
		button_note_fa_1 = Gtk.Button("Fa  1")
		button_note_fa_s_1 = Gtk.Button("Fa#  1")
		button_note_sol_1 = Gtk.Button("Sol  1")
		button_note_sol_s_1 = Gtk.Button("Sol#  1")
		button_note_la_1 = Gtk.Button("La  1")
		button_note_la_s_1 = Gtk.Button("La#  1")
		button_note_si_1 = Gtk.Button("Si  1")
		
		#Las ponemos en diferentes tuplas
		notes_1_1 = (button_note_do_1, button_note_do_s_1, button_note_re_1, button_note_re_s_1, button_note_mi_1, button_note_fa_1)
		notes_1_2 = (button_note_fa_s_1, button_note_sol_1, button_note_sol_s_1, button_note_la_1, button_note_la_s_1, button_note_si_1)
		
		#Octava 2
		button_note_do_2 = Gtk.Button("Do  2")
		button_note_do_s_2 = Gtk.Button("Do#  2")
		button_note_re_2 = Gtk.Button("Re  2")
		button_note_re_s_2 = Gtk.Button("Re#  2")
		button_note_mi_2 = Gtk.Button("Mi  2")
		button_note_fa_2 = Gtk.Button("Fa  2")
		button_note_fa_s_2 = Gtk.Button("Fa#  2")
		button_note_sol_2 = Gtk.Button("Sol  2")
		button_note_sol_s_2 = Gtk.Button("Sol#  2")
		button_note_la_2 = Gtk.Button("La  2")
		button_note_la_s_2 = Gtk.Button("La#  2")
		button_note_si_2 = Gtk.Button("Si  2")
		
		#Las ponemos en diferentes tuplas
		notes_2_1 = (button_note_do_2, button_note_do_s_2, button_note_re_2, button_note_re_s_2, button_note_mi_2, button_note_fa_2)
		notes_2_2 = (button_note_fa_s_2, button_note_sol_2, button_note_sol_s_2, button_note_la_2, button_note_la_s_2, button_note_si_2)
		
		#Octava 3
		button_note_do_3 = Gtk.Button("Do  3")
		button_note_do_s_3 = Gtk.Button("Do#  3")
		button_note_re_3 = Gtk.Button("Re  3")
		button_note_re_s_3 = Gtk.Button("Re#  3")
		button_note_mi_3 = Gtk.Button("Mi  3")
		button_note_fa_3 = Gtk.Button("Fa  3")
		button_note_fa_s_3 = Gtk.Button("Fa#  3")
		button_note_sol_3 = Gtk.Button("Sol  3")
		button_note_sol_s_3 = Gtk.Button("Sol#  3")
		button_note_la_3 = Gtk.Button("La  3")
		button_note_la_s_3 = Gtk.Button("La#  3")
		button_note_si_3 = Gtk.Button("Si  3")
		
		#Las ponemos en diferentes tuplas
		notes_3_1 = (button_note_do_3, button_note_do_s_3, button_note_re_3, button_note_re_s_3, button_note_mi_3, button_note_fa_3)
		notes_3_2 = (button_note_fa_s_3, button_note_sol_3, button_note_sol_s_3, button_note_la_3, button_note_la_s_3, button_note_si_3)
		
		#Octava 4
		button_note_do_4 = Gtk.Button("Do  4")
		button_note_do_s_4 = Gtk.Button("Do#  4")
		button_note_re_4 = Gtk.Button("Re  4")
		button_note_re_s_4 = Gtk.Button("Re#  4")
		button_note_mi_4 = Gtk.Button("Mi  4")
		button_note_fa_4 = Gtk.Button("Fa  4")
		button_note_fa_s_4 = Gtk.Button("Fa#  4")
		button_note_sol_4 = Gtk.Button("Sol  4")
		button_note_sol_s_4 = Gtk.Button("Sol#  4")
		button_note_la_4 = Gtk.Button("La  4")
		button_note_la_s_4 = Gtk.Button("La#  4")
		button_note_si_4 = Gtk.Button("Si  4")
		
		#Las ponemos en diferentes tuplas
		notes_4_1 = (button_note_do_4, button_note_do_s_4, button_note_re_4, button_note_re_s_4, button_note_mi_4, button_note_fa_4)
		notes_4_2 = (button_note_fa_s_4, button_note_sol_4, button_note_sol_s_4, button_note_la_4, button_note_la_s_4, button_note_si_4)
		
		#Octava 5
		button_note_do_5 = Gtk.Button("Do  5")
		button_note_do_s_5 = Gtk.Button("Do#  5")
		button_note_re_5 = Gtk.Button("Re  5")
		button_note_re_s_5 = Gtk.Button("Re#  5")
		button_note_mi_5 = Gtk.Button("Mi  5")
		button_note_fa_5 = Gtk.Button("Fa  5")
		button_note_fa_s_5 = Gtk.Button("Fa#  5")
		button_note_sol_5 = Gtk.Button("Sol  5")
		button_note_sol_s_5 = Gtk.Button("Sol#  5")
		button_note_la_5 = Gtk.Button("La  5")
		button_note_la_s_5 = Gtk.Button("La#  5")
		button_note_si_5 = Gtk.Button("Si  5")
		
		#Las ponemos en diferentes tuplas
		notes_5_1 = (button_note_do_5, button_note_do_s_5, button_note_re_5, button_note_re_s_5, button_note_mi_5, button_note_fa_5)
		notes_5_2 = (button_note_fa_s_5, button_note_sol_5, button_note_sol_s_5, button_note_la_5, button_note_la_s_5, button_note_si_5)
		
		#Octava 6
		button_note_do_6 = Gtk.Button("Do  6")
		button_note_do_s_6 = Gtk.Button("Do#  6")
		button_note_re_6 = Gtk.Button("Re  6")
		button_note_re_s_6 = Gtk.Button("Re#  6")
		button_note_mi_6 = Gtk.Button("Mi  6")
		button_note_fa_6 = Gtk.Button("Fa  6")
		button_note_fa_s_6 = Gtk.Button("Fa#  6")
		button_note_sol_6 = Gtk.Button("Sol  6")
		button_note_sol_s_6 = Gtk.Button("Sol#  6")
		button_note_la_6 = Gtk.Button("La  6")
		button_note_la_s_6 = Gtk.Button("La#  6")
		button_note_si_6 = Gtk.Button("Si  6")
		
		#Las ponemos en diferentes tuplas
		notes_6_1 = (button_note_do_6, button_note_do_s_6, button_note_re_6, button_note_re_s_6, button_note_mi_6, button_note_fa_6)
		notes_6_2 = (button_note_fa_s_6, button_note_sol_6, button_note_sol_s_6, button_note_la_6, button_note_la_s_6, button_note_si_6)
		
		#Octava 7
		button_note_do_7 = Gtk.Button("Do  7")
		button_note_do_s_7 = Gtk.Button("Do#  7")
		button_note_re_7 = Gtk.Button("Re  7")
		button_note_re_s_7 = Gtk.Button("Re#  7")
		button_note_mi_7 = Gtk.Button("Mi  7")
		button_note_fa_7 = Gtk.Button("Fa  7")
		button_note_fa_s_7 = Gtk.Button("Fa#  7")
		button_note_sol_7 = Gtk.Button("Sol  7")
		button_note_sol_s_7 = Gtk.Button("Sol#  7")
		button_note_la_7 = Gtk.Button("La  7")
		button_note_la_s_7 = Gtk.Button("La#  7")
		button_note_si_7 = Gtk.Button("Si  7")
		
		#Las ponemos en diferentes tuplas
		notes_7_1 = (button_note_do_7, button_note_do_s_7, button_note_re_7, button_note_re_s_7, button_note_mi_7, button_note_fa_7)
		notes_7_2 = (button_note_fa_s_7, button_note_sol_7, button_note_sol_s_7, button_note_la_7, button_note_la_s_7, button_note_si_7)
		
		#Octava 8
		button_note_do_8 = Gtk.Button("Do  8")
		button_note_do_s_8 = Gtk.Button("Do#  8")
		button_note_re_8 = Gtk.Button("Re  8")
		button_note_re_s_8 = Gtk.Button("Re#  8")
		button_note_mi_8 = Gtk.Button("Mi  8")
		button_note_fa_8 = Gtk.Button("Fa  8")
		button_note_fa_s_8 = Gtk.Button("Fa#  8")
		button_note_sol_8 = Gtk.Button("Sol  8")
		button_note_sol_s_8 = Gtk.Button("Sol#  8")
		button_note_la_8 = Gtk.Button("La  8")
		button_note_la_s_8 = Gtk.Button("La#  8")
		button_note_si_8 = Gtk.Button("Si  8")
		
		#Las ponemos en diferentes tuplas
		notes_8_1 = (button_note_do_8, button_note_do_s_8, button_note_re_8, button_note_re_s_8, button_note_mi_8, button_note_fa_8)
		notes_8_2 = (button_note_fa_s_8, button_note_sol_8, button_note_sol_s_8, button_note_la_8, button_note_la_s_8, button_note_si_8)
		#Octava 9
		button_note_do_9 = Gtk.Button("Do  9")
		button_note_do_s_9 = Gtk.Button("Do#  9")
		button_note_re_9 = Gtk.Button("Re  9")
		button_note_re_s_9 = Gtk.Button("Re#  9")
		button_note_mi_9 = Gtk.Button("Mi  9")
		button_note_fa_9 = Gtk.Button("Fa  9")
		button_note_fa_s_9 = Gtk.Button("Fa#  9")
		button_note_sol_9 = Gtk.Button("Sol  9")
		button_note_sol_s_9 = Gtk.Button("Sol#  9")
		button_note_la_9 = Gtk.Button("La  9")
		button_note_la_s_9 = Gtk.Button("La#  9")
		button_note_si_9 = Gtk.Button("Si  9")
		
		#Las ponemos en diferentes tuplas
		notes_9_1 = (button_note_do_9, button_note_do_s_9, button_note_re_9, button_note_re_s_9, button_note_mi_9, button_note_fa_9)
		notes_9_2 = (button_note_fa_s_9, button_note_sol_9, button_note_sol_s_9, button_note_la_9, button_note_la_s_9, button_note_si_9)

		#Creamos los títulos para cada cuadro de octava
		label_note_0 = Gtk.Label("Octava 0")
		label_note_1 = Gtk.Label("Octava 1")
		label_note_2 = Gtk.Label("Octava 2")
		label_note_3 = Gtk.Label("Octava 3")
		label_note_4 = Gtk.Label("Octava 4")
		label_note_5 = Gtk.Label("Octava 5")
		label_note_6 = Gtk.Label("Octava 6")
		label_note_7 = Gtk.Label("Octava 7")
		label_note_8 = Gtk.Label("Octava 8")
		label_note_9 = Gtk.Label("Octava 9")
		
		#Todo ponemos en tuplas
		labels_titles = (label_note_0, label_note_1, label_note_2, label_note_3, label_note_4, label_note_5, label_note_6,
			label_note_7, label_note_8, label_note_9)

		#Agregamos los títulos a las diversas cajas secundarias
		for i in range(10):
			self.pack_elements(box_box[i], labels_titles[i], 5)

		#Agregamos los botones a las cajas de botones y le damos un espaciado para mejor visualización
		for boton in range(6):			
			self.pack_elements(box_notes_0[0], notes_0_1[boton], 5)
			self.pack_elements(box_notes_1[0], notes_0_2[boton], 5)
			self.pack_elements(box_notes_0[1], notes_1_1[boton], 5)
			self.pack_elements(box_notes_1[1], notes_1_2[boton], 5)
			self.pack_elements(box_notes_0[2], notes_2_1[boton], 5)
			self.pack_elements(box_notes_1[2], notes_2_2[boton], 5)
			self.pack_elements(box_notes_0[3], notes_3_1[boton], 5)
			self.pack_elements(box_notes_1[3], notes_3_2[boton], 5)
			self.pack_elements(box_notes_0[4], notes_4_1[boton], 5)
			self.pack_elements(box_notes_1[4], notes_4_2[boton], 5)
			self.pack_elements(box_notes_0[5], notes_5_1[boton], 5)
			self.pack_elements(box_notes_1[5], notes_5_2[boton], 5)
			self.pack_elements(box_notes_0[6], notes_6_1[boton], 5)
			self.pack_elements(box_notes_1[6], notes_6_2[boton], 5)
			self.pack_elements(box_notes_0[7], notes_7_1[boton], 5)
			self.pack_elements(box_notes_1[7], notes_7_2[boton], 5)
			self.pack_elements(box_notes_0[8], notes_8_1[boton], 5)
			self.pack_elements(box_notes_1[8], notes_8_2[boton], 5)
			self.pack_elements(box_notes_0[9], notes_9_1[boton], 5)
			self.pack_elements(box_notes_1[9], notes_9_2[boton], 5)
			#Aca terminamos de empaquetar todos los botones a todas las cajas

		#Conectamos todos los botones al evento 'enter'
		for i in range(6):
			self.event_button(notes_0_1[i], dialog_create)
			self.event_button(notes_0_2[i], dialog_create)
			self.event_button(notes_1_1[i], dialog_create)
			self.event_button(notes_1_2[i], dialog_create)
			self.event_button(notes_2_1[i], dialog_create)
			self.event_button(notes_2_2[i], dialog_create)
			self.event_button(notes_3_1[i], dialog_create)
			self.event_button(notes_3_2[i], dialog_create)
			self.event_button(notes_4_1[i], dialog_create)
			self.event_button(notes_4_2[i], dialog_create)
			self.event_button(notes_5_1[i], dialog_create)
			self.event_button(notes_5_2[i], dialog_create)
			self.event_button(notes_6_1[i], dialog_create)
			self.event_button(notes_6_2[i], dialog_create)
			self.event_button(notes_7_1[i], dialog_create)
			self.event_button(notes_7_2[i], dialog_create)
			self.event_button(notes_8_1[i], dialog_create)
			self.event_button(notes_8_2[i], dialog_create)
			self.event_button(notes_9_1[i], dialog_create)
			self.event_button(notes_9_2[i], dialog_create)

		#Aquí empaquetamos las cajas con las notas a todas las cajas principales y todo eso
		for i in range(10):
			self.pack_elements(box_box[i], box_notes_0[i], 5)
			self.pack_elements(box_box[i], box_notes_1[i], 5)
			if i < 5:
				self.pack_elements(vbox_notes_1, box_box[i], 5)
			elif i >= 5:
				self.pack_elements(vbox_notes_2, box_box[i], 5)
		
		#Creamos los botones para las opciones
		button_song = Gtk.CheckButton("Reproducir sonido")
		button_song.set_active(True)
		button_save = Gtk.Button("Guardar")
		button_try = Gtk.Button("Probar creación")
		button_last = Gtk.Button("Remover nota")
		button_delete = Gtk.Button("Eliminar canción")
		button_close = Gtk.Button("Cerrar")

		#Tooltips para los botones de opciones
		button_song.set_tooltip_text("Cheque para hacer sonar las notas al pasar el cursor sobre ellas")
		button_save.set_tooltip_text("Guardar la obra de arte recién creada")
		button_try.set_tooltip_text("Reproducir las notas agregadas hasta ahora")
		button_last.set_tooltip_text("Elimina la última nota agregada, si no hay notas agregadas, no hará nada")
		button_delete.set_tooltip_text("Elimina todas las notas agregadas hasta el momento, es decir, elimina la canción entera")
		
		#Eventos para los botones de opciones
		button_song.connect("toggled", self.play_or_not)
		button_save.connect("clicked", self.save_song, dialog_create)
		button_try.connect("clicked", self.try_song, dialog_create)
		button_last.connect("clicked", self.last_note, dialog_create)
		button_delete.connect("clicked", self.delete_song, dialog_create)
		button_close.connect("clicked", self.close_box, dialog_create)

		#Empaquetamos las opciones en el cuadro de opciones
		vbox_option.pack_start(button_song, True, True, 15)
		vbox_option.pack_start(button_save, True, True, 15)
		vbox_option.pack_start(button_try, True, True, 15)
		vbox_option.pack_start(button_last, True, True, 15)
		vbox_option.pack_start(button_delete, True, True, 15)
		vbox_option.pack_start(button_close, True, True, 15)

		#Empaquetamos las cajas secundarias a la principal y la principal al cuadro
		hbox_songs.pack_start(vbox_notes_1, True, True, 5)
		hbox_songs.pack_start(vbox_notes_2, True, True, 5)
		hbox_songs.pack_start(vbox_notes_3, True, True, 5)
		hbox_songs.pack_start(vbox_option, True, True, 10)
		box_create = dialog_create.get_content_area()
		box_create.add(hbox_songs)

		#Mostramos el cuadro y esperamos una accion
		dialog_create.show_all()

	#Evento que conecta los botones a las señales necesarias para poder trabajar con las acciones
	def event_button(self, widget, parent):
		widget.connect("enter", self.play_note) #Método si se pasa el cursor sobre los botones
		widget.connect("clicked", self.click_note, parent) #Método si se clickea sobre un botón

	#Función para saber si quiere hacer sonar las notas o no
	def play_or_not(self, widget):
		#Lo único que hará esta función es agregar elementos a la lista, la magia se hará en la función play_note
		play_yes.append(0)
	
	#Eliminar la nota o canción
	def delete(self, widget, parent):
		#Conseguimos el texto del botón
		label_widget = widget.get_label()
		
		#Preguntamos si eliminará la última nota o la canción completa
		if label_widget == "Si":
			music.delete_last()
		elif label_widget == "Si, estoy seguro":
			music.delete_all()

		#Destruimos el cuadro de diálogo después de elegir la opción
		self.close_box(widget, parent)

	#Función si se presiona un botón
	def click_note(self, widget, parent):
		dialog_click = Gtk.Dialog()
		dialog_click.set_title("¡Atención!")
		dialog_click.set_default_size(240, 120)
		dialog_click.set_border_width(5)
		dialog_click.set_modal(True)
		dialog_click.set_transient_for(parent)
		dialog_click.set_resizable(False)

		#Creamos la caja que contendrá los elementos del diálogo
		vbox_click = Gtk.VBox(spacing = 5)
		hbox_click = Gtk.HBox(spacing = 5)

		#Ahora los elementos que contendrá la caja
		label_note = widget.get_label()
		label_click = Gtk.Label("Ingrese el tiempo (milisegundos)")
		label_ex = Gtk.Label("1 segundo = 1000 milisegundos")
		duration_note = Gtk.Entry()
		button_add = Gtk.Button("Agregar")
		button_cancel = Gtk.Button("Cancelar")

		#Evento click para los botones
		button_cancel.connect("clicked", self.close_box, dialog_click)
		button_add.connect("clicked", self.pass_note, label_note, duration_note, dialog_click)

		#Ahora empaquetamos todo en la caja
		hbox_click.pack_start(button_add, True, True, 5)
		hbox_click.pack_start(button_cancel, True, True, 5)
		vbox_click.pack_start(label_click, True, True, 5)
		vbox_click.pack_start(label_ex, True, True, 5)
		vbox_click.pack_start(duration_note, True, True, 5)
		vbox_click.pack_start(hbox_click, True, True, 5)

		#Ahora la caja la colocamos al cuadro
		box_click = dialog_click.get_content_area()
		box_click.add(vbox_click)

		#Y mostramos el cuadro de diálogo
		dialog_click.show_all()

	#Reproducimos la nota cuando el cursor pasa sobre un botón
	def play_note(self, widget):
		note = widget.get_label()
		
		#Obtenemos a que octava pertenece la nota
		octava_n = int(note[len(note)-1])
		
		#Obtenemos la nota
		note_e = note[:4]
		
		#Acá se hace la magia para hacer sonar o no las notas
		play_count = len(play_yes)
		if play_count % 2 != 0:
			#Si la longitud de la lista es impar entonces sonará las notas, pero si es par, no hará nada
			#La pasamos al otro script para hacerla sonar
			music.play_note(note_e, octava_n)

	#Creamos la función donde se pasarán las notas al otro script
	def pass_note(self, widget, note, duration, dialog):
		#Obtenemos el texto del botón para saber que nota es y a que octava pertenece
		label_duration = duration.get_text()
		
		#Obtenemos la octava a la que pertenece
		octava_n = int(note[len(note)-1])
		
		#Obtenemos la nota
		note_e = note[:4]
		
		#Le pasamos al otro script para agregar la nota y la duración de la misma
		music.add_note(note_e, octava_n, label_duration)
		
		#Destruimos el cuadro para poder seguir agregando más
		self.close_box(self, dialog)

	#Método para eliminar la canción completa
	def delete_song(self, widget, parent):
		dialog_delete = Gtk.Dialog()
		dialog_delete.set_title("¡Atención!")
		dialog_delete.set_default_size(240, 120)
		dialog_delete.set_border_width(5)
		dialog_delete.set_modal(True)
		dialog_delete.set_transient_for(parent)
		dialog_delete.set_resizable(False)

		#Agregamos los botones necesarios para realizar las acciones necesarias
		button_yes = Gtk.Button("Si, estoy seguro")
		button_no = Gtk.Button("No, cancelar")

		#Conectamos los botones a los eventos correspondientes
		button_yes.connect("clicked", self.delete, dialog_delete)
		button_no.connect("clicked", self.close_box, dialog_delete)

		#Cajas donde estarán los elementos que se mostrarán
		vbox_delete = Gtk.VBox(spacing = 5)
		hbox_delete = Gtk.HBox(homogeneous = True, spacing = 5)

		#Mensaje que se mostrará para confirmar la eliminación
		label_delete = Gtk.Label("¿Estás seguro que desea eliminar la canción completa?")
		
		#Empaquetamos todo a las cajas correspondientes
		hbox_delete.pack_start(button_yes, True, True, 5)
		hbox_delete.pack_start(button_no, True, True, 5)
		vbox_delete.pack_start(label_delete, True, True, 5)
		vbox_delete.pack_start(hbox_delete, True, True, 5)

		#La caja principal la ponemos al cuadro de diálogo
		box_delete = dialog_delete.get_content_area()
		box_delete.add(vbox_delete)
		
		#Mostramos el cuadro
		dialog_delete.show_all()

	#Método para eliminar la última nota agregada
	def last_note(self, widget, parent):
		dialog_last = Gtk.Dialog()
		dialog_last.set_title("¡Atención!")
		dialog_last.set_default_size(240, 120)
		dialog_last.set_border_width(5)
		dialog_last.set_modal(True)
		dialog_last.set_transient_for(parent)
		dialog_last.set_resizable(False)

		#Agregamos los botones necesarios para realizar las acciones necesarias
		button_yes = Gtk.Button("Si")
		button_no = Gtk.Button("No")

		#Conectamos los botones a los eventos correspondientes
		button_yes.connect("clicked", self.delete, dialog_last)
		button_no.connect("clicked", self.close_box, dialog_last)

		#Cajas donde estarán los elementos que se mostrarán
		vbox_last = Gtk.VBox(spacing = 5)
		hbox_last = Gtk.HBox(homogeneous = True, spacing = 5)

		#Mensaje que se mostrará para confirmar la eliminación
		label_last = Gtk.Label("¿Estás seguro que desea eliminar la nota?")
		
		#Empaquetamos los elementos a las cajas correspondientes
		hbox_last.pack_start(button_yes, True, True, 5)
		hbox_last.pack_start(button_no, True, True, 5)
		vbox_last.pack_start(label_last, True, True, 5)
		vbox_last.pack_start(hbox_last, True, True, 5)

		#Agregamos la caja principal al cuadro de diálogo
		box_last = dialog_last.get_content_area()
		box_last.add(vbox_last)
		
		#Mostramos el cuadro
		dialog_last.show_all()

	#Cuadro antes de guardar la canción
	def save_song(self, widget, parent):
		dialog_save = Gtk.Dialog()
		dialog_save.set_title("Guardar Canción")
		dialog_save.set_default_size(240, 120)
		dialog_save.set_border_width(5)
		dialog_save.set_modal(True)
		dialog_save.set_transient_for(parent)
		dialog_save.set_resizable(False)

		#Creamos la caja, los botones y el texto con el campo
		vbox_save = Gtk.VBox(spacing = 5)
		hbox_save = Gtk.HBox(homogeneous = True, spacing = 5)
		label_save = Gtk.Label("Ingrese el nombre para la canción")
		name_song = Gtk.Entry()
		button_save = Gtk.Button("Guardar")
		button_cancel = Gtk.Button("Cancelar")

		#Le conectamos a los métodos correspondientes, y un tooltip para el botón guardar
		button_save.set_tooltip_text("Si existe un archivo con ese nombre, se agregará al final del archivo ya existente")
		button_cancel.connect("clicked", self.close_box, dialog_save)
		button_save.connect("clicked", self.save_with_name, name_song, dialog_save)

		#Empaquetamos en las cajas correspondientes
		hbox_save.pack_start(button_save, True, True, 5)
		hbox_save.pack_start(button_cancel, True, True, 5)
		vbox_save.pack_start(label_save, True, True, 5)
		vbox_save.pack_start(name_song, True, True, 5)
		vbox_save.pack_start(hbox_save, True, True, 5)

		#Agregamos la caja principal al cuadro
		box_save = dialog_save.get_content_area()
		box_save.add(vbox_save)

		#Mostramos el cuadro de diálogo
		dialog_save.show_all()

	#Guardar la canción con el nombre ingresado
	def save_with_name(self, widget, name, parent):
		#Conseguimos el nombre elegido y llamamos al método de guardado que hay en el otro script
		name_song = name.get_text()
		music.save_all(name_song)
		
		#Acá destruimos el cuadro después de haber guardado
		self.close_box(widget, parent)

	#Método que reproducirá la canción que se tiene hasta el momento
	def try_song(self, widget, parent):
		dialog_try = Gtk.Dialog()
		dialog_try.set_title("Reproduciendo canción")
		dialog_try.set_default_size(240, 120)
		dialog_try.set_border_width(5)
		dialog_try.set_modal(True)
		dialog_try.set_transient_for(parent)
		dialog_try.set_resizable(False)
		
		#Ahora crearemos un spinner que girará mientras se reproduce la canción
		spinner_try = Gtk.Spinner()
		spinner_try.start()

		#Texto que se mostrará debajo del spinner
		label_try = Gtk.Label("Se recomienda no cerrar la ventana hasta terminar de reproducir")
		
		#Creamos la caja principal y empaquetamos los elementos
		vbox_try = Gtk.VBox(spacing = 10)
		vbox_try.pack_start(spinner_try, True, True, 5)
		vbox_try.pack_start(label_try, True, True, 5)

		#Agregamos la caja principal al cuadro de diálogo
		box_try = dialog_try.get_content_area()
		box_try.add(vbox_try)

		#Mostramos el cuadro de diálogo
		dialog_try.show_all()

		#Acá llamamos a la función que reproducirá la canción
		music.play_song()

	#Termina las funciones para las notas músicales

	#Empieza las funciones para los sensores y leds

	#Método que se ativará si se hace clic en el botón 'Sensores y LEDS'
	def view_sensors_leds(self, widget, ventana):
		dialog_sensors = Gtk.Dialog()
		dialog_sensors.set_title("Sensores y LEDs")
		dialog_sensors.set_border_width(5)
		dialog_sensors.set_modal(True)
		dialog_sensors.set_transient_for(ventana)
		dialog_sensors.set_resizable(False)

		#Creamos las cajas que contendrán las diferentes acciones e información de los sensores
		vbox_sensors = Gtk.VBox(spacing = 2)
		hbox_led_rgb = Gtk.HBox(homogeneous = True, spacing = 2)
		vbox_led_button = Gtk.VBox(homogeneous = True, spacing = 2)
		vbox_led_r = Gtk.VBox(homogeneous = True, spacing = 2)
		vbox_led_g = Gtk.VBox(homogeneous = True, spacing = 2)
		vbox_led_b = Gtk.VBox(homogeneous = True, spacing = 2)
		hbox_led = Gtk.HBox(spacing = 2)
		hbox_see = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_light = Gtk.HBox(homogeneous = True, spacing = 5)
		hbox_sounds = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_sense = Gtk.HBox(homogeneous = True, spacing = 2)
		cajas = (hbox_led_rgb, hbox_led, hbox_see, hbox_light, hbox_sounds, hbox_sense)

		#Para el LED RGB
		btn_led_off = Gtk.Button("Apagar LED RGB")
		btn_led_rgb = Gtk.Button("Encender LED RGB")
		btn_led_rgb.set_tooltip_text("El LED RGB necesita de 3 valores: Rojo, Verde y Azul (del inglés) y la combinación forma un solo color, si desea prender de color rojo ponga un valor de 255 al rojo y el resto en 0, 0 en todo para apagar")
		label_led_r = Gtk.Label("Valor Rojo")
		value_led_r = Gtk.Entry()
		value_led_r.set_max_length(3)
		value_led_r.set_placeholder_text("Solo números")
		label_led_g = Gtk.Label("Valor Verde")
		value_led_g = Gtk.Entry()
		value_led_g.set_max_length(3)
		value_led_g.set_placeholder_text("Solo números")
		label_led_b = Gtk.Label("Valor Azul")
		value_led_b = Gtk.Entry()
		value_led_b.set_max_length(3)
		value_led_b.set_placeholder_text("Solo números")

		#Función para apagar el LED
		def off_led(self):
			action.led_rgb(0, 0, 0)
			value_led_r.set_placeholder_text("Solo números")
			value_led_r.set_text("")
			value_led_g.set_placeholder_text("Solo números")
			value_led_g.set_text("")
			value_led_b.set_placeholder_text("Solo números")
			value_led_b.set_text("")

		#Conectamos el botón a su respectiva retrollamada
		btn_led_rgb.connect("clicked", self.led_rgb_change, value_led_r, value_led_g, value_led_b)
		btn_led_off.connect("clicked", off_led)

		#Ahora empaquetaremos todo en la caja
		vbox_led_button.pack_start(btn_led_rgb, True, True, 1)
		vbox_led_button.pack_start(btn_led_off, True, True, 1)
		vbox_led_r.pack_start(label_led_r, True, True, 1)
		vbox_led_r.pack_start(value_led_r, True, True, 1)
		vbox_led_g.pack_start(label_led_g, True, True, 1)
		vbox_led_g.pack_start(value_led_g, True, True, 1)
		vbox_led_b.pack_start(label_led_b, True, True, 1)
		vbox_led_b.pack_start(value_led_b, True, True, 1)
		hbox_led_rgb.pack_start(vbox_led_button, True, True, 1)
		hbox_led_rgb.pack_start(vbox_led_r, True, True, 1)
		hbox_led_rgb.pack_start(vbox_led_g, True, True, 1)
		hbox_led_rgb.pack_start(vbox_led_b, True, True, 1)

		#Ahora para el led normal
		btn_led = Gtk.ToggleButton("Encender LED")
		btn_led.set_active(False)
		btn_led.set_tooltip_text("Este es un botón que enciende y apaga el pequeño LED que tiene RoDI")
		btn_led.connect("toggled", self.led_change)

		#Ahora empaquetamos en su respectiva caja
		hbox_led.pack_start(btn_led, True, True, 5)

		#Ahora para el sensor de distancia
		btn_see = Gtk.Button("Medir distancia")
		btn_see.set_tooltip_text("Este es un botón hace que RoDI meda distancia entre un objeto y él")
		entry_see = Gtk.Entry()
		entry_see.set_text("No veo nada")
		entry_see.set_editable(False)
		btn_see.connect("clicked", self.rodi_see, entry_see)

		#Ahora empaquetamos a su respectiva caja
		hbox_see.pack_start(btn_see, True, True, 5)
		hbox_see.pack_start(entry_see, True, True, 5)

		#Ahora para la intensidad del luz en el ambiente
		btn_light = Gtk.Button("Intensidad de luz")
		btn_light.set_tooltip_text("Medir la intensidad de luz que hay en el ambiente")
		entry_light = Gtk.Entry()
		entry_light.set_text("Intensidad")
		entry_light.set_editable(False)
		btn_light.connect("clicked", self.rodi_light, entry_light)

		#Ahora empaquetamos a su respectiva caja
		hbox_light.pack_start(btn_light, True, True, 5)
		hbox_light.pack_start(entry_light, True, True, 5)

		#Ahora para el sonido
		btn_frecuency = Gtk.Button("Reproducir frecuencia")
		btn_frecuency.set_tooltip_text("Reproduce una frecuencia por un determinado tiempo")
		value_frecuency = Gtk.Entry()
		value_frecuency.set_placeholder_text("Frecuencia")
		value_time = Gtk.Entry()
		value_time.set_placeholder_text("Duración (segundos)")

		#Ahora conectaremos a su retrollamada
		btn_frecuency.connect("clicked", self.play_frecuency, value_frecuency, value_time)

		#Empaquetar para el sonido
		hbox_sounds.pack_start(btn_frecuency, True, True, 2)
		hbox_sounds.pack_start(value_frecuency, True, True, 2)
		hbox_sounds.pack_start(value_time, True, True, 2)

		#Ahora los sensores seguidores de línea
		btn_sensors = Gtk.Button("Sensores seguidor de línea")
		btn_sensors.set_tooltip_text("El RoDI tiene dos sensores abajo, que detectan si están sobre algún objeto de color blanco(1) o negro(0)")
		value_iz = Gtk.Entry()
		value_iz.set_editable(False)
		value_iz.set_placeholder_text("Sensor izquierdo")
		value_der = Gtk.Entry()
		value_der.set_editable(False)
		value_der.set_placeholder_text("Sensor derecho")

		#Ahora conectaremos a su retrollamada
		btn_sensors.connect("clicked", self.sensors, value_iz, value_der)

		#Empaquetamos para los sensores
		hbox_sense.pack_start(btn_sensors, True, True, 2)
		hbox_sense.pack_start(value_iz, True, True, 2)
		hbox_sense.pack_start(value_der, True, True, 2)
		
		#Este solo es un título para el cuadro de diálogo haciendo referencia a que el RoDI es capaz de realizar acciones más complejas
		label_title = Gtk.Label()
		label_title.set_markup("Estas son las funciones básicas de las funcionalidades del RoDI")
		vbox_sensors.pack_start(label_title, True, True, 5)

		#Agregamos todas las cajas a la caja principal
		for i in range(6):
			self.pack_elements(vbox_sensors, cajas[i], 5)

		#Agregamos las cajas al cuadro de diálogo
		box_sensors = dialog_sensors.get_content_area()
		box_sensors.add(vbox_sensors)

		#Y mostramos la caja
		dialog_sensors.show_all()

	#Función para encender el LED RGB
	def led_rgb_change(self, widget, r, g, b):
		#Probamos agarrar los valores de los campos de texto y convertirlos en enteros, y salta alguna excepción la manejaremos
		try:
			value_r = int(r.get_text())
		except ValueError:
			r.set_placeholder_text("Error")
			r.set_text("")
		try:
			value_g = int(g.get_text())
		except ValueError:
			g.set_placeholder_text("Error")
			g.set_text("")
		try:
			value_b = int(b.get_text())
		except ValueError:
			b.set_placeholder_text("Error")
			b.set_text("")
		#Preguntamos si los datos ingresados son enteros
		try:
			if type(value_r) != int or type(value_g) != int or type(value_b) != int:
				r.set_placeholder_text("Debe ser número")
				g.set_placeholder_text("Debe ser número")
				b.set_placeholder_text("Debe ser número")
				r.set_text("")
				g.set_text("")
				b.set_text("")
			elif value_r < 0 or value_r > 255 or value_g < 0 or value_g > 255 or value_b < 0 or value_b > 255:
				r.set_placeholder_text("Valor de 0 a 255")
				g.set_placeholder_text("Valor de 0 a 255")
				b.set_placeholder_text("Valor de 0 a 255")
				r.set_text("")
				g.set_text("")
				b.set_text("")
			else:
				action.led_rgb(value_r, value_g, value_b)
		except UnboundLocalError:
			r.set_placeholder_text("Error")
			g.set_placeholder_text("Error")
			b.set_placeholder_text("Error")

	#Función para encender y apagar el LED normal
	def led_change(self, widget):
		state = widget.get_active()
		if state:
			widget.set_label("Apagar LED")
			action.led(state)
		else:
			widget.set_label("Encender LED")
			action.led(state)

	#Función para medir distancia de rodi a un objeto que tiene adelante
	def rodi_see(self, widget, text):
		distance = action.see()
		response = "Veo un objeto a " + str(distance)
		text.set_text(response)

	#Función para medir la intensidad de luz
	def rodi_light(self, widget, text):
		intensity = action.light()
		res = "Hay " + str(intensity) + "% de luz"
		text.set_text(res)

	#Función para reproducir una frecuencia
	def play_frecuency(self, widget, frecuency, time):
		#Probamos agarrar los valores de los campos de texto y convertirlos en enteros, y si salta alguna excepción la manejaremos
		try:
			value_fre = float(frecuency.get_text())
		except ValueError:
			frecuency.set_placeholder_text("Error")
			frecuency.set_text("")
		try:
			value_time = float(time.get_text())
		except ValueError:
			time.set_placeholder_text("Error")
			time.set_text("")
		#Preguntamos si los datos ingresados son enteros
		try:
			if type(value_fre) != float or type(value_time) != float:
				frecuency.set_placeholder_text("Debe ser número")
				time.set_placeholder_text("Debe ser número")
				frecuency.set_text("")
				time.set_text("")
			else:
				action.play_sing(value_fre, value_time)
		except UnboundLocalError:
			frecuency.set_placeholder_text("Error")
			time.set_placeholder_text("Error")

	#Función para los sensores de línea
	def sensors(self, widget, left, right):
		sen_iz, sen_der = action.sensores()
		value_left = str(int((sen_iz+1)/512))+" Left"
		value_right = str(int((sen_der+1)/512))+" Right"
		left.set_text(value_left)
		right.set_text(value_right)

	#Termina las funciones para los sensores y leds

	#Empieza las funciones para los movimientos del rodi 

	#Método para ver los posibles movimientos del RoDI
	def view_moves(self, widget, box, ventana):
		self.close_box(widget, box)
		dialog_moves = Gtk.Dialog()
		dialog_moves.set_title("Movimientos Básicos")
		dialog_moves.set_border_width(5)
		dialog_moves.set_modal(True)
		dialog_moves.set_transient_for(ventana)
		dialog_moves.set_resizable(False)

		vbox_main = Gtk.VBox(spacing = 5)
		label_title = Gtk.Label("Poner el cursor encima de una flecha para ir a esa dirección, clic para ir más rápido")
		hbox_moves_up = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_moves_middle = Gtk.HBox(homogeneous = True, spacing = 2)
		hbox_moves_down = Gtk.HBox(homogeneous = True, spacing = 2)
		cajas = (label_title, hbox_moves_up, hbox_moves_middle, hbox_moves_down)

		for i in range(4):
			self.pack_elements(vbox_main, cajas[i], 0)
		
		#Para las imágenes
		image_left_up = Gtk.Image()
		image_left_up.set_from_file("images/move_left_up.png")
		image_up = Gtk.Image()
		image_up.set_from_file("images/move_up.png")
		image_right_up = Gtk.Image()
		image_right_up.set_from_file("images/move_right_up.png")
		image_left = Gtk.Image()
		image_left.set_from_file("images/move_left.png")
		image_stop = Gtk.Image()
		image_stop.set_from_file("images/move_stop.png")
		image_right = Gtk.Image()
		image_right.set_from_file("images/move_right.png")
		image_left_down = Gtk.Image()
		image_left_down.set_from_file("images/move_left_down.png")
		image_down = Gtk.Image()
		image_down.set_from_file("images/move_down.png")
		image_right_down = Gtk.Image()
		image_right_down.set_from_file("images/move_right_down.png")

		#Para los movimientos de hacia arriba
		btn_left_up = Gtk.Button()
		btn_left_up.set_image(image_left_up)
		btn_left_up.set_tooltip_text("Adelante izquierda")
		btn_up = Gtk.Button()
		btn_up.set_image(image_up)
		btn_up.set_tooltip_text("Adelante")
		btn_right_up = Gtk.Button()
		btn_right_up.set_image(image_right_up)
		btn_right_up.set_tooltip_text("Adelante derecha")
		box_up = (btn_left_up, btn_up, btn_right_up)

		#Para los del medio con una imagen del rodi
		btn_left = Gtk.Button()
		btn_left.set_image(image_left)
		btn_left.set_tooltip_text("Izquierda")
		btn_stop = Gtk.Button()
		btn_stop.set_image(image_stop)
		btn_stop.set_tooltip_text("Detiene a RoDI")
		btn_right = Gtk.Button()
		btn_right.set_image(image_right)
		btn_right.set_tooltip_text("Derecha")
		box_middle = (btn_left,btn_stop, btn_right)

		#Para los de abajo
		btn_left_down = Gtk.Button()
		btn_left_down.set_image(image_left_down)
		btn_left_down.set_tooltip_text("Atrás izquierda")
		btn_down = Gtk.Button()
		btn_down.set_image(image_down)
		btn_down.set_tooltip_text("Atrás")
		btn_right_down = Gtk.Button()
		btn_right_down.set_image(image_right_down)
		btn_right_down.set_tooltip_text("Atrás derecha")
		box_down = (btn_left_down, btn_down, btn_right_down)

		#Conectamos a los botones los eventos de enter y clicked
		for i in range(3):
			self.event_button_action(box_up[i])
			self.event_button_action(box_middle[i])
			self.event_button_action(box_down[i])

		#Empaquetamos todos los botones y la imagen a sus respectivas cajas
		for i in range(3):
			self.pack_elements(hbox_moves_up, box_up[i], 0)
			self.pack_elements(hbox_moves_middle, box_middle[i], 0)
			self.pack_elements(hbox_moves_down, box_down[i], 0)

		box_moves = dialog_moves.get_content_area()
		box_moves.add(vbox_main)

		dialog_moves.show_all()

	#Evento para los botnoes de movimientos
	def event_button_action(self, widget):
		#Agarramos todos los botones de movimientos y los conectamos a los eventos respectivos para mover el rodi
		widget.connect("leave", self.move_stop)
		widget.connect("enter", self.move_rodi)
		widget.connect("clicked", self.move_rodi_fast)

	#Mover el rodi a su velocidad media
	def move_rodi(self, widget):
		tooltip = widget.get_tooltip_text()
		velocity = 30
		move.find_action(tooltip, velocity)

	#Mover el rodi a su máxima velocidad
	def move_rodi_fast(self, widget):
		tooltip = widget.get_tooltip_text()
		velocity = 100
		move.find_action(tooltip, velocity)

	#Llamamos al método para detener los movimientos
	def move_stop(self, widget):
		#Sólo detenemos todos los movimientos
		move.stop()
		
	#Termina las funciones para los movimientos

	#Empieza las funciones para los modos

	def view_moods(self, widget, parent):
		dialog_mood = Gtk.Dialog()
		dialog_mood.set_border_width(5)
		dialog_mood.set_title("Modos")
		dialog_mood.set_modal(True)
		dialog_mood.set_transient_for(parent)
		dialog_mood.set_resizable(False)

		#Creamos las cajas que contendrán los elementos
		vbox_mood = Gtk.VBox(spacing = 5)
		hbox_moods = Gtk.HBox(homogeneous = True, spacing = 5)

		#Creamos los elementos que tendrá el cuadro de diálogo
		label_note = Gtk.Label()
		label_note.set_markup("""<b><big>Modos</big></b>
Los modos están realizados solo para competir (Seguidor de Línea), con el único deseo
de que se realice competencias entre robots para seguir de línea (no puede doblar curvas
cerradas), el modo de sumo fue puesto solo para conocer que hay como un mundo de
competencias entre robots, no fue hecho con la intención de destrozar robots por
diversión, sino para demostrar como sería el caso de ver una batalla de sumo entre
dos robots preparados con sus respectivas protecciones, se recomienda
<b>no usar el modo sumo</b>
""")
		label_note.set_justify(Gtk.Justification.CENTER)
		button_seguidor = Gtk.Button("Seguidor de Línea")
		button_seguidor.set_tooltip_text("Activa el modo seguidor de línea, solo active cuando tenga la pista")
		button_seguidor.connect("clicked", self.mood_seguidor, dialog_mood)
		button_close = Gtk.Button("Cerrar")
		button_close.connect("clicked", self.close_box, dialog_mood)

		#Agregamos a las cajas
		hbox_moods.pack_start(button_seguidor, True, True, 2)
		hbox_moods.pack_start(button_close, True, True, 2)
		vbox_mood.pack_start(label_note, True, True, 5)
		vbox_mood.pack_start(hbox_moods, True, True, 2)

		#Agregamos la caja al cuadro
		box_mood = dialog_mood.get_content_area()
		box_mood.add(vbox_mood)
		
		#Mostramos el cuadro
		dialog_mood.show_all()

	#Función para seguidor de línea
	def mood_seguidor(self, widget, parent):
		dialog_seguidor = Gtk.Dialog()
		dialog_seguidor.set_border_width(5)
		dialog_seguidor.set_title("Seguidor de línea")
		dialog_seguidor.set_modal(True)
		dialog_seguidor.set_transient_for(parent)
		dialog_seguidor.set_resizable(False)

		#Creamos los elementos que contendrá el cuadro
		vbox_seguidor = Gtk.VBox(homogeneous = True, spacing = 2)
		hbox_buttons = Gtk.HBox(homogeneous = True, spacing = 2)

		label_text = Gtk.Label("Ingrese el número de curvas que tiene la pista")
		entry_curve = Gtk.Entry()
		button_start = Gtk.Button("Empezar")
		button_start.connect("clicked", self.start_follower, entry_curve)
		button_close = Gtk.Button("Cerrar")
		button_close.connect("clicked", self.close_box, dialog_seguidor)

		hbox_buttons.pack_start(button_start, True, True, 2)
		hbox_buttons.pack_start(button_close, True, True, 2)
		vbox_seguidor.pack_start(label_text, True, True, 2)
		vbox_seguidor.pack_start(entry_curve, True, True, 2)
		vbox_seguidor.pack_start(hbox_buttons, True, True, 2)


		#Agregamos los elementos al cuadro y lo mostramos
		box_seguidor = dialog_seguidor.get_content_area()
		box_seguidor.add(vbox_seguidor)
		dialog_seguidor.show_all()

	def start_follower(self, widget, curve):
		try:
			curves = int(curve.get_text())
		except ValueError:
			curve.set_placeholder_text("Error")
			curve.set_text("")
		#Preguntamos si ingresó un número
		try:
			if type(curves) != int:
				curve.set_placeholder_text("Debe ser número")
				curve.set_text("")
			else:
				mood.line_follower(curves)
		except UnboundLocalError:
			curve.set_placeholder_text("Error")

	#Termina las funciones para los modos

	#Empieza las funciones que se pueden utilizar para cualquier método

	#Página siguiente
	def next_page(self, widget, notebook):
		notebook.next_page()

	#Página anterior
	def back_page(self, widget, notebook):
		notebook.prev_page()

	#Función para cerrar cualquier cuadro de diálogo
	def close_box(self, widget, box):
		box.destroy()

	#Creamos una funcion para empaquetar los diversos botones para ahorrar algunas lineas
	def pack_elements(self, box, element, space):
		box.pack_start(element, True, True, space)

	#Termina las funciones globales por decirlo
		
	#Cerramos la ventana y terminamos la ejecución de Gtk
	def exit(self, widget):
		Gtk.main_quit()

	#Empezamos a ejecutar el programa aquí esperando alguna acción por parte del usuario
	def main(self):
		Gtk.main()

#Aquí llamamos a la función 'main' de la clase app para poder ejecutar el programa
if __name__ == "__main__":
	a = app()
	a.main()