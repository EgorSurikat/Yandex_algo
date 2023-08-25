def is_good(string):
    stack = []
    for el in string:
        if el in ['(', '[', '{']:
            stack.append(el)
        elif el == ')':
            if stack == [] or stack.pop() != '(':
                return 'no'
        elif el == ']':
            if stack == [] or stack.pop() != '[':
                return 'no'
        elif el == '}':
            if stack == [] or stack.pop() != '{':
                return 'no'
    if not stack:
        return 'yes'
    else:
        return 'no'


st = input()
print(is_good(st))