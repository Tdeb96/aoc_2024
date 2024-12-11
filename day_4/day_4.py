import re

with open("day_4/input.txt") as f:
    data = f.readlines()

# remove \n from each line
data = [line.strip() for line in data]


def find_xmas(input):
    # Regex string for 'XMAS'
    input = str(input)
    pattern = r"XMAS"
    pattern_reverse = r"SAMX"
    matches = re.findall(pattern, input)
    matches_reverse = re.findall(pattern_reverse, input)
    return len(matches) + len(matches_reverse)


horizontal_count = 0
# Horizontal
for line in data:
    horizontal_count += find_xmas(line)

print("horizontal matches: ", horizontal_count)

# Vertical
vertical_count = 0
for i in range(0, len(data[0])):
    vertical_count += find_xmas("".join([line[i] for line in data]))

print("vertical matches: ", vertical_count)

# Diagonal
diagonal_count = 0
data_diagonal = []

# reverse all data
data_reversed = [line[::-1] for line in data]

for row_number in range(0, len(data)):
    for column_number in range(0, len(data[0])):
        if row_number + 3 >= len(data) or column_number + 3 >= len(data[0]):
            continue
        char_1 = data[row_number][column_number]
        char_2 = data[row_number + 1][column_number + 1]
        char_3 = data[row_number + 2][column_number + 2]
        char_4 = data[row_number + 3][column_number + 3]

        char_1_r = data_reversed[row_number][column_number]
        char_2_r = data_reversed[row_number + 1][column_number + 1]
        char_3_r = data_reversed[row_number + 2][column_number + 2]
        char_4_r = data_reversed[row_number + 3][column_number + 3]

        data_diagonal.append(char_1 + char_2 + char_3 + char_4)
        data_diagonal.append(char_1_r + char_2_r + char_3_r + char_4_r)

for line in data_diagonal:
    diagonal_count += find_xmas(line)

print("diagonal matches: ", diagonal_count)
print("Total matches: ", horizontal_count + vertical_count + diagonal_count)


# Part 2:
count_double_mas = 0
for row_number in range(0, len(data)):
    for column_number in range(0, len(data[0])):
        if row_number + 2 >= len(data) or column_number + 2 >= len(data[0]):
            continue
        # 4 options now
        if (
            data[row_number][column_number] == "M"
            and data[row_number][column_number + 2] == "M"
        ):
            if data[row_number + 1][column_number + 1] == "A":
                if (
                    data[row_number + 2][column_number] == "S"
                    and data[row_number + 2][column_number + 2] == "S"
                ):
                    count_double_mas += 1
        elif (
            data[row_number][column_number] == "M"
            and data[row_number][column_number + 2] == "S"
        ):
            if data[row_number + 1][column_number + 1] == "A":
                if (
                    data[row_number + 2][column_number] == "M"
                    and data[row_number + 2][column_number + 2] == "S"
                ):
                    count_double_mas += 1
        elif (
            data[row_number][column_number] == "S"
            and data[row_number][column_number + 2] == "S"
        ):
            if data[row_number + 1][column_number + 1] == "A":
                if (
                    data[row_number + 2][column_number] == "M"
                    and data[row_number + 2][column_number + 2] == "M"
                ):
                    count_double_mas += 1
        elif (
            data[row_number][column_number] == "S"
            and data[row_number][column_number + 2] == "M"
        ):
            if data[row_number + 1][column_number + 1] == "A":
                if (
                    data[row_number + 2][column_number] == "S"
                    and data[row_number + 2][column_number + 2] == "M"
                ):
                    count_double_mas += 1
print("Answer to part 2: ", count_double_mas)
