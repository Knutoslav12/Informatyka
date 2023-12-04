tekst = input("Podaj tekst: ") # tekst jawny
k = int(input("Podaj klucz: "))  # klucz szyfrujący
szyfrogram = ""
dl = len(tekst)
for i in range(0,k):  # wiersze
    for j in range(i, dl, k):  # kolumny
        szyfrogram += tekst[j]
print(szyfrogram)
