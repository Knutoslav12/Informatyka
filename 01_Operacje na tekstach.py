import random # zaimportowałem bibliotekę random na potrzeby zadania 5

# zadanie 1
print("---ZADANIE NR 1---")
tekst = input("Podaj tekst: ")
dl_tekst = len(tekst)
print("Długość tekstu:", dl_tekst)
for i in range(1, dl_tekst, 2):
    print(tekst[i])

# zadanie 2
print("---ZADANIE NR 2---")
tekst = input("Podaj tekst: ")
print(tekst[::-1])

# zadanie 3
print("---ZADANIE NR 3---")
tekst = input("Podaj tekst: ")
dl_tekst = len(tekst)
tekst_zmieniony = ''
for i in range(0, dl_tekst):
    if i%2 == 0:
        tekst_zmieniony += tekst[i].upper()
    else:
        tekst_zmieniony += tekst[i]
print(tekst_zmieniony)

# zadanie 4
print("---ZADANIE NR 4---")
tekst = input("Podaj tekst: ")
dl_tekst = len(tekst)
tekst_zmieniony = ''
for i in range(0,dl_tekst):
    if i == 0 or i == 1 or i == dl_tekst - 1 or i == dl_tekst - 2:
        tekst_zmieniony += tekst[i].upper()
    else:
        tekst_zmieniony += tekst[i]
print(tekst_zmieniony)

# zadanie 5
# SPOSÓB NR 1 (z biblioteką random)
print("---ZADANIE NR 5 (sposób 1)---")
tekst = input("Podaj tekst: ")
tekst_odwr = tekst[::-1]
if tekst_odwr == tekst:
    print("Wyraz", tekst, "jest palindromem.") # tekst jest palindromem, program kończy działanie
else:
    tekst_litery = []
    for i in tekst:
        tekst_litery.append(i)
    random.shuffle(tekst_litery) # funkcja "mieszająca" elementy w liście tekst_litery
    anagram = ''
    for i in tekst_litery:
        anagram += i
    print(anagram)
    
# SPOSÓB NR 2 (bez biblioteki random)tekst_odwr = tekst[::-1]
print("---ZADANIE NR 5 (sposób 2)---")
tekst = input("Podaj tekst: ")
tekst_odwr = tekst[::-1]
if tekst_odwr == tekst:
    print("Wyraz", tekst, "jest palindromem.") # tekst jest palindromem, program kończy działanie
else:
    tekst_litery = []
    for i in tekst:
        tekst_litery.append(i)
    tekst_litery.sort()
    anagram = ''
    anagram = ''
    for i in tekst_litery:
        anagram += i
    print(anagram)
