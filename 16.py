class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        return 'ok'

    def pop(self):
        if len(self.queue) == 0:
            return 'error'
        el = self.queue[0]
        del self.queue[0]
        return el

    def front(self):
        if len(self.queue) == 0:
            return 'error'
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        return 'ok'


stack = Queue()
comm = input()
while comm != 'exit':
    if comm[:4] == 'push':
        print(stack.push(comm.split()[-1]))
    elif comm[:3] == 'pop':
        print(stack.pop())
    elif comm[:5] == 'front':
        print(stack.front())
    elif comm[:4] == 'size':
        print(stack.size())
    elif comm[:5] == 'clear':
        print(stack.clear())
    comm = input()
print('bye')