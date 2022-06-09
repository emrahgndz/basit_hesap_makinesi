secim = input("Bir işlem seçiniz: ")
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

if secim == "*" :
    sonuc = a * b
    print(sonuc)
elif secim == "+" :
    sonuc = a + b
    print(sonuc)
elif secim == "-" :
    sonuc = a - b
    print(sonuc)
elif secim == "/" :
    sonuc = a / b
    print(sonuc)
else:
    print("Yanlış Seçim !")