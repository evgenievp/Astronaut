from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    breathe_units = 15

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.breathe_units
