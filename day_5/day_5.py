with open("day_5/input_order.txt") as f:
    orders = f.readlines()

order_cleaned = {}
for line in orders:
    if int(line.split("|")[0]) not in order_cleaned:
        order_cleaned[int(line.split("|")[0])] = [int(line.split("|")[1])]
    else:
        order_cleaned[int(line.split("|")[0])] += [int(line.split("|")[1])]

with open("day_5/updates.txt") as f:
    updates = f.readlines()

updates = [line.strip() for line in updates]
updates = [item.split(",") for item in updates]
updates = [[int(num) for num in sublist] for sublist in updates]


# Part 1
sum = 0
faulty_ordered_lists = []
for update in updates:
    valid = True
    for idx, before in enumerate(update):
        if not valid:
            break
        subset_rules = order_cleaned[before]
        for after in subset_rules:
            if after in update:
                if update.index(after) < idx:  # If not valid
                    valid = False
                    faulty_ordered_lists.append(update)
                    break
    if valid:
        sum += update[len(update) // 2]

print("Solution part 1: ", sum)

# Part 2
for update in faulty_ordered_lists:
    faulty = True
    while faulty:
        for before_index, before in enumerate(update):
            breaked = False
            subset_rules = order_cleaned[before]
            for after in subset_rules:
                if after in update:
                    if update.index(after) < before_index:  # If not valid
                        print("Before: ", before, "After: ", after)
                        print("Update before: ", update)
                        # Remove before from list
                        update.remove(before)
                        print("List after removal: ", update)
                        # Add before 1 index before after
                        update.insert(update.index(after), before)
                        print("Update after: ", update)
                        breaked = True
                        break
            if breaked:
                break
        print("Should be correct now")
        if not breaked:
            faulty = False

sum = 0
print(len(faulty_ordered_lists))

for update in faulty_ordered_lists:
    sum += update[len(update) // 2]

print("Solution part 2: ", sum)
