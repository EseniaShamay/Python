from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, N, Sum, Average, rand_sum, result, Z')

N=888888
Sum[X] = ((1+X)*X)/2
print(Sum[N] == Sum)

Average[X] = (X+1)/2
print(Average[N] == Average)

rand_numbers = [random.choice(range(N)) for i in range(100)]
(result["rand_sum"] == sum_(Z, for_each=Z)) <= Z.in_(rand_numbers)
print(result["rand_sum"] == X)

print("mediana: ", (rand_numbers[48]+rand_numbers[49])/2)
