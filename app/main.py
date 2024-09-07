from clases import Ventana, Nave, Aluminio, Vidrio, Cotizacion

def main():
    # Crear instancias de Aluminio y Vidrio
    aluminio_pulido = Aluminio(acabado="Pulido", precio_por_metro_lineal=50700)
    vidrio_transparente = Vidrio(tipo="Transparente", precio_por_cm2=8.25)
    
    # Crear una instancia de Ventana
    ventana = Ventana(ancho=120, alto=90, estilo="XOX")
    
    # Añadir naves a la ventana
    nave1 = Nave(tipo="X", ancho=40, alto=90)
    nave2 = Nave(tipo="O", ancho=40, alto=90)
    nave3 = Nave(tipo="X", ancho=40, alto=90)
    
    ventana.naves.append(nave1)
    ventana.naves.append(nave2)
    ventana.naves.append(nave3)
    
    # Calcular el costo de la ventana
    costo_ventana = ventana.calcular_costo()
    print(f"Costo de la ventana: {costo_ventana}")
    
    # Crear una instancia de Cotizacion
    cotizacion = Cotizacion(ventana=ventana, cantidad=120, descuento=0.10)
    
    # Calcular el total de la cotización
    total_cotizacion = cotizacion.calcular_total()
    print(f"Total de la cotización: {total_cotizacion}")

if __name__ == "__main__":
    main()
