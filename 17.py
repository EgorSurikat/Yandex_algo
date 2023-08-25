class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)

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


first = Queue()
second = Queue()
data_1 = [int(x) for x in input().split()]
for x in data_1:
    first.push(x)
data_2 = [int(x) for x in input().split()]
for x in data_2:
    second.push(x)
count = 0
while first.size() != 0 and second.size() != 0:
    f = first.pop()
    s = second.pop()
    if f > s:
        if f == 9 and s == 0:
            second.push(f)
            second.push(s)
        else:
            first.push(f)
            first.push(s)
    else:
        if f == 0 and s == 9:
            first.push(f)
            first.push(s)
        else:
            second.push(f)
            second.push(s)
    count += 1
    if count > pow(10, 6):
        print('botva')
if count < pow(10, 6):
    if first.size() == 0:
        print('second', count)
    else:
        print('first', count)