import re

keys = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

map = {}
seeds = []
min = None


currentKey = None

with open("./input.txt") as file:
    for line in file:
        splt = re.split(r"\s", line)

        if splt[0] in keys:
            currentKey = splt[0]
            map[currentKey] = []
        elif currentKey and splt[0].isnumeric():
            entry = [splt[0], splt[1], splt[2]]
            map[currentKey].append([int(x) for x in entry])
        elif splt[0] == "seeds:":
            for num in splt:
                if num.isnumeric():
                    seeds.append(int(num))

for seed in seeds:
    value = seed
    for key in keys:
        found = False
        for arr in map[key]:
            if value >= arr[1] and value < arr[1] + arr[2]:
                offset = value - arr[1]
                value = arr[0] + offset
                found = True
                break
    if min == None or min > value:
        min = value

print(min)
