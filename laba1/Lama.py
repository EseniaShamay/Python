from Animal import Animal
class Lama(Animal):
    def __init__(self, continent, color, max_speed, symbol, _name):
        super().__init__(continent, color)
        self.name = _name
        self._max_speed = max_speed
        self._symbol = symbol
        
    def __repr__(self):
        return f'Animal(_name="{self.name}", continent="{self._continent}", color="{self._color}", max_speed={self._max_speed}, symbol="{self._symbol}"'
