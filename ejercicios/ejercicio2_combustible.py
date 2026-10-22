"""
Ejercicio 2. Consumo de combustible

ESPECIFICACIÓN
==============

PROBLEMA
    Calcular el rendimiento de combustible (km/L) de un vehículo y el costo
    total del combustible consumido en un recorrido.

ENTRADAS
    - distancia: float, kilómetros (km), mayor que 0.
    - litros: float, litros (L), mayor que 0.

SALIDAS (tabla con tabulate)
    - Distancia recorrida (km, 2 decimales).
    - Litros consumidos (L, 2 decimales).
    - Precio por litro (MXN, 2 decimales).
    - Rendimiento del vehículo (km/L, 2 decimales).
    - Costo total del combustible (MXN, 2 decimales).
    - Frase identificadora: "Resultado del consumo de combustible del recorrido".

REGLAS Y SUPUESTOS
    - Precio por litro fijo: $24.00 MXN.
    - distancia > 0 y litros > 0; si no, se vuelve a pedir el dato.
    - rendimiento = distancia / litros.
    - costo = litros * precio por litro.
    - Redondeo: a 2 decimales solo al mostrar; los cálculos usan el valor completo.
    - Los montos se muestran en pesos mexicanos con el formato "$0.00".

ALGORITMO
    1. Leer distancia (km) y validar que sea un número > 0.
    2. Leer litros (L) y validar que sea un número > 0.
    3. rendimiento = distancia / litros.
    4. costo = litros * 24.00.
    5. Mostrar distancia, litros, precio por litro, rendimiento y costo con tabulate.

CASOS DE PRUEBA (calculados manualmente)
    Caso | Distancia | Litros | Rendimiento | Costo total
    -----|-----------|--------|-------------|------------
      1  |  120 km   |   10   | 12.00 km/L  |  $240.00
      2  |  250 km   |   20   | 12.50 km/L  |  $480.00
      3  |  180 km   |   15   | 12.00 km/L  |  $360.00
      4  |  300 km   |   25   | 12.00 km/L  |  $600.00

RESTRICCIONES PARA EL AGENTE
    - Usar solo la biblioteca estándar de Python y tabulate (única externa).
    - Respetar nombres, parámetros y retornos del contrato de funciones.
    - Validar la entrada con ciclo y manejo de ValueError.
    - Los cálculos no imprimen; solo mostrarResultados imprime.
    - Constantes en MAYÚSCULAS; sin variables globales mutables.

CONTRATO DE FUNCIONES
    leerDatos() -> tuple[float, float]
        Pide distancia y litros por teclado; retorna (distancia, litros),
        ambos > 0.
    calcularRendimiento(distancia: float, litros: float) -> float
        Retorna distancia / litros (km/L).
    calcularCosto(litros: float) -> float
        Retorna litros * PRECIO_LITRO.
    mostrarResultados(distancia: float, litros: float, rendimiento: float,
                      costo: float) -> None
        Muestra la tabla de resultados con tabulate.
"""

from tabulate import tabulate

PRECIO_LITRO = 24.00


def _leerPositivo(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            valor = float(texto)
        except ValueError:
            print("Error: escribe un número válido.")
            continue
        if valor <= 0:
            print("Error: el valor debe ser mayor que cero.")
            continue
        return valor


def leerDatos():
    distancia = _leerPositivo("Distancia recorrida (km): ")
    litros = _leerPositivo("Litros consumidos: ")
    return distancia, litros


def calcularRendimiento(distancia, litros):
    return distancia / litros


def calcularCosto(litros):
    return litros * PRECIO_LITRO


def mostrarResultados(distancia, litros, rendimiento, costo):
    filas = [
        ["Distancia recorrida", f"{distancia:,.2f} km"],
        ["Litros consumidos", f"{litros:,.2f} L"],
        ["Precio por litro", f"${PRECIO_LITRO:,.2f}"],
        ["Rendimiento del vehículo", f"{rendimiento:,.2f} km/L"],
        ["Costo total del combustible", f"${costo:,.2f}"],
    ]
    print("\nResultado del consumo de combustible del recorrido")
    print(tabulate(filas, headers=["Concepto", "Valor"], tablefmt="grid",
                   colalign=("left", "right")))
