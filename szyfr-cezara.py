# szyfr cezara
# wyraz ABC, klucz = 3
# A --> D, B --> E, C --> F
# XYZ, k = 3
# X --> A, Y --> B, Z --> C
# 88+3=91-26 = 65 -> A      jeśli przekracza zakres, dodajemy i odejmujemy od tego 26

print("Szyfr cezara: ")
tekst = input("Podaj teskt: ")
k = int(input("Podaj klucz: "))
szyfr = ""
dl = len(tekst)

for i in range(0, dl):
    litera = tekst[i]
    litera_ascii = ord(tekst[i])
    litera_ascii_szyfr = litera_ascii + k
    if litera_ascii_szyfr > 90:
        litera_ascii_szyfr = litera_ascii_szyfr - 26
    szyfr = szyfr + chr(litera_ascii_szyfr)
print(szyfr)

# odwrotność
enc_text = input(": ")
k = int(input("Klucz: "))
l = len(enc_text)
text = ""
for i in range(0, l):
    char = enc_text[i]
    enc_text_ascii = ord(char) - k
    if enc_text_ascii < 65:
        enc_text_ascii += 26
    text = text + chr(enc_text_ascii)
print(text)