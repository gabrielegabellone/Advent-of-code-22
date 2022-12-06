all_rucksacks = []
with open("input.txt") as file:
    for line in file:
        all_rucksacks.append(line.strip())

#part one
counter = 0
priority = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
for rucksack in all_rucksacks:
    character_found = ""
    for character in rucksack[:len(rucksack)//2]:
        if character in rucksack[len(rucksack)//2:] and character != character_found:
            character_found = character
            if character in priority:
                counter += priority[character]
            else: counter += priority[character.lower()]+26

print (counter)

#part two
counter = 0
i = 0            
while i < len(all_rucksacks):
    character_found = ""
    for character in all_rucksacks[i]:
        if character in all_rucksacks[i+1] and character in all_rucksacks[i+2] and character != character_found:
            character_found = character
            if character in priority:
                counter += priority[character]
            else: counter += priority[character.lower()]+26
    i+=3

print (counter)