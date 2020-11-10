from modelo import ClassDatos
import xlrd

import matplotlib.pyplot as plt

class Modelo:

    def __init__(self, path):
        self.personas = []
        self.cargar(path)

    def cargar(self, path):
        open = xlrd.open_workbook(path)

        sheet = open.sheet_by_index(0)

        posx = posy = 0

        while not 1 in sheet.row_types(posx, 0):
            posx += 1

        while not 1 in sheet.col_types(posy, 0):
            posy += 1

        for i in range(posx + 1, sheet.nrows):
            if sheet.row_values(i, posy)[0]:
                self.personas += [ClassDatos.datos(sheet.row_values(i, posy))]

    def menu(self, opcion):

        if opcion == "1":
            self.mostrar()
        elif opcion == "2":
            self.promedioEntrada()
        elif opcion == "3":
            self.promedioSalida()
        elif opcion == "4":
            self.promedioGeneral()
        elif opcion == "5":
            print("ingrese el id")
            print(self.promedioPorPersona(str(input())))
        elif opcion == "6":
            self.temperaturaMasAltaEntrada()
        elif opcion == "7":
            self.temperaturaMasAltaSalida()
        elif opcion == "8":
            self.graficaPorFechas()
        elif opcion == "9":
            print("ingrese la fecha")
            self.graficoPorPersonasFecha(str(input()))

    def mostrar(self):
        for persona in self.personas:
            print(persona._id, " ", persona._nombre, " ", persona._apellido)

    def promedioEntrada(self):
        promedio = 0
        for persona in self.personas:
            promedio += persona._tempEntrada

        promedio = promedio / len(self.personas)

        print(promedio)

    def promedioSalida(self):
        promedio = 0
        for persona in self.personas:
            promedio += persona._tempSalida

        promedio = promedio / len(self.personas)

        print(promedio)

    def promedioGeneral(self):
        promedio = 0
        for persona in self.personas:
            promedio += ((persona._tempSalida + persona._tempEntrada)/2)

        promedio = promedio / len(self.personas)
        print(promedio)

    def promedioPorPersona(self, id):
        promedio = 0
        cant = 0
        for persona in self.personas:
            if persona._id == int(id):
                promedio += persona._tempEntrada
                cant +=1
        promedio = promedio / cant
        return promedio

    def temperaturaMasAltaEntrada(self):
        todos = [{
            "id": 0,
            "name": "",
            "last": "",
            "temp": 0,
            "date": ""}]

        for persona in self.personas:
            alta = {
                "id": persona._id,
                "name": persona._nombre,
                "last": persona._apellido,
                "temp": persona._tempEntrada,
                "date": persona._fecha
            }
            if persona._tempEntrada > todos[0]['temp']:
                todos = [alta]
            elif persona._tempEntrada == todos[0]['temp']:
                todos += [alta]

        print(todos)

    def temperaturaMasAltaSalida(self):
        todos = [{
            "id": 0,
            "name": "",
            "last": "",
            "temp": 0,
            "date": "" }]

        for persona in self.personas:
            alta = {
                "id": persona._id,
                "name": persona._nombre,
                "last": persona._apellido,
                "temp": persona._tempSalida,
                "date": persona._fecha
            }
            if persona._tempSalida>todos[0]['temp']:
                todos = [alta]
            elif persona._tempSalida==todos[0]['temp']:
                todos += [alta]

        print(todos)

    def graficaPorFechas(self):

        dataFecha = {}
        temp = 0
        cont = 1
        fecha = ""

        for persona in self.personas:
            if persona._fecha != fecha and cont >1:
                temp = 0
                cont = 1
            fecha = persona._fecha
            temp += persona._tempEntrada
            dataFecha[persona._fecha] = temp / cont
            cont +=1

        if not dataFecha:
            dataFecha[persona._fecha] = temp / cont

        self.grafica(dataFecha)

    def graficoPorPersonasFecha(self,fecha):

        datosPersonas = {}

        for persona in self.personas:
            if persona._fecha == fecha:
                datosPersonas[persona._nombre] = persona._tempEntrada

        if not datosPersonas:
            print("Fecha no encontrada")
        else:
            self.grafica(datosPersonas)

    def grafica(self, dataFecha):

        names = list(dataFecha.keys())
        values = list(dataFecha.values())

        fig, axs = plt.subplots(1, figsize=(0.7*len(dataFecha), 3), sharey=True)
        axs.bar(names, values)
        axs.set_ylim(34, 38)
        fig.suptitle('Categorical Plotting')
        plt.show()

