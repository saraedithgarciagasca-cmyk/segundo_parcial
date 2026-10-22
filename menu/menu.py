from ejercicios.ejercicio1_cine import (
    leerCantidad,
    calcularSubtotal,
    calcularDescuento,
    mostrarCompra,
)


from ejercicios.ejercicio2_combustible import (
    leerDatos,
    calcularRendimiento,
    calcularCosto,
    mostrarResultados,
)


def ejercicio2():
    distancia, litros = leerDatos()
    rendimiento = calcularRendimiento(distancia, litros)
    costo = calcularCosto(litros)
    mostrarResultados(distancia, litros, rendimiento, costo)


def ejercicio1():
    cantidad = leerCantidad()
    subtotal = calcularSubtotal(cantidad)
    descuento = calcularDescuento(subtotal, cantidad)
    mostrarCompra(cantidad, subtotal, descuento)


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ejercicio 1. Venta de boletos de cine")
    print("2. Ejercicio 2. Consumo de combustible")
    print("0. Salir")


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "0":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 0.")
