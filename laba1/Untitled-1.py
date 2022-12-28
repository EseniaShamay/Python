import sys
import json
from Animal import Animal
from Bear import Bear
from Cheetah import Cheetah
from Lama import Lama
from Penguin import Penguin

def write(data):
    jsonstr = json.dumps(data, indent = 4)
    open('./objects.json', 'w').write(jsonstr)
def read_from_json():
    return json.load(open('./objects.json', 'r'))

a = Animal("Australia", "red")
b = Bear("Asia", "brown", 56, 30)
c = Cheetah("Africa", "yellow", 110, 70)
l = Lama("South_America", "white", 50, "power")
p = Penguin("Antarctic", "black", 9, "fish")
z = [a, b, c, l, p]
data = {
    'amount' : len(z),
    'obj' : []
}
for elem in z:
    data['obj'].append(elem.__dict__)
    
write(data)
data.clear()
z.clear()
data = read_from_json()
for elem in data['obj']:
    if elem['name'] == "Animal":
        obj = Animal(elem['_continent'], elem['_color'])
    elif elem['name'] == "Bear":
        obj = Animal(elem['_continent'], elem['_color'], elem['_max_speed'], elem['_life_expectancy'])
    elif elem['name'] == "Cheetah":
        obj = Animal(elem['_continent'], elem['_color'], elem['_max_speed'], elem['_weight'])
    elif elem['name'] == "Lama":
        obj = Animal(elem['_continent'], elem['_color'], elem['_max_speed'], elem['_symbol'])
    elif elem['name'] == "Penguin":
        obj = Animal(elem['_continent'], elem['_color'], elem['_max_speed'], elem['_food'])
    z.append(obj)
for elem in z:
    elem.__repr__()
