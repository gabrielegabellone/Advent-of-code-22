all_values = []
with open ("input.txt") as file:
    for line in file:
        all_values.append(line.strip())

counter = 0
for value in all_values:
    if value == all_values[0] or value == all_values[-1]:
        counter += 99
    else:
        i = 0
        while i <= 98:
            if i == 0 or i == 98: counter += 1
            else:
                higher = True
                x = i - 1 
                while higher == True and x >= 0: #control to the left
                    if int(value[i]) <= int(value[x]):
                        higher = False
                    else: x -= 1

                if higher == False:
                    x = i + 1
                    higher = True
                    while higher == True and x <= 98: #control to the right
                        if int(value[i]) <= int(value[x]):
                            higher = False
                        else: x += 1
                    
                    if higher == False:
                        x = all_values.index(value) - 1
                        higher = True
                        while higher == True and x >= 0: #upward control
                            if int(value[i]) <= int(all_values[x][i]):
                                higher = False
                            else: x -= 1
                        
                        if higher == False:
                            x = all_values.index(value) + 1
                            higher = True
                            while higher == True and x <= 98: #downward control
                                if int(value[i]) <= int(all_values[x][i]):
                                    higher = False
                                else: x += 1

                if higher == True: counter += 1
            i += 1
print (counter)