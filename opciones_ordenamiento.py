import csv
import ordenamiento

file = open('info.csv', 'r')
csv_reader = csv.reader(file, delimiter=',')
pokemon_list = list(csv_reader)
file.close()

list_to_sort = pokemon_list[1:]

def opciones_ordenamiento():
    print("¿Quieres ordenar los Pokemones en base al nombre o las estadísticas?\n")
    print("Opción 1 - En base al nombre")
    print("Opción 2 - En base a las estadísticas\n")
    opcion = int(input("Digita tu elección: "))
    print()

    if opcion == 1:
        print("Opción 1 - Ordenar nombres de manera ascendente")
        print("Opción 2 - Ordenar nombres de manera descendente\n")
        opcion_nombre = int(input("Digita tu elección: "))

        if opcion_nombre == 1:
            list_to_sort = pokemon_list[1:]
            ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 0)
            ordenamiento.print_list(list_to_sort)
        elif opcion_nombre == 2:
            list_to_sort = pokemon_list[1:]
            ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 0)
            ordenamiento.print_list(list_to_sort)
        else:
            print("~Opción inválida~")
    elif opcion == 2:
        # print("Opción 1 - Ordenar Pokemones por su ID")
        print("Opción 1 - Ordenar Pokemones por su HP")
        print("Opción 2 - Ordenar Pokemones por su ataque")
        print("Opción 3 - Ordenar Pokemones por su defensa")
        print("Opción 4 - Ordenar Pokemones por su ataque especial")
        print("Opción 5 - Ordenar Pokemones por su defensa especial")
        print("Opción 6 - Ordenar Pokemones por su velocidad\n")
        opcion_stats = int(input("Digita tu elección: "))
        print()

        match opcion_stats:
            # Ordenando por HP
            case 1:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    list_to_sort = pokemon_list[1:]
                    ordenamiento.quick_sort_ascendelly(list_to_sort, 0, len(list_to_sort) - 1, 2)
                    ordenamiento.print_list(list_to_sort)
                elif opcion_orden == 2:
                    list_to_sort = pokemon_list[1:]
                    ordenamiento.quick_sort_descendelly(list_to_sort, 0, len(list_to_sort) - 1, 2)
                    ordenamiento.print_list(list_to_sort)
                else:
                    print("~Opción inválida~")
            # Ordenando por ataque
            case 2:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    list_to_sort = pokemon_list[1:]
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
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
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
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
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
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
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
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
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
    else:
        print("~Opción inválida~")