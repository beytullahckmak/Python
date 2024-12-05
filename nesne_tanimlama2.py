class Hayvan():
    print("Nesne Oluşturuldu..")
    
    def __init__(self,isim,tur,kategori):
        self.isim = isim
        self.tur = tur
        self.kategori = kategori
    def info(self):
        print("İsim:",self.isim)
        print("Tur:",self.tur)
        print("Kategori:",self.kategori)

class King(Hayvan):
    def __init__(self,isim,tur,kategori,liderlik):
        super().__init__(isim,tur,kategori)
        self.liderlik = liderlik  
    def info(self):
        super().info()
        print("Liderlik",self.liderlik)
    
    
aslan = Hayvan("Aslan","Yırtıcı",["memeli"])
leopar = Hayvan("Leopar","Yırtıcı",["memeli"])
gergedan = King("Gergedan","Otçul",["memeli"],"En Üst Seviye")

aslan.info()
leopar.info()
gergedan.info()