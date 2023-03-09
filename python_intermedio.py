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
    print("\n")
    return newCourse

def verTodosCursos():
    print("Estos son los cursos disponibles\n")
    for course in availableCourses:
        pretty = json.dumps(course, indent=4, sort_keys=False)
        print(pretty)

def verCurso():
    cursoaver = input("Cuál curso quiere ver? ")
    for course in availableCourses:
        tmpname = course.get('NombreDelCurso')
        if tmpname == cursoaver:
            pretty = json.dumps(course, indent=4, sort_keys=False)
            print(pretty)
        else:
            continue

def editarCurso():
    cursoaeditar = input("Cuál curso quiere editar? ")
    for course in availableCourses:
        tmpname = course.get("NombreDelCurso")
        if tmpname == cursoaeditar:
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
            pretty = json.dumps(course, indent=4, sort_keys=False)
            print(pretty)
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


verTodosCursos()
verCurso()
editarCurso()