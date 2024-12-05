#Boy-Kilo Endeks Hesaplama 
import time

print("*** Boy Kilo Endeksi Hesaplama ***")
time.sleep(1)

boy = float(input("Boyunuzu Giriniz:"))
time.sleep(1)
kilo = float(input("Kilonuzu Giriniz:"))

def ondalık(boy):
    
    boy2 = str(boy**2)
    ilk_basamak = boy2[:1]
    iki_basamak = boy2[1:3]
    parametre = float(ilk_basamak + "." + iki_basamak)
    return parametre
parametre = ondalık(boy)

endeks = kilo/parametre
print("Kilo Endeksiniz",str(endeks)[:4])

if endeks <= 18.5:
    print("Zayıfsınız")
elif endeks > 18.5 and endeks <= 24.9:
    print("Kilonuz İdeal")
elif endeks >=30 and endeks<=34.9:
    print("1.Derecede Obezite")
    