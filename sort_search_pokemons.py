import sys
import sorting
import searching

while True:
    print("¡Ordenamiento y búsqueda de Pokemons!")
    print()
    print("Opción 1 - Ordenar Pokemons en base a una estadística")
    print("Opción 2 - Buscar un Pokemon para ver sus estadísticas")
    print("Opción 3 - Salir del programa")
    print()
    opcion = int(input("Digita tu elección: "))
    print()

    if opcion == 1:
        sorting.opciones_ordenamiento()
    elif opcion == 2:
        print("Estás buscando un Pokemon")
    elif opcion == 3:
        sys.exit()
    else:
        print("~Opción inválida~")
    
    print()