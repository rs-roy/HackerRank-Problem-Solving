import re

n = int(input())

code = ""
for _ in range(n):
    code = code + input() + "\n"

temp = re.sub(r' && ', " and ", code)
temp1 = re.sub(r' && ', " and ", temp)
temp2 = re.sub(r' \|\| ', " or ", temp1)
result = re.sub(r' \|\| ', " or ", temp2)

print(result)