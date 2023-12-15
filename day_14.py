def rotate_matrix_counterclockwise( m ):
    """https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise"""
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def rotate_matrix_clockwise( m ):
    return [list(reversed([m[j][i] for j in range(len(m))])) for i in range(len(m[0]))]

def calc_north_weight( m ):
    total = 0
    m = rotate_matrix_counterclockwise(m)
    for row in m:
        for idx in range(len(row)):
            if row[idx] == "O":
                total += len(row) - idx

    return total

def tilt( m ):
    m = rotate_matrix_counterclockwise(m)
    total = 0

    for line in m:
        #print(line)
        limit = 0
        for idx in range(len(line)):
            if line[idx] == "#":
                limit = idx + 1
            elif line[idx] == "O":
                line[idx] = "."
                line[limit] = "O"
                total += (len(line)) - limit
                #print((len(line)) - limit)
                limit += 1
    return total, rotate_matrix_clockwise(m)


input_file = open("advent_of_code/day_14_input.txt", "r")
lines = input_file.readlines()
# get rid of \n chars
for line in range(len(lines)):
    lines[line] = lines[line][:-1]

lines_orig = lines

results = []
matches = []
ctr = 0
while len(matches) < 26:
    ctr += 1
    if lines in results:
        matches.append([results.index(lines), ctr])
    results.append(lines)

    # Succesful Cycle
    for _ in range(4):
        total, lines = tilt(lines)
        lines = rotate_matrix_clockwise(lines)

spacing = matches[0][1]-matches[0][0]-1
num_loops = ((1000000000-matches[0][0])%spacing) + matches[0][0]-1

lines = lines_orig

print("Num loops : ", num_loops, "Match: ", matches[0])
for _ in range(num_loops+1):
    # Succesful Cycle
    for x in range(4):
        total, lines = tilt(lines)
        lines = rotate_matrix_clockwise(lines)
    total = calc_north_weight(lines)
    
print(total)
