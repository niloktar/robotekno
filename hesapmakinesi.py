def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Sıfıra bölme hatası!"
    else:
        return a / b

print("İşlem seçiniz:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapınız (toplama/çıkarma/çarpma/bölme): ").lower()

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

if secim == 'toplama':
    print("Toplama sonucu:", toplama(sayi1, sayi2))
elif secim == 'çıkarma':
    print("Çıkarma sonucu:", cikarma(sayi1, sayi2))
elif secim == 'çarpma':
    print("Çarpma sonucu:", carpma(sayi1, sayi2))
elif secim == 'bölme':
    print("Bölme sonucu:", bolme(sayi1, sayi2))
else:
    print("Geçersiz giriş!")
