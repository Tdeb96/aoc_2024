with open("day_6/input.txt") as f:
    rows = f.readlines()

rows = [line.strip() for line in rows]

# Find start position
start_position = [0, 0]
for row_id, row in enumerate(rows):
    for column_id, place in enumerate(row):
        if place == "^":
            start_position = [row_id, column_id]

positions = set()
positions.add(tuple(start_position))
print(positions)

# Maze traversing algorithm


def out_of_bounds(position):
    if position[0] >= len(rows) or position[0] < 0:
        return True
    elif position[1] >= len(rows[0]) or position[1] < 0:
        return True
    return False


up_or_down = True
left_or_right = True

current_position = start_position
while True:
    new_position = current_position.copy()
    print(new_position)
    if up_or_down and left_or_right:
        new_position[0] = new_position[0] - 1
        if out_of_bounds(new_position):
            break
        elif rows[new_position[0]][new_position[1]] == "#":
            print("Hit a wall, going right")
            up_or_down = False
            left_or_right = True
            continue
        else:
            current_position = new_position
            positions.add(tuple(current_position))
    elif left_or_right and not up_or_down:
        new_position[1] = new_position[1] + 1
        if out_of_bounds(new_position):
            break
        elif rows[new_position[0]][new_position[1]] == "#":
            print("Hit a wall, going down")
            up_or_down = False
            left_or_right = False
            continue
        else:
            current_position = new_position
            positions.add(tuple(current_position))
    elif not up_or_down and not up_or_down:
        new_position[0] = new_position[0] + 1
        if out_of_bounds(new_position):
            break
        elif rows[new_position[0]][new_position[1]] == "#":
            print("Hit a wall, going left")
            up_or_down = True
            left_or_right = False
            continue
        else:
            current_position = new_position
            positions.add(tuple(current_position))
    elif up_or_down and not left_or_right:
        new_position[1] = new_position[1] - 1
        if out_of_bounds(new_position):
            break
        elif rows[new_position[0]][new_position[1]] == "#":
            print("Hit a wall, going up")
            up_or_down = True
            left_or_right = True
            continue
        else:
            current_position = new_position
            positions.add(tuple(current_position))
print(positions)
print("Made it out of the maze in ", len(positions), " steps")


# Part 2


def find_infinite_loop(rows):
    up_or_down = True
    left_or_right = True

    positions = set()
    positions.add(tuple(start_position))

    count_not_infinite = 0
    infinite_loop = False

    current_position = start_position
    while True:
        new_position = current_position.copy()
        if up_or_down and left_or_right:
            new_position[0] = new_position[0] - 1
            if out_of_bounds(new_position):
                break
            elif rows[new_position[0]][new_position[1]] == "#":
                up_or_down = False
                left_or_right = True
                continue
            else:
                current_position = new_position
                if tuple(current_position) in positions:
                    count_not_infinite += 1
                    if count_not_infinite >= len(positions):
                        infinite_loop = True
                        break
                positions.add(tuple(current_position))
        elif left_or_right and not up_or_down:
            new_position[1] = new_position[1] + 1
            if out_of_bounds(new_position):
                break
            elif rows[new_position[0]][new_position[1]] == "#":
                up_or_down = False
                left_or_right = False
                continue
            else:
                current_position = new_position
                if tuple(current_position) in positions:
                    count_not_infinite += 1
                    if count_not_infinite >= len(positions):
                        infinite_loop = True
                        break
                positions.add(tuple(current_position))
        elif not up_or_down and not up_or_down:
            new_position[0] = new_position[0] + 1
            if out_of_bounds(new_position):
                break
            elif rows[new_position[0]][new_position[1]] == "#":
                up_or_down = True
                left_or_right = False
                continue
            else:
                current_position = new_position
                if tuple(current_position) in positions:
                    count_not_infinite += 1
                    if count_not_infinite >= len(positions):
                        infinite_loop = True
                        break
                positions.add(tuple(current_position))
        elif up_or_down and not left_or_right:
            new_position[1] = new_position[1] - 1
            if out_of_bounds(new_position):
                break
            elif rows[new_position[0]][new_position[1]] == "#":
                up_or_down = True
                left_or_right = True
                continue
            else:
                current_position = new_position
                if tuple(current_position) in positions:
                    count_not_infinite += 1
                    if count_not_infinite >= len(positions):
                        infinite_loop = True
                        break
                positions.add(tuple(current_position))
    return infinite_loop


# For all possible combinations of start positions, count the number of infinite loops
infinite_loop_count = 0
for row_id, row in enumerate(rows):
    for column_id, place in enumerate(row):
        if place == "#":
            continue
        rows_test = rows.copy()
        old_string = rows_test[row_id]

        rows_test[row_id] = old_string[:column_id] + "#" + old_string[column_id + 1 :]
        if find_infinite_loop(rows_test):
            infinite_loop_count += 1

print(infinite_loop_count)
