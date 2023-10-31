# encryption
text = input("Tekst: ")
key = int(input("Klucz szyfrowania [liczba]: "))
enc_text = ""
l = len(text)

for i in range(0, l):
    text_ascii = ord(text[i]) + key
    if text_ascii > 90:
        text_ascii -= 26
    enc_text += chr(text_ascii)
print(f"Zaszyfrowany tekst: {enc_text}")

# decryption
enc_text = input("Zaszyfrowany tekst: ")
key = int(input("Klucz: "))
l = len(enc_text)
text = ""

for i in range(0, l):
    enc_text_ascii = ord(enc_text[i]) - key
    if enc_text_ascii < 65:
        enc_text_ascii += 26
    text += chr(enc_text_ascii)
print(f"Odszyfrowany tekst: {text}")
