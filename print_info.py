import requests

""" 
Escribir la información de los primeros n pokemones en un archivo CSV
Escribir: nombre, altura, peso, puntos de salud; stats
el atributo "stats" de un pokemon es una lista
en cada elemento de "stats" hay una clave llamada "base_stat" que te dice el stat de la cualidad en cuestión, 
como salud, ataque, defensa, etc. 
El orden de los elementos es: hp, attack, defense
"""

def main():
	# este endpoint contiene una lista de 1200 pokemones
	url = 'https://pokeapi.co/api/v2/pokemon?limit=10'

	try:
		# hacemos una petición GET a la API
		response = requests.get(url)

		# si se pudo hacer la conexión, regresa un código de 200
		if response.status_code == 200:
			json_response = response.json()

			# una lista que contiene los resultados de los pokemones
			pokemons = json_response["results"]

			for pokemon in pokemons:
				pokemon_url = pokemon["url"]

				# hacemos una petición GET a la url del pokemon en cuestión y agarramos el JSON
				data = requests.get(pokemon_url).json()
				# acceder a: nombre, id y stats
				print(f"Nombre: {data['name']}, id: {data['id']}")

				# la clave "stats" es una lista
				stats = data["stats"]
				for stat in stats:
					print(f"{stat['stat']['name']}: {stat['base_stat']}")
		else:
			print(f"Error al hacer la solicitud: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error en la solicitud: {e}")

# if __name__ == "__main__":
# 	main()