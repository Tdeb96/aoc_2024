with open("day_2/input.txt") as file:
    data = [list(map(int, line.split())) for line in file]


# Part 1
def validate_report(report):
    mono_increase = all(
        0 < (report[i] - report[i - 1]) <= 3 for i in range(1, len(report))
    )
    mono_decrease = all(
        0 < (report[i - 1] - report[i]) <= 3 for i in range(1, len(report))
    )
    return mono_increase or mono_decrease


pt_1 = len([report for report in data if validate_report(report)])
print("Answer to part 1: ", pt_1)


# Part 2
def validate_with_fault_tolerance(report):
    if validate_report(report):
        return True
    # Check all possible single-level removals
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if validate_report(modified_report):
            return True
    return False


safe_count = 0
for report in data:
    if validate_with_fault_tolerance(report):
        safe_count += 1

print("Answer to part 2: ", safe_count)
