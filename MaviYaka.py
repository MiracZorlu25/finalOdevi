
from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)

        self.yipranma_payi = yipranma_payi



    def get_yipranma_payi(self):
        return self.yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.tecrube <= 2:
                return self.yipranma_payi * 10
            elif 2 < self.tecrube <= 4 and self.maas < 15000:
                return (self.maas % self.tecrube) / 2 + self.yipranma_payi * 10
            elif self.tecrube > 4 and self.maas < 25000:
                return (self.maas % self.tecrube) / 3 + self.yipranma_payi * 10
            else:
                return self.maas

        except Exception as e:
            print("Zam hesaplanamadı:", e)

    def get_yeni_maas(self):
        return self.zam_hakki()

    def __str__(self):
        yeni_maas = self.zam_hakki()
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nTecrübe: {self.tecrube} yıl\nYeni Maaş: {yeni_maas}"
