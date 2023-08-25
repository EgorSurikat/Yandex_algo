data = input().split()
res = 0
stack = []
for el in data:
    if el in ['+', '-', '*']:
        first = stack.pop()
        second = stack.pop()
        if el == '+':
            res = second + first
        elif el == '-':
            res = second - first
        else:
            res = second * first
        stack.append(res)
    else:
        stack.append(int(el))
res = stack.pop()
print(res)