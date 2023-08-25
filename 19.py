class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, n):
        self.heap.append(n)
        self.heap = sift_up(self.heap)

    def extract(self):
        ret = self.heap[0]
        self.heap = sift_down(self.heap)
        return ret


def sift_down(heap):
    heap[0] = heap[-1]
    pos = 0
    l = 1
    r = 2
    while r < len(heap):
        if heap[l] > heap[r]:
            min_pos = l
        else:
            min_pos = r
        if heap[pos] < heap[min_pos]:
            heap[pos], heap[min_pos] = heap[min_pos], heap[pos]
            pos = min_pos
        else:
            break
        l = pos * 2 + 1
        r = pos * 2 + 2
    del heap[len(heap) - 1]
    return heap


def sift_up(heap):
    pos = len(heap) - 1
    par_pos = (pos - 1) // 2
    while pos > 0 and heap[pos] > heap[par_pos]:
        heap[pos], heap[par_pos] = heap[par_pos], heap[pos]
        pos = par_pos
        par_pos = (pos - 1) // 2
    return heap


stack = Heap()
n = int(input())
for i in range(n):
    comm = input()
    if comm[0] == '0':
        stack.insert(int(comm.split()[-1]))
    else:
        print(stack.extract())