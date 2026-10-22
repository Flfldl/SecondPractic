start, end = input('Введите комбинацию ходов: ').split('-')

dx = abs(ord(start[0]) - ord(end[0]))
dy = abs(int(start[1]) - int(end[1]))

if (dx, dy) in [(1, 2), (2, 1)]:
    print("YES")
else:
    print("NO")