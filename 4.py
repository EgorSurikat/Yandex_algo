students = int(input())
variants = int(input())
row = int(input())
left_or_right = int(input())
next_row = row + variants // 2
prev_row = row - variants // 2
next_pos = left_or_right
prev_pos = left_or_right
if variants % 2 == 1:
    if left_or_right + 1 > 2:
        next_row += 1
        next_pos = 1
    else:
        next_pos = 2
    if left_or_right - 1 < 1:
        prev_row -= 1
        prev_pos = 2
    else:
        prev_pos = 1

if prev_row > 0 and ((next_row - 1) * 2 + next_pos - 1) < students:
    if (row - prev_row) < (next_row - row):
        print(str(prev_row) + ' ' + str(prev_pos))
    else:
        print(str(next_row) + " " + str(next_pos))
elif prev_row <= 0 and ((next_row - 1) * 2 + next_pos - 1) < students:
    print(str(next_row) + " " + str(next_pos))
elif prev_row > 0:
    print(str(prev_row) + " " + str(prev_pos))
else:
    print(-1)