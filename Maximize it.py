from itertools import product

k , m = tuple(map(int, input().split()))
myListInput = []
for _ in range(k):
    myListInput.append(list(map(int, input().split())))
mylist = list(map(lambda l: l[1:], myListInput))

elementCombo = list(product(*mylist))
#print(elementCombo)
result = []

for item in elementCombo:
    temp = sum(map(lambda x: x*x, item))
    result.append(temp%m)

print(max(result))




