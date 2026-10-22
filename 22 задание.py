import math

N, K, M = map(int, input('Введите N, K, M: ').split())
if K >= N:
    A = M * 2
    print(A)
elif K < N:
    B = 2 * N / K
    C = math.ceil(B)
    D = (C * M)
    print(D)
