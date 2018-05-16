from abc import ABCMeta, abstractmethod
import random

class Unit(metaclass=ABCMeta):
    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, dmg):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def attack_power(self):
        pass

    @property
    @abstractmethod
    def recharge(self):
        # добавить глобальный clock по которому следить за recharge!!!!!!!!!!!!!!!
        # каждый attack() мы устанавливаем next_attack = clock.time + recharge
        pass

    @property
    @abstractmethod
    def members(self):
        pass


class Soldier(Unit):
    def __init__(self, clock):
        self.recharge = random.randrange(500, 2000)
        self._clock = clock
        self.next_time_attack = self._clock.time + self.recharge

    def attack(self, target):
        pass

    # attack koef * damage =
