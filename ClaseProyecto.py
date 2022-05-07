class Proyecto:

    __idProyecto = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0

    def __init__(self, idProyecto='', titulo='', palabrasClave='', puntaje = 0):
        self.__idProyecto = idProyecto
        self.__titulo = titulo
        self.__palabrasClave = palabrasClave
        self.__puntaje = puntaje

    def __str__(self):
        return "{:5}   {:70}    {:40}   {}\n".format(self.__idProyecto, self.__titulo, self.__palabrasClave,
                                                     self.__puntaje)

    def __gt__(self, other):
        return self.__puntaje > other.__puntaje

    def getIdProyecto(self):
        return self.__idProyecto

    def getTitulo(self):
        return self.__titulo

    def getPalabrasClave(self):
        return self.__palabrasClave

    def setPuntaje(self, puntos):
        self.__puntaje = puntos

    def getPuntaje(self):
        return self.__puntaje

    def calcularPuntaje(self, mi):
        self.__puntaje = self.contarIntegrantes(mi) + self.contarDirector(mi) + \
                         self.contarCodirector(mi) + self.contarRol(mi)
        return self.__puntaje

    def contarIntegrantes(self, mi):
        cant = 0
        for i in range(0, mi.obtenerLongitud()):
            unIntegrante = mi.obtenerIntegrante(i)
            if self.__idProyecto == unIntegrante.getIdProyecto() and unIntegrante.getRol() == 'integrante':
                cant += 1
        if cant >= 3:
            puntos = 10
        else:
            puntos = -20
        if puntos == -20:
            print('El Proyecto debe tener como mínimo 3 integrantes')
        return puntos

    def contarDirector(self, mi):
        puntos = 0
        for i in range(0, mi.obtenerLongitud()):
            unIntegrante = mi.obtenerIntegrante(i)
            if self.__idProyecto == unIntegrante.getIdProyecto():
                if unIntegrante.getRol() == 'director':
                    if unIntegrante.getCategoria() == 'I' or unIntegrante.getCategoria() == 'II':
                        puntos = 10
                    else:
                        puntos = -5
        if puntos == -5:
            print('El Director del Proyecto debe tener categoría I o II')
        return puntos

    def contarCodirector(self, mi):
        puntos = 0
        for i in range(0, mi.obtenerLongitud()):
            unIntegrante = mi.obtenerIntegrante(i)
            if self.__idProyecto == unIntegrante.getIdProyecto():
                if unIntegrante.getRol() == 'codirector':
                    if unIntegrante.getCategoria() == 'I' \
                            or unIntegrante.getCategoria() == 'II' or unIntegrante.getCategoria() == 'III':
                        puntos = 10
                    else:
                        puntos = -5
        if puntos == -5:
            print('El Codirector del Proyecto debe tener como mínimo categoría III')
        return puntos

    def contarRol(self, mi):
        puntos = 0
        for i in range(0, mi.obtenerLongitud()):
            unIntegrante = mi.obtenerIntegrante(i)
            if self.__idProyecto == unIntegrante.getIdProyecto():
                if unIntegrante.getRol() != 'director':
                    if unIntegrante.getRol() != 'codirector':
                        if unIntegrante.getRol() != 'integrante':
                            puntos = -10
        if puntos == -10:
            print('El Proyecto debe tener un Director')
            print('El Proyecto debe tener un CoDirector')
        return puntos
