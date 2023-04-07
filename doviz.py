#Bu kod, bir pencere oluşturur ve döviz kurlarını bir API'den alarak türk lirası miktarını dolar ve euro karşılıklarına dönüştürür.
#requests kütüphanesini kullanarak API'den veri alırız. Kurları global değişkenlerde saklarız, 
#böylece hesaplama fonksiyonu bu verilere erişebilir. Hesaplama fonksiyonu, kullanıcının girdiği miktarı alır, 
#kurlarla çarpar ve sonucu etiketlere yazdırır. 
#Uygulamayı çalıştırdığınızda, verileri_al() fonksiyonu döviz kurlarını almak için otomatik olarak çağrılır.

import tkinter as tk
import requests

def döviz_hesapla():
    try:
        miktar = float(döviz_giriş.get())
        dolar = round(miktar / float(dolar_kuru), 2)
        euro = round(miktar / float(euro_kuru), 2)
        dolar_etiket.config(text=f"${dolar}")
        euro_etiket.config(text=f"€{euro}")
    except ValueError:
        dolar_etiket.config(text="Geçersiz miktar!")
        euro_etiket.config(text="Geçersiz miktar!")

def verileri_al():
    global dolar_kuru, euro_kuru
    response = requests.get("https://api.exchangerate-api.com/v4/latest/TRY")
    veriler = response.json()
    dolar_kuru = veriler["rates"]["USD"]
    euro_kuru = veriler["rates"]["EUR"]

root = tk.Tk()
root.title("Döviz Hesaplama")
root.geometry("300x200")
root.resizable(False, False)

verileri_al()

döviz_giriş = tk.Entry(root, width=10)
döviz_giriş.place(x=100, y=20)

tk.Label(root, text="TL", font=("Arial", 12)).place(x=200, y=20)

tk.Button(root, text="Hesapla", font=("Arial", 12), command=döviz_hesapla).place(x=120, y=50)

tk.Label(root, text="Dolar", font=("Arial", 12)).place(x=50, y=100)
tk.Label(root, text="Euro", font=("Arial", 12)).place(x=50, y=130)

dolar_etiket = tk.Label(root, font=("Arial", 12))
dolar_etiket.place(x=120, y=100)

euro_etiket = tk.Label(root, font=("Arial", 12))
euro_etiket.place(x=120, y=130)

root.mainloop()
