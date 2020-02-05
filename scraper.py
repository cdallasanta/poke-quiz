import requests
from bs4 import BeautifulSoup
from pokemon import Pokemon

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
    sanitized_name = self.sanitize(pokemon["name"])
    url = "https://www.pokemon.com/us/pokedex/{}".format(sanitized_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = self.gather_data(soup, pokemon)

    return Pokemon(data)
  
  def sanitize(self, name):
    dict = {
      " ": "-",
      ".": "",
      "'": "",
      ":": "",
      "♀": "-female",
      "♂": "-male"
    }
    for old_char, new_char in dict.items():
      name = name.replace(old_char, new_char)
    return name

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

if __name__ == '__main__':
  # testing that all pokemon can be scraped, in case there are url changes or weird names
  scraper = Scraper()
  n_dex = scraper.set_national_dex()
  for i, p in enumerate(n_dex):
    print(p["name"])
    try:
      scraper.fetch_pokemon_data(p)
    except AttributeError:
      if p["name"] == "grookey":
        print("Generations 1-7 passed, Gen 8 failed as expected")
      else:
        print("Failed at #{} - {}".format(p["id"], p["name"]))
      break