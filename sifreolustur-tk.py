import random
import string
import tkinter as tk

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

def sifre_olustur_buton_callback():
    sifre_uzunlugu = int(sifre_uzunlugu_giris.get())
    sayi_iste = sayi_iste_degisken.get()
    sembol_iste = sembol_iste_degisken.get()

    olusturulan_sifre = sifre_olustur(sifre_uzunlugu, sayi_iste, sembol_iste)
    sonuc_etiket.config(text="Oluşturulan Şifre: " + olusturulan_sifre)

# Ana uygulama penceresi oluştur
uygulama = tk.Tk()
uygulama.title("Şifre Oluşturucu")

# Etiketler ve giriş alanları oluştur
sifre_uzunlugu_etiket = tk.Label(uygulama, text="Parola Uzunluğu:")
sifre_uzunlugu_etiket.grid(row=0, column=0)

sifre_uzunlugu_giris = tk.Entry(uygulama)
sifre_uzunlugu_giris.grid(row=0, column=1)

sayi_iste_degisken = tk.BooleanVar()
sayi_iste_checkbutton = tk.Checkbutton(uygulama, text="Sayı İçersin mi?", variable=sayi_iste_degisken)
sayi_iste_checkbutton.grid(row=1, column=0)

sembol_iste_degisken = tk.BooleanVar()
sembol_iste_checkbutton = tk.Checkbutton(uygulama, text="Sembol İçersin mi?", variable=sembol_iste_degisken)
sembol_iste_checkbutton.grid(row=2, column=0)

sifre_olustur_buton = tk.Button(uygulama, text="Şifre Oluştur", command=sifre_olustur_buton_callback)
sifre_olustur_buton.grid(row=3, column=0, columnspan=2)  

sonuc_etiket = tk.Label(uygulama, text="")
sonuc_etiket.grid(row=4, column=0, columnspan=2, pady=10)

# Uygulamayı başlat
uygulama.mainloop()
