class Alumno:

    def __init__(self, alumnoId=None, nombre='', apellido=''):
        self.alumnoId = alumnoId
        self.nombre = nombre
        self.apellido = apellido

    @property
    def alumnoId(self):
        return self.__alumnoId

    @alumnoId.setter
    def alumnoId(self, value):
        self.__alumnoId = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    def __repr__(self):
        return '{} - {}, {}'.format(self.alumnoId, self.apellido, self.nombre)


if __name__ == '__main__':
    alumno = Alumno(nombre='Juan', apellido='Garcia')
    print(alumno)
