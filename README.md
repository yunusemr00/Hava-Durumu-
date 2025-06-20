
# Ankara İlçeleri Hava Durumu ve Etkinlik Öneri Uygulaması 🌤️🎯

Bu proje, Ankara'nın belirli ilçeleri için **5 günlük hava durumu verilerini** alarak:
- Belirli bir ilçede, belirli bir tarihte hava durumu incelemesi yapmanızı sağlar.  
- Hava koşullarına ve saate uygun **etkinlik önerilerinde** bulunur.

Veriler [OpenWeatherMap API](https://openweathermap.org/forecast5) üzerinden alınmaktadır.

---

## 🚀 Özellikler

- İlçe bazında 5 günlük hava durumu (sıcaklık, nem, rüzgar, bulutluluk vs.)
- Randevu/etkinlik planı için **rastgele bir saat seçimi**
- Havanın açık, yağmurlu, karlı, sisli veya fırtınalı olmasına göre öneriler
- Gündüz/gece sıcaklık farkı dikkate alınarak öneri yapılır
- CLI (komut satırı) üzerinden kullanıcıyla etkileşimli menü

---

## 🛠️ Kurulum

1. Python yüklü değilse [Python.org](https://www.python.org/) üzerinden kurun.
2. Proje klasörüne terminal veya komut satırından gidin.
3. Gereken paketleri yükleyin:

```bash
pip install requests
```

---

## ⚙️ Kullanım

1. `ana_program.py` dosyasını çalıştır:

```bash
python ana_program.py
```

2. Karşına gelen menüden:
   - `A`: İlçe bazında hava durumu detaylarını incele
   - `B`: Etkinlik önerilerini al
   - `Q`: Çıkış yap

---

## 🗺️ İlçeler

Şu ilçeler desteklenir:

- Çankaya
- Keçiören
- Yenimahalle
- Mamak
- Altındağ
- Etimesgut
- Gölbaşı
- Sincan
- Bala

---

## 📝 Notlar

- `weather_data.json` dosyası çalıştırma sırasında otomatik olarak oluşturulur.
- Bu dosya, OpenWeatherMap'ten alınan verilerin kaydını içerir.
- JSON dosyasını `.gitignore` içine alman önerilir.

---

## 📄 Lisans

Bu proje açık kaynak olup dilediğiniz gibi geliştirilebilir.

---

## 🤝 Katkı

Geliştirmek, farklı şehirler veya ülkeler için uyarlamak istersen:  
Pull request göndermekten çekinme!
