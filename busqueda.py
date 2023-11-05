import csv
from ordenamiento import quick_sort_ascendelly

""" 
Se definen funciones para buscar un pokemon por su nombre o su ID
"""

def crear_lista():
    file = open('info.csv', 'r')
    csv_reader = csv.reader(file, delimiter=',')
    pokemon_list = list(csv_reader)
    file.close()

    list_to_sort = pokemon_list[1:]
    return list_to_sort

# Buscar un Pokemon con binary search
def busqueda_nombre(list, pokemon_to_find):
    encabezados = ["nombre", "id", "puntos de salud", "ataque", "defensa", "ataque especial", "defensa especial", "velocidad"]
    quick_sort_ascendelly(list, 0, len(list) - 1, 0)

    pokemon_to_find = pokemon_to_find.lower()
    low = 0
    high = len(list) - 1

    while low <= high:
        mid_position = int((low + high) / 2)
        mid_pokemon = list[mid_position][0]

        if pokemon_to_find == mid_pokemon:
            for i in range(8):
                print(f'{encabezados[i]}: {list[mid_position][i]}')
        
        if pokemon_to_find < mid_pokemon:
            high = mid_position - 1
        else:
            low = mid_position + 1
    return -1

# Método para buscar por ID
def busqueda_id(id: int):
    encabezados = ["nombre", "id", "puntos de salud", "ataque", "defensa", "ataque especial", "defensa especial", "velocidad"]

    # El CSV se convierte en lista y se accede al índice correspondiente
    with open('info.csv', 'r') as file:
        info_list = list(csv.reader(file))
        pokemon_info = info_list[id]

        for i in range(8):
            print(f"{encabezados[i]}: {pokemon_info[i]}")