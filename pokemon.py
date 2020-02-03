import pdb

class Pokemon:
  all_types = [
    "normal",
    "fire",
    "water",
    "grass",
    "flying",
    "fighting",
    "poison",
    "electric",
    "ground",
    "rock",
    "psychic",
    "bug",
    "ghost",
    "dark",
    "steel",
    "ice",
    "dragon",
    "fairy"
  ]

  def __init__(self, data):
    self.id = data["id"]
    self.name = data["name"]
    self.types = data["types"]
    self.weaknesses = data["weaknesses"]
  
  def is_weak_to(self, type):
    return type in self.weaknesses

  def matches_all_weaknesses(self, types):
    return sorted(self.weaknesses) == sorted(types)