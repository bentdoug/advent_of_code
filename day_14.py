import time
import concurrent.futures

def rotate_matrix( m ):
    """https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise"""
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def shift_and_count(line):
    total = 0
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
    return total, line

def roll_rocks(matrix):
    total = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(matrix)) as executor:
        future_to_line = {executor.submit(shift_and_count, matrix[idx]):idx for idx in range(len(matrix))}
        #print(future_to_line)
        for future in concurrent.futures.as_completed(future_to_line):
            idx = future_to_line[future]
            try:
                data = future.result() # Should be line_total, newly arranged line
                #print(data)
                total += data[0]
                matrix[idx] = data[1]
            except Exception as exc:
                print('Line %r generated an exception: %s' % (idx, exc))
            else:
                pass
    return matrix, total

input_file = open("Advent_of_Code\day_14_input.small", "r")
lines = input_file.readlines()

matrix = lines
times = {}
start = time.time()
for _ in range(1):
    for x in range(4):
        matrix = rotate_matrix(matrix)
        matrix, total = roll_rocks(matrix)
for i in matrix:
    print(i)
end = time.time()
times=(end-start)
print(times)

print(total)
