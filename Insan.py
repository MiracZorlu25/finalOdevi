# Insan.py

class Insan:
    def __init__(self,tc_no, ad, soyad, yaş, cinsiyet, uyruk):
        self.tc_no = tc_no
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş
        self.cinsiyet = cinsiyet
        self.uyruk = uyruk

    def get_tc_no(self):
        return self.tc_no

    def set_tc_no(self, tc_no):
        self.tc_no = tc_no

    def get_ad(self):
        return self.ad

    def set_ad(self, ad):
        self.ad = ad

    def get_soyad(self):
        return self.soyad

    def set_soyad(self, soyad):
        self.soyad = soyad

    def get_yaş(self):
        return self.yaş

    def set_yaş(self, yaş):
        self.yaş = yaş

    def get_cinsiyet(self):
        return self.cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.uyruk

    def set_uyruk(self, uyruk):
        self.uyruk = uyruk

    def __str__(self):
        return f"TC No: {self.tc_no}\nAd: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yaş}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}"
