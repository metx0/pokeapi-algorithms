import csv
from ordenamiento import quick_sort_ascendelly

""" 
Modulo donde se definen funciones para buscar un pokemon por su nombre o su ID,
e imprimir los resultados
"""

ENCABEZADOS = ["Nombre", "ID", "Tipo primario", "Tipo secundario", "Puntos de salud", "Ataque", "Defensa", "Ataque especial", "Defensa especial", "Velocidad"]

# Buscar un pokemon por nombre, con binary search, en la lista de pokemones
def busqueda_nombre(pokemon_a_encontrar) -> None:
    # Se crea la lista en donde se buscará el pokemon
    with open('info.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        lista_pokemon = list(csv_reader)[1:]

    # Se ordena de forma ascendente con quick sort
    quick_sort_ascendelly(lista_pokemon, 0, 999, 0)

    pokemon_a_encontrar = pokemon_a_encontrar.lower()
    low = 0
    # El último índice
    high = 999

    while low <= high:
        mid_position = (low + high) // 2
        # mid_position = int((low + high) / 2)
        mid_pokemon = lista_pokemon[mid_position][0]

        if pokemon_a_encontrar == mid_pokemon:
            # El elemento de la lista que corresponde al pokemon a encontrar
            pokemon_info = lista_pokemon[mid_position]

            for i in range(10):
                # Si no tiene tipo secundario, saltamos la iteración
                if i == 3 and pokemon_info[3] == "None":
                    continue

                print(f'{ENCABEZADOS[i]}: {pokemon_info[i]}')
            return
        elif pokemon_a_encontrar < mid_pokemon:
            high = mid_position - 1
        else:
            low = mid_position + 1

    print(f"El pokemon de nombre {pokemon_a_encontrar} no se ha encontrado")

# Método para buscar por ID
def busqueda_id(id: int):
    # El CSV se convierte en lista y se accede al índice correspondiente
    with open('info.csv', 'r') as file:
        info_list = list(csv.reader(file))
        pokemon_info = info_list[id]

        for i in range(10):
            if i == 3 and pokemon_info[3] == "None":
                continue
            
            print(f"{ENCABEZADOS[i]}: {pokemon_info[i]}")