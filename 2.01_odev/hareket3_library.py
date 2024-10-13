import time
konumx = 29.02320
konumy = 41.10161

hedefx1 = 29.01541
hedefy1 = 41.10623
hedefx2 = 29.03553
hedefy2 = 41.11044
hedefx3 = 29.02411
hedefy3 = 41.10093

def func():
    global konumx
    global konumy

    print("Kalkışa geçiliyor..")
    time.sleep(1)
    
    while True:
      konumx -= 0.0001
      konumy += 0.000059230769
      time.sleep(0.1)
      if konumx <= 29.01541:
        print("İlk durak")
      if konumx <= 29.01541:
        break
    
    print("İlk durağa ulaşıldı")
    while True:
      konumx += 0.0001
      konumy += 0.000020914059
      time.sleep(0.1)
      if konumx >= 29.035529:
        break
    print("İkinci durağa ulaşıldı")

    while True:
        konumx -= 0.0001
        konumy -= 0.000083274956
        time.sleep(0.1)
        if konumx == 29.02411:
            print("Son durak")
        if konumx <= 29.02412:
            break
    print("Son durağa ulaşıldı")

def veri_al():
        return "{:.5f},{:.5f}".format(konumx,konumy)
     
