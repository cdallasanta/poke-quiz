import requests
from bs4 import BeautifulSoup
from pokemon import Pokemon
import pdb

class Scraper:
  def set_national_dex(self):
    national_dex = []
    url = "https://pokemondb.net/pokedex/national"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for card in soup.find_all("div", "infocard"):
      card_content = card.find('span', 'text-muted')
      poke_id = int(card_content.find('small').text.replace('#', ''))
      poke_name = str(card_content.find('a').text).lower()
      national_dex.append({
        "id": poke_id,
        "name": poke_name
      })
      
    return national_dex

  def fetch_pokemon_data(self, pokemon):
    url = "https://www.pokemon.com/us/pokedex/{}".format(pokemon["name"].replace('. ', '-'))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = self.gather_data(soup, pokemon)

    return self.create_pokemon(data)

  def gather_data(self, soup, pokemon):
    types = []
    for weakness in soup.find('div', 'dtm-type').find_all('a'):
      types.append(weakness.text.strip().lower())

    weaknesses = []
    for weakness in soup.find('div', 'dtm-weaknesses').find_all('a'):
      weaknesses.append(weakness.text.strip().lower())

    data = ({
      "id": pokemon["id"],
      "name": pokemon["name"],
      "types": types,
      "weaknesses": weaknesses
    })

    return data

  def create_pokemon(self, p_data):
    return Pokemon(p_data)