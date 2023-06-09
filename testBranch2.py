# Main.py
import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    # İnsan sınıfı için 2 nesne oluşturulması
    insan1 = Insan("12345678900", "Ali", "Yılmaz", 30, "Erkek", "Türk")
   # print("insan1 başarılı")

    insan2 = Insan("98765432100", "Ayşe", "Demir", 25, "Kadın", "Türk")
   # print("insan1 başarılı")

    # İşsiz sınıfı için 3 nesne oluşturulması

    issiz1 = Issiz("12345678900", "Ahmet", "Türk", 30, "Erkek", "Türk", {"mavi yaka": 5, "beyaz yaka": 3, "yönetici": 8})

    #print("issiz1 başarılı")

    issiz2 = Issiz("98765432100", "Ayşen", "Altindis", 25, "Kadın", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})

  #  print("issiz2 başarılı")

    issiz3 = Issiz("45678912300", "Burak", "yılmaz", 35, "Erkek", "Türk", {"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})

   # print("issiz3 başarılı")

    # Çalışan sınıfı için 3 nesne oluşturulması
    calisan1 = Calisan("12345678900", "Buse", "Çelik", 30, "Erkek", "Türk", "teknoloji", 3, 12000)

   # print("calisan1 başarılı")

    calisan2 = Calisan("98765432100", "Sude", "Çelik", 25, "Kadın", "Türk", "muahsebe", 4, 14000)

   # print("calisan2 başarılı")

    calisan3 = Calisan("45678912300", "Oğuz", "Öztürk", 35, "Erkek", "Türk", "inşaat", 6, 18000)

   # print("calisan3 başarılı")

    # Mavi Yaka sınıfı için 3 nesne oluşturulması
    mavi_yaka1 = MaviYaka("12345678900", "Abuzer", "Kömürcü", 30, "Erkek", "Türk", 0.2, 1500, 100,0.2)

    #print("maviyaka1 başarılı")

    mavi_yaka2 = MaviYaka("98765432100", "Polat", "alemdar", 25, "Kadın", "Türk", 0.5, 2000, 150,0.2)

    #print("maviyaka2 başarılı")

    mavi_yaka3 = MaviYaka("45678912300", "Beyza", "Özgil", 35, "Erkek", "Türk", 0.3, 1800, 120,0.2)

  #  print("maviyaka3 başarılı")

    # Beyaz Yaka sınıfı için 3 nesne oluşturulması
    beyaz_yaka1 = BeyazYaka("12345678900", "Su", "Yıldırım", 30, "Erkek", "Türk", 500, 5000, 200,100)

   # print("beyazyaka1 başarılı")

    beyaz_yaka2 = BeyazYaka("98765432100", "Ayşenur", "Angili", 25, "Kadın", "Türk", 2500, 7000, 300,1000)

  #  print("beyazyaka2 başarılı")

    beyaz_yaka3 = BeyazYaka("45678912300", "Melek", "Naz", 35, "Erkek", "Türk", 1000, 6000, 250,2000)

   # print("beyazyaka3 başarılı")

    # Çalışan, mavi yaka ve beyaz yaka nesnelerinin değerlerini içeren bir pandas DataFrame oluşturma
    data = {
        "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
        "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
        "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
        "Yeni Maaş": [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(), mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas()]
    }

    # DataFrame oluşturma
    df = pd.DataFrame(data)

    # Bazı değişken değerlerinin boş olması durumunda 0 atama
    df.fillna(0, inplace=True)

    # Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını hesaplama
    gruplanmis_df = df.groupby("Nesne Değeri").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})
    print("Gruplandırılmış DataFrame:")
    print(gruplanmis_df)

    # Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
    maas_ust_limit = 15000
    maas_ust_limit_sayisi = df[df["Yeni Maaş"] > maas_ust_limit].shape[0]
    print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", maas_ust_limit_sayisi)

    # Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
    sirali_df = df.sort_values("Yeni Maaş")
    print("Sıralanmış DataFrame:")
    print(sirali_df)

    # Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
    tecrube_limit = 3
    beyaz_yaka_tecrube = df[(df["Nesne Değeri"] == "Beyaz Yaka") & (df["Tecrübe"] > tecrube_limit)]
    print("Tecrübesi 3 seneden fazla olan Beyaz Yakalılar:")
    print(beyaz_yaka_tecrube)

    # Yeni maaşı 10000 TL üzerinde olanlar için tc_no ve yeni_maaş sütunlarını seçme ve gösterme
    yeni_maas_limit = 10000
    yeni_maas_ust_limit = df[df["Yeni Maaş"] > yeni_maas_limit].iloc[:,[1,5]]
    print("Yeni maaşı 10000 TL üzerinde olanların TC No ve Yeni Maaş bilgileri:")
    print(yeni_maas_ust_limit)

    # Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturma
    yeni_df = df[["Ad", "Soyad", "Yeni Maaş"]]
    print("Yeni DataFrame:")
    print(yeni_df)

except Exception as e:
        print("HATA", str(e))