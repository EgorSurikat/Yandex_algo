data = [int(x) for x in input().split()]
n, k = data[0], data[1]
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    new_count = 0
    x, step = i - 1, 1
    while x > 0 and k >= step:
        new_count += dp[x]
        x -= 1
        step += 1
    dp[i] = new_count
print(dp[-1])