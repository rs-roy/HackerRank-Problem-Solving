from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sorted_arr = sorted(arr, key=itemgetter(k))

    for data in sorted_arr:
        print(*data)