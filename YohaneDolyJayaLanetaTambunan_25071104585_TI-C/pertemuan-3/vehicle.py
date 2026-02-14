class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
    
    def sound(self):
        return "suara"


class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, warna):
        super().__init__(jenis, merk, tahun_rilis)   # WAJIB
        self.__warna = warna 
        
    def get_warna(self):
        return self.__warna


class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, rating):
        super().__init__(jenis, merk, tahun_rilis)   # WAJIB
        self.__rating = rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_rating(self):
        return self.__rating


p1 = Vehicle('ferari', 'full', 2007)
Mobil1 = Mobil('avanza', 'toyota', 2008, 'hitam')
Motor1 = Motor('nmax', 'yamaha', 2009, 10)

for x in (p1, Mobil1, Motor1):
    print(x.jenis)
    print(x.merk)
    print(x.sound())   # harus di print
  
