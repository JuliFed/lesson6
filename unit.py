from abc import ABCMeta, abstractmethod


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
        # возвращает количество ходов при атаке которые будем простаивать
        pass

    # @abstractmethod
    # def tick(self):
    #     # уменьшает recharge для юнитов каждый ход
    #     pass

    # добавить глобальный clock по которому следить за recharge!!!!!!!!!!!!!!!




