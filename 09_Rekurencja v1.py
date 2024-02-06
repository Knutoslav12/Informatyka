n = int(input('Podaj n: '))
def ciag(n):
    if n == 1:
        return 1 # a_1
    elif n == 2:
        return 3 # a_2
    else:
        return 2*(ciag(n-2) + ciag(n-1)) #a_n
print(f'{n} - ty wyraz ciągu wynosi {ciag(n)}.')
