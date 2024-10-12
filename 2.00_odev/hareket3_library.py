import time
konumx = 29.02320
konumy = 41.10161

def func():
    print("func() fonksiyonu çalıştı.")

    while True:
     konumx -= 0.0001
     konumy += 0.000059230769
     time.sleep(0.1)
     return (konumx,konumy)

def veri_al(self):
        return (self.konumx,self.konumy)
     
