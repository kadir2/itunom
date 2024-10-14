class Arac:
    def __init__(self, isim = "tanımsız", konum = [0, 0], hız = [0, 0], hız_katsayısı = 1, yön = 0, irtifa = 0):
        self.isim = isim
        self.konum = konum
        self.hız = hız
        self.hız_katsayısı = hız_katsayısı
        self.yön = yön
        self.irtifa = irtifa

    def set_baslangic_konum(self, konum):
        self.konum = konum
    
    def get_konum(self):
        return self.konum

class Quadcopter(Arac):
    def __init__(self, isim = "tanımsız", konum = [0, 0], hız = [0, 0], hız_katsayısı = 1, yön = 0, irtifa = 0, motor_durumu = [0, 0, 0, 0]):
        super().__init__(isim, konum, hız, hız_katsayısı, yön, irtifa)
        self.motor_durumu = motor_durumu

        if len(motor_durumu) != 4:
            print("Motor sayısı 4 olmalıdır.")
            self.motor_durumu = [0, 0, 0, 0]

class FixedWing(Arac):
    def __init__(self, isim="tanımsız", konum=[0, 0], hız=[0, 0], hız_katsayısı = 1, yön=0, irtifa=0, motor_sayısı = 1, motor_durumu = [0]):
        super().__init__(isim, konum, hız, hız_katsayısı, yön, irtifa)
        
        if len(motor_durumu) != motor_sayısı:
            print("Motor sayısı ile motor durumu uyuşmuyor.")
            motor_sayısı = len(motor_durumu)

        self.motor_sayısı = motor_sayısı
        self.motor_durumu = motor_durumu