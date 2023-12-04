import re

res = 0

with open("./calibration.txt", "r") as file:
    for line in file:
        digits = re.findall("\d", line)

        digit = digits[0] + digits[-1]
        res += int(digit)


print(res)
