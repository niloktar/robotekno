import time

def giriş(): 
    print("""
    ********************
    Gece Okulda Kapalı Kaldın
    ********************
    Müdürün odasına girmen gerekiyor, çünkü anahtarı bulman lazım!
    Ancak odada 5 kutu var ve her birinin içinde bir sürpriz var.
    Soruları doğru cevaplayarak, doğru kutuyu bulmalısın!
    Unutma, yanlış cevap verirsen alarm çalar! 
    Başlamak için hazır mısın? (evet/hayır)
    """)
    seçim = input("> ").lower()
    if seçim == "evet":
        print("Harika! Macera başlıyor...\n")
        time.sleep(2)
        kutu_sec()
    else:
        print("Daha sonra görüşürüz!")
        exit()

def kutu_sec():
    print("Müdürün odasında 5 kutu var. Birini seçmelisin! Seçebileceğin kutular:")
    print("1. Kutu 1\n2. Kutu 2\n3. Kutu 3\n4. Kutu 4\n5. Kutu 5")
    kutu = input("> ")

    if kutu == "1":
        kutu1()
    elif kutu == "2":
        kutu2()
    elif kutu == "3":
        kutu3()
    elif kutu == "4":
        kutu4()
    elif kutu == "5":
        kutu5()
    else:
        print("Geçersiz kutu! Alarm çaldı!")
        alarm()

def kutu1():
    print("Kutu 1'i seçtin. Şimdi soruyu cevapla!")
    print("Soru: Hangisi bir string'tir?")
    print("1. 'Python'\n2. 123\n3. True")
    cevap = input("> ")

    if cevap == "1":
        print("Doğru! Kutuyu açtın ve içinde **yiyecek** çıktı! Atıştırmalık kazandın...\n")
        time.sleep(2)
        kutu_sec()  # Yeni kutu seçilmesine olanak tanır
    else:
        print("Yanlış cevap! Alarm çaldı!")
        alarm()

def kutu2():
    print("Kutu 2'yi seçtin. Şimdi soruyu cevapla!")
    print("Soru: 'if koşulu sağlanmadığı durumlarda çalışacak olan kod bloğu hangisidir?")
    print("1. else: \n2. while True: \n3. def:")
    cevap = input("> ")

    if cevap == "1":
        print("Doğru cevap! Kutuyu açtın ve içinde **oyun konsolu** çıktı! Biraz eğlenceli vakit geçirebilirsin...\n")
        time.sleep(2)
        kutu_sec()  # Yeni kutu seçilmesine olanak tanır
    else:
        print("Yanlış cevap! Alarm çaldı!")
        alarm()

def kutu3():
    print("Kutu 3'ü seçtin. Şimdi soruyu cevapla!")
    print("Soru: Hangisi doğru bir değişken atamasıdır?")
    print("1. 10 = sayi\n2. sayi : 10\n3. sayi = 10")
    cevap = input("> ")

    if cevap == "3":
        print("Doğru! Kutuyu açtın ve içinde **karaoke seti** çıktı! Şimdi eğlenceli bir şarkı söyleme zamanı...\n")
        time.sleep(2)
        kutu_sec()  # Yeni kutu seçilmesine olanak tanır
    else:
        print("Yanlış cevap! Alarm çaldı!")
        alarm()

def kutu4():
    print("Kutu 4'ü seçtin. Şimdi soruyu cevapla!")
    print("Soru: Liste=[1,2,3,4] nin ilk öğesini 5 ile değiştirmek istiyorsun?")
    print("1. list.add(5)\n2. list[0] = 5\n3. list.append(5)")
    cevap = input("> ")

    if cevap == "2":
        print("Harika! Kutuyu açtın ve içinde **sınav soruları** çıktı! Zor zamanlar için strateji geliştirme zamanı...\n")
        time.sleep(2)
        kutu_sec()  # Yeni kutu seçilmesine olanak tanır
    else:
        print("Yanlış cevap! Alarm çaldı!")
        alarm()

def kutu5():
    print("Kutu 5'i seçtin. Şimdi son kutuyu açtın. Fakat önce bir soru var!")
    print("Soru: Python'da bir fonksiyon nasıl tanımlanır?")
    print("1. function() \n2. def() \n3. fun()")
    cevap = input("> ")

    if cevap == "2":
        print("Doğru! Kutuyu açtın ve içinde **anahtar** çıktı! Şimdi çıkmak için her şey hazır...\n")
        print("Artık okuldan kaçmak için anahtarını buldun! Oyunu kazandın ve başarıyla sınıftan kaçtın!")
        print("Kazandığın Ödüller: Yiyecek, Oyun Konsolu, Karaoke Seti, Sınav Soruları ve Anahtar! Her şey tamam!")
        exit()
    else:
        print("Yanlış cevap! Alarm çaldı!")
        alarm()

def alarm():
    print("\nAlarm çaldı! Herkes duydu ve seni yakaladılar!")
    print("Sınıfın dağılması gerekti ve güvenlik uyarı vermeye başladı.")
    print("Oyunu sonlandırıyorsunuz. Görüşmek üzere!")
    exit()

def yeniden_baslat():
    print("\nOyunu yeniden başlatmak isterseniz 'evet' yazın.")
    print("Çıkmak isterseniz 'hayır' yazın.")
    cevap = input("> ").lower()
    if cevap == "evet":
        giriş()
    else:
        print("Oyunu sonlandırıyorsunuz. Görüşmek üzere!")
        exit()

# Oyunu başlat
giriş()
