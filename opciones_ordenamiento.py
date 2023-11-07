import csv
import ordenamiento

""" 
Módulo donde se imprimen y manejan las distintas opciones de ordenamiento
Se permite ordenar según las estadísticas
"""

# Validar las opciones de ordenamiento ascendente o descendente
# Siempre se valida si la entrada es 1 o 2; se puede modelar como función
def validar() -> int:
    while True:
        opcion = input("¿Ordenar de manera ascendente (1) o descendente (2)?: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in (1, 2):
                return opcion
            else:
                print("La opción debe ser 1 o 2")
        else:
            print("La opción debe ser 1 o 2")

# Se crea la lista a ordenar
with open('info.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        lista_pokemon = list(csv_reader)[1:]

def opciones_ordenamiento():
    print("¿Por cuál stat quiere ordenar a los pokémon?")
    print("1 - Ordenar Pokemones por su salud")
    print("2 - Ordenar Pokemones por su ataque")
    print("3 - Ordenar Pokemones por su defensa")
    print("4 - Ordenar Pokemones por su ataque especial")
    print("5 - Ordenar Pokemones por su defensa especial")
    print("6 - Ordenar Pokemones por su velocidad\n")

    # Validar que sea un entero en el rango de [1, 6]
    while True:
        opcion = input("Digita tu elección: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                break
            else:
                print("Opción incorrecta. Debe estar en el rango de 1-6")
        else:
            print("La opción debe ser un número entero en el rango de 1-6")

    # Manejar los distintos casos, del 1-6
    match opcion:
        # Ordenando por salud
        case 1:
            opcion_orden = validar()

            # De forma ascendente
            if opcion_orden == 1: pass
                # list_to_sort = pokemon_list[1:]
                # ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 2)
                # ordenamiento.print_list(list_to_sort)
            else: pass
                # Ordenar de forma descendente
                # list_to_sort = pokemon_list[1:]
                # ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 2)
                # ordenamiento.print_list(list_to_sort)
                
        # Ordenando por ataque
        case 2:
            opcion_orden = validar()

            if opcion_orden == 1:
                # la lista a ordenar se declara al inicio; solo falta pasarla de parámetro. 
                # len(lista_pokemon) - 1 es 999
                list_to_sort = lista_pokemon
                ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 3)
                ordenamiento.print_list(list_to_sort)
            elif opcion_orden == 2:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 3)
                ordenamiento.print_list(list_to_sort)
            else:
                print("~Opción inválida~")
        # Ordenando por defensa
        case 3:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 4)
                ordenamiento.print_list(list_to_sort)
            elif opcion_orden == 2:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 4)
                ordenamiento.print_list(list_to_sort)
            else:
                print("~Opción inválida~")
        # Ordenando por ataque especial
        case 4:
            opcion_orden = validar()

            if opcion_orden == 1:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 5)
                ordenamiento.print_list(list_to_sort)
            elif opcion_orden == 2:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 5)
                ordenamiento.print_list(list_to_sort)
            else:
                print("~Opción inválida~")
        # Ordenando por defensa especial
        case 5:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 6)
                ordenamiento.print_list(list_to_sort)
            elif opcion_orden == 2:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 6)
                ordenamiento.print_list(list_to_sort)
            else:
                print("~Opción inválida~")
        # Ordenando por velocidad
        case 6:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 7)
                ordenamiento.print_list(list_to_sort)
            elif opcion_orden == 2:
                list_to_sort = pokemon_list[1:]
                ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 7)
                ordenamiento.print_list(list_to_sort)
            else:
                print("~Opción inválida~")