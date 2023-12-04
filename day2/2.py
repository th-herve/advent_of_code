import re

map = {"red": 12, "green": 13, "blue": 14}

sum = 0

with open("input.txt") as file:
    for line in file:
        valid = True
        splt = re.split(r"\s|,|;|:", line)

        for i, value in enumerate(splt):
            if value in map and int(splt[i - 1]) > map[value]:
                valid = False
                break
        if valid:
            sum += int(splt[1])
print(sum)
