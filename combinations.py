from itertools import combinations

a, b = input().split()

mylist = []

for i in range(1, int(b)+1):
    mylist = list(combinations(sorted(a), i))
    #print(mylist)
    for item in mylist:
        print("".join(item))