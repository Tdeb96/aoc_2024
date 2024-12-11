from itertools import product

# Preprocess lines
with open("day_7/input.txt") as f:
    rows = f.readlines()

rows = [line.strip() for line in rows]

result = {}
for line in rows:
    key, values = line.split(":")
    key = int(key.strip())
    values_list = list(map(int, values.strip().split()))
    result[key] = values_list


def is_possible(line):
    key, values = line.split(":")
    key = int(key.strip())
    values = list(map(int, values.strip().split()))

    combinations = ["".join(bits) for bits in product("01", repeat=len(values) - 1)]

    for operators in combinations:
        total = values[0]
        for idx, number in enumerate(values):
            if idx == 0:
                continue
            if operators[idx - 1] == "0":
                total += number
            else:
                total *= number

        if total == key:
            return True
    return False


total = 0
for line in rows:
    if is_possible(line):
        key, values = line.split(":")
        key = int(key.strip())
        total += key

print("Total part 1: ", total)


def is_possible_part2(line):
    key, values = line.split(":")
    key = int(key.strip())
    values = list(map(int, values.strip().split()))

    combinations = ["".join(bits) for bits in product("012", repeat=len(values) - 1)]

    for operators in combinations:
        total = values[0]
        for idx, number in enumerate(values):
            if idx == 0:
                continue
            if operators[idx - 1] == "0":
                total += number
            elif operators[idx - 1] == "1":
                total *= number
            else:
                total = int(str(total) + str(number))

        if total == key:
            return True
    return False


total = 0
for line in rows:
    if is_possible_part2(line):
        key, values = line.split(":")
        key = int(key.strip())
        total += key
print("Total part 2: ", total)
