import tkinter as tk
from tkinter import messagebox

# Kayıt bilgilerini gösteren fonksiyon
def show_info():
    name = name_entry.get()
    age = age_entry.get()
    favorite_color = color_entry.get()
    
    info = f"Ad: {name}\nYaş: {age}\nEn Sevdiğiniz Renk: {favorite_color}"
    messagebox.showinfo("Bilgileriniz", info)

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Kayıt Formu")

# Etiketler ve Giriş Kutuları
tk.Label(root, text="Adınızı girin:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Yaşınızı girin:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="En sevdiğiniz yemeği girin:").grid(row=2, column=0, padx=10, pady=5)
color_entry = tk.Entry(root)
color_entry.grid(row=2, column=1, padx=10, pady=5)

# Kayıt ol butonu
register_button = tk.Button(root, text="Kayıt Ol", command=show_info)
register_button.grid(row=3, column=0, columnspan=2, pady=10)

# Ana döngüyü başlatma
root.mainloop()
