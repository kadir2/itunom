import time
import random
import math



zaman_sabiti = 0.000001
konumlar = [0,0,0,0,0,0,0,0]
q = 0
z = 0


def func(arac):
    

    def git():

        hiz_orantisi_y = None
        isaret = None
        


        # hız hesaplama kısmı
        def hiz_hesapla(f_y, f_x, l_y, l_x):     #f_y = first y, f_x = first x, l_y = last y, l_x = last x
        

            r= 6371 #dünya yarıçapı


            f_y = math.radians(f_y)
            f_x = math.radians(f_x)
            l_y = math.radians(l_y)
            l_x = math.radians(l_x)

            en = l_y - f_y
            boy = l_x - f_x

            

            a = abs(math.sin(en / 2) ** 2 + math.cos(f_y) * math.cos(l_y) * math.sin(boy / 2) ** 2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


            mesafe = r * c
            return mesafe


        def irt_yon():

            global q
            global z
            global hiz_sabiti

            #yön kısmı
            arac.yön = math.degrees(math.atan2(hedefy-arac.konum[1], hedefx-arac.konum[0]))



            


                                        #hız kısmı
            if arac.id == "0001": 
                if q % 2 == 0:
                    konumlar[0]=arac.konum[0]
                    konumlar[1]=arac.konum[1]
                else:
                    konumlar[2]=arac.konum[0]
                    konumlar[3]=arac.konum[1]  

                q += 1      
                if q%4 == 0:
                    arac.hız = hiz_hesapla(konumlar[0],konumlar[1],konumlar[2],konumlar[3])/0.24*3600

            elif arac.id == "0002":
                if z % 2 == 0:
                    konumlar[4]=arac.konum[0]
                    konumlar[5]=arac.konum[1]
                else:
                    konumlar[6]=arac.konum[0]
                    konumlar[7]=arac.konum[1]  

                z += 1    

            
                if z%4 == 0:
                    arac.hız = hiz_hesapla(konumlar[4],konumlar[5],konumlar[6],konumlar[7])/0.24*3600 



            if arac.hız > arac.hiz_siniri[1]:
                arac.hiz_sabiti -= arac.hiz_sabiti/10
       

            if arac.hız < arac.hiz_siniri[0]:
                arac.hiz_sabiti += arac.hiz_sabiti/10

            if arac.durak_sayaci == 2 and arac.hız >13 and abs(arac.duraklar[2][0]-arac.duraklar[1][0])/2 > abs(arac.konum[0]-arac.duraklar[2][0]) and abs(arac.duraklar[2][1]-arac.duraklar[1][1])/2 > abs(arac.konum[1]-arac.duraklar[2][1]):
                arac.hiz_sabiti -= arac.hiz_sabiti/10
            


            #irtifa kısmı

            if arac.irtifa < 100 and arac.durak_sayaci == 0:                        # durak sayısı değişirse sıkıntı çıkarır     !!  
             arac.irtifa += random.uniform(0.007 , 0.009) * arac.hiz_sabiti

            elif arac.irtifa >= 100 and arac.durak_sayaci == 0:
                arac.irtifa = arac.irtifa + random.uniform(-0.04 , 0.04)

            elif arac.durak_sayaci == 1 and arac.irtifa >= 100:
                arac.irtifa = arac.irtifa + random.uniform(-0.04 , 0.04)

            elif   arac.durak_sayaci == 1 and arac.irtifa < 100:
                arac.irtifa += random.uniform(0.005 , 0.007)  * arac.hiz_sabiti

            elif arac.durak_sayaci == 2 and hedefx != arac.konum[0]:
               arac.irtifa -= arac.irtifa / (abs(hedefx-arac.konum[0]) / (zaman_sabiti * arac.hiz_sabiti))









        for i in range(0, len(arac.motor_durumu)):
                arac.motor_durumu[i] = 1
              

      

        



        while round(arac.konum[0],5) != hedefx:

            if arac.konum[0] != hedefx:
                hiz_orantisi_y = float(hedefy-arac.konum[1]) / float(abs(arac.konum[0]-hedefx))
            else:
                hiz_orantisi_y = 1


            if round(arac.konum[0],5) > hedefx:
                isaret = -1
            elif round(arac.konum[0],5) < hedefx:
                isaret = 1
            else:
                if arac.konum[1]<hedefy:
                    isaret = 1
                else:
                    isaret = -1    


            irt_yon()


            arac.konum[0] += isaret * zaman_sabiti * arac.hiz_sabiti
            arac.konum[1] += hiz_orantisi_y * zaman_sabiti * arac.hiz_sabiti


            time.sleep(0.03)


            

           

            


        if round(arac.konum[0],5) == round(hedefx,5) and round(arac.konum[1],5) != round(hedefy,5):           # olası konum hatası düzeltme
           
            while round(arac.konum[1],5) != hedefy:

                if arac.konum[1] > hedefy:
                    arac.konum[1] -=  zaman_sabiti * arac.hiz_sabiti

                elif arac.konum[1] < hedefy:
                    arac.konum[1] += zaman_sabiti * arac.hiz_sabiti

                irt_yon()    
                  
                time.sleep(0.03)

        print(f"{arac.isim} {arac.durak_sayaci + 1}. durakta")  



           
               

    
   



    while True:                     
         #print(f"arac.duraklar[arac.durak_sayaci]: {arac.duraklar[arac.durak_sayaci]}")

         hedefx = arac.duraklar[arac.durak_sayaci][0]
         hedefy = arac.duraklar[arac.durak_sayaci][1]

         time.sleep(0.4)

         git()

         #print(f"test kısmıııı   {arac.isim}  {arac.konum[0]}  {arac.konum[1]}")

         arac.durak_sayaci += 1

         if arac.duraklar[arac.durak_sayaci-1] == arac.duraklar[-1]:
            print(f"{arac.isim} Son durakta")

            for i in range(0, len(arac.motor_durumu)):
                arac.motor_durumu[i] = 0

            arac.hız = 0
    
            break