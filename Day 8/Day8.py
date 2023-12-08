import re
import math

instructions = ''
storage = {}
starting = []

def handle_line(line):
    pattern = r'\b([A-Z]{3})\s*=\s*\(([A-Z]{3}),\s*([A-Z]{3})\)'
    matches = re.match(pattern, line)
    if matches:
        key = matches.group(1)
        val1 = matches.group(2)
        val2 = matches.group(3)
    storage[key] = (val1, val2)
    if key[-1] == "A":
        starting.append(key)

with open('d8.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            instructions = line
        elif line != '':
            handle_line(line)

def solve(instructions, storage, starting):
    steps = 0
    loop = 0

    while True:
        # Handle looping around
        if steps == len(instructions):
            loop += 1
            steps = 0

        step = instructions[steps]

        starting = [storage[key][0] if step == "L" else storage[key][1] for key in starting]

        steps += 1

        if all(key[-1] == "Z" for key in starting):
            break

    return steps + loop * len(instructions)

# Calculate the least common multiple for starting positions ending with 'A'
ret = math.lcm(*[solve(instructions, storage, [start]) for start in starting])

print("Final key:", starting[0])
print("Total steps:", ret)

               


