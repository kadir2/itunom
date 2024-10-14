import time
import threading
import hareket_library





class araclar:
    def __init__( self ,isim="tanımsız", konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ):
        self.isim = isim
        self.konumx = konumx
        self.konumy = konumy
        self.hiz = hiz
        self.yon = yon
        self.irtifa = irtifa
    
    def konum(self):
        return (self.konumx,self.konumy)

class quadcopter(araclar):
   def __init__(self,isim="tanımsız", konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,motor_sayisi="bilinmiyor",motorlarin_durumu="pasif"):
         super().__init__(isim, konumx, konumy, hiz, yon, irtifa)
         self.motor_sayisi = motor_sayisi
         self.motorların_durumu = motorlarin_durumu




class fixedwing(araclar):
    def __init__(self,isim="tanımsız", konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,kanat_uzunlugu=0,motor_saayisi="bilinmiyor",motorlarin_durumu="pasif"):
        super().__init__(isim, konumx, konumy, hiz, yon, irtifa)
        self.kanat_genisligi = kanat_uzunlugu
        self.motor_sayisi = motor_saayisi
        self.motorların_durumu = motorlarin_durumu




arac1 = quadcopter("şimsek",0,0,0,0,0,4,"aktif")
arac2 = fixedwing("dişsiz",0,0,0,0,0,120,2,"aktif")

print("başlatılıyor..")
time.sleep(0.5)
print(f"{arac1.isim} çalıştırılıyor..")
time.sleep(0.1)
print(f"{arac2.isim} çalıştırılıyor..")
time.sleep(0.5)
#print(f"şimşek motor sayısı:{arac1.motor_sayisi}\ndişsiz kanat genişliği:{arac2.kanat_genisligi} motor sayısı:{arac2.motor_sayisi}")

#while True:
    #print(f"{arac1.isim}  Konum: {arac1.konum()} Hız: {arac1.hiz} Yön: {arac1.yon}° İrtifa: {arac1.irtifa} Motorların Durumu: {arac1.motorların_durumu}")
    #print(f"{arac2.isim}  Konum: {arac2.konum()} Hız: {arac2.hiz} Yön: {arac2.yon}° İrtifa: {arac2.irtifa} Motorların Durumu: {arac2.motorların_durumu}")
    #time.sleep(1)

#while True:
 #   if (hareket_library.hareket(arac1,arac2) == 1):
   #     break
  #  time.sleep(0.1)
  




print("kalkışa geçiliyor..")
threading.Thread(target=hareket_library.func).start()    # START

#t=threading.Thread(target=hareket_library.func)
#t.start()

threading.Thread(target=hareket_library.yukseklik).start()    


while True:
    time.sleep(1)
    arac1.konumx = "{:.5f}".format(hareket_library.konumx)
    arac1.konumy = "{:.5f}".format(hareket_library.konumy)
    arac1.irtifa = "{:.2f}".format(hareket_library.irtifa)
    print(f"{arac1.isim}  Konum: {arac1.konum()} Hız: {arac1.hiz} Yön: {arac1.yon}° İrtifa: {arac1.irtifa} Motorların Durumu: {arac1.motorların_durumu}")
    print(f"{arac2.isim}  Konum: {arac2.konum()} Hız: {arac2.hiz} Yön: {arac2.yon}° İrtifa: {arac2.irtifa} Motorların Durumu: {arac2.motorların_durumu}")
    
    


    
