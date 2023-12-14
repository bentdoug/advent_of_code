def rotate_matrix( m ):
    """https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise"""
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]



input_file = open("Advent_of_Code\day_14_input.txt", "r")
lines = input_file.readlines()

rotated = rotate_matrix(lines)

total = 0

for line in rotated:
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
            
    #print(line)
print(total)