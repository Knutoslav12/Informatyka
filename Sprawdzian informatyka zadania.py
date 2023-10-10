# zadanie 1
tekst = input("Tekst: ")
ilosc_znakow = len(tekst)
print("Ilość znaków:", ilosc_znakow)
for i in range(1, ilosc_znakow, 2):
    print(tekst[i])

# zadanie 2
print(tekst[::-1])

# zadanie 3 (prawdopodobnie będzie inne)
# znienne tekst i ilosc_znakow bierzemy z zadania 1
tekst_powiekszony = '' 
for i in range(0, ilosc_znakow, 1):
    if i % 2 == 0:
        tekst_powiekszony += tekst[i].upper()
    else:
        tekst_powiekszony += tekst[i]
print(tekst_powiekszony)