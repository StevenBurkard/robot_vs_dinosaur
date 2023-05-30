class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name} for {self.attack_power} damage! \n{robot.name} now has {robot.health} health left. \n")
    