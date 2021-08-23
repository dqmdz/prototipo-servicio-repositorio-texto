class Alumno:

    def __init__(self, alumnoId=None, nombre='', apellido=''):
        self.alumnoId = alumnoId
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return '{} - {}, {}'.format(self.alumnoId, self.apellido, self.nombre)


if __name__ == '__main__':
    alumno = Alumno(nombre='Juan', apellido='Garcia')
    print(alumno)
