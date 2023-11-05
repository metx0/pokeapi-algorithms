import csv

""" 
Se definen funciones para buscar un pokemon por su nombre o su ID
"""

def busqueda_nombre(nombre: str):
    # se ordena la lista y se aplica búsqueda binaria
    pass

def busqueda_id(id: int):
    encabezados = ["nombre", "id", "puntos de salud", "ataque", "defensa", "ataque especial", "defensa especial", "velocidad"]

    # El CSV se convierte en lista y se accede al índice correspondiente
    with open('info.csv', 'r') as file:
        info_list = list(csv.reader(file))
        pokemon_info = info_list[id]

        for i in range(8):
            print(f"{encabezados[i]}: {pokemon_info[i]}")