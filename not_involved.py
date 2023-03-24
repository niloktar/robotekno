from tkinter import *

def hesapla():
    not1 = float(giris_not1.get())
    not2 = float(giris_not2.get())
    
    if not1 < 0 or not1 > 100 or not2 < 0 or not2 > 100:
        sonuc.config(text="Lütfen geçerli bir not giriniz")
    elif not2 < 50:
        sonuc.config(text="İkinci sınavdan en az 50 almanız gerekiyor")
    else:
        ortalama = (not1 + not2) / 2
        if ortalama >= 50:
            sonuc.config(text="Tebrikler, dersi geçtiniz! Ortalama: {:.2f}".format(ortalama))
        else:
            ikinci_sınav_puanı = (50 - (not1 * 0.50)) / 0.5
            sonuc.config(text="Dersten geçmek için ikinci sınavdan en az {:.2f} almanız gerekiyor".format(ikinci_sınav_puanı))

def yeniden_hesapla():
    giris_not1.delete(0, END)
    giris_not2.delete(0, END)
    sonuc.config(text="")

pencere = Tk()
pencere.geometry("320x230")
pencere.title("Not Ortalaması Hesaplama")

giris_not1 = Entry(pencere, width=10)
giris_not1.pack(pady=10)

giris_not2 = Entry(pencere, width=10)
giris_not2.pack(pady=10)

hesapla_buton = Button(pencere, text="Hesapla", command=hesapla)
hesapla_buton.pack(pady=10)

yeniden_hesapla_buton = Button(pencere, text="Yeniden Hesapla", command=yeniden_hesapla)
yeniden_hesapla_buton.pack(pady=10)

sonuc = Label(pencere, text="")
sonuc.pack()

pencere.mainloop()
