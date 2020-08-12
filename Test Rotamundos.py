class Alumno:
	def __init__(self, nombre, edad, tarea1, tarea2, tarea3, tarea4, examen1, examen2, examen3):
		self.nombre = nombre
		self.edad = edad
		self.tareas = [tarea1, tarea2, tarea3, tarea4]
		self.examenes = [examen1, examen2, examen3]

class Grupo:
	def __init__(self):
		self.alumnos = []

	def agregarAlumno(self, alumno):
		self.alumnos.append(alumno)

	def score(self, nombre):
		i = 0
		studentFound = False;

		for x in self.alumnos:
			if(nombre == x.nombre):
				index = i
				studentFound = True
				break
			i+=1

		if(studentFound == True):
			promedio = (sum(self.alumnos[index].tareas)/len(self.alumnos[index].tareas)*0.20 + sum(self.alumnos[index].examenes)/len(self.alumnos[index].examenes)*0.80)/10
			#En caso de querer el valor del promedio a dos digitos y a un decimal, descomentar la línea siguiente y comentar la línea anterior.
			#promedio = sum(self.alumnos[index].tareas)/len(self.alumnos[index].tareas)*0.20 + sum(self.alumnos[index].examenes)/len(self.alumnos[index].examenes)*0.80
			return round(promedio, 1)
		else:
			return "Alumno no encontrado."

	def score_group(self):
		promedios = []

		for x in self.alumnos:
			promedios.append(self.score(x.nombre))

		promedioTotal = sum(promedios)/len(self.alumnos)

		return round(promedioTotal, 1)

	def max_score(self):
		promedios = []

		for x in self.alumnos:
			promedios.append(self.score(x.nombre))

		maxScoreIndex = promedios.index(max(promedios))

		return self.alumnos[maxScoreIndex].nombre
		

Alumnos = []
Alumnos.append(Alumno("Raymundo", 25, 90.0, 95.0, 85.5, 100.0, 87.0, 92.5, 85.0))
Alumnos.append(Alumno("Aleja", 23, 72.0, 89.5, 95.0, 100.0, 90.0, 90.0, 85.0))
Alumnos.append(Alumno("Víctor", 28, 95.0, 80.0, 100.0, 0.0, 70.0, 85.0, 100.0))

Grupo = Grupo()

for x in Alumnos:
	Grupo.agregarAlumno(x)

print(Grupo.score("Raymundo"))
print(Grupo.score("Aleja"))
print(Grupo.score("Víctor"))
print(Grupo.score("Jorge"))

print(Grupo.score_group())

print(Grupo.max_score())