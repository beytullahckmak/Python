import sqlite3;

deneme = sqlite3.connect('deneme');

baglan = deneme.cursor();

if baglan:
    print("Bağlantı Başarılı ")
else:
    print("Bağlantı Başarısız")

veriler=baglan.execute('''
              SELECT * FROM yeni
               ''');

for veriler in veriler.fetchall():
    if veriler:
        print ("Uye Numarası:%s || Uye Adı:%s || Uye Soyadı:%s || Uye Memleketi:%s"%veriler)


deneme.commit();
deneme.close();