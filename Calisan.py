from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube,maas):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)

        self.sektor = sektor
        self.tecrube = tecrube
        self.maas = maas



    def get_sektor(self):
        return self.sektor

    def set_sektor(self, sektor):
        self.sektor = sektor

    def get_tecrube(self):
        return self.tecrube

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_maas(self):
        return self.maas

    def set_maas(self, maas):
        self.maas = maas

    def zam_hakki(self):
        try:
            if self.tecrube <= 2:
                return 0
            elif 2 < self.tecrube <= 4 and self.maas < 15000:
                return (self.maas % self.tecrube) / 100
            elif self.tecrube > 4 and self.maas < 25000:
                return (self.maas % self.tecrube) / 200
            else:
                return self.maas

        except Exception as e:
            print("Zam hesaplanamadı:", e)

    def get_yeni_maas(self):
        return self.zam_hakki()

    def __str__(self):
        yeni_maas = self.zam_hakki()
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nTecrübe: {self.tecrube} ay\nYeni Maaş: {yeni_maas}"
