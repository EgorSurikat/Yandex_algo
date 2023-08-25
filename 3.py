def bin_search(mass, target, right):
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if mass[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return right


n = int(input())
data_d = list(set([int(x) for x in input().split()]))
data_d.sort()
k = int(input())
data_k = [int(x) for x in input().split()]
for kol in range(k):
    print(bin_search(data_d, data_k[kol], len(data_d) - 1) + 1)