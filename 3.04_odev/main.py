import time
import threading
import tanımlama_library
import hareket_library4

Araclar = []
                                              #       konum   hız   hz_ktsy yön  irtifa  drk_sycı  duraklar     motor_durumu
Araclar.append(tanımlama_library.quadcopter("şimşek", [0, 0], [0, 0], 10,    0,      0,      0,     [],    [0, 0, 0, 0]))
Araclar.append(tanımlama_library.fixedwing("dişsiz",  [0, 0], [0, 0], 8,    0,      0,      0,     [],    2,   [0, 0]))
                                                                                                    #motor_sayısı

Araclar[0].duraklar.append([29.01541, 41.10623]) #ilk durak
Araclar[0].duraklar.append([29.03553, 41.11044]) #ikinci durak
Araclar[0].duraklar.append([29.02411, 41.10093]) #son durak

#for arac in Araclar:                                   duraklar aynıysa
   # arac.duraklar.append([29.01541, 41.10623]) 
   # arac.duraklar.append([29.03553, 41.11044])
   # arac.duraklar.append([29.02411, 41.10093])

Araclar[1].duraklar.append([29.03212, 41.10182]) #ilk durak
Araclar[1].duraklar.append([29.03292, 41.10920]) #ikinci durak
Araclar[1].duraklar.append([29.02411, 41.10093]) #son durak

print("Program başlatılıyor..")
for arac in Araclar:
    arac.set_baslangic_konum([29.02320, 41.10161])
    #Araclar[0].set_baslangic_konum([29.02320, 41.10161])
    #Araclar[1].set_baslangic_konum([29.02320, 41.10161])
    threading.Thread(target=hareket_library4.func, args=(arac,)).start() # argümanlar kısmına dikkat edilmeli




while True:
    for arac in Araclar:
        print(f"{arac.isim} Konum: {arac.get_konum()} Hız: {arac.hız} Yön: {arac.yön}° İrtifa: {arac.get_irtifa()} Motor Durumu: {arac.motor_durumu}")
    time.sleep(1)

    if Araclar[0].durak_sayaci == 3 and Araclar[1].durak_sayaci == 3:
        print(f"son durum bilgisi: {Araclar[0].isim} {Araclar[0].get_konum()} {Araclar[0].get_irtifa()} {Araclar[0].motor_durumu} \n {Araclar[1].isim} {Araclar[1].get_konum()} {Araclar[1].get_irtifa()} {Araclar[1].motor_durumu}")
        print("Program sonlandırıldı.")
        break
