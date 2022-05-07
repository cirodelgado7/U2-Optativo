import csv
from ClaseProyecto import Proyecto


class ManejadorPro:

    __listaProyectos = []

    def __init__(self):
        self.__listaProyectos = []

    def __str__(self):
        s = ""
        for lista in self.__listaProyectos:
            s += str(lista) + '\n'
        return s

    def cargarProyectos(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                idProyecto = fila[0]
                titulo = fila[1]
                palabrasClave = fila[2]
                unProyecto = Proyecto(idProyecto, titulo, palabrasClave, 0)
                self.agregarProyecto(unProyecto)
        archivo.close()

    def agregarProyecto(self, unProyecto):
        self.__listaProyectos.append(unProyecto)

    def modificarPuntaje(self, mi):
        self.cargarProyectos()
        for p in self.__listaProyectos:
            p.setPuntaje(p.calcularPuntaje(mi))
        self.__listaProyectos.sort()