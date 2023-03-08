n = int(input())
if n == 1:
    print(2)
elif n == 2:
    print(4)
else:
    dp = {'00': 1, '01': 1, '10': 1, '11': 1}
    for i in range(n - 2):
        dp_00, dp_01, dp_10, dp_11 = dp['00'], dp['01'], dp['10'], dp['11']
        dp['00'] = dp_00 + dp_10
        dp['01'] = dp_00 + dp_10
        dp['10'] = dp_01 + dp_11
        dp['11'] = dp_01
    print(dp['00'] + dp['01'] + dp['10'] + dp['11'])