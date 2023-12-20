from collections import Counter
import sys

numberOfShow = int(input())
shoeSizelist = list(map(int, input().split()))

if len(shoeSizelist) != numberOfShow:
    print("Incorrect list of shoe sizes, try again")
    sys.exit()
    
shoeSizeCount = Counter(shoeSizelist)
#print(shoeSizeCount)

numberOfCustomer = int(input())
totalEarning = 0

for i in range(numberOfCustomer):
    shoeSize, price = list(map(int, input().split()))
    if shoeSize in shoeSizeCount and shoeSizeCount[shoeSize] > 0:
        shoeSizeCount[shoeSize] = shoeSizeCount[shoeSize] - 1
        totalEarning = totalEarning + price

print(totalEarning)