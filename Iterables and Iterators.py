from itertools import combinations
from math import comb


n = int(input())
list1 = input().split()
k = int(input())
x = 0
all = list(combinations(list1, k))
#print(all)

for item in all:
    if 'a' in item:
        x+=1
result = x / comb(n,k)
print(result)