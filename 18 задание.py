A, B = map(int, input('Введите A * B: ').split('*'))
C, D, E = map(int, input('Введите C * D * E: ').split('*'))
if C <= D and D <= B:
    print('да')
else:
    print('нет')