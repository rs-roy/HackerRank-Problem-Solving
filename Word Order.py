from collections import Counter

n = int(input())
wordlist = []
for _ in range(n):
    wordlist.append(input().strip())
#print(wordlist)
mydict = Counter(wordlist) 
print(len(mydict))
print(*mydict.values())