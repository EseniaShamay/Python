class Animal:
    def __init__(self, continent, color, _name):
        self.name = "Animal"
        self._continent = continent
        self._color = color
        
    def __repr__(self):
        return f'Animal (_name="{self.name}", continent="{self._continent}", color="{self._color}"'
        
