from scraper import Scraper
from pokemon import Pokemon
import random

class Quiz:
  colors = {
    "normal": "\033[1;37;40m",
    "fire": "\033[1;31;40m",
    "water": "\033[1;34;40m",
    "grass": "\033[1;32;40m",
    "flying": "\033[1;37;40m",
    "fighting": "\033[1;31;40m",
    "poison": "\033[1;35;40m",
    "electric": "\033[1;33;40m",
    "ground": "\033[1;33;40m",
    "rock": "\033[1;32;40m",
    "psychic": "\033[1;35;40m",
    "bug": "\033[1;32;40m",
    "ghost": "\033[1;35;40m",
    "dark": "\033[1;37;40m",
    "steel": "\033[1;37;40m",
    "ice": "\033[1;36;40m",
    "dragon": "\033[1;34;40m",
    "fairy": "\033[1;33;40m",
    "correct": "\033[1;32;40m",
    "incorrect": "\033[1;31;40m",
    "reset": "\033[0m"
  }

  def __init__(self, show_types, all_answers):
    self.scraped_pokemon = []
    self.show_types = show_types
    self.all_answers = all_answers
    self.scraper = Scraper()
    self.national_dex = self.scraper.set_national_dex()
  
  def run(self):
    self.rules()
    self.setup()
    correct_answer = self.question()
    self.ending(correct_answer)

  def setup(self):
    # TODO: currently not using the most recent generation until pokemon.com/pokedex is updated 
    # replace the following two lines when it is
    # poke_id = random.randint(1,len(self.national_dex))
    poke_id = random.randint(1,809)
    self.answer_pokemon = self.find_from_scraped(poke_id)
    if not self.answer_pokemon:
      self.answer_pokemon = self.scraper.fetch_pokemon_data(self.national_dex[poke_id-1])
      self.scraped_pokemon.append(self.answer_pokemon)
  
  def find_from_scraped(self, id):
    for poke in self.scraped_pokemon:
      if poke.id == id:
        return poke
    return None
    
  def rules(self):
    print("")
    print("{}Welcome trainer, to the Pokemon Types Quiz!{}".format(self.colors["normal"], self.colors["reset"]))
    print("You will be presented with a pokemon's name{}, and must guess what type{} effective against it".format((" and types" if self.show_types else ""), ("s are" if self.all_answers else " is")))
  
  def question(self):
    print("")
    print("Pokemon's name: {}{}{}".format(self.colors["normal"], self.answer_pokemon.name.title(), self.colors["reset"]))
    if self.show_types:
      types = []
      for type in self.answer_pokemon.types:
        types.append(self.colors[type] + type + self.colors["reset"])
      print("Pokemon's types(s): {}".format(" & ".join(types))) 

    print("What super effective against {}{}{}".format(self.colors["normal"], self.answer_pokemon.name.title(), self.colors["reset"]))
    if self.all_answers:
      print("Enter all possible answers, seperated by a comma and a space (e.g. \"fire, water, bug\")")
      answer = self.validate_answer()
    else:
      answer = self.validate_answer("Enter a single pokemon type: ")

    return self.check_answer(answer)

  def validate_answer(self, msg = ""):
    answer = ""
    print("(for a list of types, enter \"help\")")
    while answer is "":
      answer = input(msg).lower()
      if answer == "help":
        self.list_types()
        answer = ""
        print("What super effective against {}{}{}".format(self.colors["normal"], self.answer_pokemon.name.title(), self.colors["reset"]))
    return answer

  def check_answer(self, answer):
    if self.all_answers:
      return self.answer_pokemon.matches_all_weaknesses(answer.split(", "))
    else:
      return self.answer_pokemon.is_weak_to(answer)
    
  def list_types(self):
    types = []
    for type in Pokemon.all_types:
    
      types.append(self.colors[type] + type + self.colors["reset"])
    print("All types: {}".format(", ".join(types))) 
  
  def ending(self, correct_answer):
    print()
    if correct_answer:
      print(self.colors["correct"] + "Congratulations, you are correct!" + self.colors["reset"])
    else:
      if self.all_answers:
        print(self.colors["incorrect"] + "Sorry, that was not all of the pokemon's weaknesses. They were:" + self.colors["reset"])
      else:
        print(self.colors["incorrect"] + "Sorry, that is not in the list of the pokemon's weaknesses. They were:" + self.colors["reset"])
      weaknesses = []
      for weakness in self.answer_pokemon.weaknesses:
        weaknesses.append(self.colors[weakness] + weakness + self.colors["reset"])
      print("Pokemon's weaknesses: {}".format(", ".join(weaknesses))) 
    
    replay = input("Would you like to play again? (y/n): ").lower()
    while not replay in ["yes", "y", "no", "n"]:
      print("I don't understand that input")
      replay = input("Would you like to play again? (y/n): ").lower()
    
    if replay in ["yes", "y"]:
      self.run()
    else:
      print("Thank you for playing, goodbye!")
