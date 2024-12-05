import sqlite3

connect = sqlite3.connect("veriler.db") #Varsa Bağlanır Yoksa Yeni Database Oluşturur.

if(connect):
    print("Bağlantı Başarılı")
else:
    print("Bağlantı Başarısız!")
    
deneme = connect.cursor() #CURSOR NESNESİ OLUŞTURUR VERİ TABANINA BAĞLANMIŞ BİR ŞEKİLDE İŞLERİMİZİ DAHA KOLAY YAPARIZ

#deneme.execute('''
#CREATE TABLE kitaplar(
#    kitap_no INTEGER PRIMARY KEY,
#    kitap_adi VARCHAR(50),
#    kitap_kategori INTEGER(2))
#''') Tablo Oluşturulduğu için tekrar oluşturmamıza gerek yok.

kitaplar = deneme.execute("SELECT * FROM kitaplar") 

for k in kitaplar.fetchall():
    print("Kitap Numarası:%s §§ Kitap Adı:%s && Kitap Kategorisi:%s"%k)

connect.commit()#BAĞLANTIYI TEKRAR GÖNDERİR / YAPTIĞIMIZ DEĞİŞİKLİKLERİ KAYDETMEK İÇİN
connect.close()#BAĞLANTIYI KAPATIR
