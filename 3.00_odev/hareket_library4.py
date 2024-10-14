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

zaman_sabiti = 0.03


def func(arac):

    def git():
        sabit=1
        egim=float((arac.konum[1]-hedefy)/(arac.konum[0]-hedefx))

        if egim < 0 and hedefx-arac.konum[0] < 0:
            egim = -egim
            sabit = -1
        elif egim > 0 and hedefx-arac.konum[0] < 0:
                egim = -egim
                sabit = -1
        while True:
            arac.konum[0] += sabit*0.00001 * arac.hız_katsayısı
            arac.konum[1] += egim*0.00001 * arac.hız_katsayısı
            #print("{:.5f} {:.5f}".format(Arac.konum[0],Arac.konum[1]))          #test amaçlı
            arac.konum[0] = arac.konum[0]
            arac.konum[1] = arac.konum[1]
            time.sleep(zaman_sabiti)
            if hedefx==round(arac.konum[0],5):
                break    
    
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
     