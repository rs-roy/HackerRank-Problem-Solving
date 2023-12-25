from itertools import groupby

inputStr = input()
result = ""

for k, v in groupby(inputStr):
    temp = len(tuple(v)), int(k)
    result = result + str(temp) + " "

print(result)