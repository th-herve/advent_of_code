import cmath
import math
import re

races = []
res = 1

# Create a list of all the race with this format: [ { time: 22, dist: 22 }, { time... } ]
with open("input") as file:
    for line in file:
        splt = re.split(r"\s+|:", line)
        race = {}
        key = splt[0]
        i = 0
        for num in splt:
            if num.isnumeric():
                try:
                    races[i][key] = int(num)
                except IndexError:
                    l = {key: int(num)}
                    races.append(l)
                i += 1

"""
We can use a quadratic equation like ax^2 - bx + c to solve the problem in O(1) for each race
With: distance = speed * (timeLimit - speed), we can find the the values that gives the min and max speeds to get above the distance to beat
d = x * (t - x)
0 = x^2 - t * x + d 
then: https://www.programiz.com/python-programming/examples/quadratic-roots
"""
for race in races:
    wins = 0
    # a = 1
    b = -race["Time"]
    c = race["Distance"]
    # We can use the quadratic equation x^2 - t*x + d where x the unknown is the 2 time to push that equals the record
    d = (b**2) - (4 * c)

    min = math.floor(((-b - cmath.sqrt(d)) / 2).real + 1)
    max = math.ceil(((-b + cmath.sqrt(d)) / 2).real - 1)
    wins = max - min + 1

    res *= wins


print(res)
