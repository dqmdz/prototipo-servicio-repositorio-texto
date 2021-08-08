from alumno import Alumno
from alumnoRepository import AlumnoRepository


class AlumnoService:

    def __init__(self):
        self.repository = AlumnoRepository()

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, value: AlumnoRepository):
        self.__repository = value

    def findAll(self):
        return self.repository.findAll()

    def findByAlumnoId(self, alumnoId: int):
        try:
            return self.repository.findByAlumnoId(alumnoId)
        except KeyError as err:
            print(err)

    def add(self, alumno: Alumno):
        return self.repository.save(alumno)

    def update(self, newAlumno: Alumno, alumnoId: int):
        try:
            alumno = self.repository.findByAlumnoId(alumnoId)
            return self.repository.save(Alumno(alumno.alumnoId, newAlumno.nombre, newAlumno.apellido))
        except KeyError as err:
            print(err)

    def deleteByAlumnoId(self, alumnoId: int):
        try:
            self.repository.findByAlumnoId(alumnoId)
            self.repository.deleteByAlumnoId(alumnoId)
        except KeyError as err:
            print(err)

    def flush(self):
        self.repository.write()


if __name__ == '__main__':
    service = AlumnoService()
    print(service.findAll())
    alumno = service.add(Alumno(nombre='Juan', apellido='Garcia'))
    print(service.findAll())
    alumno = service.findByAlumnoId(1)
    alumno = service.update(
        Alumno(alumno.alumnoId, 'Ana', 'Flores'), alumno.alumnoId)
    print(service.findAll())
    service.flush()
