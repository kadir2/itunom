
import time


class araclar:
    def __init__( self , konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ):
        self.konumx = konumx
        self.konumy = konumy
        self.hiz = hiz
        self.yon = yon
        self.irtifa = irtifa
    

class quadcopter(araclar):
   def __init__(self, konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,motor_sayisi="bilinmiyor",motorların_durumu="pasif"):
         super().__init__(konumx, konumy, hiz, yon, irtifa)
         self.motor_sayisi = motor_sayisi
         self.motorların_durumu = motorların_durumu




class fixedwing(araclar):
    def __init__(self, konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,kanat_uzunlugu=0,motor_saayisi="bilinmiyor"):
        super().__init__(konumx, konumy, hiz, yon, irtifa)
        self.kanat_genisligi = kanat_uzunlugu
        self.kanat_tipi = motor_saayisi




quadcopter1 = quadcopter(0,0,0,0,0,4,"aktif")

print(quadcopter1.motorların_durumu)
print(quadcopter1.motor_sayisi)
