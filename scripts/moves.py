from scripts import rodi

robot = rodi.RoDI()

#Lista de las acciones que puede hacer el rodi
actions = ["Adelante izquierda", "Adelante", "Adelante derecha", "Izquierda", "Derecha", "Atrás izquierda", "Atrás", "Atrás derecha", "Detiene a RoDI"]

class moves:
	
	#Función para saber que acción realizar y con qué velocidad
	def find_action(self, tooltip, velocity):
		action = int
		for i in range(len(actions)):
			if tooltip == actions[i]:
				action = i+1
		if action == 1:
			self.left_up(velocity)
		elif action == 2:
			self.up(velocity)
		elif action == 3:
			self.right_up(velocity)
		elif action == 4:
			self.left(velocity)
		elif action == 5:
			self.right(velocity)
		elif action == 6:
			self.left_down(velocity)
		elif action == 7:
			self.down(velocity)
		elif action == 8:
			self.right_down(velocity)
		else:
			self.stop()

	#Función para ir adelante izquierda
	def left_up(self, velocity):
		vel_right = velocity
		vel_left = velocity / 2
		robot.move(vel_left, vel_right)

	#Función para ir adelante
	def up(self, velocity):
		vel_right = velocity
		vel_left = velocity
		robot.move(vel_left, vel_right)

	#Función para ir adelante derecha
	def right_up(self, velocity):
		vel_right = velocity / 2
		vel_left = velocity
		robot.move(vel_left, vel_right)

	#Función para ir a la izquierda
	def left(self, velocity):
		vel_right = 0
		vel_left = velocity
		robot.move(vel_left, vel_right)

	#Función para ir a la derecha
	def right(self, velocity):
		vel_right = velocity
		vel_left = 0
		robot.move(vel_left, vel_right)

	#Función para ir atrás izquierda
	def left_down(self, velocity):
		vel_right = velocity - velocity * 2
		vel_left = velocity - velocity * 1.5
		robot.move(vel_left, vel_right)

	#Función para ir atrás
	def down(self, velocity):
		vel_right = velocity - velocity * 2
		vel_left = velocity - velocity * 2
		robot.move(vel_left, vel_right)

	#Función para ir atrás derecha
	def right_down(self, velocity):
		vel_right = velocity - velocity * 1.5
		vel_left = velocity - velocity * 2
		robot.move(vel_left, vel_right)
	
	#Función para paras las acciones
	def stop(self):
		#Solo le enviamos una velocidad neutra a los motores para que no hagan nada
		robot.move(0, 0)

#Fin del script