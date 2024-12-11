with open("day_8/input.txt") as f:
    rows = f.readlines()

rows = [line.strip() for line in rows]

# Job 1: Collect all locations of lowercase letter, uppercase letter, or digit and collect them in dicts
locations = {}
for row_id, row in enumerate(rows):
    for column_id, place in enumerate(row):
        if place.islower() or place.isupper() or place.isdigit():
            if place not in locations:
                locations[place] = [(row_id, column_id)]
            else:
                locations[place] += [(row_id, column_id)]


def is_in_bounds(position):
    if position[0] >= len(rows) or position[0] < 0:
        return False
    elif position[1] >= len(rows[0]) or position[1] < 0:
        return False
    return True


# Create the antinodes
antinodes = set()

for key, value in locations.items():
    # For each combination of values, create a path
    for idx, value1 in enumerate(value):
        for value2 in value[idx + 1 :]:
            # Get difference in first and second elements of the tuple value
            diff = (value2[0] - value1[0], value2[1] - value1[1])
            antinode_1 = (value1[0] - diff[0], value1[1] - diff[1])
            antinode_2 = (value2[0] + diff[0], value2[1] + diff[1])
            if is_in_bounds(antinode_1):
                antinodes.add(antinode_1)
            if is_in_bounds(antinode_2):
                antinodes.add(antinode_2)

print("Answer to part1: ", len(antinodes))

# Part 2

antinodes = set()
for key, value in locations.items():
    # For each combination of values, create a path
    for idx, value1 in enumerate(value):
        for value2 in value[idx + 1 :]:
            # Get difference in first and second elements of the tuple value
            diff = (value2[0] - value1[0], value2[1] - value1[1])
            antinode_1 = (value1[0] - diff[0], value1[1] - diff[1])
            antinode_2 = (value2[0] + diff[0], value2[1] + diff[1])
            while is_in_bounds(antinode_1):
                antinodes.add(antinode_1)
                antinode_1 = (antinode_1[0] - diff[0], antinode_1[1] - diff[1])
            while is_in_bounds(antinode_2):
                antinodes.add(antinode_2)
                antinode_2 = (antinode_2[0] + diff[0], antinode_2[1] + diff[1])
            antinodes.add(value1)
            antinodes.add(value2)


print("Answer to part2: ", len(antinodes))
