class Hayvan ():
    print("Hayvan Nesnesi Oluşturuldu.")
    tur = "memeli"
    
    def __init__(self):
        self.isim = []
        self.sayi = 0
    def deneme(self):
        self.sayi +=1

kanguru = Hayvan()
kanguru.isim.append("Kanguru")
print(kanguru.sayi)

kuş = Hayvan()
kuş.deneme()
kuş.isim.append("Kuş")
print(kuş.sayi)