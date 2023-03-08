from math import inf

n = int(input())
data = [[inf, inf, inf], [inf, inf, inf]] + [[int(x) for x in input().split()] for i in range(n)]
dp = [0, 0] + [0] * n
for i in range(2, n + 2):
    dp[i] = min(dp[i - 1] + data[i][0], dp[i - 2] + data[i - 1][1], dp[i - 3] + data[i - 2][2])
print(dp[-1])