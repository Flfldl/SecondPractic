a = int(input('Введите пин-код: '))
b = a // 1000 % 10
c = a // 100 % 10
d = a // 10 % 10
e = a % 10
if a >= 1900 and a <= 2050:
    print('ERROR')
elif b == c or b == d or b == e or c == d or c == e or d == e:
    print('ERROR')
elif a < 1000 and a > 9999:
    print('ERROR')
else:
    print('OK')

