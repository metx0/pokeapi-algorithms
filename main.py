import requests

""" 
Escribir la información de los primeros n pokemones en un archivo CSV
"""

def main():
	url = 'https://pokeapi.co/api/v2/pokemon?limit=1200'

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
				# hacemos una petición a la url del pokemon en cuestión y agarramos el JSON
				data = requests.get(pokemon_url).json()
				print(data["height"], data["name"], data["id"])
		else:
			print(f"Error al hacer la solicitud: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error en la solicitud: {e}")

main()