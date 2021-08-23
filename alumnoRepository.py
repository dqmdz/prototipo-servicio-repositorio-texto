from alumno import Alumno


class AlumnoRepository:

    def __init__(self):
        self.alumnos = {}
        self.alumnoId = 0
        self.read()

    def findAll(self):
        return list(self.alumnos.values())

    def findByAlumnoId(self, alumnoId: int):
        if not alumnoId in self.alumnos:
            raise KeyError('Clave Inexistente')
        return self.alumnos[alumnoId]

    def save(self, alumno: Alumno):
        print('Antes {}'.format(alumno))
        if alumno.alumnoId is None:
            self.alumnoId += 1
            alumno.alumnoId = self.alumnoId
        self.alumnos[alumno.alumnoId] = alumno
        print('Después {}'.format(alumno))
        return self.alumnos[alumno.alumnoId]

    def deleteByAlumnoId(self, alumnoId: int):
        if not alumnoId in self.alumnos:
            raise KeyError('Clave Inexistente')
        self.alumnos.pop(alumnoId)

    def read(self):
        with open('alumno.txt', 'r') as file:
            for line in file.readlines():
                elements = line[:-1].split(';;')
                self.alumnos[int(elements[0])] = Alumno(
                    elements[0], elements[1], elements[2])
                self.alumnoId = int(elements[0])

    def write(self):
        with open('alumno.txt', 'w') as file:
            for alumno in self.alumnos.values():
                file.write('{};;{};;{}\n'.format(
                    alumno.alumnoId, alumno.nombre, alumno.apellido))


if __name__ == '__main__':
    repository = AlumnoRepository()
    print(repository.findAll())
    alumno = repository.save(Alumno(nombre='Juan', apellido='Garcia'))
    print(repository.findAll())
    print(repository.findByAlumnoId(1))
    repository.write()
