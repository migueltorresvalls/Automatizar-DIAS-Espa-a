import pandas as pd

from declaracion import Declaracion

# Clase utilizada para leer y escribir los datos al excel

class Excel:
    def __init__(self, ruta):
        self.ruta = ruta
        self.data_frame = pd.read_excel(ruta)

    # Funcion que lee filas en el excel
    def leer_declaraciones(self):
        declaraciones = []

        for i in range(len(self.data_frame)):
            fecha = self.data_frame.iloc[(i,0)]
            resolucion = self.data_frame.iloc[(i,1)]
            proyecto = self.data_frame.iloc[(i,2)]
            tecnologia = self.data_frame.iloc[(i,3)]
            hibridacion = self.data_frame.iloc[(i,4)]
            size = self.data_frame.iloc[(i,5)]
            capacidad = self.data_frame.iloc[(i,6)]
            spv = self.data_frame.iloc[(i,7)]
            sociedad = self.data_frame.iloc[(i,8)]
            ubicacion = self.data_frame.iloc[(i,9)]
            resultado = self.data_frame.iloc[(i,10)]
            motivacion = self.data_frame.iloc[(i,11)]
            ruta = self.data_frame.iloc[(i,12)]

            declaracion = Declaracion(fecha, resolucion, proyecto, tecnologia, hibridacion, size, capacidad, spv, sociedad, ubicacion, resultado, motivacion, ruta)
            declaraciones.append(declaracion)

        return declaraciones

    # Escribe filas en el excel
    def escribir_declaraciones(self, declaraciones):
        # fecha publicación, tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion

        # Creamos columnas. Solo si el excel se empieza de cero y está vacío previamente
        # data_frame = pd.DataFrame(columns=['Fecha', 'Resolucion', 'Proyecto', 'Tecnologia', 'Hibridacion', 'Tamaño', 'Capacidad acceso', 'SPV', 'Sociedad', 'Ubicacion'])
        offset = len(self.data_frame)
        for i in range(len(declaraciones)): 
            # Añadimos una fila para cada declaración
            self.data_frame.loc[i+offset] = declaraciones[i].to_excel()

        self.data_frame.to_excel(self.ruta, index=False)