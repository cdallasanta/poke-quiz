class Pokemon:
  def __init__(self, data):
    self.id = data["id"]
    self.name = data["name"]
    self.types = data["types"]
    self.weaknesses = data["weaknesses"]
  
  def is_weak_to(type):
    type in weaknesses