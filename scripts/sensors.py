from scripts import rodi
from time import sleep

robot = rodi.RoDI()

class sensors:
	
	#Función para encender el led rgb de varios colores
	def led_rgb(self, r, g, b):
		#Lo único que se hace acá es llamar a la función pixel del rodi
		robot.pixel(r, g, b)

	#Función para encender o apagar el led
	def led(self, state):
		#Agarra el valor del botón y decide si apagar o encender el led
		value = int
		if state:
			value = 1
		else:
			value = 0
		robot.led(value)

	#Función para medir las distancias entre un objeto y el rodi
	def see(self):
		#Llama a la función see para saber a que distancia está el objeto y almacena el resultado en 'distance'
		distance = robot.see()
		return distance

	#Función para medir lala intensidad de luz
	def light(self):
		#Llama a la función see para saber cuanta luz hay en el ambiente
		intensity = robot.light()
		light = int(intensity * 100 / 1023)
		return light

	#Función para reproducir una frecuencia
	def play_sing(self, frecuency, time):
		#Llamamos a la función para reproducir frecuencias
		duration = time * 1000
		robot.sing(frecuency, duration)
		sleep(time)

	#Función para los sensores de línea
	def sensores(self):
		values = robot.sense()
		sense_left = values[0]
		sense_right = values[1]
		return sense_left, sense_right

#Fin del script