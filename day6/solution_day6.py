with open("input.txt") as file:
    for line in file:
        text = str(line.strip())

# Part One
i = 0
first_marker = False
while first_marker != True:
    temp_string = text[i:i+3]
    if text[i+3] not in temp_string:
        if text[i] != text[i+1] and text[i] != text[i+2] and text[i+1] != text[i+2]:
            first_marker = True
            processed_characters = i + 4
    i += 1

print(processed_characters, "characters have been processed before the first start-of-packet marker is found.")

# Part Two
i = 0
start_of_message_marker = False
while start_of_message_marker != True:
    temp_string = text[i:i+13]
    if text[i+13] not in temp_string:
        same_character = False
        c = 0
        while c < len(temp_string)-1:
            if temp_string[c] in temp_string[c+1:]:
                same_character = True
            c += 1
        if same_character == False:
            start_of_message_marker = True
        processed_characters = i + 14
    i += 1

print(processed_characters, "characters have been processed before the first start-of-message marker is found.")