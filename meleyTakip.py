import pyautogui as py
from datetime import datetime
import time
from datetime import timedelta

def SureTut():
    durum="duruyor"

    if durum=="duruyor":
        while True:

            try:
                boss=py.locateOnScreen("idall.png",confidence=0.8)
                suan=datetime.now()

                if boss:
                    bossCikti=suan.strftime("%d/%m/%Y %H:%M")
                    print(bossCikti," zamanında boss göründü.")
                    durum="çalışıyor"
                    break

            except py.ImageNotFoundException:
                print("Boss bulunamadı.")
            time.sleep(0.5)


    if durum=="çalışıyor":
        baslangic = time.time()
        onceki = -1

        while True:
            gecen = time.time() - baslangic
            kalan = 120 - gecen
            if kalan <= 0:
                baslangic = time.time()
                kalan = 120

            if int(kalan) != onceki:
                onceki = int(kalan)
                dakika, saniye = divmod(int(kalan), 60)
                print(f"{dakika:02d}:{saniye:02d}")
                if kalan <= 30:
                    print("Zaman azalıyor")

            try:
                bitis=py.locateOnScreen("yazi.png",confidence=0.8)
                if bitis:
                    durum="durdu"
                    print("Program durdu")
                    break
            except py.ImageNotFoundException:
                pass
            time.sleep(0.2)

def bakacaz():
    suan=datetime.now()

    loncalar={

    }
    for a in range(5):
        ekle=input("Lonca ismi: ")
        sure=int(input("Süre: "))
        loncalar[ekle]=suan + timedelta(hours=-sure)
        print("Eklendi")
        #Geçici olarak yaptım deneme amaçlı


        


    sonrasi=suan + timedelta(hours=-2)
    a=sonrasi.strftime("%d/%m/%y %H:%M")
    b=datetime.strptime(a,"%d/%m/%y %H:%M")



    for lonca , zaman in loncalar.items():
        if zaman < b:
            print(f"{lonca} süresi geçti")
        else:
            print(f"{lonca} süresi var")

suan=datetime.now()
loncalar={

}

def kayitAl():
    isim=input("Lonca ismini gir: ")
    zaman=suan
    if isim in loncalar[isim]:
        print(f"{isim} zaten mevcut!")
    else:
        loncalar[isim]=zaman

    for lonca,zaman in loncalar.items():
        if lonca>10:
            loncalar.pop(lonca,zaman[0])
