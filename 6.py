m = int(input())
n = int(input())
sec = []
for i in range(n):
    new_line = [int(x) for x in input().split()]
    if not sec:
        sec.append([new_line[0], new_line[1]])
    else:
        to_del = []
        for x in range(len(sec)):
            if (new_line[0] <= sec[x][0] and sec[x][1] <= new_line[1]) or (sec[x][0] <= new_line[0] <= sec[x][1]) or (sec[x][0] <= new_line[1] <= sec[x][1]):
                to_del.append(x)
        for x in range(len(to_del) - 1, -1, -1):
            del sec[to_del[x]]
        sec.append([new_line[0], new_line[-1]])
print(len(sec))