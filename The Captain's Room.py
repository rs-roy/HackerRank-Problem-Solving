from collections import Counter

k = int(input())
roomList = list(map(int,(input().split())))
counterDict = Counter(roomList)

for key,value in counterDict.items():
    if value == 1:
        print(key)
