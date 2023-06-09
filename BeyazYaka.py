from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor,tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor ,tecrube, maas)

        self.tesvik_primi = tesvik_primi


    def get_tesvik_primi(self):
        return self.tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.tesvik_primi = tesvik_primi

    def get_yeni_maas(self):
        try:
            if self.tecrube <= 2:
                return self.tesvik_primi
            elif 2 < self.tecrube <= 4 and self.maas < 15000:
                return (self.maas * self.tecrube / 100) * 5 + self.tesvik_primi
            elif self.tecrube > 4 and self.maas < 25000:
                return (self.maas * self.tecrube / 100) * 4 + self.tesvik_primi
            else:
                return self.maas

        except Exception as e:
            print("Zam hesaplanamadı:", e)

    def __str__(self):
        yeni_maas = self.get_yeni_maas()
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nTecrübe: {self.tecrube} yıl\nYeni Maaş: {yeni_maas}"
