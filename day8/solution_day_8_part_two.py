all_values = []
with open ("day8/input.txt") as file:
    for line in file:
        all_values.append(line.strip())


highest_score = 0
for value in all_values:
    if value == all_values[0] or value == all_values[-1]:
        score = 0
    else:
        i = 1
        while i < len(value) - 1:
            looking_up = 0 #upward control
            x = all_values.index(value) - 1
            visibility = True
            while x >= 0 and visibility == True:
                if int(all_values[x][i]) >= int(value[i]):
                    visibility = False
                looking_up += 1
                x -= 1
            
            looking_left = 0 #control on the left
            x = i - 1
            visibility = True
            while x >= 0 and visibility == True:
                if int(value[x]) >= int(value[i]):
                    visibility = False
                looking_left += 1
                x -= 1
            
            looking_down = 0 #downward control
            x = all_values.index(value) + 1
            visibility = True
            while x <= len(value) - 1 and visibility == True:
                if int(all_values[x][i]) >= int(value[i]):
                    visibility = False
                looking_down += 1
                x += 1
            
            looking_right = 0 #control to the right
            x = i + 1
            visibility = True
            while x <= len(value) - 1 and visibility == True:
                if int(value[x]) >= int(value[i]):
                    visibility = False
                looking_right += 1
                x += 1
            
            score = looking_down * looking_left * looking_right * looking_up
            if score > highest_score:
                highest_score = score                
            
            i += 1
            

print(highest_score)