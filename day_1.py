input_file = open("Advent_of_Code\day_1_input.txt", "r")
lines = input_file.readlines()

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

total = 0
# twone <- doesn't account for something like this
for line in lines:
    for key, value in num_dict.items():
        key_idx = 0
        while key in line[key_idx+1:]:
            print(line[key_idx+2:])
            key_len = len(key)
            key_idx = line[key_idx+1:].index(key)
            first_half = line[0:key_idx]
            last_half = line[key_idx:]
            line = first_half+value+last_half

    line_f = filter(str.isdigit, line)
    digits = []
    for i in line_f:
        digits.append(i)
    num = digits[0]+digits[-1]
    total += int(num)
print(total)