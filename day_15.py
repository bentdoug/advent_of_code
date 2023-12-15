def holiday_ascii_hash(string):
    string_value = 0
    for char in string:
        string_value += ord(char)
        string_value *= 17
        string_value = string_value%256
    return string_value

input_file = open("Advent_of_Code\day_15_input.txt", "r")
lines = input_file.readlines()

init_sequence = lines[0].split(",")
total = 0
for step in init_sequence:
    total+=holiday_ascii_hash(step)
print(total)
