pair_list = []
with open("input.txt") as file:
    for line in file:
        pair_list.append(line.strip())

fully_contained_ranges = 0
overlapped_ranges = 0
for pair in pair_list:
    first_pair = pair[:pair.index(",")]
    second_pair = pair[(pair.index(",")+1):]
    first_number = int(first_pair[:first_pair.index("-")])
    second_number = int(first_pair[first_pair.index("-")+1:])
    third_number = int(second_pair[:second_pair.index("-")])
    fourth_number = int(second_pair[second_pair.index("-")+1:])

    if third_number <= first_number <= fourth_number and third_number <= second_number <= fourth_number:
        fully_contained_ranges += 1
        overlapped_ranges += 1
    elif first_number <= third_number <= second_number and first_number <= fourth_number <= second_number:
        fully_contained_ranges += 1
        overlapped_ranges += 1
    elif third_number <= first_number <= fourth_number or third_number <= second_number <= fourth_number:
        overlapped_ranges += 1

print ("Fully contained ranges:", fully_contained_ranges)
print ("Overlapped ranges:", overlapped_ranges)