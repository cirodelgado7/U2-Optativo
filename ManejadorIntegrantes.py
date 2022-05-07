import csv
from ClaseIntegrante import Integrante


class ManejadorInt:

    __listaIntegrantes = []

    def __init__(self):
        self.__listaIntegrantes = []

    def __str__(self):
        s = ""
        for lista in self.__listaIntegrantes:
            s += str(lista) + '\n'
        return s

    def cargarIntegrantes(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                idProyecto = fila[0]
                apellidoNombre = fila[1]
                dni = fila[2]
                categoriaInvestigacion = fila[3]
                rol = fila[4]
                unIntegrante = Integrante(idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol)
                self.agregarIntegrante(unIntegrante)
        self.ordenarIntegrantes()
        archivo.close()

    def agregarIntegrante(self, unIntegrante):
        self.__listaIntegrantes.append(unIntegrante)

    def buscarIntegrante(self, clave):
        for indice, Integrantes in enumerate(self.__listaIntegrantes):
            if Integrantes.obtenerIdentificador() == clave:
                return indice

    def obtenerIntegrante(self, indice):
        return self.__listaIntegrantes[indice]

    def ordenarIntegrantes(self):
        list.sort(self.__listaIntegrantes, key=lambda Integrantes: Integrantes.getIdProyecto())

    def obtenerLongitud(self):
        return len(self.__listaIntegrantes)
