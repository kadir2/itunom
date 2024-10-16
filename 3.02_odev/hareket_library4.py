import time
import random

#duraklar = []
#duraklar.append([29.01541, 41.10623]) #ilk durak
#duraklar.append([29.03553, 41.11044]) #ikinci durak
#duraklar.append([29.02411, 41.10093]) #son durak


#fixedwing_duraklar = quadcopter_duraklar       #duraklar aynı olunca


zaman_sabiti = 0.00001

def func(arac):
    

    def git():

        hiz_orantisiti = None
        isaret = None


        hiz_orantisiti = float(hedefy-arac.konum[1]) / float(abs(arac.konum[0]-hedefx))


        print(f"{arac.isim} Hız oranı: ", hiz_orantisiti,"\n")
        print(f"{arac.duraklar[-1]}")

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
        print(f"{arac.isim} {arac.durak_sayaci + 1}. durakta")    

               

    
   



    while True:
         print(f"arac.duraklar[arac.durak_sayaci]: {arac.duraklar[arac.durak_sayaci]}")
         hedefx = arac.duraklar[arac.durak_sayaci][0]
         hedefy = arac.duraklar[arac.durak_sayaci][1]
         time.sleep(0.4)
         git()
         print(f"test kısmıııı   {arac.isim}  {arac.durak_sayaci}")
         arac.durak_sayaci += 1
         if arac.duraklar[arac.durak_sayaci-1] == arac.duraklar[-1]:
            print(f"{arac.isim} Son durakta")
            break
            

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
     