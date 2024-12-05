import time
class makine():
    
    def __init__(self):
        self.devir = 0
        self.mürekkep = 100
        self.şarj = 100 
        self.dergiler = []
    def calis(self):
        if(self.mürekkep<3):
            print("Hata Yeterli Mürekkep yok!!")
        elif(self.şarj<5):
            print("Yeterli Şarj Yok")
        else:
            self.devir +=1
            self.mürekkep -=3
            self.şarj -= 5
            print("Makine çalışıyor lütfen bekleyiniz..")
            time.sleep(0.5)
            if(self.devir ==20):
                self.devir = 0
                self.yeniDergi()
    def yeniDergi(self):
        print("Yeni Dergi Çıktı Hadi Gene iyisin :)")
        a = input("Derginin İsmi Ne olsun:")
        self.dergiler.append(a)
        time.sleep(1)
    def sarjDoldur(self):
        if(self.şarj<100):
            self.şarj += 10
            print("Şarj Dolduruldu Mevcut Şarj->",self.şarj+10)
            time.sleep(1)
    def mürekkepDoldur(self):
        if(self.mürekkep<100):
            self.mürekkep+=10
            print("Mürekkep Dolduruldu Mevcut Mürekkep->",self.mürekkep+10)
    def mevcutDurum(self):
        print("Makinenin Mevcut Durumu:")
        print("Mürekkep Yüzdesi:",self.mürekkep)
        print("Şarj Yüzdesi:",self.şarj)
        print("Toplam Çıkarılan Dergiler:",len(self.dergiler))
        if(len(self.dergiler)>0):
            print("Çıkarılan Dergiler:")
            for i in self.dergiler:
                print(i)
        print("Yeni Çıkacak Derginin %",self.devir*5,"Kısmı Tamamlandı")
        
        
makine1 = makine()

print("Matbama Hoşgeldiniz :) ")
while True:
    print("Makineyi çalıştırmak için -> 1 \n"
        "Makinenin durumunu öğrenmek için -> 2 \n" 
        "Makinenin şarjını doldrmak için -> 3 \n"
        "Makinenin mürekkebini doldurmak için -> 4 \n")
    komut = int(input("Yapmak istediğiniz işlemi giriniz:"))

    if(komut == 1):
        makine1.calis()
    elif(komut == 2):
        makine1.mevcutDurum()
    elif(komut == 3):
        makine1.sarjDoldur()
    elif(komut == 4 ):
        makine1.mürekkepDoldur()
    else:
         print("Hatalı bir karakter girdiniz.")
