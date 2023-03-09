"""
QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos. En este sentido el
sistema debe contar con la posibilidad de crear un  Curso, el cual tendrán un nombre, cantidad de alumnos,
un estado y cantidad de clases.
El sistema debe poder dar de alta un Curso.
El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)
El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar
toda la información del curso.
"""
import json

availableCourses = []
def altaCurso():
    # Inicializando detalles del curso
    numberOfStudents = None
    numberOfLessons = None

    courseName = input("Nombre del curso: ")
    while numberOfStudents == None or numberOfStudents < 0:
        numberOfStudents = int(input("Alumnos inscritos: "))
        if numberOfStudents < 0:
            print("Ingrese un número valido")
    while numberOfLessons == None or numberOfLessons <= 0:
        numberOfLessons = int(input("Cuantas clases tiene el curso? "))
        if numberOfLessons <= 0:
            print("Ingrese un número valido")
    courseActive = input("El curso ya empezó? Responda con s/n en minusculas ").lower().strip() == 's'

    #Creando diccionario del curso
    newCourse = {
        "NombreDelCurso": courseName,
        "EstudiantesInscritos": numberOfStudents,
        "Lecciones": numberOfLessons,
        "CursoActivo": courseActive
    }
    return newCourse

def verTodosCursos():
    for course in availableCourses:
        pretty = json.dumps(course, indent=4, sort_keys=False)
        print(pretty)
def verCurso(nombrecurso):
    for course in availableCourses:
        tmpname = course.get('NombreDelCurso')
        if tmpname == nombrecurso:
            pretty = json.dumps(course, indent=4, sort_keys=False)
            print(pretty)
        else:
            continue
    else:
        print("El curso no existe")

def editarCurso(nombrecurso):
    for course in availableCourses:
        tmpname = course.get("NombreDelCurso")
        if tmpname == nombrecurso:
            numberOfStudents = course.get("EstudiantesInscritos")
            numberOfLessons = course.get("Lecciones")
            courseActive = course.get("CursoActivo")

            # Ingresando nuevos datos
            courseName = input("Nuevo nombre del curso: ")
            numberOfStudents = int(input("Alumnos inscritos: "))
            numberOfLessons = int(input("Cuantas clases tiene el curso? "))
            courseActive = input("El curso ya empezó? Responda con s/n en minusculas ").lower().strip() == 's'

            # Creando nuevo diccionario del curso editado
            editedcourse = {
                "NombreDelCurso": courseName,
                "EstudiantesInscritos": numberOfStudents,
                "Lecciones": numberOfLessons,
                "CursoActivo": courseActive
            }
            course.update(editedcourse)
            print(course)
        else:
            continue



    #############################################################################

numberOfNewCourses = 0
while numberOfNewCourses <= 0:
    numberOfNewCourses = int(input("Cuantos cursos desea agregar?"))
    if numberOfNewCourses <= 0:
        print("Ingrese un numero valido")

while numberOfNewCourses > 0:
    print("Registrar nuevo curso\n")
    availableCourses.append(altaCurso())
    numberOfNewCourses -= 1

print("*"*50)
print("\n")
#verTodosCursos()
#cursoaver = input("Cuál curso quiere ver? ")
#verCurso(nombredelcurso)
cursoaeditar = input("Cuál curso quiere editar? ")
editarCurso(cursoaeditar)