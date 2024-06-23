#21100011001
#Derya Nailiye Kımırtı

import random
def menu():
    print("#"*10,"DERYA DERSHANELERİ","#"*10)
    print("1) Öğrenci Ekle")
    print("2) Sınav Ekle")
    print("3) Öğrenci Sil")
    print("4) Sınav Sil")
    print("5) Öğrenci Bilgilerini Güncelle")
    print("6) Sınav Bilgilerini güncelle")
    print("7) Öğrenci Arama")
    print("8) Sınav Arama")
    print("9) Öğrenci Listesi") #eski secenek
    print("10) Sınav Listesi")   #eski secenek
    print("11) Son Sinav Puanlari") #yeni secenek
    print("12) +18 Yas Ogrenciler") #yeni secenek
    print("13) Cikis")
    a = int(input("Seçiminiz:"))
    return a


def ogrenciEkleme():
    ogrenci={}     # Öğrenci bilgileri sözlük veri tipinde tutuldu.
    numara = random.randint(100,999)  #ogrenci no randomla atanır.
    ogrenci["NUMARA"] = numara
    isim = input("Adı:")
    ogrenci["ISIM"] = isim
    soyisim = input("Soyadı:")
    ogrenci["SOYISIM"] = soyisim
    yas = input("Yaş:")
    ogrenci["YAS"] = yas
    dosya = open("21100011001_ogrenciler.txt","a") # 'a' dosyanın sonundan yeni verileri eklemeye başlar.
    dosya.write(str(ogrenci) + "\n") #veriler alt alta yazdırılsın.
    print("Öğrenci Başarıyla Eklendi...✔")
    dosya.close()

def yeniSinav():
    sinav = {}
    sinavID = random.randint(1000,9999) #random sinavID atanir
    sinav["sinavID"] = sinavID
    ogrNo = input("Sınava Giren Öğrencinin Numarası>>>")
    sinav["OGRENCI NO."] = ogrNo
    turkceDogru = int(input("Türkçe Doğru Sayısı:"))
    sinav["TURKCE(dogru)"] = turkceDogru
    turkceYanlis = int(input("Türkçe Yanlış Sayısı:"))
    sinav["TURKCE(yanlis)"] = turkceYanlis
    turkceNet = turkceDogru - (float(turkceYanlis) / 4)
    sinav["TURKCE(net)"] = turkceNet
    matDogru = int(input("Matematik Doğru Sayısı:"))
    sinav["MAT(dogru)"] = matDogru
    matYanlis = int(input("Matematik Yanlış Sayısı:"))
    sinav["MAT(yanlis)"] = matYanlis
    matNet = matDogru - (float(matYanlis)/4)
    sinav["MAT(net)"] = matNet
    fenDogru = int(input("Fen Doğru Sayısı:"))
    sinav["FEN(dogru)"] = fenDogru
    fenYanlis = int(input("Fen Yanlış Sayısı:"))
    sinav["FEN(yanlis)"] = fenYanlis
    fenNet = fenDogru - (float(fenYanlis)/4)
    sinav["FEN(net)"] = fenNet
    sosyalDogru = int(input("Sosyal Doğru Sayısı:"))
    sinav["SOSYAL(dogru)"] = sosyalDogru
    sosyalYanlis = int(input("Sosyal Yanlış Sayısı:"))
    sinav["SOSYAL(yanlis)"] = sosyalYanlis
    sosyalNet = sosyalDogru - (float(sosyalYanlis)/4)
    sinav["SOSYAL(net)"] = sosyalNet

    sinavPuani = (turkceNet*3.75)+(matNet*3.75)+(fenNet*2.5)+(sosyalNet*2.5)
    sinav["PUAN:"] = sinavPuani

    dosya = open("21100011001_sinavlar.txt","a")
    dosya.write(str(sinav) + "\n")
    print("Sınav başarıyla eklendi...✔")
    dosya.close()

def ogrenciyiSil():
    num = input("Silinecek Öğrencinin Numarası>>>")
    dosya = open("21100011001_ogrenciler.txt","r")
    satir = []   # Dosyadaki satırları diziye eklemek için boş dizi

    for i in dosya:
        satir.append(i)  # satirları ekleme
    dosya.close()
    index =0
    for i in satir:
        index = index + 1   #girilen numaranın hangi satırda olduğunu bulma
        if num == i[11:14]:
            break

    yeniveri = ""
    k = open("21100011001_ogrenciler.txt","r")
    kaynak = k.read().splitlines() #satırları ayırmak icin
    for x,z in enumerate(kaynak,1):
        if x == index:
            continue
        yeniveri = yeniveri + z + "\n"
    k.close()
    with open("21100011001_ogrenciler.txt","w") as k:
        k.write(yeniveri)
    k.close()
    print("Öğrenci Başarıyla Silindi...✔")

def sinavSil():
    num = input("Silinecek Sınavın ID>>>")
    dosya = open("21100011001_sinavlar.txt", "r")
    satir = []
    for i in dosya:
        satir.append(i)
    dosya.close()
    index = 0
    for i in satir:
        index = index + 1
        if num == i[12:16]:
            break

    yeniveri = ""
    k = open("21100011001_sinavlar.txt", "r")
    kaynak = k.read().splitlines()
    for x, z in enumerate(kaynak, 1):
        if x == index:
            continue
        yeniveri = yeniveri + z + "\n"
    k.close()
    with open("21100011001_sinavlar.txt", "w") as k:
        k.write(yeniveri)
    k.close()
    print("Sınav Başarıyla silindi...✔")

def ogrenciGuncelle():
    num = input("Güncellenecek Öğrencinin Numarası>>>")
    dosya = open("21100011001_ogrenciler.txt", "r")
    satir = []  # Dosyadaki satırları diziye eklemek için boş dizi

    for i in dosya:
        satir.append(i)  # satirları ekleme
    dosya.close()
    index = 0
    for i in satir:
        index = index + 1  # girilen numaranın hangi satırda olduğunu bulma
        if num == i[11:14]:
            break

    yeniveri = ""
    k = open("21100011001_ogrenciler.txt", "r")
    kaynak = k.read().splitlines()
    for x, z in enumerate(kaynak, 1):
        if x == index:
            continue
        yeniveri = yeniveri + z + "\n"
    k.close()
    with open("21100011001_ogrenciler.txt", "w") as k:
        k.write(yeniveri)
    k.close()

    ogrenci = {}  # oğrenci bilgileri sözlük veri tipinde tutuldu.
    numara = random.randint(100,999)
    ogrenci["NUMARA"] = numara
    isim = input("Öğrencinin Adı:")
    ogrenci["ISIM"] = isim
    soyisim = input("Öğrencinin Soyadı:")
    ogrenci["SOYISIM"] = soyisim
    yas = input("Öğrencinin Yasi:")
    ogrenci["YAS"] = yas

    with open("21100011001_ogrenciler.txt", "a") as dosya:
        dosya.write(str(ogrenci) + "\n")
    print("Öğrenci Başarıyla Güncellendi...✔")
    dosya.close()

def sinavGuncelle():
    num = input("Güncellenecek Sınavın ID'si>>>")
    dosya = open("21100011001_sinavlar.txt", "r")
    satir = []
    for i in dosya:
        satir.append(i)
    dosya.close()
    index = 0
    for i in satir:
        index = index + 1
        if num == i[12:16]:
            break

    yeniveri = ""
    k = open("21100011001_sinavlar.txt", "r")
    kaynak = k.read().splitlines()
    for x, z in enumerate(kaynak, 1):
        if x == index:
            continue
        yeniveri = yeniveri + z + "\n"
    k.close()
    with open("21100011001_sinavlar.txt", "w") as k:
        k.write(yeniveri)
    k.close()

    sinav = {}
    sinavID = random.randint(1000,9999)
    sinav["sinavID"] = sinavID
    ogrNo = input("Sınava Giren Öğrencinin Numarasi>>>")
    sinav["OGRENCI NO."] = ogrNo
    turkceDogru = int(input("Türkçe Doğru Sayısı:"))
    sinav["TURKCE(dogru)"] = turkceDogru
    turkceYanlis = int(input("Türkçe Yanlış Sayısı:"))
    sinav["TURKCE(yanlis)"] = turkceYanlis
    turkceNet = turkceDogru - (float(turkceYanlis) / 4)
    sinav["TURKCE(net)"] = turkceNet
    matDogru = int(input("Matematik Doğru Sayısı:"))
    sinav["MAT(dogru)"] = matDogru
    matYanlis = int(input("Matematik Yanlış Sayısı:"))
    sinav["MAT(yanlis)"] = matYanlis
    matNet = matDogru - (float(matYanlis) / 4)
    sinav["MAT(net)"] = matNet
    fenDogru = int(input("Fen Doğru Sayısı:"))
    sinav["FEN(dogru)"] = fenDogru
    fenYanlis = int(input("Fen Yanlış Sayısı:"))
    sinav["FEN(yanlis)"] = fenYanlis
    fenNet = fenDogru - (float(fenYanlis) / 4)
    sinav["FEN(net)"] = fenNet
    sosyalDogru = int(input("Sosyal Doğru Sayısı:"))
    sinav["SOSYAL(dogru)"] = sosyalDogru
    sosyalYanlis = int(input("Sosyal Yanlış Sayısı:"))
    sinav["SOSYAL(yanlis)"] = sosyalYanlis
    sosyalNet = sosyalDogru - (float(sosyalYanlis) / 4)
    sinav["SOSYAL(net)"] = sosyalNet
    sinavPuani = (turkceNet * 3.75) + (matNet * 3.75) + (fenNet * 2.5) + (sosyalNet * 2.5)
    sinav["PUAN:"] = sinavPuani

    dosya = open("21100011001_sinavlar.txt", "a")
    dosya.write("\n" + str(sinav))
    print("Sınav başarıyla güncellendi...✔")
    dosya.close()


def ogrenciAra():
 try:
    num = input("Aranan Öğrencinin Numarası>>")
    int(num)
    dosya = open("21100011001_ogrenciler.txt", "r")
    satir = []  # Dosyadaki satırları diziye eklemek için boş dizi
    for i in dosya:
        satir.append(i)  # satirları ekleme
    dosya.close()
    index = 1
    for i in satir:
        if num == i[11:14]:
            print(f"{num} numaralı öğrenci, {index}. satırda bulunuyor.")
            break
        index+=1
    else:
        print(f"{num} numaralı öğrenci bulunamadı.")

 except ValueError:
     print("Hata: Ogrenci No icin sadece sayı kullanın.")
 except Exception as e:
     print("Hata oluştu:", str(e))



def sinavAra():
 try:
    num = input("Aranan Sınavın ID'si>>")
    int(num)
    dosya = open("21100011001_sinavlar.txt", "r")
    satir = []
    for i in dosya:
        satir.append(i)
    dosya.close()
    index = 0
    for i in satir:
        if num == i[12:16]:
            break
        index = index + 1

    if index < len(satir):
        print(satir[index])
    else:
        print("Sınav bulunamadı.")

 except ValueError:
     print("Hata: SinavID icin sadece sayı kullanın.")
 except Exception as e:
     print("Hata oluştu:", str(e))


def ogrenciListesi():
    dosya = open("21100011001_ogrenciler.txt","r")
    for i in dosya:
        print(i)
    dosya.close()

def sinavListesi():
    dosya = open("21100011001_sinavlar.txt","r")
    for i in dosya:
        print(i)
    dosya.close()

def yasUstuOgrenciler():
    with open("21100011001_ogrenciler.txt", "r") as dosya:
        ogrenciler = dosya.readlines()
    yasUstuOgrenciler = []
    for ogrenci in ogrenciler:
        ogrenciBilgileri = eval(ogrenci)  # eval() fonksiyonunu kullanarak satırı bir sözlük nesnesine dönüştürüyoruz
        if int(ogrenciBilgileri["YAS"]) >= 18:
            yasUstuOgrenciler.append(ogrenciBilgileri)
    print("18 Yaş Üstü Öğrenciler:")
    for ogrenci in yasUstuOgrenciler:
        print(ogrenci)


def sonToplamPuan():
    with open("21100011001_sinavlar.txt", "r") as dosya:
        sinavlar = dosya.readlines()
    toplamPuanlar = []
    for sinav in sinavlar:
        sinavBilgileri = eval(sinav)  #satırı bir sözlük nesnesine dönüştürüyoruz
        toplamPuan = (
            sinavBilgileri["TURKCE(net)"]*3.75
            + sinavBilgileri["MAT(net)"]*3.75
            + sinavBilgileri["SOSYAL(net)"]*2.5
            + sinavBilgileri["FEN(net)"]*2.5
        )
        toplamPuanlar.append(toplamPuan)
    print("Son Toplam Sınav Puanları:")
    for i, puan in enumerate(toplamPuanlar, 1):
        print(f"Sınav {i}: {puan}")

while 1: #ana menu
    secim = menu()

    if secim == 1:
        ogrenciEkleme()
    elif secim == 2:
        yeniSinav()
    elif secim == 3:
        ogrenciyiSil()
    elif secim == 4:
        sinavSil()
    elif secim == 5:
        ogrenciGuncelle()
    elif secim == 6:
        sinavGuncelle()
    elif secim == 7:
        ogrenciAra()
    elif secim == 8:
        sinavAra()
    elif secim == 9:
        ogrenciListesi()
    elif secim == 10:
        sinavListesi()
    elif secim == 11:
        sonToplamPuan()
    elif secim == 12:
        yasUstuOgrenciler()
    elif secim == 13:
        print("Cikis yapiliyor...")
        break  # cikis
    else:
        print("Yanlış tuşladınız! Tekrar deneyiniz...")
        menu()