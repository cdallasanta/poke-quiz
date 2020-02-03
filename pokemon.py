class Pokemon:
  def __init__(self, id, name, types, weaknesses):
    self.id = id
    self.name = name
    self.types = types
    self.weaknesses = weaknesses
  
  def is_weak_to(type):
    type in weaknesses