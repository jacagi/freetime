import re, itertools
from operator import methodcaller

print("-*-*-*-*-*-*-*-*-*-*-*-")
file = open("input2.txt", "r").read().splitlines()
forwardness = sum(map(int,itertools.chain(*map(re.compile("(?<=forward )\d").findall, file))))
depth = sum(map(int,itertools.chain(*map(re.compile("(?<=down )\d").findall, file)))) - sum(map(int,itertools.chain(*map(re.compile("(?<=up )\d").findall, file))))
print("Day 2 Part 1: " + str(depth * forwardness))
aim = 0;depth = 0;forwardness = 0
for f in map(methodcaller("split"," "),file):
    if f[0] == "forward":
        forwardness += int(f[1])
        depth += int(f[1]) * aim
    elif f[0] == "down":
        aim += int(f[1])
    elif f[0] == "up":
        aim -= int(f[1])
print("Day 2 Part 2: " + str(depth * forwardness))
print("-*-*-*-*-*-*-*-*-*-*-*-")