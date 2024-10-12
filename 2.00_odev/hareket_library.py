def hareket(arac1,arac2):
      
    if not hasattr(hareket, "hop"):
        hareket.hop = 29.02320
        hareket.hop2 = 41.10161
    arac1.konumx = hareket.hop
    arac1.konumy = hareket.hop2
    hareket.hop  -= 0.0001
    hareket.hop2 += 0.000059230769
    print("%.5f" % float(hareket.hop), "%.5f" % float(hareket.hop2))

    def oku(self):
        return (self.konumx,self.konumy)

    if hareket.hop <= 29.01541:
        print("aşama 2:") 

        if not hasattr(hareket, "mop"):
            hareket.mop1 = 29.01540
            hareket.mop2 = 41.10623
        hareket.mop1 += 0.0001
        hareket.mop2 += 0.000020914059
        print("%.5f" % float(hareket.mop1), "%.5f" % float(hareket.mop2))

   


