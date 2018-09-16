#Importamos las librerias necesarias, la de rodi y el método sleep de la libreria time
from scripts import rodi
from time import sleep

#Heredamos todos los métodos de la clase RoDI a la variable robot
robot = rodi.RoDI()

#La frecuencia de las notas para cada octava respectivamente
notes_frecuency_0 = (16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87)
notes_frecuency_1 = (32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.0, 51.91, 55.0, 58.27, 61.74)
notes_frecuency_2 = (65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.0, 103.83, 110.0, 116.54, 123.47)
notes_frecuency_3 = (130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.0, 196.0, 207.65, 220.0, 233.08, 246.94)
notes_frecuency_4 = (261.63, 277.18, 293.67, 311.13, 329.63, 349.23, 369.99, 392.0, 415.31, 440.0, 466.16, 493.88)
notes_frecuency_5 = (523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61, 880.0, 932.33, 987.77)
notes_frecuency_6 = (1046.50, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.0, 1864.66, 1975.51)
notes_frecuency_7 = (2093.01, 2217.46, 2349.32, 2489.02, 2637.02, 2793.83, 2959.96, 3135.96, 3322.44, 3520.0, 3729.31, 3951.07)
notes_frecuency_8 = (4186.01, 4434.92, 4698.64, 4978.03, 5274.04, 5587.65, 5919.91, 6271.93, 6644.88, 7040.0, 7458.62, 7902.13)
notes_frecuency_9 = (8372.02, 8869.84, 9397.27, 9956.06, 10548.08, 11175.30, 11839.82, 12543.86, 13289.75, 14080.0, 14917.24, 15804.26)
notes_name = ("Do  ", "Do# ", "Re  ", "Re# ", "Mi  ", "Fa  ", "Fa# ", "Sol ", "Sol#", "La  ", "La# ", "Si  ")

#Listas donde se almacenarán las notas y tiempos para las canciones de los usuarios
note_frecuency = []
time_sleep = []
time_note = []

class music:
	
	#Función para encontrar la nota y la duración de ella
	def search(self, note, octava):
		indice_note = int
		for i in range(12):
			if notes_name[i] == note:
				indice_note = i
		if octava == 0:
			frecuency = notes_frecuency_0[indice_note]
		elif octava == 1:
			frecuency = notes_frecuency_1[indice_note]
		elif octava == 2:
			frecuency = notes_frecuency_2[indice_note]
		elif octava == 3:
			frecuency = notes_frecuency_3[indice_note]
		elif octava == 4:
			frecuency = notes_frecuency_4[indice_note]
		elif octava == 5:
			frecuency = notes_frecuency_5[indice_note]
		elif octava == 6:
			frecuency = notes_frecuency_6[indice_note]
		elif octava == 7:
			frecuency = notes_frecuency_7[indice_note]
		elif octava == 8:
			frecuency = notes_frecuency_8[indice_note]
		else:
			frecuency = notes_frecuency_9[indice_note]

		#Retornamos la frecuencia de la nota que se quiere reproducir
		return frecuency

	#Función para agregar las notas y el tiempo de la nota
	def add_note(self, note, octava, duration):
		#Retornamos la frecuencia de la nota a agregar
		frecuency = self.search(note, octava)
		
		#Agregamos la frecuencia a la lista de notas para reproducirlas
		note_frecuency.append(frecuency)
		
		#Agregamos el tiempo que se detendrá el programa para que reproduzca bien los sonidos
		time_note.append(int(duration))
		
		#Agregamos el tiempo que se reproducirá la nota
		time_sleep.append(int(duration)/1000)

	#Método que reproducirá los sonidos al momento de pasar el cursor sobre el botón
	def play_note(self, note, octava):
		#Retornamos la frecuencia de la nota a reproducir
		frecuency = self.search(note, octava)

		#Le decimos a rodi que reproduzca el sonido
		robot.sing(frecuency, 300)

	#Función para reproducir las notas existentes
	def play_song(self):
		#Le pasamos las notas en un ciclo que se repita la cantidad de notas que tiene hasta ahora
		for i in range(len(note_frecuency)):
			robot.sing(note_frecuency[i], time_note[i])
			sleep(time_sleep[i])

	#Función para eliminar la última nota agregada
	def delete_last(self):
		#Seleccionamos los últimos agregados
		note_delete = note_frecuency[len(note_frecuency) - 1]
		time_delete = time_note[len(time_note) - 1]
		time_s_delete = time_sleep[len(time_sleep) - 1]
		
		#Eliminamos las notas
		note_frecuency.remove(note_delete)
		time_note.remove(time_delete)
		time_sleep.remove(time_s_delete)

	#Función para eliminar las canciones
	def delete_all(self):
		#Vaciamos todas las listas para volver a agregar las notas
		for i in range(len(note_frecuency)):
			for notas in note_frecuency:
				note_frecuency.remove(notas)
			for time_s in time_sleep:
				time_sleep.remove(time_s)
			for time_n in time_note:
				time_note.remove(time_n)

	#Función para guardar la canción en un archivo
	def save_all(self, name):
		#Agarramos el nombre para la canción y le ponemos la extensión para el archivo
		name += ".txt"

		#Le pedimos que abra el archivo, y si no existe que cree
		save_song = open("songs/"+name, "w+")
		
		#Ahora le pasamos todas las notas y tiempos al archivo
		save_song.write("This is a song\n")
		for i in range(len(note_frecuency)):
			save_song.write(str(note_frecuency[i]))
			save_song.write("\n")
			save_song.write(str(time_note[i]))
			save_song.write("\n")
		
		#Cerramos el archivo después de utilizarlo
		save_song.close()

		#Ahora borramos todas las notas agregadas para que se pueda crear otra canción
		self.delete_all()

	#Función que reproduce la canción creada
	def play_archive(self, archive, name):
		archive_song = open(archive, "r")
		validate_song = archive_song.readline()
		if validate_song == "This is a song\n":
			all_notes = archive_song.readlines()
			for i in range(len(all_notes)):
				if i % 2 == 0:
					note_frecuency.append(float(all_notes[i]))
				else:
					time_note.append(int(all_notes[i]))
					time_sleep.append(int(all_notes[i])/1000)
			return True, "Reproduciendo " + name + ", favor espere"
		else:
			return False, "Erro en el archivo " + name
	
#Fin del script