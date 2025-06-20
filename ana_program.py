import requests
import json
import time
import random

API_KEY = "e7d12d39ea878adb75a2aef6980fb0d2"

ilcelerin_koordinatlari = {
    "Cankaya": (39.9179, 32.8625),
    "Kecioren": (39.9862, 32.8660),
    "Yenimahalle": (39.9667, 32.8167),
    "Mamak": (39.9206, 32.8969),
    "Altindag": (39.9500, 32.8667),
    "Etimesgut": (39.9503, 32.6833),
    "Golbasi": (39.7994, 32.8025),
    "Sincan": (39.9611, 32.5833),
    "Bala": (39.5611, 33.2425)
}

tum_veriler = {}

for ilce_koordinati, (lat, lon) in ilcelerin_koordinatlari.items():
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=tr"
        response = requests.get(url)

        if response.status_code == 200:
            veri = response.json()
            tum_veriler[ilce_koordinati] = veri
            print(f"{ilce_koordinati} verisi basariyla alindi.")
        else:
            print(f"{ilce_koordinati} icin veri alma basarisiz oldu. Durum kodu: {response.status_code}")

        time.sleep(1)  

    except Exception as e:
        print(f"{ilce_koordinati} icin hata olustu:", e)

with open("weather_data.json", "w", encoding="utf-8") as dosya:
    json.dump(tum_veriler, dosya, indent=4, ensure_ascii=False)

print("Tum veriler buraya kaydedildi: 'weather_data.json'.")

ilceler_sozluk = { "A" :"Cankaya",
    "B" :"Kecioren",
    "C" :"Yenimahalle",
    "D" :"Mamak",
    "E" :"Altindag",
    "F" :"Etimesgut",
    "G" :"Golbasi",
    "H" :"Sincan",
    "I" :"Bala"}

ilceler_liste = ["Cankaya","Kecioren","Yenimahalle","Mamak","Altindag","Etimesgut","Golbasi","Sincan","Bala"]

class HavaVerisi:
    def __init__(self,ilce, dt_txt, temp, feels_like, description, humidity, pressure, wind_speed, clouds, visibility,weather_id):
        self.ilce = ilce
        self.dt_txt = dt_txt
        self.temp = temp
        self.feels_like = feels_like
        self.description = description
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.clouds = clouds
        self.visibility = visibility
        self.weather_id = weather_id


    def yazdir(self):
        print(f"Tarih : {self.dt_txt}\n"
              f"Hava Durumu : {self.description}\n"
              f"Sicaklik (Celsius): {self.temp}\n"
              f"Hissedilen Sicaklik (Celsius): {self.feels_like}\n"
              f"Nem Oranı (%) : {self.humidity}\n"
              f"Rüzgar Hizi (m/s) : {self.wind_speed}\n"
              f"Basinc (pHa) : {self.pressure}\n"
              f"Bulutluluk Orani (%) : {self.clouds}\n"
              f"Gorus Mesafesi (m) : {self.visibility}\n")
        
        
                

hava_listesi = []


for ilce in ilceler_liste:
    for veri in tum_veriler[ilce]["list"]:
        nesne = HavaVerisi(
            ilce=ilce, 
            dt_txt = veri["dt_txt"],
            temp = veri["main"]["temp"],
            feels_like = veri["main"]["feels_like"],
            description = veri["weather"][0]["description"],
            humidity = veri["main"]["humidity"],
            pressure = veri["main"]["pressure"],
            wind_speed = veri["wind"]["speed"],
            clouds = veri["clouds"]["all"],
            visibility = veri.get("visibility", 0),
            weather_id = veri["weather"][0]["id"] 
        )
        hava_listesi.append(nesne)

while True:
    print("Hangi islemi yapmak istersiniz?\n"
          "A : Sececeginiz ilce ve gun icin hava durumu degerlerini gorun.\n"
          "B : Yasadiginiz ilce icin onerilen etkinlikleri inceleyin.\n" \
          "Q : Programdan cikin.")
    islem = input("Seciniz(A,B,Q olarak):").strip().upper()

    if islem == "A":
        while True:
            print("\nHangi ilceyi secmek istersiniz?")
            for secim,ilce in ilceler_sozluk.items():
                print(f"{secim} : {ilce}")
            secilen_ilce =input("İlcenin adini yazin:").strip()
            if secilen_ilce in ilceler_liste:
                break
            else:
                print("\nHatali yazim ya da tanimli olmayan konum, tekrar deneyin!")

        tarihler = []
        for hava in hava_listesi:
            if hava.dt_txt.split()[0] not in tarihler:
                tarihler.append(hava.dt_txt.split()[0])
            else:
                pass


        while True:
            print("\nHangi tarihi secmek istersiniz?")
            for index,tarih in enumerate(tarihler):
                print(f"{index+1} : {tarih}")
            secilen_tarih = input("Tarihi yazilan sekli ile giriniz:").strip()
            if secilen_tarih in tarihler:
                break
            else:
                print("\nHatali yazim ya da tanimli olmayan tarih, tekrar deneyin!\n")


        def detay_ilce(secilen_ilce,secilen_tarih):
            istenilen_bilgiler = list(filter(lambda hava : secilen_ilce == hava.ilce and secilen_tarih ==hava.dt_txt.split()[0] ,hava_listesi))
            for nesne in istenilen_bilgiler:
                nesne.yazdir()
                print("-" * 50 + "\n")

        detay_ilce(secilen_ilce,secilen_tarih)   

    elif islem == 'B':
        while True:
            print("\nHangi ilceyi secmek istersiniz?")
            for secim,ilce in ilceler_sozluk.items():
                print(f"{secim} : {ilce}")
            secilen_ilce_B =input("İlcenin adini yazin:").strip()
            if secilen_ilce_B in ilceler_liste:
                break
            else:
                print("\nHatali yazim ya da tanimli olmayan konum, tekrar deneyin!\n")

        tarihler = []
        for hava in hava_listesi:
            if hava.dt_txt.split()[0] not in tarihler:
                tarihler.append(hava.dt_txt.split()[0])
            else:
                pass


        while True:
            print("\nHangi tarihi secmek istersiniz?")
            for index,tarih in enumerate(tarihler):
                print(f"{index+1} : {tarih}")
            secilen_tarih_B = input("Tarihi yazilan sekli ile giriniz:").strip()
            if secilen_tarih_B in tarihler:
                break
            else:
                print("\nHatali yazim ya da tanimli olmayan tarih, tekrar deneyin!")

        etkinlikler_firtinali= ["Muzik dinleyebilirsiniz",
                                "Film izleyebilirsiniz",
                                "Kahve esliginde kitap okuyabilirsiniz."] 

        etkinlikler_karli= ["Kartopu oynayabilirsiniz",
                            "Kardan adam yapabilirsiniz."]

        etkinlikler_acik={"gunduz": {"soguk": ["Kalin kiyafet giyerek yuruyus yapabilirsiniz."],
                                     "orta":["Piknik yapabilirsiniz.",
                                             "Bisiklet sürebilirsiniz.",
                                             "Turistik yerleri gezebilirsiniz."],
                                     "sicak": ["Havuza yüzmeye gidebilirsiniz.",
                                               "Serin bir yerde sohbet edebilirsiniz."]},
                          "gece": {"soguk": ["Evde dizi izleyebilirsiniz.",
                                             "Pencereden yildizlari izleyebilirsiniz."],
                                   "sicak": ["Disarida yildizlari izleyebilirsiniz.",
                                             "Sessiz bir yerde keman calabilirsiniz.",
                                             "Yuruyuse cikabilirsiniz."]}}  

        etkinlikler_sisli = ["Evde kalin, yemek tariflerini yapmayi deneyebilirsiniz."]

        etkinlikler_bulutlu = {"az bulutlu" : {"sicak" :["Disari cikip yuruyus yapabilirsiniz."],
                                               "soguk" :["Evde kalin, kitap okuyabilirsiniz."]},
                               "cok bulutlu": ["Evde kalin, puzzle yapabilirsiniz."]}
    
        etkinlikler_yagmurlu = ["Evde kalin, odanizi düzenleyebilirsiniz. Varsa eğer cicek bakimi yapabilirsiniz."]

        etkinlik_ciseleme = ["Cok estetik bir atmosfer olabilir, fotograf cekebilirsiniz.",
                             "Terasli bir mekanda sicak icecekle rahatlayabilirsiniz."]


    
        saatler = []
        for hava in hava_listesi:
            if hava.dt_txt not in saatler :
                if hava.dt_txt.split()[0] == secilen_tarih_B:
                    saatler.append(hava.dt_txt)
                else:
                    pass    
            else:
                pass
   

        def etkinlik_ilce(rastgele_saat,secilen_ilce_B):
            filtrelenmis_nesne = filter(lambda hava: hava.ilce == secilen_ilce_B and hava.dt_txt == rastgele_saat, hava_listesi)
            yeni_nesne = next(filtrelenmis_nesne, None)
            if 200 <= yeni_nesne.weather_id <= 232:
                return f"Bugün saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {random.choice(etkinlikler_firtinali)}"    
            elif 300 <= yeni_nesne.weather_id <= 321:
                return f"Bugün saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {random.choice(etkinlik_ciseleme)}"       
            elif 500 <= yeni_nesne.weather_id <= 531:
                return f"Bugün saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {etkinlikler_firtinali}"       
            elif 600 <= yeni_nesne.weather_id <= 622:
                return f"Bugün saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {random.choice(etkinlikler_karli)}"           
            elif 701 <= yeni_nesne.weather_id <= 781:
                return f"Bugün saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {etkinlikler_firtinali}"            
            elif yeni_nesne.weather_id == 800:
                if   6 <= int(yeni_nesne.dt_txt[11:13]) < 20:
                    if yeni_nesne.temp <= 15:
                        return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                               f" {random.choice(etkinlikler_acik['gunduz']['soguk'])}"
                    elif 15 < yeni_nesne.temp <= 25:
                        return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                               f" {random.choice(etkinlikler_acik['gunduz']['orta'])}"
                    else:
                        return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                               f" {random.choice(etkinlikler_acik['gunduz']['sicak'])}"
                else:
                    if yeni_nesne.temp < 17:
                        return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                               f" {random.choice(etkinlikler_acik['gece']['soguk'])}"
                    else:
                        return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                               f" {random.choice(etkinlikler_acik['gece']['sicak'])}"           
            elif yeni_nesne.weather_id in [801, 802]:
                if yeni_nesne.temp < 17:
                    return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                           f" {etkinlikler_bulutlu['az bulutlu']['soguk']}" 
                else:
                    return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                           f" {etkinlikler_bulutlu['az bulutlu']['sicak']}"     
            elif yeni_nesne.weather_id in [803, 804]:
                return f"{yeni_nesne.dt_txt[0:10]} saat {yeni_nesne.dt_txt[11:16]} icin hava {yeni_nesne.description}." \
                       f" {random.choice(etkinlikler_bulutlu['cok bulutlu'])}"     
            else:
                return "Tanimlanamayan bir durum, tekrar deneyin!"
        
        while True:
            rastgele_saat = random.choice(saatler)
            sonuc = etkinlik_ilce(rastgele_saat, secilen_ilce_B)
            if sonuc == "Tanimlanamayan bir durum, tekrar deneyin!":
                print(sonuc)
                continue 
            else:
                print(f"\n{sonuc}\n")
                break  
            
    
    elif islem == "Q":
        print("Programdan cikiliyor, iyi günler dileriz!")
        break

    else :
        print("\nTanimlanamayan girdi, tekrar deneyin!")

        





      


            


            

            

            
        




    
        


    