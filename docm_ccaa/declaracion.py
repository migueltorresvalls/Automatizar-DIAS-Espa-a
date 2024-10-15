# Clase que agrupa todos los valores de una declaracion

class Declaracion:
    def __init__(self, fecha, resolucion, proyecto, tecnologia, hibridacion, size, capacidad, spv, sociedad, ubicacion, resultado, motivacion, ruta):
        self.fecha = fecha
        self.resolucion = resolucion
        self.proyecto = proyecto
        self.tecnologia = tecnologia
        self.hibridacion = hibridacion
        self.size = size
        self.capacidad = capacidad
        self.spv = spv
        self.sociedad = sociedad
        self.ubicacion = ubicacion
        self.resultado = resultado
        self.motivacion = motivacion
        self.ruta = ruta
    
    # Crea una lista con los valores de la fila que luego se añadiran al excel
    def to_excel(self):
        fila = [self.fecha, self.resolucion, self.proyecto, self.tecnologia, self.hibridacion, float(self.size), float(self.capacidad), self.spv, self.sociedad, self.ubicacion, self.resultado, self.motivacion, self.ruta]

        return fila

    # Sobreescribir método == de python. No tocar
    def __eq__(self, resp): 
        if self.ruta == resp.ruta: 
            return True
        return False

    # Sobreescribe el metodo print de python. 
    def __str__(self):
        return f"fecha={self.fecha}, resolucion={self.resolucion}, proyecto={self.proyecto}, tecnologia={self.tecnologia}, hibridacion={self.hibridacion}, tamaño={self.size}, capacidad={self.capacidad}, spv={self.spv}, sociedad={self.sociedad}, ubicacion={self.ubicacion}, resultado={self.resultado}, motivos={self.motivacion}, ruta={self.ruta}"

