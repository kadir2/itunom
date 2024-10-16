import time
import random




zaman_sabiti = 0.000001

def func(arac):
    

    def git():

        hiz_orantisiti = None
        isaret = None


        hiz_orantisiti = float(hedefy-arac.konum[1]) / float(abs(arac.konum[0]-hedefx))

        for i in range(0, len(arac.motor_durumu)):
                arac.motor_durumu[i] = 1
              

        #print(f"{arac.isim} Hız oranı: ", hiz_orantisiti,"\n")
        #print(f"{arac.duraklar[-1]}")

        if round(arac.konum[0],5) > hedefx:
            isaret = -1
        elif round(arac.konum[0],5) < hedefx:
            isaret = 1
        else:
            if arac.konum[1]<hedefy:
                isaret = 1
            else:
                isaret = -1
                                                           #kontrol et

        while round(arac.konum[0],5) != hedefx:


            arac.konum[0] += isaret * zaman_sabiti * arac.hız_katsayısı
            arac.konum[1] += hiz_orantisiti * zaman_sabiti * arac.hız_katsayısı
            time.sleep(0.03)

            #irtifa kısmı

            if arac.irtifa < 100 and arac.durak_sayaci == 0:                        # durak sayısı değişirse sıkıntı çıkarır     !!  
             arac.irtifa += random.uniform(0.07 , 0.09)

            elif arac.irtifa >= 100 and arac.durak_sayaci == 0:
                arac.irtifa = arac.irtifa + random.uniform(-0.04 , 0.04)

            elif arac.durak_sayaci == 1 and arac.irtifa >= 100:
                arac.irtifa = arac.irtifa + random.uniform(-0.04 , 0.04)

            elif   arac.durak_sayaci == 1 and arac.irtifa < 100:
                arac.irtifa += random.uniform(0.05 , 0.07)

            elif arac.durak_sayaci == 2:
               arac.irtifa -= arac.irtifa / (abs(hedefx-arac.konum[0]) / (zaman_sabiti * arac.hız_katsayısı))

            else:
                break


        if round(arac.konum[0],5) == round(arac.duraklar[-1][0],5) and round(arac.konum[1],5) != round(arac.duraklar[-1][1],5):           # olası konum hatası düzeltme
            while round(arac.konum[1],5) != arac.duraklar[-1][1]:
                arac.konum[1] += zaman_sabiti * arac.hız_katsayısı
                time.sleep(0.03)
        print(f"{arac.isim} {arac.durak_sayaci + 1}. durakta")    


           
               

    
   



    while True:
         #print(f"arac.duraklar[arac.durak_sayaci]: {arac.duraklar[arac.durak_sayaci]}")

         hedefx = arac.duraklar[arac.durak_sayaci][0]
         hedefy = arac.duraklar[arac.durak_sayaci][1]

         time.sleep(0.4)

         git()

         print(f"test kısmıııı   {arac.isim}  {arac.konum[0]}  {arac.konum[1]}")

         arac.durak_sayaci += 1

         if arac.duraklar[arac.durak_sayaci-1] == arac.duraklar[-1]:
            print(f"{arac.isim} Son durakta")

            for i in range(0, len(arac.motor_durumu)):
                arac.motor_durumu[i] = 0
            break
            