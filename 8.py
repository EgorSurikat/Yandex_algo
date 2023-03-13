k = int(input())
data = [[int(x) for x in input().split()] for i in range(k)]
data.sort(key=lambda x: x[0])
min_x, max_x = data[0][0], data[-1][0]
data.sort(key=lambda x: x[1])
min_y, max_y = data[0][1], data[-1][1]
print(min_x, min_y, max_x, max_y)