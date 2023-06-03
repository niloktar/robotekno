import random

def bilmece_oyunu():
    bilmece_sorulari = [
        {
            "soru": "Göklerde uçan, kuyruğunda yanan, adı alev alan nedir?",
            "cevap": "yıldırım"
        },
        {
            "soru": "Yürüdükçe çoğalır, oturdukça erir. Nedir?",
            "cevap": "ayak izi"
        },
        {
            "soru": "Ne zaman ağlarsanız onlar güler. Nedir?",
            "cevap": "kahpe dostlar"
        },
        {
            "soru": "Hangi yolda araba gitmez?",
            "cevap": "saman yolu"
        },
        {
            "soru": "Karnında gız gız gız",
            "cevap": "zil"
        }
    ]

    random.shuffle(bilmece_sorulari)
    print("Bilmece oyununa hoş geldiniz!")
    print("Sorulacak sorulara cevap verebilirsiniz :)")
    for bilmece in bilmece_sorulari:
        print(bilmece["soru"])
        cevap = input("Cevabınızı girin: ")

        if cevap.lower() == bilmece["cevap"]:
            print("Tebrikler, doğru cevap!")
        else:
            print("Maalesef, yanlış cevap. Doğru cevap: " + bilmece["cevap"])

        devam_et = input("Devam etmek istiyor musunuz? (Evet/Hayır): ")
        if devam_et.lower() == "hayır":
            print("Oyun bitti. Teşekkürler!")
            break
        elif devam_et.lower != "evet":
            print("devam ediyorsunuz")
    
bilmece_oyunu()
