import sqlite3

connect = sqlite3.connect("Ogrenci-Bilgi-Sistemi.db");

if(connect):
    print("Bağlantı Başarılı");
else:
    print("Bağlantı Başarısız");

safe = connect.cursor();

print("*"*5+"Öğrenci Bilgi Sistemine Hoşgeldiniz"+"*"*5);
print("""Öğrenci Bilgilerini görmek için ->1 \n 
      Yeni Öğrenci Eklemek İçin ->2 \n
      Ders Notu Eklemek İçin ->3\n
      Devamsızlık Eklemek İçin ->4\n
      """)


def ogrBilgi(ad):
    veri = safe.execute("Select * from ogrenci WHERE ogrenci_adi=?",(ad,));
    print(veri.fetchall())    

def yeniOgrenci(no,ad,soyad):
    ekle = safe.execute("INSERT INTO ogrenci(ogrenci_no,ogrenci_adi,ogrenci_soyadi) VALUES(?,?,?)",(no,ad,soyad));
    if ekle:
        print("Kayıt Başarılı");
    else:
        print("Kayıt Başarısız ");

def dersNotEkle(no,mat,fiz,biy):
    sonuc = safe.execute("INSERT INTO notlar(ogrenci_no,matematik,fizik,biyoloji) VALUES(?,?,?,?)",(no,mat,fiz,biy));
    if sonuc:
        print("Ders Notu Ekleme Başarılı..")
    else :
        print("İşlem Başarısız")

def devamsizlikEkle(no,devamsizlik):
    cikti = safe.execute("INSERT INTO devamsizlik(ogrenci_no,devamsizlik) VALUES (?,?)",(no,devamsizlik));
    if cikti:
        print("Veri Ekleme Başarılı")
    else:
        print("İşlem Başarısız")
print("Yapmak istediğiniz işlemi giriniz:");
islem = int(input())

if (islem>0 and islem<5):
    if(islem ==1):
        print("Bigilerini öğrenmek istediğiniz öğrencinin adını girin:");
        isim = input();
        ogrBilgi(isim);   
    if(islem==2):
        print("Eklemek istediğiniz öğrencinin numarasını girin:")
        no= input()
        print("Eklemek istediğiniz öğrencinin adını girin:")     
        ad = input()
        print("Eklemek istediğiniz öğrencinin soyadını girin:")
        soyad = input()
        yeniOgrenci(no,ad,soyad)
    if(islem ==3):
        print("Eklemek istediğiniz notdaki öğrencinin numarasını girin:")
        no= input()
        print("Eklemek istediğiniz öğrencinin matematik notunu girin:")     
        mat = input()
        print("Eklemek istediğiniz öğrencinin fizik notunu girin:")
        fiz = input()             
        print("Eklemek istediğiniz öğrencinin biyoloji notunu girin:")
        biy = input()
        dersNotEkle(no,mat,fiz,biy);
    if(islem == 4):
        print("Devamsızlığı olan öğrencinin numarasını girin:")
        no = input()
        print("Öğrencinin devamsızlık sayısını girin:")     
        dev = input()
        devamsizlikEkle(no,dev)
else:
    print("Hatalı bir sayı girdiniz.");



connect.commit()
connect.close()