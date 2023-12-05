monety = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1,2,5,10,20,50] # zakładamy, że automat ma nieskończoną ilość monet
kwota = float(input("Wartość wrzuconej kwoty: "))
zakupy = float(input("Wartość zakupów: "))
reszta = kwota - zakupy
print(f'Reszta = {reszta} zł')
i = len(monety) - 1 # pozycja
while reszta != 0 :
    ilosc = 0
    while monety[i] <= reszta :
        print(monety[i])
        reszta -= monety[i]
        ilosc += 1
    print(f'{ilosc} x {monety[i]} zł.')
    i = i-1
