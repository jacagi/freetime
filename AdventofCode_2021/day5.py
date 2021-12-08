from collections import Counter

print("-*-*-*-*-*-*-*-*-*-*-*-")
format_file_day5 = lambda x: list(map(int,x.replace(" ", "").replace("->", ",").split(",")))

file = list(map(format_file_day5,open("input5.txt", "r").read().splitlines()))
coor_list = []
for line in file:
    if line[0] == line[2]:
        start = line[1] if line[1] < line[3] else line[3]
        end = line[1] if line[1] > line[3] else line[3]
        for i in range(start, end+1):
            coor_list.append(str(line[0]) + "-" + str(i))
    elif line[1] == line[3]:
        start = line[0] if line[0] < line[2] else line[2]
        end = line[0] if line[0] > line[2] else line[2]
        for i in range(start, end+1):
            coor_list.append(str(i) + "-" + str(line[1]))
coor_dict = dict(Counter(coor_list))
print("Day 5 Part 1: " + str(sum(1 for a in coor_dict.values() if a > 1)))

coor_list = []
for line in file:
    if line[0] == line[2]:
        start = line[1] if line[1] < line[3] else line[3]
        end = line[1] if line[1] > line[3] else line[3]
        for i in range(start, end+1):
            coor_list.append(str(line[0]) + "-" + str(i))
    elif line[1] == line[3]:
        start = line[0] if line[0] < line[2] else line[2]
        end = line[0] if line[0] > line[2] else line[2]
        for i in range(start, end+1):
            coor_list.append(str(i) + "-" + str(line[1]))
    elif line[1] != line[3] and line[0] != line[2]:
        startx = line[0] if line[0] < line[2] else line[2]
        endx = line[0] if line[0] > line[2] else line[2]
        starty = line[1] if line[0] < line[2] else line[3]
        endy = line[1] if line[0] > line[2] else line[3]
        while startx <= endx:
            coor_list.append(str(startx) + "-" + str(starty))
            startx +=1
            if starty < endy:
                starty +=1
            else:
                starty -=1
coor_dict = dict(Counter(coor_list))
print("Day 5 Part 2: " + str(sum(1 for a in coor_dict.values() if a > 1)))
print("-*-*-*-*-*-*-*-*-*-*-*-")