from abc import ABC, abstractmethod


class Astronaut(ABC):
    breathe_units = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for char in value:  #
            if char.isalpha():
                self.__name = value
                return
        raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount):
        self.oxygen += amount
