import time
konumx = 29.02320
konumy = 41.10161

hedefx1 = 29.01541
hedefy1 = 41.10623
hedefx2 = 29.03553
hedefy2 = 41.11044
hedefx3 = 29.02411
hedefy3 = 41.10093
sabit1 = 1
sabit2 = 1
sabit3 = 1



def func():
    global konumx
    global konumy
    global sabit1
    global sabit2
    global sabit3

    egim1=float((konumy-hedefy1)/(konumx-hedefx1))

    if egim1 < 0 and hedefx1-konumx < 0:
        egim1 = -egim1
        sabit1 = -1
    elif egim1 > 0 and hedefx1-konumx < 0:
        egim1 = -egim1
        sabit1 = -1    

    while True:
        konumx += sabit1*0.00001
        konumy += egim1*0.00001
        #print("{:.5f} {:.5f}".format(konumx,konumy))
        time.sleep(0.005)
        if konumx <= 29.01541:
            print(f"İlk durakk({konumx:.5f},{konumy:.5f})")
            break

    egim2=float((konumy-hedefy2)/(konumx-hedefx2))
    if egim2 < 0 and hedefx2-konumx < 0:
        egim2 = -egim2
        sabit2 = -1
    elif egim2 > 0 and hedefx2-konumx < 0:
        egim2 = -egim2
        sabit2 = -1    

    while True:
        konumx += sabit2*0.00001
        konumy += egim2*0.00001
        #print("{:.5f} {:.5f}".format(konumx,konumy))
        time.sleep(0.005)
        if konumx >= 29.03553:
            print(f"İkinci durak({konumx:.5f},{konumy:.5f})")
            break


    egim3=float((konumy-hedefy3)/(konumx-hedefx3))
    if egim3 < 0 and hedefx3-konumx < 0:
        egim3 = -egim3
        sabit3 = -1
    elif egim3 > 0 and hedefx3-konumx < 0:
        egim3 = -egim3
        sabit3 = -1


    while True:
        konumx += sabit3*0.00001
        konumy += egim3*0.00001
        #print("{:.5f} {:.5f}".format(konumx,konumy))
        time.sleep(0.005)
        if konumx <= 29.02411:
            print(f"Son durak({konumx:.5f},{konumy:.5f})")
            break


def veri_al():
        return "{:.5f},{:.5f}".format(konumx,konumy)
     
