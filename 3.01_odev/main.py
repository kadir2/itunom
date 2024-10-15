import time
import threading
import tanımlama_library
import hareket_library4

Araclar = []

Araclar.append(tanımlama_library.quadcopter("şimşek", [0, 0], [0, 0],4 , 0, 0, [0, 0, 0, 0]))
Araclar.append(tanımlama_library.fixedwing("dişsiz", [0, 0], [0, 0], 1.5, 0, 0, 2, [0, 0]))

for arac in Araclar:
    arac.set_baslangic_konum([29.02320, 41.10161])
    #Araclar[0].set_baslangic_konum([29.02320, 41.10161])
    #Araclar[1].set_baslangic_konum([29.02320, 41.10161])
    threading.Thread(target=hareket_library4.func, args=(arac,)).start() # argümanlar kısmına dikkat edilmeli






while True:
    for arac in Araclar:
        print(f"{arac.isim} Konum: {arac.get_konum()} Hız: {arac.hız} Yön: {arac.yön}° İrtifa: {arac.irtifa} Motor Durumu: {arac.motor_durumu}")
    time.sleep(1)
