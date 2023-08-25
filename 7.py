a = [int(x) for x in input().split(':')]
b = [int(x) for x in input().split(':')]
c = [int(x) for x in input().split(':')]
a = a[0] * 60 * 60 + a[1] * 60 + a[2]
c = c[0] * 60 * 60 + c[1] * 60 + c[2]
if c > a:
    now = (c - a) / 2
else:
    now = (24 * 60 * 60 - a + c) / 2
if now - int(now) < 0.5:
    now = int(now)
else:
    now = int(now) + 1
b[2] += now
if b[2] > 59:
    b[1] += b[2] // 60
    b[2] %= 60
    if b[1] > 59:
        b[0] += b[1] // 60
        b[1] %= 60
    if b[0] > 23:
        b[0] %= 24
b[0], b[1], b[2] = str(int(b[0])), str(int(b[1])), str(int(b[2]))
if int(b[0]) < 10:
    b[0] = '0' + b[0]
if int(b[1]) < 10:
    b[1] = '0' + b[1]
if int(b[2]) < 10:
    b[2] = '0' + b[2]
print(b[0] + ':' + b[1] + ':' + b[2])