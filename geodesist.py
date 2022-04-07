from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    breathe_units = 10

    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.breathe_units