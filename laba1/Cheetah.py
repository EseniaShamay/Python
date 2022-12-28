from Animal import Animal
class Cheetah(Animal):
    def __init__(self, continent, color, max_speed, weight, _name):
        super().__init__(continent, color)
        self.name = _name
        self._max_speed = max_speed
        self._weight = weight
        
    def __repr__(self):
        return f'Animal(_name="{self.name}", continent="{self._continent}", color= "{self._color}", max_speed={self._max_speed}, weight={self._weight}'
