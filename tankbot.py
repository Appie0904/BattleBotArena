from bot import BotMaker


class TankBot(BotMaker):
    def __init__(self, name):
        super().__init__(name, power=30, armor=20, speed=5)

    def attack(self):
        return super().attack() + 5  # Extra damage

    def special_move(self):
        self._armor += 5
        print(f"{self.__class__.__name__} armor upgraded!")
