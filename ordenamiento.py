""" 
Este módulo define el algoritmo de ordenamiento quick sort, para ordenar la lista en base
a distintos parámetros
"""

INDICE_TIPO_PRIMARIO = 2
INDICE_TIPO_SECUNDARIO = 3

# Ordenar la lista en base a un subíndice, de manera ascendente
def quick_sort_ascendelly(this_list, low, high, subindex):
    if low >= high: return

    pivotIndex = partition_ascendelly(this_list, low, high, subindex)
    quick_sort_ascendelly(this_list, low, pivotIndex - 1, subindex)
    quick_sort_ascendelly(this_list, pivotIndex + 1, high, subindex)

def partition_ascendelly(this_list, low, high, subindex):
    pivot = high
    i = low - 1

    for j in range(low, pivot):
        if this_list[low][subindex].isdigit():
            # Convierte las cadenas a enteros antes de comparar
            if int(this_list[j][subindex]) < int(this_list[pivot][subindex]):
                i += 1
                this_list[i], this_list[j] = this_list[j], this_list[i]
        else:
            if this_list[j][subindex] < this_list[pivot][subindex]:
                i += 1
                this_list[i], this_list[j] = this_list[j], this_list[i]
    i += 1
    this_list[i], this_list[pivot] = this_list[pivot], this_list[i]

    return i


# Ordenar la lista en base a un subíndice, de manera descendente
def quick_sort_descendelly(this_list, low, high, subindex):
    if low >= high: return

    pivotIndex = partition_descendelly(this_list, low, high, subindex)
    quick_sort_descendelly(this_list, low, pivotIndex - 1, subindex)
    quick_sort_descendelly(this_list, pivotIndex + 1, high, subindex)

def partition_descendelly(this_list, low, high, subindex):
    pivot = high
    i = low - 1

    for j in range(low, pivot):
        if this_list[low][subindex].isdigit():
            # Convierte las cadenas a enteros antes de comparar
            if int(this_list[j][subindex]) > int(this_list[pivot][subindex]):
                i += 1
                this_list[i], this_list[j] = this_list[j], this_list[i]
        else:
            if this_list[j][subindex] > this_list[pivot][subindex]:
                i += 1
                this_list[i], this_list[j] = this_list[j], this_list[i]
    i += 1
    this_list[i], this_list[pivot] = this_list[pivot], this_list[i]

    return i

# secuencias de escape para imprimir con color en la terminal
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_list(lista_pokemon, stat):
    for i in range(1000):
        pokemon = lista_pokemon[i]

        # imprimir el nombre, los tipos, id, y estadística
        # si no tiene tipo secundario, se imprime de forma diferente

        if pokemon[INDICE_TIPO_SECUNDARIO] != "None":
            print(f"{colors.HEADER}{pokemon[0]}{colors.ENDC}, {colors.OKBLUE}id: {pokemon[1]}{colors.ENDC}, {colors.OKCYAN}tipo primario: {pokemon[INDICE_TIPO_PRIMARIO]}{colors.ENDC}, {colors.OKGREEN}tipo secundario: {pokemon[INDICE_TIPO_SECUNDARIO]}{colors.ENDC}, {colors.WARNING}stat: {pokemon[stat]}{colors.ENDC}")
        else:
            print(f"{colors.HEADER}{pokemon[0]}{colors.ENDC}, {colors.OKBLUE}id: {pokemon[1]}{colors.ENDC}, {colors.OKCYAN}tipo primario: {pokemon[INDICE_TIPO_PRIMARIO]}{colors.ENDC}, {colors.WARNING}stat: {pokemon[stat]}{colors.ENDC}")