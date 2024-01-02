import re

a = input()
s = re.findall(r'[a-z]',a)
b = re.findall(r'[A-Z]',a)
od = re.findall(r'[13579]',a)
ed = re.findall(r'[02468]',a)

str1 = "".join(sorted(s)) + "".join(sorted(b)) + "".join(sorted(od)) + "".join(sorted(ed))
print(str1)