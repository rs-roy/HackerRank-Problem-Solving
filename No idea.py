n,m = list(map(int,input().split()))
array_elements = list(map(int,input().split()))
#print(array_elements)

setA = set(map(int,input().split()))
setB = set(map(int,input().split()))

happinessSum = 0

for element in array_elements:
    if element in setA:
        happinessSum = happinessSum + 1
    elif element in setB:
        happinessSum = happinessSum - 1

print(happinessSum)
