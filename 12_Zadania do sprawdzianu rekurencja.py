# NWD Euklides
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

print(nwd(125,25))

# zadanie 1
def zadanie_1(n):
    if n == 1:
        return 3
    if n == 2:
        return 6
    else:
        return (zadanie_1(n-2) * zadanie_1(n-1)) // 2

# zadanie 2
def zadanie_2(n):
    if n == 1:
        return 5
    if n == 2:
        return 7
    else:
        return (zadanie_2(n-2) + zadanie_2(n-1)) % 3

def zadanie_3(a, b): #algorytm Euklidesa
    if b == 0:
        return a
    return nwd(b, a%b)
a = 12
b = 4
d = zadanie_3(a, b)
print(f'{a/d} / {b/d}')

def NWD(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)
n = 5
m = 3
NWW = (n * m) / NWD(n, m)
print(f'Zespoły M i N spotkają się po {NWW} dniach.')

# zadanie 5
n = 5
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
def srednia(n):
    suma = 0
    for i in range(1, n+1):
        suma += fibonacci(i)
    return suma / n
srednia(n)

print(f'Średnia sumy {n} wyrazów ciągu Fibonacciego wynosi {srednia(n)}')
