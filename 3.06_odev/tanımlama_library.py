class Arac:
    def __init__(self, isim = "tanımsız", konum = [0, 0], hız = 0, hız_katsayısı = 1, yön = 0, irtifa = 0 , durak_sayaci = 0, duraklar = []):
        self.isim = isim
        self.konum = konum
        self.hız = hız
        self.hız_katsayısı = hız_katsayısı
        self.yön = yön
        self.irtifa = irtifa
        self.durak_sayaci = durak_sayaci
        self.duraklar = duraklar

    def set_baslangic_konum(self, konum):
        self.konum = konum
    
    def get_konum(self):
        self.konum = [round(self.konum[0], 5), round(self.konum[1], 5)]
        return self.konum
    
    def get_irtifa(self):
        return round(self.irtifa,2)

class quadcopter(Arac):
    def __init__(self, isim = "tanımsız", konum = [0, 0], hız = 0, hız_katsayısı = 1, yön = 0, irtifa = 0, durak_sayaci = 0, duraklar = [], motor_durumu = [0, 0, 0, 0]):
        super().__init__(isim, konum, hız, hız_katsayısı, yön, irtifa, durak_sayaci, duraklar)
        self.motor_durumu = motor_durumu

        if len(motor_durumu) != 4:
            print("Motor sayısı 4 olmalıdır.")
            self.motor_durumu = [0, 0, 0, 0]

class fixedwing(Arac):
    def __init__(self, isim="tanımsız", konum=[0, 0], hız = 0, hız_katsayısı = 1, yön = 0, irtifa = 0, durak_sayaci = 0, duraklar = [], motor_sayısı = 1, motor_durumu = [0]):
        super().__init__(isim, konum, hız, hız_katsayısı, yön, irtifa , durak_sayaci, duraklar)
        
        if len(motor_durumu) != motor_sayısı:
            print("Motor sayısı ile motor durumu uyuşmuyor.")
            motor_sayısı = len(motor_durumu)

        self.motor_sayısı = motor_sayısı
        self.motor_durumu = motor_durumu