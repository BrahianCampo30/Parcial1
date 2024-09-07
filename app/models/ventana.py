class Ventana:
    def __init__(self, ancho, alto, estilo):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.naves = []

    def calcular_costo(self):
        costo_aluminio = self.calcular_costo_aluminio()
        costo_vidrio = self.calcular_costo_vidrio()
        return costo_aluminio + costo_vidrio

    def calcular_area_total(self):
        return self.ancho * self.alto

    def calcular_costo_aluminio(self):
        # Implementación del cálculo del costo del aluminio
        pass

    def calcular_costo_vidrio(self):
        # Implementación del cálculo del costo del vidrio
        pass