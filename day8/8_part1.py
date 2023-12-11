import re

instructions = []
map = {}
steps = 0

with open("input") as file:
    for line in file:
        if not instructions:
            for char in line.strip():
                instructions.append(0 if char == "L" else 1)
        elif not len(line.strip()) == 0:
            values = re.findall(r"[A-Z]{3}", line)
            map[values[0]] = [values[1], values[2]]


found = False
i = 0
key = "AAA"

while not found and steps < 100:
    if i >= len(instructions):
        i = 0
    key = map[key][instructions[i]]
    print(instructions[i])

    if key == "ZZZ":
        found = True

    steps += 1
    i += 1
print(steps)
