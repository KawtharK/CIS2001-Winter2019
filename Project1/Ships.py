from enum import Enum


class Alignment(Enum):
    Us = "Us"
    Them = "Them"
    Chaotic = "Chaotic"


class Ship:

    def __init__(self, name, x, y, alignment,
                 max_health, range, attack_power):
        self.name = name
        self._x_loc = x
        self._y_loc = y
        self._alignment = alignment
        self.max_health = max_health
        self.current_health = max_health
        self.range = range
        self.attack_power = attack_power

    def attack(self, target):
        # if target has 0 health, don't bother attacking
        if self._is_target_within_range(target)\
                and self._should_attack(target):
            target.assess_damage(self.attack_power)

    def _is_target_within_range(self, target):
        return self.range >= \
               ( ( self.get_y() - target.get_y() )**2 + \
                (self.get_x() - target.get_x()) ** 2) ** .5

    def _should_attack(self, target):
        return self.get_alignment() == Alignment.Chaotic \
            or self.get_alignment() != target.get_alignment()

    def get_type(self):
        raise NotImplementedError("Ship doesn't have a type")

    def get_x(self):
        return self._x_loc

    def get_y(self):
        return self._y_loc

    def get_alignment(self):
        return self._alignment

    def status(self):
        return "{} type: {}\nhealth:{}\nlocation: ({}, {})"\
            .format(self.name, self.get_type(),
                    self.current_health,
                    self.get_x(), self.get_y())

    def move(self):
        self.assess_damage(-1)

    def change_alignment(self):
        if self._alignment == Alignment.Us:
            self._alignment = Alignment.Them
        elif self._alignment == Alignment.Them:
            self._alignment = Alignment.Us

    def assess_damage(self, amt):
        self.current_health -= amt
        if self.current_health < 0:
            self.current_health = 0
        if self.current_health > self.max_health:
            self.current_health = self.max_health


class Battle(Ship):

    MAX_HEALTH = 100
    RANGE = 10
    ATTACK_POWER = 10

    def __init__(self, name, x , y, align):
        super().__init__(name, x, y, align, Battle.MAX_HEALTH, Battle.RANGE, Battle.ATTACK_POWER )
        self.torpedoes = 10

    def get_type(self):
        return "Battleship"

    def status(self):
        return super().status() \
               + "\nTorpedoes: {}".format(self.torpedoes)

    def attack(self, target):
        if self.torpedoes > 0:
            self.attack_power += 10
            super().attack(target)
            self.attack_power -= 10
            self.torpedoes -= 1
        else:
            super().attack(target)


battleship = Battle("Ship 1", 0, 0, Alignment.Us)
print(battleship.status())

