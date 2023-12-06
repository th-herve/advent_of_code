import re

sum = 0

convert = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("part2") as file:
    regex = r"one|two|three|four|five|six|seven|eight|nine|\d"

    for line in file:
        digits = re.findall(regex, line)

        first = digits[0]
        last = digits[-1]

        if first in convert:
            first = convert[first]
        if last in convert:
            last = convert[last]

        num = str(first) + str(last)
        print(int(num))

        sum += int(num)

print(sum)
