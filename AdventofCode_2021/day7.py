import itertools

to_objective = lambda x,y: x-y if x>y else y-x
to_objective_progressive = lambda x,y: (x-y+1)*((x-y)/2) if x>y else (y-x+1)*((y-x)/2) 


file = list(map(int,open("input7.txt", "r").read().split(",")))
file.sort()

print("-*-*-*-*-*-*-*-*-*-*-*-")
print("Day 7 Part 1: " + str(min(sum(map(to_objective, file, itertools.repeat(objective, len(file))))for objective in range(file[-1]))))
print("Day 7 Part 2: " + str(int(min(sum(map(to_objective_progressive, file, itertools.repeat(objective, len(file))))for objective in range(file[-1])))))
print("-*-*-*-*-*-*-*-*-*-*-*-")