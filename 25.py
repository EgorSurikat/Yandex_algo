n = int(input())
data = [0] + [int(x) for x in input().split()]
data.sort()
length = [0] * (n + 1)
for i in range(0, n + 1):
    if i == 0 or i == 1:
        continue
    elif i == 2 or i == 3:
        length[i] = data[i] - data[1]
    else:
        length[i] = min(length[i - 1], length[i - 2]) + data[i] - data[i - 1]
print(length[-1])
