class Character:
    name: None
    health_points: None

    def __init__(self, name):
        self.name = name
        self.health_points = 100

    def display(self):
        if self.health_points >= 50:
            print(":-D")
        elif self.health_points >= 30:
            print(":-)")
        elif self.health_points > 0:
            print(":-o")
        else:
            print("x__X")

    def damage(self, points):
        self.health_points -= points

        if self.health_points < 0:
            self.health_points = 0

    def heal(self, points):
        self.health_points += points


# Geralt = Character()
# Geralt.name = "Geralt"
# Geralt.health_points = 100
# Geralt = Character("Geralt")
# Geralt.display()
# Geralt.damage(80)
# Geralt.display()
# Geralt.heal(15)
# Geralt.display()

# Sammy = Character("Sammy")
# Sammy.display()
