# def sort_names_ascendelly(list)
# def sort_names_descendelly(list)
# def sort_stats_ascendelly(list, subindex)
# def sort_stats_descendelly(list, subindex)

def opciones_ordenamiento():
    print("¿Quieres ordenar los Pokemones en base al nombre o las estadísticas?")
    print()
    print("Opción 1 - En base al nombre")
    print("Opción 2 - En base a las estadísticas")
    print()
    opcion = int(input("Digita tu elección: "))
    print()

    if opcion == 1:
        print("Opción 1 - Ordenar nombres de manera ascendente")
        print("Opción 2 - Ordenar nombres de manera descendente")
        print()
        opcion_nombre = int(input("Digita tu elección: "))

        if opcion_nombre == 1:
            print("sort_names_ascendelly()")
        elif opcion_nombre == 2:
            print("sort_names_descendelly()")
        else:
            print("~Opción inválida~")
    elif opcion == 2:
        print("Opción 1 - Ordenar Pokemones por su ID")
        print("Opción 2 - Ordenar Pokemones por su HP")
        print("Opción 3 - Ordenar Pokemones por su ataque")
        print("Opción 4 - Ordenar Pokemones por su defensa")
        print("Opción 5 - Ordenar Pokemones por su ataque especial")
        print("Opción 6 - Ordenar Pokemones por su defensa especial")
        print("Opción 7 - Ordenar Pokemones por su velocidad")
        print()
        opcion_stats = int(input("Digita tu elección: "))
        print()

        opcion_orden = 0

        match opcion_stats:
            # Ordenando por ID
            case 1:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(1 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(1 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por HP
            case 2:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(2 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(2 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por ataque
            case 3:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(3 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(3 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por defensa
            case 4:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(4 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(4 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por ataque especial
            case 5:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(5 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(5 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por defensa especial
            case 6:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(6 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(6 in this case))")
                else:
                    print("~Opción inválida~")
            # Ordenando por velocidad
            case 7:
                opcion_orden = int(input("¿Ordenar de manera ascendente (1) o descendente (2)?: "))
                print()
                if opcion_orden == 1:
                    print("sort_stats_ascendelly(list, index of subarray(7 in this case))")
                elif opcion_orden == 2:
                    print("sort_stats_descendelly(list, index of subarray(7 in this case))")
                else:
                    print("~Opción inválida~")
    else:
        print("~Opción inválida~")