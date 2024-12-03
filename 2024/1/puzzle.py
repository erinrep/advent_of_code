print("Day 1: Historian Hysteria")

with open("input.txt", encoding="utf-8") as f:
    lines = [x.replace("\n", "") for x in list(f)]

total = 0
lOne = []
lTwo = []

for line in lines:
    [a, b] = line.split("   ")
    lOne.append(int(a))
    lTwo.append(int(b))

lOne.sort()
lTwo.sort()

for i, x in enumerate(lOne):
    total += abs(lOne[i] - lTwo[i])

print("Part 1:", total)

simScores = []

for x in lOne:
    simScores.append(x * lTwo.count(x))

print("Part 2:", sum(simScores))
