N, M = map(int, input('Введите M, N: ').split('*'))
K = int(input('Введите K: '))
if K % M == 0 and K < N * M or K % N == 0 and K < N * M:
    print('Успешно')
else:
    print('Неосуществимо')