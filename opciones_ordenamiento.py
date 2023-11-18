import csv
import ordenamiento

""" 
Módulo donde se imprimen y manejan las distintas opciones de ordenamiento
Se permite ordenar según las estadísticas
"""

INDICE_SALUD = 4
INDICE_ATAQUE = 5
INDICE_DEFENSA = 6
INDICE_ATAQUE_ESPECIAL = 7
INDICE_DEFENSA_ESPECIAL = 8
INDICE_VELOCIDAD = 9

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
            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_SALUD)
                ordenamiento.print_list(lista_pokemon, INDICE_SALUD)
            else: 
                # Ordenar de forma descendente
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_SALUD)
                ordenamiento.print_list(lista_pokemon, INDICE_SALUD)
                
        # Ordenando por ataque
        case 2:
            opcion_orden = validar()

            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_ATAQUE)
                ordenamiento.print_list(lista_pokemon, INDICE_ATAQUE)
            else:
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_ATAQUE)
                ordenamiento.print_list(lista_pokemon, INDICE_ATAQUE)
        # Ordenando por defensa
        case 3:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_DEFENSA)
                ordenamiento.print_list(lista_pokemon, INDICE_DEFENSA)
            else:
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_DEFENSA)
                ordenamiento.print_list(lista_pokemon, INDICE_DEFENSA)
        # Ordenando por ataque especial
        case 4:
            opcion_orden = validar()

            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_ATAQUE_ESPECIAL)
                ordenamiento.print_list(lista_pokemon, INDICE_ATAQUE_ESPECIAL)
            else:
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_ATAQUE_ESPECIAL)
                ordenamiento.print_list(lista_pokemon, INDICE_ATAQUE_ESPECIAL)
        # Ordenando por defensa especial
        case 5:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_DEFENSA_ESPECIAL)
                ordenamiento.print_list(lista_pokemon, INDICE_DEFENSA_ESPECIAL)
            else:
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_DEFENSA_ESPECIAL)
                ordenamiento.print_list(lista_pokemon, INDICE_DEFENSA_ESPECIAL)
        # Ordenando por velocidad
        case 6:
            opcion_orden = validar()
            
            if opcion_orden == 1:
                ordenamiento.quick_sort_ascendelly(lista_pokemon, 0, 999, INDICE_VELOCIDAD)
                ordenamiento.print_list(lista_pokemon, INDICE_VELOCIDAD)
            else:
                ordenamiento.quick_sort_descendelly(lista_pokemon, 0, 999, INDICE_VELOCIDAD)
                ordenamiento.print_list(lista_pokemon, INDICE_VELOCIDAD)