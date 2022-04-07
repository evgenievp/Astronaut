from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    mission_count = 0
    incompleted_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type in ['Biologist', 'Meteorologist', 'Geodesist']:
            for astronaut in self.astronaut_repository.astronauts:
                if astronaut.name == name:
                    return f"{name} is already added."
            if astronaut_type == 'Biologist':
                self.astronaut_repository.astronauts.append(Biologist(name))
            elif astronaut_type == 'Geodesist':
                self.astronaut_repository.astronauts.append(Geodesist(name))
            elif astronaut_type == 'Meteorologist':
                self.astronaut_repository.astronauts.append(Meteorologist(name))
            return f'Successfully added {astronaut_type}: {name}.'
        raise Exception('Astronaut type is not valid!')

    def add_planet(self, name, items):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f'{name} is already added.'
        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.planets.append(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(astronaut)
                return f"Astronaut {name} was retired!"
        raise Exception(f'Astronaut {name} doesn\'t exist!')

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name):
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                suitable = {}
                sorted_suitable = None
                for astronaut in self.astronaut_repository.astronauts:
                    if astronaut.oxygen > 30:
                        suitable[astronaut] = astronaut.oxygen
                if len(suitable) == 0:
                    raise Exception('You need at least one astronaut to explore the planet!')
                elif len(suitable) > 5:
                    sorted_suitable = sorted(suitable.items(), key=lambda kvp: -kvp[1])[:5]
                elif len(suitable) <= 5:
                    sorted_suitable = sorted(suitable.items(), key=lambda kvp: -kvp[1])
                count = 0
                suitable_list = [a[0] for a in sorted_suitable]
                for astronaut in suitable_list:
                    count += 1
                    while planet.items:
                        current_item = planet.items[-1]
                        if astronaut.oxygen - astronaut.breathe_units >= 0:
                            astronaut.backpack.append(current_item)
                            planet.items.pop()
                            astronaut.breathe()
                        else:
                            break
                    if not planet.items:
                        break
                if len(planet.items) == 0:
                    self.mission_count += 1
                    return f"Planet: {planet_name} was explored. {count} astronauts participated in collecting items."
                else:
                    self.incompleted_missions += 1
                    return f"Mission is not completed."
        raise Exception('Invalid planet name!')

    def report(self):
        result = f"{self.mission_count} successful missions!\n"
        result += f"{self.incompleted_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f'Name: {astronaut.name}\n'
            result += f'Oxygen: {astronaut.oxygen}\n'
            if astronaut.backpack:
                result += f"Backpack items: {', '.join([s for s in astronaut.backpack])}" + '\n'
            else:
                result += f'Backpack items: none\n'
        return result.strip()
