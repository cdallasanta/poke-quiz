import requests
from bs4 import BeautifulSoup
import pdb

class Scraper:
  all_pokemon = []
  national_dex = []

  def __init__(self):
    self.get_pokemon_list()

  def get_pokemon_list(self):
    url = "https://pokemondb.net/pokedex/national"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for card in soup.find_all("div", "infocard"):
      card_content = card.find('span', 'text-muted')
      poke_id = int(card_content.find('small').text.replace('#', ''))
      poke_name = str(card_content.find('a').text).lower()
      self.national_dex.append({
        "id": poke_id,
        "name": poke_name
      })

  def run(self):
    # pick random number from 0 - len(national_dex)
    # if it's in all_pokemon, serve it to quiz
    # else, send to fetch_pokemon_data(id)

    # quiz part here: ______
    pass

  def fetch_pokemon_data(self, id):
    # get name from national_dex
    # fetch from https://www.pokemon.com/us/pokedex/{name}
    # send to create_pokemon
    pass

  def create_pokemon(self, data):
    self.all_pokemon.append(Pokemon(p_data))