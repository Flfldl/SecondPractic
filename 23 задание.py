n = int(input("Введите порядковый номер цифры: "))
if n < 1 or n > 493:
    print("Максимальное число символов 493, минимальное - 1")
elif n == 1:
    print(0)
else:
    k = n - 1
    if k <= 9:
        digit = k
    else:
        k -= 9
        if k <= 180:
            d = 2
            start = 10
        else:
            k -= 180
            d = 3
            start = 100

        A = k - 1
        number = start + A // d
        pos = A % d
        digit = (number // 10 ** (d - 1 - pos)) % 10

    print(digit)