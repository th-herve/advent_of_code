res = 0


def hash(code):
    h = 0
    for c in code:
        h += ord(c)
        h *= 17
        h %= 256
    return h


with open("./input") as file:
    for line in file:
        arr = line.split(",")
        for w in arr:
            res += hash(w.strip())


print(res)
