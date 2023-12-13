
def rotate_matrix( m ):
    """https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise"""
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def find_symmetry(pattern):
    # Find symmetry in first row using window starting at len 4
    works = False
    row_1 = pattern[0]
    window = [0, 2]
    while window[1] < len(row_1):
        windowed = row_1[window[0]:window[1]]
        #print(window, windowed)
        if list(windowed[0:1]) == list(reversed(windowed[1:])):
            # Found symmetry in window len 4 - follow it to an end and confirm continue symmetry
            e_window = window.copy()
            while e_window[0] > 0 and e_window[1] < len(row_1):
                e_window[0] -= 1
                e_window[1] += 1
            
            expanded = row_1[e_window[0]:e_window[1]]
            print(window, e_window, expanded, list(expanded) == list(reversed(expanded))) 
            if list(expanded) == list(reversed(expanded)):
                # Found semblance of symmetry - check it for every other row
                works = True
                
                for row in pattern:
                    windowed_row = row[e_window[0]:e_window[1]]
                    print(list(windowed_row[:len(windowed_row)//2]) , list(reversed(windowed_row[len(windowed_row)//2:])))
                    if not list(windowed_row[:len(windowed_row)//2]) == list(reversed(windowed_row[len(windowed_row)//2:])):
                        works = False
                        break
                if works:
                    print(window)
                    break
                else:
                    window[0] += 1
                    window[1] += 1
            else:
                window[0] += 1
                window[1] += 1
        else:
            window[0] += 1
            window[1] += 1
    if works:
        return sum(window)//2
    else: return 0

input_file = open("Advent_of_Code\day_13_input.txt", "r")
lines = input_file.readlines()

patterns = []
pattern = []
for line in lines:
    if "." in line:
        pattern.append(line[:-1])
    else:
        patterns.append(pattern)
        pattern = []
#print(patterns)

lr_total = 0
ud_total = 0
total = 0
for pattern in patterns:
    print("-------------START NEW PATTERN------------")
    lr = find_symmetry(pattern)
    if lr == 0:
        ud = find_symmetry(rotate_matrix(pattern))
    else:
        ud = 0
    print("Return Vals: lr:{}, ud:{}".format(lr, ud))
    for i in pattern:
        print(i)

    lr_total += lr
    ud_total += ud
    
total += lr_total + (100*ud_total)
print(total)