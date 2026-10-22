n = int(input('Введите число попугаев: '))
last = n % 10
last2 = n % 100

if last2 >= 11 and last2 <= 14:
    print(n, "попугаев")
elif last == 1:
    print(n, "попугай")
elif last >= 2 and last <= 4:
    print(n, "попугая")
else:
    print(n, "попугаев")