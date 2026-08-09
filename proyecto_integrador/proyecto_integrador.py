"""
Sistema de Préstamos de Equipos
--------------------------------
Aplicación que gestiona el inventario, préstamos y devoluciones de
equipos de cómputo, aplicando listas, tuplas y diccionarios.

Estructura principal de datos (diccionario anidado):

equipos = {
    "Portátil Dell 01": {
        "disponible": True,
        "prestamos": [("Juan Pérez", "09/08/2026 10:15"), ...]
    },
    ...
}
"""

from datetime import datetime

# Diccionario principal del inventario.
# Se inicia con algunos equipos de ejemplo para poder probar el programa.
equipos = {
    "Portátil Dell 01": {"disponible": True, "prestamos": []},
    "Portátil HP 02": {"disponible": True, "prestamos": []},
    "Videobeam Epson 01": {"disponible": True, "prestamos": []},
}


def mostrar_equipos():
    """
    Muestra en pantalla todos los equipos registrados y su estado actual
    (disponible o prestado).
    """
    print("\n--- Listado de equipos ---")
    if not equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"- {nombre}: {estado}")


def registrar_prestamo():
    """
    Registra el préstamo de un equipo a un usuario, guardando el dato
    como una tupla inmutable (usuario, fecha) en el historial del equipo.
    """
    print("\n--- Registrar préstamo ---")
    mostrar_equipos()

    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ").strip()

    # Validar que el equipo exista
    if nombre_equipo not in equipos:
        print(f"Error: el equipo '{nombre_equipo}' no existe en el sistema.")
        return

    # Validar que el equipo esté disponible
    if not equipos[nombre_equipo]["disponible"]:
        print(f"Error: el equipo '{nombre_equipo}' ya se encuentra prestado.")
        return

    usuario = input("Ingrese el nombre del usuario que solicita el préstamo: ").strip()

    if not usuario:
        print("Error: debe indicar el nombre del usuario.")
        return

    # Se registra la fecha actual del préstamo
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    # La tupla es inmutable: una vez creada, ese registro histórico no cambia
    registro_prestamo = (usuario, fecha)
    equipos[nombre_equipo]["prestamos"].append(registro_prestamo)

    # Se actualiza el estado del equipo
    equipos[nombre_equipo]["disponible"] = False

    print(f"\nPréstamo registrado con éxito: '{nombre_equipo}' fue prestado a "
          f"{usuario} el {fecha}.")


def devolver_equipo():
    """
    Marca un equipo como devuelto, cambiando su estado a disponible.
    """
    print("\n--- Devolver equipo ---")
    nombre_equipo = input("Ingrese el nombre exacto del equipo a devolver: ").strip()

    # Validar que el equipo exista
    if nombre_equipo not in equipos:
        print(f"Error: el equipo '{nombre_equipo}' no existe en el sistema.")
        return

    # Validar que el equipo esté actualmente prestado
    if equipos[nombre_equipo]["disponible"]:
        print(f"Error: el equipo '{nombre_equipo}' no está prestado, "
              f"ya se encuentra disponible.")
        return

    equipos[nombre_equipo]["disponible"] = True
    print(f"\nEl equipo '{nombre_equipo}' ha sido devuelto correctamente.")


def ver_historial():
    """
    Muestra el historial completo de préstamos de todos los equipos.
    """
    print("\n--- Historial de préstamos ---")
    if not equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for nombre, datos in equipos.items():
        print(f"\nEquipo: {nombre}")
        historial = datos["prestamos"]  # lista de tuplas (usuario, fecha)

        if not historial:
            print("  Sin préstamos registrados.")
        else:
            for usuario, fecha in historial:
                print(f"  - Usuario: {usuario} | Fecha: {fecha}")


def agregar_equipo():
    """
    Agrega un nuevo equipo al inventario, con estado disponible
    y una lista vacía de préstamos.
    """
    print("\n--- Agregar nuevo equipo ---")
    nombre_equipo = input("Ingrese el nombre del nuevo equipo: ").strip()

    if not nombre_equipo:
        print("Error: el nombre del equipo no puede estar vacío.")
        return

    # Verificar que el equipo no exista ya en el diccionario
    if nombre_equipo in equipos:
        print(f"Error: el equipo '{nombre_equipo}' ya existe en el sistema.")
        return

    equipos[nombre_equipo] = {"disponible": True, "prestamos": []}
    print(f"\nEl equipo '{nombre_equipo}' fue registrado exitosamente.")


def menu():
    """
    Función principal que muestra el menú interactivo y dirige
    al usuario a la opción correspondiente hasta que decida salir.
    """
    opciones_validas = {"1", "2", "3", "4", "5", "6"}

    while True:
        print("\n===== SISTEMA DE PRÉSTAMOS DE EQUIPOS =====")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir del programa")

        opcion = input("Seleccione una opción (1-6): ").strip()

        # Validar que la opción sea correcta
        if opcion not in opciones_validas:
            print("Opción inválida. Por favor seleccione un número del 1 al 6.")
            continue

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\nGracias por usar el Sistema de Préstamos de Equipos. ¡Hasta luego!")
            break


if __name__ == "__main__":
    menu()