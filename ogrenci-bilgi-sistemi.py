import sqlite3

connect = sqlite3.connect("Ogrenci-Bilgi-Sistemi.db");

if(connect):
    print("Bağlantı Başarılı");
else:
    print("Bağlantı Başarısız");

safe = connect.cursor();

def dersNotuGetir(no):
    notlar = safe.execute("SELECT * From notlar WHERE ogrenci_no=?",(no,));
    results = notlar.fetchall();
    for rs in results:
        id,no,mat,fiz,biy = rs;
        print(f"Matematik:{mat} Fizik:{fiz} Biyoloji:{biy}")
    
def devamsizlikGetir(no):
    result = safe.execute("SELECT * From devamsizlik where ogrenci_no=?",(no,));
    
    for rs in result.fetchall():
        id,number,devamsizlik = rs;
        print(f"Bu öğrencinin devamsızlığı {devamsizlik}");     

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

def ogrBilgi(ad):
    veri = safe.execute("Select * from ogrenci WHERE ogrenci_adi=?",(ad,));
    result = veri.fetchall() #fetchall bir kere çağrılır ve bellekte tutulmaz veriler.Bir sonrakinde boş döner!!
    if(len(result) == 0):
        print("Öğrenci Bulunamadı!!");
        return 0;
    else:
        return result; 

def sorgu(no):
    veri = safe.execute("SELECT * FROM ogrenci WHERE ogrenci_no=?",(no,));
    result = veri.fetchall();
    if(len(result) == 0):
        return 0;
    else:
        return 1;
    
def devamsizlikSorgu(no):
    veri = safe.execute("SELECT * FROM devamsizlik WHERE ogrenci_no=?",(no,));
    result = veri.fetchall();
    if(len(result) == 0):
        return 0;
    else:
        return 1;

def notSorgu(no):
    veri = safe.execute("SELECT * FROM notlar WHERE ogrenci_no=?",(no,));
    result = veri.fetchall();
    if(len(result) == 0):
        return 0;
    else:
        return 1;

print("*"*5+"Öğrenci Bilgi Sistemine Hoşgeldiniz"+"*"*5);
print("""Öğrenci Bilgilerini görmek için ->1 \n 
      Yeni Öğrenci Eklemek İçin ->2 \n
      Ders Notu Eklemek İçin ->3\n
      Devamsızlık Eklemek İçin ->4\n
      """)

print("Yapmak istediğiniz işlemi giriniz:");
islem = int(input())
if (islem>0 and islem<5):
    if(islem ==1):
        print("Bigilerini öğrenmek istediğiniz öğrencinin adını girin:");
        isim = input();    
        result = ogrBilgi(isim);  
        if(result !=0):
            print(result);
            for row in result:
                id,no,adi,soyadi = row;
                numara = no;
            if(notSorgu(numara) == 1 and devamsizlikSorgu(numara) == 0):
                print("""Bu öğrencinin notlarını görmek için 1 tuşlayın.""")
                girdi = int(input());
                if(girdi == 1):
                    dersNotuGetir(numara);
                else:
                    print("Hatalı girdi");    
            elif(notSorgu(numara) == 0 and devamsizlikSorgu(numara) == 1):
                print("""Bu öğrencinin devamsızlığını görmek için 1 tuşlayın.""")
                girdi = int(input());
                if(girdi == 1):
                    devamsizlikGetir(numara);
                else:
                    print("Hatalı girdi");    
            elif(notSorgu(numara) == 1 and devamsizlikSorgu(numara) == 1):
                print("""Bu öğrencinin notlarını görmek için 1 tuşlayın.\nDevamsızlığını görmek için 2 yi tuşlayın""")
                girdi = int(input());
                if(girdi == 1):
                    dersNotuGetir(numara);
                elif(girdi == 2):
                    devamsizlikGetir(numara);    
                else:
                    print("Hatalı girdi");   
              
    elif(islem==2):
        print("Eklemek istediğiniz öğrencinin numarasını girin:")
        no = input()
        print("Eklemek istediğiniz öğrencinin adını girin:")     
        ad = input()
        print("Eklemek istediğiniz öğrencinin soyadını girin:")
        soyad = input()
        yeniOgrenci(no,ad,soyad)
    elif(islem ==3):
        print("Eklemek istediğiniz notdaki öğrencinin numarasını girin:")
        no= input()
        if(sorgu(no) == 1):
            print("Eklemek istediğiniz öğrencinin matematik notunu girin:")     
            mat = input()
            print("Eklemek istediğiniz öğrencinin fizik notunu girin:")
            fiz = input()             
            print("Eklemek istediğiniz öğrencinin biyoloji notunu girin:")
            biy = input()
            dersNotEkle(no,mat,fiz,biy);
        elif(sorgu(no) == 0):
             print("Sistemde bu numaraya ait bir öğrenci yok!!")
    elif(islem == 4):
        if(sorgu(no) == 1):
            print("Devamsızlığı olan öğrencinin numarasını girin:")
            no = input()
            print("Öğrencinin devamsızlık sayısını girin:")     
            dev = input()
            devamsizlikEkle(no,dev)
        elif(sorgu(no) == 0):
            print("Sistemde bu numaraya ait bir öğrenci yok!!")
else:
    print("Hatalı bir sayı girdiniz.");



connect.commit()
connect.close()