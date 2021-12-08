
check_1478 = lambda x: 1 if len(x) in [2,3,4,7] else 0
split_signals = lambda x: x.split(" | ")[1].split(" ")

print("-*-*-*-*-*-*-*-*-*-*-*-")
sumatotal = 0
for x in list(map(split_signals,open("input8.txt", "r").read().splitlines())):
    sumatotal += sum(map(check_1478, x))
print("Day 8 Part 1: " + str(sumatotal))

def calculate_result(line):
    complete_line = line.split(" | ")
    codes = sorted(complete_line[0].split(" "), key=len)
    result = complete_line[1].split(" ")
    numbers = {}
    numbers[8] = 'abcdefg'
    numbers[1] = "".join(sorted(codes.pop(0)))
    numbers[7] = "".join(sorted(codes.pop(0)))
    numbers[4] = "".join(sorted(codes.pop(0)))
    for code in codes:
        if len(code) == 5:
            if len(list(set(code)&set(numbers[1]))) == 2:
                numbers[3] = "".join(sorted(code))
            elif len(list(set(code)&set(numbers[4]))) == 3:
                numbers[5] = "".join(sorted(code))
            else:
                numbers[2] = "".join(sorted(code))
        elif len(code) == 6:
            if len(list(set(code)&set(numbers[1]))) == 1:
                numbers[6] = "".join(sorted(code))
            elif len(list(set(code)&set(numbers[4]))) == 4:
                numbers[9] = "".join(sorted(code))
            else:
                numbers[0] = "".join(sorted(code))
    coderesult = []
    for r in result:
        coderesult.append(list(numbers.keys())[list(numbers.values()).index("".join(sorted(r)))])
    return coderesult[0]*1000 + coderesult[1]*100 + coderesult[2]*10 + coderesult[3]

print("Day 8 Part 2: " + str(sum(map(calculate_result, open("input8.txt", "r").read().splitlines()))))
print("-*-*-*-*-*-*-*-*-*-*-*-")