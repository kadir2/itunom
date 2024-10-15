import time
import random

hedefx=None
hedefy=None
hedefx1 = 29.01541   #ilk hedef
hedefy1 = 41.10623

hedefx2 = 29.03553   #ikinci hedef
hedefy2 = 41.11044

hedefx3 = 29.02411   #son hedef
hedefy3 = 41.10093

zaman_sabiti = 0.00001


def func(arac):

    def git():
        sabit=1
        egim=float((arac.konum[1]-hedefy)/(arac.konum[0]-hedefx))
        hiz_orantisiti = None
        isaret = None

        hiz_orantisiti = float(hedefy-arac.konum[1]) / float(abs(arac.konum[0]-hedefx))
        print("Hız oranı: ", hiz_orantisiti)

        if arac.konum[0] > hedefx:
            isaret = -1
        elif arac.konum[0] < hedefx:
            isaret = 1
        else:
            isaret = ""                                           #kontrol et

        while round(arac.konum[0],5) != hedefx:
            

            arac.konum[0] += isaret * zaman_sabiti * arac.hız_katsayısı
            arac.konum[1] += hiz_orantisiti * zaman_sabiti * arac.hız_katsayısı
            time.sleep(0.03)
    
    hedefx=hedefx1
    hedefy=hedefy1
    git()
    print("İlk durakk")
    #print("test 1",konumx,konumy)

    hedefx=hedefx2
    hedefy=hedefy2
    git()
    print("2. durakk")
    #print("test 2",konumx,konumy)


    hedefx=hedefx3
    hedefy=hedefy3
    git()
    print("son durakk")
    #print("test 3",konumx,konumy)

def yukseklik():
    global irtifa
    global hedefx
    global hedefx1
    global hedefx2
    global hedefx3

    while True:
     if irtifa < 100 and hedefx==hedefx1:
        irtifa += random.uniform(0.5 , 0.7)
        time.sleep(0.1)
     elif irtifa >= 100 and hedefx==hedefx1:
        irtifa = irtifa + random.uniform(-0.4 , 0.4)
        time.sleep(0.1)
     elif hedefx == hedefx2:
        irtifa = irtifa+random.uniform(-0.4 , 0.4)
        time.sleep(0.1)   
     elif irtifa >= 2 and hedefx == hedefx3:
        irtifa -= random.uniform(0.5 , 0.7)
        time.sleep(0.1)
     elif irtifa <= 3 and hedefx == hedefx3:
         irtifa -= 0.008
         time.sleep(0.1)
     