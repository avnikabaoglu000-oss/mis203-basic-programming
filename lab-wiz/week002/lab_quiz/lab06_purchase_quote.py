
branslar = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []



ogrenci1_ad = " Ali Yılmaz ".strip()
ogrenci2_ad = "Ayşe Kaya".strip()
ogrenci3_ad = " Mehmet Demir ".strip()

tum_ogrenciler.append([ogrenci1_ad, [branslar[0]]])            # Ali -> Yazılım
tum_ogrenciler.append([ogrenci2_ad, [branslar[1], branslar[2]]]) # Ayşe -> Tasarım, Pazarlama
tum_ogrenciler.append([ogrenci3_ad, [branslar[0]]])            # Mehmet -> Yazılım

print("--- Adım 2 Sonrası Liste ---")
print(tum_ogrenciler)


# Madde 3.1: Listenin en başına insert() ile "Başkan" ekleme
baskan_ad = " Zeynep Şahin ".strip()
tum_ogrenciler.insert(0, [baskan_ad, [branslar[0], branslar[1]]])

print("\n--- Adım 3 ---")
print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")


# Madde 4.1: remove() ile belirli bir öğrenciyi silme (Örn: Ali Yılmaz)
for ogrenci in tum_ogrenciler:
    if ogrenci[0] == "Ali Yılmaz":
        tum_ogrenciler.remove(ogrenci)
        break

son_ogrenci = tum_ogrenciler.pop()
print("\n--- Adım 4 ---")
print(f"Sistemden en son çıkan öğrenci: {son_ogrenci[0]}")



yeni_ogrenci_ad = " Burak Tan ".strip()
tum_ogrenciler.append([yeni_ogrenci_ad, [branslar[1]]]) # Tasarım branşı


gecici_sirali = sorted(tum_ogrenciler)

print("\n--- Adım 5.2 (Geçici Sıralama) ---")
print("Alfabetik (Geçici) Sıralı Liste:", gecici_sirali)
print("Orijinal Liste (Değişmedi):    ", tum_ogrenciler)

tum_ogrenciler.sort()

print("\n--- Adım 5.3 (Kalıcı Sıralama) ---")
print("Kalıcı Sıralanmış Ana Liste:   ", tum_ogrenciler)
