import requests
import csv

""" 
Consultar la API para obtener la información de n pokemones y guardar la información de cada pokemon
en una lista. La lista final es una matriz donde cada fila es una lista que contiene la información de 
un pokemon
"""
def get_data():
	# este endpoint devuelve una lista de 1200 pokemones
	url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'

	try:
		# hacemos una petición GET a la API
		response = requests.get(url)

		# si se pudo hacer la conexión, regresa un código de 200
		if response.status_code == 200:
			json_response = response.json()

			# una lista que contiene los resultados de los pokemones
			pokemons = json_response["results"]

			# aquí se guardará la información de todos los pokemones consultados
			pokemons_data = []

			for pokemon in pokemons:
				# lista que contendrá la información del pokemon actual
				current_pokemon = []

				pokemon_url = pokemon["url"]

				# hacemos una petición GET a la url del pokemon en cuestión y agarramos el JSON
				data = requests.get(pokemon_url).json()
				
				current_pokemon.extend([data["name"], data["id"]])

				# la clave "stats" es una lista
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
def write_csv(data):
	with open('info.csv', 'w', newline="") as file:
			# se crea un objeto escritor de archivos CSV que escribirá en 
			# el archivo representado por file, que es "info.csv"
			writer = csv.writer(file)

			headers = ["name", "id", "hp", "attack", "defense", "special-attack", "special-defense", "speed"]
			writer.writerow(headers)

			# se itera a través de cada elemento de data
			for fila in data:
				writer.writerow(fila)

# def main():
# 	pokemons_data = get_data()
# 	write_csv(pokemons_data)

# if __name__ == "__main__":
# 	main()