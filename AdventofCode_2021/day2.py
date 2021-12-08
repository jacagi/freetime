import re, itertools
from operator import methodcaller

file = open("input2.txt", "r").read().splitlines()
forwardness = sum(map(int,itertools.chain(*map(re.compile("(?<=forward )\d").findall, file))))
depth = sum(map(int,itertools.chain(*map(re.compile("(?<=down )\d").findall, file)))) - sum(map(int,itertools.chain(*map(re.compile("(?<=up )\d").findall, file))))
aim = 0;depthp2 = 0;forwardnessp2 = 0
for f in map(methodcaller("split"," "),file):
    if f[0] == "forward":
        forwardnessp2 += int(f[1])
        depthp2 += int(f[1]) * aim
    elif f[0] == "down":
        aim += int(f[1])
    elif f[0] == "up":
        aim -= int(f[1])
        
print("-*-*-*-*-*-*-*-*-*-*-*-")
print("Day 2 Part 1: " + str(depth * forwardness))
print("Day 2 Part 2: " + str(depthp2 * forwardnessp2))
print("-*-*-*-*-*-*-*-*-*-*-*-")