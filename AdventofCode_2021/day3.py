import itertools, re

next_char_one = lambda x, y: 1 if x[y] == "1" else 0
invert_binary = lambda x: bin(int(x, 2)^ (2 ** (len(x) + 1) - 1))[3 : ]
get_most_common_one_zero = lambda i, file: "1" if sum(map(next_char_one, file, itertools.repeat(i, len(file)))) > len(file)/2 else "0"
check_next_common = lambda options, component: 1 if re.findall(r'(?<=^' + component +').',options)[0] == "1" else 0

print("-*-*-*-*-*-*-*-*-*-*-*-")
file = open("input3.txt", "r").read().splitlines()
#This could be solved with for loops, but i wanted to try a trickier solution
gamma_rate=''.join(map(get_most_common_one_zero, range(len(file[0])), itertools.repeat(file, len(file[0]))))
print("Day 3 Part 1: " + str(int(gamma_rate,2)*int(invert_binary(gamma_rate),2)))
CO2 = "";oxygen = ""
while len(oxygen)<len(file[0]):
    optionsO2 = [f for f in file if f.startswith(oxygen)];optionsCO2 = [f for f in file if f.startswith(CO2)]
    
    unos = sum(map(check_next_common, optionsCO2, itertools.repeat(CO2, len(optionsCO2))))
    
    oxygen+="1" if sum(map(check_next_common, optionsO2, itertools.repeat(oxygen, len(optionsO2)))) >= len(optionsO2)/2 else "0"
    CO2+="1" if (unos < len(optionsCO2)/2 and len(optionsCO2) > 1) or (len(optionsCO2) == 1 and unos == 1) else "0"
print("Day 3 Part 2: " + str(int(oxygen,2)*int(CO2,2)))
print("-*-*-*-*-*-*-*-*-*-*-*-")