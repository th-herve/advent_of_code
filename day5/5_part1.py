import re

keys = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature","temperature-to-humidity", "humidity-to-location" ]

map = {}
seeds = None
min = None

# {key: [ [0,1,4], [1,2,3]]}

currentKey = None

with open("./input.txt") as file:
    for line in file:
        splt = re.split(r"\s",line)

        if (splt[0] in keys):
            currentKey = splt[0]
            map[currentKey] = []
        elif currentKey and splt[0].isnumeric():
            entry = [splt[0], splt[1], splt[2]]
            map[currentKey].append(entry)
        elif splt[0] == "seeds":


print(map)


