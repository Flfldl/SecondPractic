a, b = map(int, input("Введите через пробел счет двух команд ").split(":"))
if a > b:
    print("1")
elif a < b:
        print("2")
else:
        print("0")