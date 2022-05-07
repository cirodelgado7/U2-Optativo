class Integrante:

    __idProyecto = ''
    __apellidoNombre = ''
    __dni = ''
    __categoriaInvestigacion = ''
    __rol = ''

    def __init__(self, idProyecto, apellidNombre, dni, categoriaInvestigacion, rol):
        self.__idProyecto = idProyecto
        self.__apellidoNombre = apellidNombre
        self.__dni = dni
        self.__categoriaInvestigacion = categoriaInvestigacion
        self.__rol = rol

    def __str__(self):
        return " %s   %20s   %10s   %5s   %15s " % (
            self.__idProyecto, self.__apellidoNombre, self.__dni, self.__categoriaInvestigacion, self.__rol)

    def getIdProyecto(self):
        return self.__idProyecto

    def getApellidoNombre(self):
        return self.__apellidoNombre

    def getDNI(self):
        return self.__dni

    def getCategoria(self):
        return self.__categoriaInvestigacion

    def getRol(self):
        return self.__rol
