# CourseManagementSystem_with_Python
# Dershane Otomasyonu – Yapılacak İşlemler 
1. Öğrenci Bilgileri: isim, soyisim, yas isminde “karakter” tipindeki değişkenler; numara ise (random) “integer” tipinde değişken barındıracaktır.  
2. Sınav Bilgileri: sinavID, turkceDogru, turkceYanlis, matDogru, matYanlis, fenDogru, fenYanlis, sosyalDogru, sosyalYanlis “integer” tipindeki değişkenler; turkceNet, matNet, fenNet, sosyalNet ve sinavPuani “float” tipinde; işlem yapılacak olan öğrenci numarası ogrNo “string” tipinde değişken barındıracaktır.
   
Uygulamada Yapılması Gerekenler:  
1. Tüm öğrenci bilgileri “ogrenci” ismiyle sözlük(dict) tipinde tutulacaktır.  
2. Tüm sınav bilgileri “sinav” ismiyle sözlük(dict) tipinde tutulacaktır.  
3. Tüm öğrenci ve sınav bilgileri ayrı ayrı .txt uzantılı dosyalardan alınacaktır ve sözlüklerde atanacaktır.  
4. Kullanıcıya yeni kayıt, silme, güncelleme, arama, listeleri görüntüleme ve on sekiz yaş üstü öğrencilerin listesi seçenekleri sunulacaktır.
   
Uygulama Akışı:  
İlk olarak .txt uzantılı dosyada saklanan öğrenci ve sınav bilgileri dosyadan okunarak dizilere aktarılacak ve tüm bilgiler bu dizilerde saklanacaktır. Ardından, kullanıcının öğrenci veya sınav ekleme işlemi yapılabilecektir. Kullanıcı yeni bilgiler ekledikçe bunlar .txt uzantılı dosyalarda saklanacaktır. Kullanıcıya sunulan bilgi güncelleme, arama veya bilgilerin listelenmesi işlemleri bu dosyalar üzerinden gerçekleştirilecektir. İşlemini bitiren kullanıcı her seferinde yeni bir menü ekranı görecektir. Kullanıcı “çıkış” için gereken tuşlamayı yapmadığı sürece “menü” daima açık kalacaktır.  

Tanımlanacak Fonksiyonlar ve Görevleri:
1. menu(): Bu fonksiyon otomasyonun gereken özelliklerini her seferinde kullanıcıya sunar.  
2. ogrenciEkleme(): Bu fonksiyon, ogrenci bilgilerini dict tipinde tutar. Öğrenciye numarayı random bir şekilde atar. İsim Soyisim gibi bilgileri kullanıcıdan ister ve “ogrenciler.txt” dosyasına kaydeder.  
3. yeniSinav(): Bu fonksiyon, sınav bilgilerini dict tipinde tutar. Sınav ID sini random bir şekilde atar. Her dersin doğru yanlış sayılarını input ile alır ve puan hesabı yapar. Puanlar float tipinde alınır.  
4. ogrenciyiSil (): Silinmek istenen öğrencinin numarası istenir. Var olan dosya yeni bir satır şeklinde korumaya alınır ve istenilen numaradaki öğrenci silinir. Fakat diğer bilgiler silinmemiş olur.  
5. sinavSil(): Silinmek istenen sınavın ID si istenir. Var olan dosya yeni bir satır şeklinde korumaya alınır ve istenilen ID deki sınav silinir. Fakat diğer bilgiler silinmemiş olur.  
6. ogrenciGuncelle(): Bilgiler güncellenir  
7. sinavGuncelle(): Bilgiler güncellenir ve puan yeniden hesaplanır.  
8. ogrenciAra(): Kullanıcıdan numarasını ister ve girilen numarayla .txt dosyasından bilgi çeker.  
9. sinavAra(): Kullanıcıdan sınav ID sini ister ve girilen ID ile .txt dosyasından bilgi çeker. Kullanıcıya sunar.  
10. ogrenciListesi(): Öğrenci listesini görüntüler.  
11. sinavListesi(): Sınav listesini görüntüler. 
12. sonToplamPuan(): Yapılan sınavların genel puanlarını listeler.  
13. yasUstuOgrenciler(): Kayıtlı olan öğrencilerin yaş durumuna bağlı olarak +18 yaş öğrencileri seçip listeler. Fonksiyonlar içerisinde en az 2 tane oluşabilecek hatayı yakalayıp işleyen trycatch exception bloğu kullanılmıştır.
