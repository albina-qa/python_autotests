import requests

token = "c62ad9c4183ca36071c5b28b5d0d4621"
appjs = "application/json"
response = requests.post("https://api.pokemonbattle.me:9104/pokemons", json = {
    "name": "Бульбазаврик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'c62ad9c4183ca36071c5b28b5d0d4621'
}
              )
print(response.text)




responserename = requests.put ("https://api.pokemonbattle.me:9104/pokemons", json = {
    "pokemon_id": "21516",
    "name": "PythonPokemon",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'c62ad9c4183ca36071c5b28b5d0d4621'
}
              )
print(responserename.text)





responsepokeball = requests.post ("https://api.pokemonbattle.me:9104/trainers/add_pokeball", json = {
    "pokemon_id": "21516"
},
headers = {
    "Content-Type" : "application/json",
    "trainer_token" : 'c62ad9c4183ca36071c5b28b5d0d4621'
}
              )
print(responsepokeball.text)