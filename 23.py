n = int(input())
dp = [0] * (n + 1)
if n == 1:
    print(0)
    print(1)
elif n == 2:
    print(1)
    print('1 2')
elif n == 3:
    print(1)
    print('1 3')
else:
    dp[0], dp[1], dp[2], dp[3] = 0, 0, 1, 2
    for i in range(3, n + 1):
        new_count = dp[i - 1] + 1
        if i % 2 == 0:
            new_count = min(new_count, dp[i // 2] + 1)
        if i % 3 == 0:
            new_count = min(new_count, dp[i // 3] + 1)
        dp[i] = new_count

    answer = ""
    i = n
    while i > 1:
        i = int(i)
        if dp[i] == dp[i - 1] + 1:
            answer = str(i) + ' ' + answer
            i -= 1
        elif i % 2 == 0 and dp[i] == dp[i // 2] + 1:
            answer = str(i) + ' ' + answer
            i /= 2
        else:
            answer = str(i) + ' ' + answer
            i /= 3
    answer = str(1) + ' ' + answer
    print(dp[n])
    print(answer[:-1])