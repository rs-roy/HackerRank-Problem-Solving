t = int(input())
cube = []
for _ in range(t):
    n = int(input())
    cube.append(list(map(int, input().split())))

#print(cube)
for item in cube:
    if len(item) == 2:
        print("Yes")
        continue
    elif item[0] >= max(item[1:-1]) or item[-1] >= max(item[1:-1]):
        print("Yes")
    else:
        print("No")