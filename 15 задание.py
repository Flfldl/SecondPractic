N, K, M = map(int, input('Введите N, K, M: ').split())
if K == M:
    print('0')
else:
    d = abs(K - M)
    c = min(d, N - d) - 1
    print(c)