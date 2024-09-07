class Nave:
    def __init__(self, tipo, ancho, alto):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_costo_vidrio(self):
        # Implementación del cálculo del costo del vidrio
        pass