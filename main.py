from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon  
from battlefield import Battlefield      


weapon = Weapon("Ion Blaster", 20)
dinosaur = Dinosaur("Spinosaurus", 100, 25)
#From the movie: I, Robot 
robot = Robot("Sonny", 100, weapon)
robot.equip_weapon(weapon)

battlefield = Battlefield("Apex Colosseum", robot, dinosaur)

battlefield.battle_scene()

