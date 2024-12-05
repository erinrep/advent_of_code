import math
from functools import cmp_to_key

print("Day 5: Print Queue")

with open("input.txt", encoding="utf-8") as f:
    lines = [x.replace("\n", "") for x in list(f)]

before = dict()
after = dict()
for i, line in enumerate(lines):
    if line == "":
        break
    [a, b] = line.split("|")
    if after.get(a):
        after[a].append(b)
    else:
        after[a] = [b]
    if before.get(b):
        before[b].append(a)
    else:
        before[b] = [a]

updates = []
for j in range(i + 1, len(lines)):
    updates.append(lines[j].split(","))


def printSort(a, b):
    must_come_before = before.get(a)
    must_come_after = after.get(a)
    if must_come_before != None and b in must_come_before:
        return 1
    elif must_come_after != None and b in must_come_after:
        return -1
    else:
        return 0


valid = 0
fixed = 0
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(printSort))
    if update == sorted_update:
        valid += int(update[math.floor(len(update) / 2)])
    else:
        fixed += int(sorted_update[math.floor(len(sorted_update) / 2)])

print("Part 1:", valid)
print("Part 2:", fixed)
