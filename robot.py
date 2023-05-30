from weapon import Weapon

class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = active_weapon

    def equip_weapon(self, weapon):
        self.active_weapon = weapon

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage! \n {dinosaur.name} now has {dinosaur.health} left. \n")
        if self.active_weapon is None:
            print(f"{self.name} currently has no weapon!")
        return
