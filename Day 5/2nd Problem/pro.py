input_file = "input.txt"
output_file = "output.txt"

# Read the input file
with open(input_file, "r") as file:
    data = file.read()

# Parse the input into rules and updates
def parseInput(data):
    rulesSec, updatesSec = data.strip().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rulesSec.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updatesSec.split("\n")]
    return rules, updates

rules, updates = parseInput(data)

# Identify and collect the incorrectly ordered updates
incorrect_updates = []
for update in updates:
    is_correct = True
    # Check the update against the rules
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                is_correct = False
                break
    if not is_correct:
        incorrect_updates.append(update)

# Function to reorder an update based on the rules
def reorder_update(update, rules):
    # Create a list of pages that need to be ordered
    ordered = update[:]
    changes = True
    while changes:
        changes = False
        for x, y in rules:
            if x in ordered and y in ordered:
                if ordered.index(x) > ordered.index(y):
                    # Swap x and y to satisfy the rule
                    x_idx, y_idx = ordered.index(x), ordered.index(y)
                    ordered[x_idx], ordered[y_idx] = ordered[y_idx], ordered[x_idx]
                    changes = True
    return ordered

# Correct the order of the incorrectly ordered updates
corrected_updates = []
for update in incorrect_updates:
    corrected_updates.append(reorder_update(update, rules))

# Calculate the total sum of the middle elements for corrected updates
total = 0
for update in corrected_updates:
    mid = len(update) // 2
    total += update[mid]

# Write the total sum to the output file
with open(output_file, "w") as file:
    file.write(f"total sum is {total}")
