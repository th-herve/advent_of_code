import re

sum = 0

with open("input2.txt") as file:
    for line in file:
        valid = True
        splt = re.split(r"\s|,|;|:", line)

        map = {"red": 0, "green": 0, "blue": 0}

        for i, value in enumerate(splt):
            if value in map and int(splt[i - 1]) > map[value]:
                map[value] = int(splt[i - 1])

        power = 1
        for key in map:
            power *= map[key]
        sum += power


print(sum)
