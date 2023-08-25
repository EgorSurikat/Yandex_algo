class Degue:
    def __init__(self):
        self.deque = []

    def push_front(self, n):
        self.deque = [n] + self.deque
        return 'ok'

    def push_back(self, n):
        self.deque.append(n)
        return 'ok'

    def pop_front(self):
        if len(self.deque) == 0:
            return 'error'
        el = self.deque[0]
        del self.deque[0]
        return el

    def pop_back(self):
        if len(self.deque) == 0:
            return 'error'
        el = self.deque[-1]
        del self.deque[-1]
        return el

    def back(self):
        if len(self.deque) == 0:
            return 'error'
        return self.deque[-1]

    def front(self):
        if len(self.deque) == 0:
            return 'error'
        return self.deque[0]

    def size(self):
        return len(self.deque)

    def clear(self):
        self.deque = []
        return 'ok'


stack = Degue()
comm = input()
while comm != 'exit':
    if comm[:10] == 'push_front':
        print(stack.push_front(comm.split()[-1]))
    elif comm[:9] == 'push_back':
        print(stack.push_back(comm.split()[-1]))
    elif comm[:9] == 'pop_front':
        print(stack.pop_front())
    elif comm[:8] == 'pop_back':
        print(stack.pop_back())
    elif comm[:4] == 'back':
        print(stack.back())
    elif comm[:5] == 'front':
        print(stack.front())
    elif comm[:4] == 'size':
        print(stack.size())
    elif comm[:5] == 'clear':
        print(stack.clear())
    comm = input()
print('bye')