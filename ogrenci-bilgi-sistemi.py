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

print("İsim giriniz:")
isim = input()

ogrBilgi(isim)


connect.commit()
connect.close()