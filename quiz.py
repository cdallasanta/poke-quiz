from scraper import Scraper
import random
import pdb

class Quiz:
  scraped_pokemon = []
  
  def __init__(self):
    self.scraper = Scraper()
    self.national_dex = self.scraper.set_national_dex()
  
  def run(self):
    poke_id = random.randint(0,len(self.national_dex)-1)
    # if it's in scraped_pokemon, serve pokemon to quiz
    answer_pokemon = next((p for p in self.scraped_pokemon if p["id"] == poke_id+1), None)
    if answer_pokemon:
      pdb.set_trace
      pass
      # move on
    else:
      answer_pokemon = self.scraper.fetch_pokemon_data(self.national_dex[poke_id-1])
      self.scraped_pokemon.append(answer_pokemon)
    # else, send to fetch_pokemon_data(id)

    pdb.set_trace()
    # quiz part here: ______
    pass
