all_values = []
all_counts = []
with open("input.txt") as file:
    for line in file:
        all_values.append(line.strip())

counter = 0
max_value = 0
i = 0
while i < len(all_values):
    while all_values[i] != "":
        counter += int(all_values[i])
        i += 1
        if i >= len(all_values): break
    if counter > max_value:
        max_value = counter
    all_counts.append(counter)
    counter = 0
    i += 1
print(max_value)
all_counts.sort()
all_counts.reverse()
print (all_counts[:3])