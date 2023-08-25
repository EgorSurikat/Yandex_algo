class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return 'ok'

    def pop(self):
        if len(self.stack) == 0:
            return 'error'
        return self.stack.pop()

    def back(self):
        if len(self.stack) == 0:
            return 'error'
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
        return 'ok'


stack = Stack()
comm = input()
while comm != 'exit':
    if comm[:4] == 'push':
        print(stack.push(comm.split()[-1]))
    elif comm[:3] == 'pop':
        print(stack.pop())
    elif comm[:4] == 'back':
        print(stack.back())
    elif comm[:4] == 'size':
        print(stack.size())
    elif comm[:5] == 'clear':
        print(stack.clear())
    comm = input()
print('bye')