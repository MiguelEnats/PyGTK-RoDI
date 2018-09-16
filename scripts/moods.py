from scripts import rodi

robot = rodi.RoDI()

#Leemos el valor de los sensores
def sensors():

	sensor = robot.sense()
	estado1 = sensor[0]
	estado2 = sensor[1]
	enemy = robot.see()

	#Retornamos los valores recogidos por los sensores
	return estado1, estado2, enemy

class moods:

	#Función para poner en modo seguidor de línea
	def line_follower(self, n_curves):
		#Ponemos la cantidad de curvas recorridas en cero y aumentará cada vez que el rodi gire

		curve = 0
		#Cada vez que el robot detecte que la línea negra tiene un curva, esta girará hacia ese sentido
		#Y después de girar deberá volver a verificar la línea para verificar si está recorriendo bien
		
		while curve <=n_curves:
			estado1, estado2, enemy = sensors()
			if estado1 > 511 and estado2 > 511:
				robot.move(-100, -100)
				estado1, estado2, enemy = sensors()
			elif estado1 < 511 and estado2 > 511:
				curve+=1
				robot.move(100, 25)
				estado1, estado2, enemy = sensors()
			elif estado1 > 511 and estado2 < 511:
				curve+=1
				robot.move(25, 100)
				estado1, estado2, enemy = sensors()
			elif estado1 < 511 and estado2 > 511:
				robot.move(100, 100)
				estado1, estado2, enemy = sensors()

		#Detenemos al rodi luego de completar las curvas
		robot.move(0, 0)


	#Función para el sumo, no hay necesidad de explicar esta parte de código
	def sumo(self):
		
		estado1, estado2, enemy = sensors()
		while True:
			if estado1 < 100 and estado2 < 100:
				if enemy == 1:
					robot.move_backward()
					sleep(0.5)
					robot.move_forward()
					estado1, estado2, enemy = sensors()
				elif enemy < 20:
					robot.move_forward()
					estado1, estado2, enemy = sensors()
				else:
					robot.move_right()
					estado1, estado2, enemy = sensors()
			elif estado1 > 100 and estado2 < 100:
				robot.move_right()
				estado1, estado2, enemy = sensors()
			elif estado1 < 100 and estado2 > 100:
				robot.move_left()
				estado1, estado2, enemy = sensors()
			else:
				robot.move_right()
				estado1, estado2, enemy = sensors()
	
	#Función para pelea de sumo sin reglas de dojo
	def callejera(self):

		estado1, estado2, enemy = sensors()
		while True:
			if enemy < 20:
				robot.move_forward()
				estado1, estado2, enemy = sensors()
			elif enemy == 1:
				robot.move_backward()
				sleep(0.5)
				robot.move_forward()
				estado1, estado2, enemy = sensors()
			else:
				robot.move_right()
				estado1, estado2, enemy = sensors()

#Fin del script