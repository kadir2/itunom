
import time

a = time.time()

class araclar:
    def __init__( self , konumx , konumy , hiz , yon , irtifa ):
        self.konumx = konumx
        self.konumy = konumy
        self.hiz = hiz
        self.yon = yon
        self.irtifa = irtifa
    
    def konum(self):
        return self.konumx , self.konumy
    
    def hiz_(self):
        return self.hiz
    
    def yonu(self):
        return self.yon
    
    def irtifa_(self):
        return self.irtifa
    
    def hiz_degistir(self , hiz):
        self.hiz = hiz

    def yon_degistir(self , yon):
        self.yon = yon

    def irtifa_degistir(self , irtifa):
        self.irtifa = irtifa

    def konum_degistir(self , konumx , konumy):
        self.konumx = konumx
        self.konumy = konumy

class quadcopter(araclar):
    def __init__





class fixedwing(araclar):
    def __init__


drone1 = araclar( 0 , 0 , 0 , 0 , 0 )
drone2 = araclar( 0 , 0 , 0 , 0 , 0 )

print("Drone1 ilk ")
print(drone1.konum())
print(drone1.hiz_())
print(drone1.yonu())
print(drone1.irtifa_())

drone1.hiz_degistir( 10 )
drone1.yon_degistir( 45 )
drone1.irtifa_degistir( 100 )
drone1.konum_degistir( 10 , 10 )

print("Drone1 son: ")
print(drone1.konum())
print(drone1.hiz_())
print(drone1.yonu())
print(drone1.irtifa_())

print("Drone2 ilk ")
print(drone2.konum())
print(drone2.hiz_())
print(drone2.yonu())
print(drone2.irtifa_())

drone2.hiz_degistir( 20 )
drone2.yon_degistir( 90 )
drone2.irtifa_degistir( 200 )
drone2.konum_degistir(20,20)

print("Drone2 son: ")
print(drone2.konum())
print(drone2.hiz_())
print(drone2.yonu())
print(drone2.irtifa_())
b = time.time()

print("%.8f" % float(b-a))
print(a)
print(b)
    
