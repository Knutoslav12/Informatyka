import random
print("Sortowanie przez wstawienie")
# przedział i ilość liczb
d = int(input("Podaj dolną granicę: "))
g = int(input("Podaj górną granicę: "))
n = int(input("Podaj ilość liczb do wylosowania: "))

liczby = []

# losowanie n liczb i dodanie ich do listy liczby
for i in range(n):
    liczby.append(random.randrange(d, g + 1))

# właściwy program
for i in range(1, n):
    pom = liczby[i]     # zmienna pomocnicza (element z listy), "ta liczba podniesiona"
    j = i-1
    while j >= 0 and liczby[j] > pom:
        liczby[j+1] = liczby[j]
        j = j - 1
    liczby[j+1] = pom
print(f'Posortowane liczby to: {liczby}')

# sortowanie malejące
for i in range(1, n):
    pom = liczby[i]     # zmienna pomocnicza (element z listy)
    j = i-1
    while j >= 0 and liczby[j] < pom:
        liczby[j+1] = liczby[j]
        j = j - 1
    liczby[j+1] = pom
print(f'Posortowane malejąco liczby to: {liczby}')
