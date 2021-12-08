import re

to_rows = lambda x: list(map(int,re.findall(r'\d+', x)))
to_box = lambda x: list(map(to_rows, x.split("\n")))

#DAY 4
print("-*-*-*-*-*-*-*-*-*-*-*-")
file = open("input4.txt", "r").read().split("\n\n")
sortedNumbers = list(map(int,file.pop(0).split(",")))

cards = list(map(to_box, file))

def remove_number(card, number):
    for row in card:
        for idx, val in enumerate(row):
            if val == number:
                row[idx] = "a"
                return True
    return False

def check_any_empty_row(card):
    for row in card:
        if sum(map(lambda r: 1 if r!="a" else 0,row)) == 0:
            return True
    return False

def check_any_empty_col(card):  
    for x in range(5):
        if sum(map(lambda r: 1 if r!="a" else 0,[card[i][x] for i in range(5)])) == 0:
            return True
    return False

def calculate_result(number, card):
    suma_total = 0
    for c in card:
        suma_total+=sum(map(lambda r: r if r!="a" else 0,c))
    return suma_total*number

def check_cards(sortedNumbers, cards):
    for number in sortedNumbers:
        for c in cards:
            if remove_number(c, number):
                if check_any_empty_row(c) or check_any_empty_col(c):
                    return calculate_result(number, c)             
print("Day 4 Part 1: " + str(check_cards(sortedNumbers, cards)))
def check_loser(sortedNumbers, cards):
    for number in sortedNumbers:
        cards_to_pop = []
        for idx, c in enumerate(cards):
            if remove_number(c, number):
                if check_any_empty_row(c) or check_any_empty_col(c):
                    if len(cards) == 1:
                        return calculate_result(number, cards[0])
                    else:
                        cards_to_pop.append(idx)   
        cards_to_pop.sort(reverse=True)  
        for c in cards_to_pop:
            cards.pop(c)
print("Day 4 Part 2: " + str(check_loser(sortedNumbers, cards)))
print("-*-*-*-*-*-*-*-*-*-*-*-")
