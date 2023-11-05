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

def print_list(this_list):
    print("['name','id','hp','attack','defense','special-attack','special-defense','speed']")
    for i in range(len(this_list)):
        print(this_list[i])