import re

with open("day_3/input.txt") as f:
    data = f.readlines()

# Combine all lines together into one string
data = "".join(data)

pattern = r"\bmul\(-?\d+,-?\d+\)"
matches = re.findall(pattern, data)


def calc_sum(mul):
    num_1 = int(mul.split("(")[1].split(",")[0])
    num_2 = int(mul.split(",")[1].split(")")[0])
    return num_1 * num_2


result = sum([calc_sum(mul) for mul in matches])
print(result)

## Part 2
pattern = r"\b(?:do|don't)\(\)|\bmul\(-?\d+,-?\d+\)"
matches = re.findall(pattern, data)

sum = 0
to_sum = 1
for i in matches:
    if i == "do()":
        to_sum = 1
    elif i == "don't()":
        to_sum = 0
    if i[0:3] == "mul":
        if to_sum:
            sum += calc_sum(i)
        else:
            continue
print(sum)
