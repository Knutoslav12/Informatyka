n = 4
def ciag(n):
    if n == 1:
        return 2
    return ciag(n-1)+5

for i in range(1,n+1):
    print(ciag(i)) # wyświetla kolejne wyrazy ciągu

def suma_a(n):
    if n == 1:
        return 2
    else:
        return suma_a(n-1) + ciag(n)
print(f'Suma {n} wyrazów ciągu wynosi {suma_a(n)}.')
