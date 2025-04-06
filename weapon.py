class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @staticmethod
    def create_basic_weapon():
        return Weapon("Laser Cannon", 10)

    def __str__(self):
        return f"{self.name} (+{self.damage} dmg)"