import re

races = []

# [ { time: 22, dist: 22 }, { time... } ]

with open("input") as file:
    for line in file:
        splt = re.split(r"\s+", line)
        race = {}
        key = splt[0]
        i = 0
        for num in splt:
            if num.isnumeric():
                pass




print(races)
