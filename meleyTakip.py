import pyautogui as py
from datetime import datetime
import time
from datetime import timedelta
import json

def kayitAc():
    try:
        with open("gecmis.json","r",encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

loncalar=kayitAc()

def kaydet():
    with open("gecmis.json","w",encoding="UTF-8") as file:
        json.dump(loncalar,file)


def kayitAl(isim):
    suan=datetime.now()
    zaman=suan.strftime("%H:%M %d/%m/%Y")
    
    if isim not in loncalar:
         loncalar[isim]=[]

    loncalar[isim].append(zaman)
        
    print("Kayıt yapıldı.")

    if len(loncalar[isim])>10:
        loncalar[isim].pop(0)

    kaydet()




def SureTut():
    durum="duruyor"

    if durum=="duruyor":
        while True:

            try:
                boss=py.locateOnScreen("idall.png",confidence=0.8)
                suan=datetime.now()

                if boss:
                    bossCikti=suan.strftime("%H:%M %d/%m/%Y")
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


def gelecekKayit(isim):
    if isim in loncalar and loncalar[isim]:
        sonKayit=loncalar[isim][-1]
        eski=datetime.strptime(sonKayit,"%H:%M %d/%m/%Y")
        return eski + timedelta(hours=+2)
    else:
        return None

def sureHesaplama():

    suan=datetime.now()

    for lonca in loncalar:
        gelecek=gelecekKayit(lonca)
        if gelecek == None:
            print("Kayıt yok!")
        elif gelecek > suan:
            fark = gelecek - suan
            print(lonca, "Kalan süre:", str(fark).split(".")[0])
        else:
            print(lonca,"Süre geçti")




#isim=input("Lonca ismini giriniz: ")
sureHesaplama()




"""
def bakacaz():
    suan=datetime.now()


    for a in range(5):
        ekle=input("Lonca ismi: ")
        sure=int(input("Süre: "))
        loncalar[ekle]=suan + timedelta(hours=-sure)
        print("Eklendi")
        #Geçici olarak yaptım deneme amaçlı


        


    sonrasi=suan + timedelta(hours=-2)
    a=sonrasi.strftime("%H:%M %d/%m/%Y")
    b=datetime.strptime(a,"%H:%M %d/%m/%Y")



    for lonca , zaman in loncalar.items():
        if zaman < b:
            print(f"{lonca} süresi geçti")
        else:
            print(f"{lonca} süresi var")
"""