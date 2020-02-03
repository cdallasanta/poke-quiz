from scraper import Scraper

class Quiz:
  def __init__(self):
    self.scraper = Scraper()
    self.national_dex = scraper.set_national_dex()
  
  def run(self):
    pdb.set_trace()
    # pick random number from 0 - len(national_dex)
    # if it's in all_pokemon, serve pokemon to quiz
    # else, send to fetch_pokemon_data(id)

    # quiz part here: ______
    pass
