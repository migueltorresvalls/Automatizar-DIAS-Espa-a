from declaracion import Declaracion

# Parsea la respuesta recibida de la IA, creando un array de objetos del tipo Declaracion

class Respuesta: 
    def __init__(self, fecha, ruta_pdf, respuesta):
        # fecha publicación, tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion
        atributos = respuesta.split("\n")
        for i in range(len(atributos)):
            campos = atributos[i].split(":")
            if len(campos)>1:
                # La fecha que aparece en el documento es la de publicación, no la de resolución
                if i == 0: 
                    resolucion = campos[1]
                elif i == 1:
                    proyecto = campos[1]
                elif i == 2: 
                    tecnologia = campos[1]
                elif i == 3: 
                    hibridacion = campos[1]
                elif i == 4: 
                    size = campos[1].replace(",",".")
                elif i == 5: 
                    capacidad = campos[1].replace(",",".")
                elif i == 6: 
                    spv = campos[1]
                elif i == 7: 
                    sociedad = campos[1]
                elif i == 8: 
                    ubicacion = campos[1]
                elif i == 9: 
                    resultado = campos[1]
                elif i == 10: 
                    motivos = campos[1]

        self.declaracion = Declaracion(fecha, resolucion, proyecto, tecnologia, hibridacion, size, capacidad, spv, sociedad, ubicacion, resultado, motivos, ruta_pdf)