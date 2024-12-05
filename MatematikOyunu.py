import random
import time

#Toplama,Çıkarma,Çarpma,Faktoriyel

secim = random.randint(1,4)
print("Oyun Yükleniyor Lütfen Bekleyiniz...")
time.sleep(2)

if secim == 1:
    print("Toplama İşlemi ->>")
    time.sleep(1)
    sayi1 = random.randint(1,20)
    sayi2 = random.randint(1,20)
    print("Soru:",sayi1,"ile",sayi2,"Sayılarının Toplamı Nedir?")
    cevap = int(input("Cevap:"))
    time.sleep(2)
    if(cevap == sayi1+sayi2):
        print("Tebrikler Doğru Bildiniz!!")
    else:
        print("Hatalı Cevap\nDoğru Cevap:",sayi1+sayi2)
elif secim == 2:
    print("Çıkarma İşlemi ->>")
    time.sleep(1)
    sayi1 = random.randint(1,20)
    sayi2 = random.randint(1,20)
    print("Soru:",sayi1,"ile",sayi2,"Sayılarının Farkı Nedir?")
    cevap = int(input("Cevap:"))
    time.sleep(2)
    if(cevap == sayi1-sayi2):
        print("Tebrikler Doğru Bildiniz!!")
    else:
        print("Hatalı Cevap\nDoğru Cevap:",sayi1-sayi2)

elif secim == 3:
    print ("Çarpma İşlemi->>")
    time.sleep(1)
    sayi1 = random.randint(1,20)
    sayi2 = random.randint(1,20)
    print("Soru:",sayi1,"ile",sayi2,"'nin Çarpımı Nedir?")
    time.sleep(2)
    cevap = int(input("Cevap:"))
    if (cevap == sayi1*sayi2):
        print("Tebrikler Doğru Bildiniz!!")
    else:
        print("Hatalı Cevap\nDoğru Cevap:",sayi1*sayi2)
    
elif secim == 4:
    print ("Faktöriyel İşlemi->>")
    time.sleep(1)
    sayi = random.randint(1,10) 
    def faktor(rand_sayi):
        factorial = 1
        for i in range(1,rand_sayi + 1):
            factorial = factorial*i
        return factorial
   
    print("Soru:",sayi,"'in Faktöriyeli Nedir?")
    time.sleep(2)
    cevap = int(input("Cevap:"))
    if (cevap == faktor(int(sayi))):
        print("Tebrikler Doğru Bildiniz!!")
    else:
        print("Hatalı Cevap\nDoğru Cevap:",faktor(int(sayi)))
    
    
    
    