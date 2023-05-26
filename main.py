from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon  
from battlefield import Battlefield      


weapon = Weapon("Plasma Pistol", 25)
dinosaur = Dinosaur("Spinosaurus", 100, 20)
robot = Robot("Droid", 100, weapon)
robot.equip_weapon(weapon)

battlefield = Battlefield("The Crucible", robot, dinosaur)

battlefield.battle_scene()

