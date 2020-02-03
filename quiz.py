from scraper import Scraper
import random
import pdb

class Quiz:
  scraped_pokemon = []
  
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.scraper = Scraper()
    self.national_dex = self.scraper.set_national_dex()
  
  def run(self):
    poke_id = random.randint(0,len(self.national_dex)-1)
    answer_pokemon = next((p for p in self.scraped_pokemon if p["id"] == poke_id+1), None)
    if not answer_pokemon:
      answer_pokemon = self.scraper.fetch_pokemon_data(self.national_dex[poke_id-1])
      self.scraped_pokemon.append(answer_pokemon)

    # quiz part here: ______
    pass
