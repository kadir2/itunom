import Arac
import threading
import hareket_library4
import time

Araclar = []

Araclar.append(Arac.Quadcopter("şimşek", [0, 0], [0, 0], 1.5, 0, 0, [0, 0, 0, 0]))
Araclar.append(Arac.FixedWing("dişsiz", [0, 0], [0, 0], 1, 0, 0, 2, [0, 0]))

for arac in Araclar:
    arac.set_baslangic_konum([29.02320, 41.10161])
    threading.Thread(target=hareket_library4.func, args=(arac,)).start()


while True:
    for arac in Araclar:
        print(f"{arac.isim} Konum: {arac.get_konum()} Hız: {arac.hız} Yön: {arac.yön}° İrtifa: {arac.irtifa} Motor Durumu: {arac.motor_durumu}")
    time.sleep(1)
