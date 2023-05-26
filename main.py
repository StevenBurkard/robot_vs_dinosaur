from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon        


weapon = Weapon("Plasma Pistol", 25)
dinosaur = Dinosaur("Spinosaurus", 100, 20)
robot = Robot("Droid", 100, weapon)
robot.equip_weapon(weapon)

print(f"{dinosaur.name} has {dinosaur.health} health and {dinosaur.attack_power} attack power")

print(f"{robot.name} has a {weapon.name} Health: {robot.health} and {weapon.attack_power} attack power")