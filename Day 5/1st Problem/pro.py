input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    data = file.read()




def parseInput(data):
    rulesSec, updatesSec = data.strip().split("\n\n")
    rules = [  list(map(int, rule.split("|"))) for rule in rulesSec.split("\n")]
    updates = [  list(map(int, update.split(","))) for update in updatesSec.split("\n")]
    return rules, updates

rules, updates = parseInput(data)
res = []
for i in range(len(updates)):
    cur = True
    for x,y in rules:
        if x in updates[i] and y in updates[i]:
            if updates[i].index(x) > updates[i].index(y):
                cur = False
                break
    if cur:
        res.append(updates[i])

total = 0
for i in range(len(res)):
    mid = len(res[i]) // 2
    total += res[i][mid]


with open(output_file, "w") as file:
    file.write(f"total sum is {total}")

