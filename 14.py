n = int(input())
data = [int(x) for x in input().split()]
stack = []
res = [0]
for el in data:
    stack.append(el)
    while stack != [] and res[-1] == stack[-1] - 1:
        res.append(stack.pop())
if not stack:
    print('YES')
else:
    print('NO')