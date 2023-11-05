import csv 

""" 
Ejemplo de escritura y lectura de archivos CSV
"""

def main():
    data = [
        ["name", "hp", "attack"],
        ["pikachu", 30, 10],
        ["bulbasur", 25, 23],
        ["ditto", 35, 44],
    ]

    with open('info.csv', 'w', newline="") as file:
        # se crea un objeto escritor de archivos csv que escribirá en 
        # el archivo representado por file, que es "info.csv"
        writer = csv.writer(file)

        # se itera a través de cada elemento de data
        for fila in data:
            writer.writerow(fila)

    # buscar un nombre en info.csv y mostrar su información

    with open('info.csv', 'r') as file:
        # se crea un objeto lector que leerá el contenido de file, que es "info.csv"
        reader = csv.reader(file)
        nombre_a_buscar = "bulbasur"

        # iterar a través de las filas del archivo
        for fila in reader:
            if nombre_a_buscar in fila:
                print("Valor encontrado")
                print(f"Nombre: {fila[0]}, hp: {fila[1]} ...")
                break

def search(name_to_search: str):
    name_to_search = name_to_search.lower()

    # buscar un pokemon por nombre o por ID
    with open('info.csv', 'r') as file:
        # se crea un objeto lector que leerá el contenido de file, que es "info.csv"
        reader = csv.reader(file)

        # iterar a través de las filas del archivo
        for row in reader:
            if name_to_search in row:
                print("Valor encontrado")

                # imprimir la información
                for info in row:
                    print(info, end="  ")
                return
        
        print(f"{name_to_search} no encontrado")

search("gholdengo")