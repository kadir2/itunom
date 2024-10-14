import time
import random

konumx = 29.02320    #kalkış noktası
konumy = 41.10161
irtifa = 0

hedefx=None
hedefy=None
hedefx1 = 29.01541   #ilk hedef
hedefy1 = 41.10623

hedefx2 = 29.03553   #ikinci hedef
hedefy2 = 41.11044

hedefx3 = 29.02411   #son hedef
hedefy3 = 41.10093




def func():
    global konumx
    global konumy
    global hedefx
    global hedefy





    def git(gelenx,geleny):
        veri1=gelenx
        veri2=geleny
        global konumx
        global konumy
        

        sabit=1
        egim=float((veri2-hedefy)/(veri1-hedefx))

        if egim < 0 and hedefx-veri1 < 0:
            egim = -egim
            sabit = -1
        elif egim > 0 and hedefx-veri1 < 0:
                egim = -egim
                sabit = -1
        while True:
            veri1 += sabit*0.00001
            veri2 += egim*0.00001
            #print("{:.5f} {:.5f}".format(veri1,veri2))          #test amaçlı
            konumx=veri1
            konumy=veri2
            time.sleep(0.03)
            if hedefx==round(veri1,5):
                break    
            
    
    
    hedefx=hedefx1
    hedefy=hedefy1
    git(konumx,konumy)
    print("İlk durakk")
    #print("test 1",konumx,konumy)

    hedefx=hedefx2
    hedefy=hedefy2
    git(konumx,konumy)
    print("2. durakk")
    #print("test 2",konumx,konumy)


    hedefx=hedefx3
    hedefy=hedefy3
    git(konumx,konumy)
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
         irtifa -= 0.01
         time.sleep(0.1)

#def veri_al():
        #return "({:.5f} , {:.5f})".format(konumx,konumy)
     
