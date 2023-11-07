import requests
import csv

""" 
Consultar la API para obtener la información de 1000 pokemones y guardar la información de cada pokemon
en una lista. 
Devuelve una matriz donde cada fila es una lista que contiene la información de un pokemon
"""
def get_data() -> list:
	# este endpoint devuelve una lista de 1000 pokemones
	url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'

	try:
		# hacemos una petición GET a la API
		response = requests.get(url)

		# si se pudo hacer la conexión, regresa un código de 200
		if response.status_code == 200:
			json_response = response.json()

			# una lista donde cada elemento contiene el nombre y url de cada pokemon
			pokemons = json_response["results"]
			# aquí se guardará la información de todos los pokemones consultados
			pokemons_data = []

			for pokemon in pokemons:
				# lista que contendrá la información del pokemon actual
				current_pokemon = []
				pokemon_url = pokemon["url"]

				# hacemos una petición GET a la url del pokemon en cuestión y agarramos el JSON
				data = requests.get(pokemon_url).json()
				
				# Añadimos el nombre y el id
				current_pokemon.extend([data["name"], data["id"]])

				# Añadimos los tipos. types es una lista
				types = data["types"]

				# Si solo tiene un tipo
				if len(types) == 1:
					type_1 = types[0]["type"]["name"]
					type_2 = "None"
					current_pokemon.extend([type_1, type_2])
				else: # Si tiene 2 tipos
					for pokemon_type in types:
						type_name = pokemon_type["type"]["name"]
						current_pokemon.append(type_name)

				# Añadimos los stats. la clave "stats" es una lista
				stats = data["stats"]
				for stat in stats:
					current_pokemon.append(stat['base_stat']) 

				pokemons_data.append(current_pokemon)

			return pokemons_data
		else:
			print(f"Error al hacer la solicitud: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error en la solicitud: {e}")

""" 
Escribir la matriz obtenida en un archivo CSV
Escribe cada elemento como una fila en el archivo
"""
def write_csv(data) -> None:
	with open('info.csv', 'w', newline="") as file:
		# se crea un objeto escritor de archivos CSV que escribirá en 
		# el archivo representado por file, que es "info.csv"
		writer = csv.writer(file)

		headers = ["name", "id", "type1", "type2", "hp", "attack", "defense", "special-attack", "special-defense", "speed"]
		writer.writerow(headers)

		# se escribe cada elemento de data
		for fila in data:
			writer.writerow(fila)

def main():
	pokemons_data = get_data()
	write_csv(pokemons_data)

if __name__ == "__main__":
	main()