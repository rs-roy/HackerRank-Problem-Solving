import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

l = []

for i in range(m):
    l = l + list(map(lambda x:x[i] , matrix))

mystr = "".join(l)

res = re.sub(r'(?<=[a-zA-Z0-9])\W+(?=[a-zA-Z0-9])'," ",mystr)

print(res)