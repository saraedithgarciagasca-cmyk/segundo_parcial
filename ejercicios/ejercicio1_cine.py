"""
Ejercicio 1. Venta de boletos de cine

ESPECIFICACIÓN
==============

PROBLEMA
    Determinar el importe a pagar por una compra de boletos de cine, aplicando
    un 10% de descuento cuando se compran 4 boletos o más.

ENTRADAS
    - cantidad: int, boletos, entero mayor que 0 (cantidad >= 1).

SALIDAS (tabla con tabulate)
    - Cantidad de boletos adquiridos (int).
    - Precio unitario del boleto (MXN, 2 decimales).
    - Subtotal de la compra (MXN, 2 decimales).
    - Descuento aplicado (MXN, 2 decimales).
    - Total a pagar (MXN, 2 decimales).
    - Frase identificadora: "Resultado de la compra de boletos de cine".

REGLAS Y SUPUESTOS
    - Precio unitario fijo: $75.00 MXN.
    - Descuento del 10% sobre el subtotal si cantidad >= 4 (4 sí aplica).
    - Si cantidad < 4 (1, 2 o 3) el descuento es $0.00.
    - La cantidad debe ser un entero > 0; si no, se vuelve a pedir el dato.
    - Redondeo: a 2 decimales solo al mostrar (formato "$0.00").
    - Total = subtotal - descuento.

ALGORITMO
    1. Leer la cantidad de boletos y validar que sea un entero mayor que 0.
    2. subtotal = cantidad * 75.00.
    3. Si cantidad >= 4: descuento = subtotal * 0.10; si no, descuento = 0.
    4. total = subtotal - descuento.
    5. Mostrar cantidad, precio unitario, subtotal, descuento y total con tabulate.

CASOS DE PRUEBA (calculados manualmente)
    Caso | Boletos | Subtotal | Descuento | Total
    -----|---------|----------|-----------|--------
      1  |    1    |  $75.00  |   $0.00   |  $75.00
      2  |    3    | $225.00  |   $0.00   | $225.00
      3  |    4    | $300.00  |  $30.00   | $270.00
      4  |    6    | $450.00  |  $45.00   | $405.00

RESTRICCIONES PARA EL AGENTE
    - Usar solo la biblioteca estándar de Python y tabulate (única externa).
    - Respetar nombres, parámetros y retornos del contrato de funciones.
    - No usar variables globales mutables; las constantes van en MAYÚSCULAS.
    - Validar la entrada con ciclo y manejo de ValueError.
    - Los cálculos no imprimen; solo mostrarCompra imprime.

CONTRATO DE FUNCIONES
    leerCantidad() -> int
        Pide la cantidad por teclado hasta recibir un entero > 0.
    calcularSubtotal(cantidad: int) -> float
        Retorna cantidad * PRECIO_BOLETO.
    calcularDescuento(subtotal: float, cantidad: int) -> float
        Retorna 10% del subtotal si cantidad >= 4; en otro caso 0.0.
    mostrarCompra(cantidad: int, subtotal: float, descuento: float) -> None
        Calcula el total (subtotal - descuento) y muestra la tabla.
"""

from tabulate import tabulate

PRECIO_BOLETO = 75.00
MINIMO_PARA_DESCUENTO = 4
PORCENTAJE_DESCUENTO = 0.10


def leerCantidad():
    while True:
        texto = input("Cantidad de boletos a comprar: ").strip()
        try:
            cantidad = int(texto)
        except ValueError:
            print("Error: escribe un número entero.")
            continue
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            continue
        return cantidad


def calcularSubtotal(cantidad):
    return cantidad * PRECIO_BOLETO


def calcularDescuento(subtotal, cantidad):
    if cantidad >= MINIMO_PARA_DESCUENTO:
        return subtotal * PORCENTAJE_DESCUENTO
    return 0.0


def mostrarCompra(cantidad, subtotal, descuento):
    total = subtotal - descuento
    filas = [
        ["Cantidad de boletos", cantidad],
        ["Precio unitario", f"${PRECIO_BOLETO:,.2f}"],
        ["Subtotal", f"${subtotal:,.2f}"],
        ["Descuento aplicado", f"${descuento:,.2f}"],
        ["Total a pagar", f"${total:,.2f}"],
    ]
    print("\nResultado de la compra de boletos de cine")
    print(tabulate(filas, headers=["Concepto", "Valor"], tablefmt="grid",
                   colalign=("left", "right")))
