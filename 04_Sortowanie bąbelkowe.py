import random

d = int(input('Dolna granica: '))
g = int(input('Górna granica: '))
n = int(input('Podaj ilość liczb do wylosowania: '))
liczby = []

for i in range(1, n+1):
    liczby.append(random.randint(d, g+1))
    # liczby.append(randrange(d,g+1))
print(liczby)

# sortowanie rosnące bąbelkowe
for i in range(1, n):
    for j in range(0, n-1):
        if liczby[j] > liczby[j+1]:
            liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
print(liczby)

# program który posortuje malejąco
for i in range(1, n):
    for j in range(0, n-1):
        if liczby[j] < liczby[j+1]:
            liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
print(liczby)

# wyraz, sortować litery
wyraz = input('Podaj wyraz [WIELKIMI LITERAMI]: ')
l = len(wyraz)
lista = []
for litera in wyraz:
    lista.append(litera)
for i in range(1, l):
    for j in range(0, l-1):
        if ord(lista[j]) > ord(lista[j+1]):
            lista[j], lista[j+1] = lista[j+1], lista[j]

wyraz_n = ""
for znak in lista:
    wyraz_n += znak
print(wyraz_n)