import re

print("Day 3: Mull It Over")

with open("input.txt", encoding="utf-8") as f:
    input = f.read()

mul_reg_ex = re.compile(r"mul\((\d{1,3},\d{1,3})\)")

muls = re.findall(mul_reg_ex, input)
total = 0
for mul in muls:
    [a, b] = mul.split(",")
    total += int(a) * int(b)

print("Part 1:", total)

total = 0
dos = input.split("do()")
for do in dos:
    really_do = do.split("don't()")[0]
    muls = re.findall(mul_reg_ex, really_do)
    for mul in muls:
        [a, b] = mul.split(",")
        total += int(a) * int(b)

print("Part 2:", total)
