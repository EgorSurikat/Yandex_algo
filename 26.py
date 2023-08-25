n, m = [int(x) for x in input().split()]
if n == 1 and m == 1:
    print(input())
else:
    data = [[int(x) for x in input().split()] for i in range(n)]
    summ = data[0][0]
    for x in range(1, m):
        data[0][x] += data[0][x - 1]
    for y in range(1, n):
        data[y][0] += data[y - 1][0]
    for x in range(1, m):
        for y in range(1, n):
            data[y][x] += min(data[y - 1][x], data[y][x - 1])
    print(data[n - 1][m - 1])