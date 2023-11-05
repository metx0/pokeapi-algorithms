from busqueda import busqueda_nombre, busqueda_id, crear_lista
from opciones_ordenamiento import opciones_ordenamiento

""" 
El usuario tiene la opción de ordenar los pokemones o de buscar entre ellos, en base a nombre o ID
Puede ordenarlo en base a su nombre o a sus stats
"""

def imprimir_opciones() -> None:
    print("\n¡Ordenamiento y búsqueda de Pokemons! ¿Qué desea hacer?")
    print("1 - Ordenar Pokemones")
    print("2 - Buscar un Pokemon")
    print("3 - Salir\n")

def busqueda(opcion: str):
    match opcion:
        case "nombre":
            # Comprobar que es una cadena alfanumérica
            while True:
                nombre = input("Digite el nombre del pokemon a buscar: ")
                if nombre.isalpha():
                    break
                else:
                    print("El nombre debe ser una cadena")

            lista = crear_lista()
            busqueda_nombre(lista, nombre)
        case "id":
            # Comprobar que es un entero y que está en el rango de 1-1000
            while True:
                id = input("Digite el ID del pokemon a buscar (1-1000): ")

                if id.isdigit():
                    id = int(id)
                    if 1 <= id <= 1000: 
                        break
                    else:
                        print("El ID debe estar en el rango de 1-1000")
                else:
                    print("El ID debe ser un número entero")

            busqueda_id(id)

def main():
    while True:
        imprimir_opciones()
        opcion = input("Digita tu elección: ")

        match opcion:
            case '1':
                opciones_ordenamiento()
                
            case '2':
                opcion_busqueda = input("¿Quiere buscarlos en base a su nombre o en base a su ID? (nombre/id): ").lower()

                while opcion_busqueda not in ("nombre, id"):
                    opcion_busqueda = input("Opción no permitida. Ingrésela de nuevo: ")
                
                busqueda(opcion_busqueda)
            case '3':
                # salir
                break
            case _:
                print("Opción inválida\n")

if __name__ == "__main__":
    main()