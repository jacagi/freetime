check_next_bigger = lambda x: 1 if x[0] < x[1] else 0
check_next_window_bigger = lambda x: 1 if sum(x[0]) < sum(x[1]) else 0

print("-*-*-*-*-*-*-*-*-*-*-*-")
file = list(map(int, open("input1.txt", "r").read().splitlines()))
print("Day 1 Part 1: " + str(sum(map(check_next_bigger,zip(file[:-1], file[1:])))))
windows = list(zip(file[:-2],file[1:-1],file[2:]))
print("Day 1 Part 2: " + str(sum(map(check_next_window_bigger,zip(windows[:-1], windows[1:])))))
print("-*-*-*-*-*-*-*-*-*-*-*-")