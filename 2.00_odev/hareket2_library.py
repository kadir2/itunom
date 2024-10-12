import time
class abcd:
    def __init__(self,konummx=0,konummy=0):
        self.konummx = konummx
        self.konummy = konummy

    def veri_al(self):
        return (self.konummx,self.konummy)
    





birinci = abcd(29.02320, 41.10161)
ikinci = abcd(0,0)

while birinci.konummx >= 29.01541:
    print(birinci.veri_al())
    birinci.konummx -= 0.0001
    birinci.konummy += 0.000059230769
    time.sleep(0.1)



