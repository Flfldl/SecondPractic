a = int(input('Введите четырехзначное число: '))
b = a // 1000
e = a // 100 % 10
c = a % 10
d = a // 10 % 10
if b == c and e == d:
    print('настоящее')
else:
    print('кривое')

