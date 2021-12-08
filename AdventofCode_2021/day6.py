from collections import Counter

def fish_generator(fish, days):
    fish_count = Counter(fish)
    fish_per_day = [fish_count[i] if fish_count[i] else 0 for i in range(9)]
    for _ in range(days):
        new_fish = fish_per_day[0]
        for key in range(9):
            fish_per_day[key] = fish_per_day[key + 1] if key != 8 else new_fish
        fish_per_day[6]+=new_fish
    return sum(fish_per_day)

print("-*-*-*-*-*-*-*-*-*-*-*-")
myList=list(map(int,open("input6.txt","r").read().replace("\n","").split(",")))
print("Day 6 Part 1: " + str(fish_generator(myList, 80)))
print("Day 6 Part 2: " + str(fish_generator(myList, 256)))
print("-*-*-*-*-*-*-*-*-*-*-*-")