from Animal import Animal
class Bear(Animal):
    def __init__(self, continent, color, max_speed, life_expectancy, _name):
        super().__init__(continent, color)
        self.name = _name
        self._max_speed = max_speed
        self._life_expectancy = life_expectancy
        
    def __repr__(self):
        return f'Animal(_name="{self.name}", continent="{self._continent}", color="{self._color}", max_speed={self._max_speed}, life_expectancy={self._life_expectancy}'
