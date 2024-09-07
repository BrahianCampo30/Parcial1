class Cotizacion:
    def __init__(self, ventana, cantidad, descuento=0):
        self.ventana = ventana
        self.cantidad = cantidad
        self.descuento = descuento

    def calcular_total(self):
        costo_unitario = self.ventana.calcular_costo()
        total = costo_unitario * self.cantidad
        return self.aplicar_descuento(total)

    def aplicar_descuento(self, total):
        if self.cantidad > 100:
            return total * (1 - self.descuento)
        return total