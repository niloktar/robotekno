print("Not Hesaplama Uygulaması'na Hoş Geldiniz")

while True:
    birinci_sinav = float(input("Birinci sınav notunuzu girin: "))
    ikinci_sinav = float(input("Ikinci sınav notunuzu girin: "))

    ortalama = (birinci_sinav + ikinci_sinav) / 2

    if ortalama >= 50 and ikinci_sinav >= 50:
        print("Tebrikler, dersten geçtiniz! Ortalamanız: ", ortalama)
    elif ikinci_sinav < 50:
        print("Maalesef, ikinci sınavdan en az 50 almalısınız.")
    else:
        kac_almasi_gerekiyor = (50 - (birinci_sinav * 0.50)) / 0.5
        print("Dersten geçmek için ikinci sınavdan en az", kac_almasi_gerekiyor, "almalısınız.")

    devam_mi = input("Başka bir notunuzu hesaplamak istiyor musunuz? (E/H): ")
    if devam_mi.lower() == 'h':
        break
