D = 13
A, B = map(int, input('Введите размеры полотна: ').split("*"))
D1 = A * 1.411421
D2 = (A ** 2 + B ** 2) ** 0.5
if A == B:
    if D1 > D:
        print('нет')
    elif D1 < D:
        print('да')
if A != B:
    if D2 > D:
        print('нет')
    elif D2 < D:
        print('да')
