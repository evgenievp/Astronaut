from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    breathe_units = 5

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.breathe_units
