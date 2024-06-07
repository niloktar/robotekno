import random

def sifre_olustur(uzunluk, sayi_iste, sembol_iste):
  """Belirtilen uzunlukta ve seçilen kriterlere göre rastgele bir şifre oluşturur."""
  kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
  buyuk_harfler = kucuk_harfler.upper()
  rakamlar = "0123456789"
  semboller = "!@#$%^&*"

  karakterler = kucuk_harfler + buyuk_harfler

  # Seçilen kriterlere göre karakter kümelerini ekleyin
  if sayi_iste:
    karakterler += rakamlar
  if sembol_iste:
    karakterler += semboller

  sifre = ""
  for _ in range(uzunluk):
    sifre += random.choice(karakterler)

  return sifre

# Kullanıcıdan şifre uzunluğunu ve seçenekleri girmesini isteyin
print("Parola Oluşturucuya Hoş Geldiniz")
print("Parolanız küçük, büyük karakterler, sayı ve sembollerden oluşturulacaktır.")
sifre_uzunlugu = int(input("Parola için bir karakter sayısı belirtin: "))
sayi_iste = input("Şifrede sayı içersin mi? (evet/hayır) ").lower() == "evet"
sembol_iste = input("Şifrede sembol içersin mi? (evet/hayır) ").lower() == "evet"

# Oluşturulan şifreyi ekrana yazdırın
olusturulan_sifre = sifre_olustur(sifre_uzunlugu, sayi_iste, sembol_iste)
print("Oluşturulan şifre:", olusturulan_sifre)
