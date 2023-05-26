from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = None

    def equip_weapon(self, weapon):
        self.active_weapon = weapon

    