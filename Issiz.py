# Issiz.py
from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, tecrube):
        super().__init__( tc_no, ad, soyad, yaş, cinsiyet, uyruk)

        self.tecrube = tecrube



    def get_tecrube(self):
        return self.tecrube

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0.2
            beyaz_yaka_etkisi = 0.35
            yonetici_etkisi = 0.45

            max_etki = 0
            max_statu = ""

            for statu, yil in self.tecrube.items():
                etki = 0
                if statu == "mavi yaka":
                    etki = yil * mavi_yaka_etkisi
                elif statu == "beyaz yaka":
                    etki = yil * beyaz_yaka_etkisi
                elif statu == "yonetici":
                    etki = yil * yonetici_etkisi

                if etki > max_etki:
                    max_etki = etki
                    max_statu = statu

            return max_statu

        except Exception as e:
            print("Statü bulunamadı:", e)

    def __str__(self):
        statu = self.statu_bul()
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nEn Uygun Statü: {statu}"
