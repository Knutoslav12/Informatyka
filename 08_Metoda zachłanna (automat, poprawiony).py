monety = [500, 200, 100, 50, 20, 10, 5, 2, 1] # 500 - 5zł
n = len(monety)
reszta_zlote = int(input('Podaj kwotę reszty w zł: '))
reszta_grosze = int(input('Podaj kwotę reszty w gr: '))
print(f'{reszta_zlote}.{reszta_grosze} zł')
reszta = reszta_zlote * 100 + reszta_grosze

i = 0
suma = 0
while reszta > 0:
    if reszta >= monety[i]:
        print(monety[i]/100)
        suma += monety[i]/100
        reszta -= monety[i]
    else:
        i += 1
print(suma)
