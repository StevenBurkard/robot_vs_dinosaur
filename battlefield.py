class Battlefield:
    def __init__(self, name, robot, dinosaur):
        self.name = name
        self.robot = robot
        self.dinosaur = dinosaur

    def battle_scene(self):
        print(f"Welcome to the {self.name}!")
        print(f"This is an epic battle between {self.robot.name} and {self.dinosaur.name}!\n")

        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                print(f"{self.dinosaur.name} has defeated {self.robot.name}! \n{self.dinosaur.name} wins the battle!")
                return
            
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                print(f"{self.robot.name} has defeated {self.dinosaur.name}! \n{self.robot.name} wins the battle!")
                return