from dinosaur import Dinosaur
from robot import Robot        



dinosaur = Dinosaur("Spinosaurus", 100, 20)
robot = Robot("Droid", 100, 15)

print(f"{dinosaur.name}")
print(f"Robot Attack Power: {robot.active_weapon}")