class Vidrio:
    def __init__(self, tipo, precio_por_cm2, esmerilado=False, costo_esmerilado=0):
        self.tipo = tipo
        self.precio_por_cm2 = precio_por_cm2
        self.esmerilado = esmerilado
        self.costo_esmerilado = costo_esmerilado

    def calcular_costo(self, area):
        costo = self.precio_por_cm2 * area
        if self.esmerilado:
            costo += self.costo_esmerilado * area
        return costo