class Entity:
  def __init__(self, name, max_health, level):
    self.name = name
    self.max_health = max_health
    self.health = max_health
    self.level = level
    self.equipments = Equipment()

  def get_info(self):
    return f"{self.name}(Lvl {self.level})"

  def roll_hit(self):
    return 0

class Enemy(Entity):
  def __init__(self, name, max_health, level, max_hit):
    super().__init__(name, max_health, level)
    self.max_hit = max_hit

  def roll_hit(self):
    return randint(0, self.max_hit)

class Player(Entity):
  def __init__(self, name, max_health, level, inventory=None):
    super().__init__(name, max_health, level)
    self.inventory = inventory

  def roll_hit(self):
    max_hit = ceil(0.1 * self.level)

    max_hit += self.equipments.get_total_attack()

    return randint(0, max_hit)
