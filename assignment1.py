class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self._alias = alias  
        self.power_level = power_level

    def reveal_identity(self):
        return f"{self.name} is also known as {self._alias}."

    def use_power(self):
        return f"{self.name} uses their superpowers with a power level of {self.power_level}!"


class Speedster(Superhero):
    def __init__(self, name, alias, power_level, top_speed):
        super().__init__(name, alias, power_level)
        self.top_speed = top_speed

    def use_power(self):
        return f"{self.name} runs at an astonishing speed of {self.top_speed} km/h!"

class Flyer(Superhero):
    def __init__(self, name, alias, power_level, flight_altitude):
        super().__init__(name, alias, power_level)
        self.flight_altitude = flight_altitude

    def use_power(self):
        return f"{self.name} soars through the skies at {self.flight_altitude} meters!"
hero1 = Superhero("Bruce Wayne", "Batman", 85)
hero2 = Speedster("Barry Allen", "The Flash", 90, 1000)
hero3 = Flyer("Clark Kent", "Superman", 95, 20000)


print(hero1.use_power())  
print(hero2.use_power())  
print(hero3.use_power())
