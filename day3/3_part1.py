import re

sum = 0

with open("input.txt") as file:
    for line in file:
        splt = re.split(r":|\|", line)
        winning_nums = re.findall(r"\d+", splt[1])
        my_nums = re.findall(r"\d+", splt[2])

        point = 0

        for num in my_nums:
            if num in winning_nums:
                if not point:
                    point = 1
                else:
                    point *= 2

        sum += point

print(sum)
