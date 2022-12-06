all_values = []
with open("input.txt") as file:
    for line in file:
        all_values.append(line.strip())

#part one
points = 0
for value in all_values:
    if value[-1] == "X": 
        points += 1
        if value[0] == "A": 
            points += 3
        elif value[0] == "B": 
            points += 0
        else: points += 6 
    elif value[-1] == "Y": 
        points += 2
        if value[0] == "A":
            points += 6
        elif value[0] == "B":
            points += 3
        else: points += 0
    else:
        points += 3
        if value[0] == "A":
            points += 0
        elif value[0] == "B":
            points += 6
        else: points += 3
print (points)
        
#part two
points = 0
for value in all_values:
    if value[-1] == "X": 
        points += 0
        if value[0] == "A":
            points += 3
        elif value[0] == "B": 
            points += 1
        else: points += 2 
    elif value[-1] == "Y": 
        points += 3
        if value[0] == "A":
            points += 1
        elif value[0] == "B":
            points += 2
        else: points += 3
    else:
        points += 6 
        if value[0] == "A":
            points += 2
        elif value[0] == "B":
            points += 3
        else: points += 1
print(points)