# Proyecto de Cotización de Ventanas para la Compañía PQR

## Introducción

La compañía PQR, dedicada a la fabricación de ventanas en aluminio, ha identificado la necesidad de mejorar su proceso de cotizaciones, el cual actualmente es manual. Este proyecto tiene como objetivo desarrollar un programa que automatice y optimice dicho proceso.

## Objetivos del Proyecto

- **Automatizar el proceso de cotización**: Reducir el tiempo y los errores asociados con el cálculo manual de cotizaciones.
- **Actualizar precios y estilos**: Permitir la actualización de precios y la inclusión de nuevos estilos de ventanas.
- **Mejorar la precisión**: Asegurar que todas las cotizaciones sean precisas y reflejen los costos actuales de materiales y mano de obra.

## Requerimientos del Sistema

### Clases y Atributos

1. **Ventana**
   - **Atributos**:
     - `ancho`: float
     - `alto`: float
     - `estilo`: string
   - **Métodos**:
     - `calcularCosto()`: float
     - `calcularAreaTotal()`: float
     - `calcularCostoAluminio()`: float
     - `calcularCostoVidrio()`: float

2. **Nave**
   - **Atributos**:
     - `tipo`: string
     - `ancho`: float
     - `alto`: float
   - **Métodos**:
     - `calcularArea()`: float
     - `calcularCostoVidrio()`: float

3. **Aluminio**
   - **Atributos**:
     - `acabado`: string
     - `precioPorMetroLineal`: float
   - **Métodos**:
     - `calcularCosto()`: float

4. **Vidrio**
   - **Atributos**:
     - `tipo`: string
     - `precioPorCm2`: float
     - `esmerilado`: boolean
     - `costoEsmerilado`: float
   - **Métodos**:
     - `calcularCosto()`: float

5. **Cotizacion**
   - **Atributos**:
     - `ventana`: Ventana
     - `cantidad`: int
     - `descuento`: float
   - **Métodos**:
     - `calcularTotal()`: float
     - `aplicarDescuento()`: float

## Navegar al directorio del proyecto
```
cd Parcial1
```
## Crear entorno virtual
```
python -m venv venv
```
## Activar el Entorno Virtual
En Windows:
```
venv\Scripts\activate
```
En macOS y Linux:
```
source venv/bin/activate
```
## Instalar Dependencias
```
pip install -r requirements.txt
```
## Ejecución del Proyecto
```
python nombre_del_script.py
```
## Uso del Proyecto
Configuración Inicial: Asegúrate de que todos los requisitos están instalados y el entorno virtual está activado.

Ejecutar el Programa: Ejecuta el script principal usando el comando indicado en la sección de Ejecución del Proyecto.

Realizar Cotizaciones: Sigue las instrucciones en pantalla para ingresar los detalles de las ventanas y generar cotizaciones.
