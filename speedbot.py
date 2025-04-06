from bot import BotMaker


class SpeedBot(BotMaker):
    def __init__(self, name):
        super().__init__(name, power=20, armor=10, speed=20)

    def attack(self):
        return super().attack() * 1.5  # An attack based on speed

    def special_move(self):
        self._speed += 5
        print(f"{self.__class__.__name__} Woah are u the Flash?!")
