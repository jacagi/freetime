from collections import Counter

def myFunc(fish, days):
    fish_count = Counter(fish)
    fish_per_day = []
    for i in range(9):
        if fish_count[i]:
            fish_per_day.append(fish_count[i])
        else:
            fish_per_day.append(0)
    for _ in range(days):
        new_fish = fish_per_day[0]
        for key in range(9):
            if key != 8: fish_per_day[key] = fish_per_day[key + 1] 
        fish_per_day[8]=new_fish
        fish_per_day[6]+=new_fish
    return sum(fish_per_day)

print("-*-*-*-*-*-*-*-*-*-*-*-")
myList=list(map(int,open("input6.txt","r").read().replace("\n","").split(",")))
print("Day 6 Part 1: " + str(myFunc(myList, 80)))
print("Day 6 Part 2: " + str(myFunc(myList, 256)))
print("-*-*-*-*-*-*-*-*-*-*-*-")