import time

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
   def __init__(self,isim="tanımsız", konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,motor_sayisi="bilinmiyor",motorların_durumu="pasif"):
         super().__init__(isim, konumx, konumy, hiz, yon, irtifa)
         self.motor_sayisi = motor_sayisi
         self.motorların_durumu = motorların_durumu




class fixedwing(araclar):
    def __init__(self,isim="tanımsız", konumx=0 , konumy=0 , hiz=0 , yon=0 , irtifa=0 ,kanat_uzunlugu=0,motor_saayisi="bilinmiyor"):
        super().__init__(isim, konumx, konumy, hiz, yon, irtifa)
        self.kanat_genisligi = kanat_uzunlugu
        self.kanat_tipi = motor_saayisi




arac1 = quadcopter("simsek",0,0,0,0,0,4,"aktif")
arac2 = fixedwing("dissiz",0,0,0,0,0,120,2)

print("başlatılıyor..")
time.sleep(0.5)
print(f"simsek çalıştırılıyor..")
time.sleep(0.5)
print(f"dissiz çalıştırılıyor..")
time.sleep(0.7)

while True:
    print(f"{arac1.isim} {arac1.konum()} {arac1.hiz} {arac1.yon} {arac1.irtifa} {arac1.motor_sayisi} {arac1.motorların_durumu}")
    print(f"{arac2.isim} {arac2.konum()} {arac2.hiz} {arac2.yon} {arac2.irtifa} {arac2.kanat_genisligi} {arac2.kanat_tipi}")
    time.sleep(1)
