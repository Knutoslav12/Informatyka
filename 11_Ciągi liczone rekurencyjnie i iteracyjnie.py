# ciag fibonacciego - rekurencja
def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)

# ciag fibonacciego - iteracja


def fibonacci_i(n):
    a = 1  # pierwszy wyraz ciągu
    b = 1  # drugi wyraz ciągu
    for i in range(2, n):
        temp = b
        b += a
        a = temp
    return b



# napisz program metodą rekurencyjną i iteracyjną, obliczający n-ty wyraz następującego ciągu:
# 4,9,14,19
def ciag_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 4
    elif n == 2:
        return 9
    else:
        return ciag_r(n-1) + 5
print(f'20 - ty wyraz ciągu, policzony metodą rekurencyjną, wynosi {ciag_r(20)}.')

def ciag_i(n):
    a = 4
    b = 9
    for i in range(2,n):
        temp = b
        b += 5
        a = temp
    return b
print(f'20 - ty wyraz ciągu, policzony metodą iteracyjną, wynosi {ciag_i(20)}.')