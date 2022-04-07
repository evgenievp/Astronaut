class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for char in value:  #
            if char.isalpha():
                self.__name = value
                return
        raise ValueError("Planet name cannot be empty string or whitespace!")
