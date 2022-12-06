import copy
stacks = {1:["V", "C", "D", "R", "Z", "G", "B", "V"], 2:["G", "W", "F", "C", "B", "S", "T", "V"],
3: ["C", "B", "S", "N", "W"], 4: ["Q", "G", "M", "N", "J", "V", "C", "P"], 5: ["T", "S", "L", "F", "D", "H", "B"],
6: ["J", "V", "T", "W", "M", "N"], 7: ["P", "F", "L", "C", "S", "T", "G"], 8: ["B", "D", "Z"], 9: ["M", "N", "Z", "W"]}
stacks_part_one = copy.deepcopy(stacks)
stacks_part_two = copy.deepcopy(stacks)
set_of_instructions = []

with open("input.txt") as file:
    for line in file:
        if line[0:4] == "move":
            instruction_line = line.strip()
            instruction = []
            crates_to_move = int(instruction_line[5:instruction_line.index("f")])
            instruction.append(crates_to_move)
            from_stack = int(instruction_line[instruction_line.index("t")-2:instruction_line.index("t")-1])
            instruction.append(from_stack)
            to_stack = int(instruction_line[instruction_line.index("t")+3:])
            instruction.append(to_stack)
            set_of_instructions.append(instruction)

# Part One
crates_on_top = ""
for i in set_of_instructions:
    for crate in range(i[0]):
        stacks_part_one[i[2]].append(stacks_part_one[i[1]].pop())
    
for k in stacks_part_one:
    crates_on_top += stacks_part_one[k][-1]

print("Solution part one:", crates_on_top)

# Part Two
crates_on_top = ""
for i in set_of_instructions:
    x = -i[0]
    while x != 0:
        stacks_part_two[i[2]].append(stacks_part_two[i[1]].pop(x))
        x += 1

for k in stacks_part_one:
    crates_on_top += stacks_part_two[k][-1]

print("Solution part two:", crates_on_top)