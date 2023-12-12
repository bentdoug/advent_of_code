import math

input_file = open("advent_of_code/day_2_input.txt", "r")
lines = input_file.readlines()
red = 12
green = 13
blue = 14

amounts = {"red":12, "green":13, "blue":14}

total = 0

for line in lines:
    id = line.split(":")[0].split(" ")[1]
    rounds = line.split(":")[1].split(";")
    rounds = [x.strip() for x in rounds]
    works = True
    for round in rounds:
        
        colors = round.split(",")
        colors = [x.strip() for x in colors]
        for color in colors:
            color = color.split(" ")
            if amounts[color[1]] < int(color[0]):
                works = False
    if works: 
        total += int(id)
print("Num working:", total)

total = 0
for line in lines:
    maxs = {"red":0, "green":0, "blue":0}

    id = line.split(":")[0].split(" ")[1]
    rounds = line.split(":")[1].split(";")
    rounds = [x.strip() for x in rounds]
    works = True
    for round in rounds:
        
        colors = round.split(",")
        colors = [x.strip() for x in colors]
        for color in colors:
            color = color.split(" ")
            if maxs[color[1]] < int(color[0]):
                maxs[color[1]] = int(color[0])
    vals = maxs.values()
    subtotal = math.prod(vals)
    total+=subtotal
print("maxs:", total)