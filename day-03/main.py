import re

with open(0, "r") as f:
    data = "".join(f.readlines())

sum1 = sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data))
print("Part 1: ", sum1)

sum2, multiply = 0, True
for cmd, a, b in re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data):
    if cmd == "do()": multiply = True
    elif cmd == "don't()": multiply = False
    elif multiply: sum2 += int(a) * int(b)

print("Part 2: ", sum2)
