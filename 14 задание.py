a = int(input('Введите количество кнатов: '))
b = a // 29
c = a % 29
d = b // 17
e = b % 17
if c == 0:
    print (d, 'галеонов', e, 'сикелей')
elif d == 0:
    print(e, 'сикелей', c, 'кнатов')
elif e == 0:
    print(d, 'галеонов', c, 'кнатов')
elif c == 0 and d == 0:
    print(e, 'сикелей')
elif e == 0 and c == 0:
    print(d, 'галеонов')
elif e == 0 and d== 0:
    prinr(c, 'кнатов')
else:
    print(d, "галеонов", e, 'сикелей', c, 'кнатов')