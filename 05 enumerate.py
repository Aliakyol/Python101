"""
enumerate sınıfı

Çıktısı enumerate sınıfıdır.
List, tuple, dict olarak dönüştürülebilir.
Bir list içindeki değerleri ve indeksleri verir.
Bir tuple içindeki değerleri ve indeksleri verir.
Sözlük için aynı anda hem key hem de value vermiyor; ya key yada value alınabiliyor



"""

sample_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for index, item in enumerate(sample_list):
    print(index, item)

######################################################################
# Another example
######################################################################

sample_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for a, b in enumerate(sample_tuple, 1):
    print(a, b)



######################################################################
# Another example
######################################################################

sample_dict = {
    "Ali": 1000,
    "Veli": 2000,
    "Hasan": 3000,
    "Mert": 4000
}


for x, y in enumerate(sample_dict.keys(), 1):
    print(x, y)

for x, y in enumerate(sample_dict.values(), 1):
    print(x, y)

for x, y, z in enumerate(sample_dict.keys(), sample_dict.values(), 1):
    print(x, y, z)

######################################################################
# Another example
######################################################################


sozluk = {'anahtar1': 'deger1', 'anahtar2': 'deger2', 'anahtar3': 'deger3'}

# Sözlüğün anahtarlarını enumerate ile dolaşma
for indeks, anahtar in enumerate(sozluk.keys()):
    print(f'İndeks {indeks}: Anahtar {anahtar}')

# Sözlüğün değerlerini enumerate ile dolaşma
for indeks, deger in enumerate(sozluk.values()):
    print(f'İndeks {indeks}: Değer {deger}')
