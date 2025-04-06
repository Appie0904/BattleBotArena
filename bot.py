class TemplateBot:
    def __init__(self, name, power, armor, speed):
        self.__name = name             # private
        self._armor = armor            # protected
        self.power = power             # public
        self._speed = speed
        self._hp = 100
        self._weapon = None

    @property
    def hp(self):
        return self._hp

    def equip_weapon(self, weapon):
        self._weapon = weapon
        self.power += weapon.damage

    def take_damage(self, amount):
        damage_taken = max(0, amount - self._armor)
        self._hp -= damage_taken

    def attack(self):
        base_attack = self.power
        if self._weapon:
            base_attack += self._weapon.damage
        return base_attack

    def __str__(self):
        return f"{self.__name} [Power: {self.power}, Armor: {self._armor}, HP: {self._hp}]"

    def __eq__(self, other):
        return self.power == other.power

    def __add__(self, weapon):
        self.equip_weapon(weapon)
        return self

    def __sub__(self, damage):
        self.take_damage(damage)
        return self