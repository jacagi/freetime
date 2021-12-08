#DAY 6
print("-*-*-*-*-*-*-*-*-*-*-*-")
myList=open("input6.txt","r").read().replace("\n","").split(",")
def myFunc(fish, days):
    numFish=1
    while days>0:
	    fish-=1
	    days-=1
	    if fish<0:
		    fish=6
		    numFish+=myFunc(8,days)
    return numFish

print("Day 6 Part 1: " + str(sum(map(myFunc,map(int,myList),[80 for i in range(len(myList))]))))
#Is so slow i have to change it
#print("Day 6 Part 2: " + str(sum(map(myFunc,map(int,myList),[256 for i in range(len(myList))]))))
print("-*-*-*-*-*-*-*-*-*-*-*-")