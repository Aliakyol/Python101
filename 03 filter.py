"""
 * filter sınıfı
 * filter(function, iterable)
 * Çıktısı filter sınıfıdır.
 * List, tuple, set olarak dönüştürülebilirler.
 * Tanımlanan fonksiyon göre tüm elemanları true yada false olarak tanımlar ve true ları bir nesneye atar

"""
######################################################################
# Another example
######################################################################
def cift_sayi(x):
    return x % 2 == 0


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrelenmis = filter(cift_sayi, liste)
print(list(filtrelenmis))


filtrelenmis = map(cift_sayi, liste)
print(list(filtrelenmis))

"""
çift_sayı fonksiyonu True / False bir değer döndürür.
map tüm elemanlara uygulanır ve sonucu True / False döndürür
filter onların içindeki True olanları alır ve sonucu değeri olarak yazar
map 

"""



def even_number(number):
    if number % 2 == 0:
        return number
    else:  # hiç bir şey yazılmaya da bilir.
        return None

######################################################################
# Another example
######################################################################

# Profesyonel python cular bu kodu şöyle yazar
def even_number_1(number):
    return number if number % 2 == 0 else None

######################################################################
# Another example
######################################################################

print(even_number(8))

sayilar = [*range(11, 31)]
print(filter(even_number, sayilar))
print(type(filter(even_number, sayilar)))

print([*filter(even_number, sayilar)])  # unpacking yap ve listeye ata

print("?" * 99)

notlar = {'Ahmet': 60,
          'Sinan': 50,
          'Mehmet': 45,
          'Ceren': 87,
          'Selen': 99,
          'Cem': 98,
          'Can': 51,
          'Kezban': 100,
          'Hakan': 66,
          'Mahmut': 80}


def süz(n):
    return n >= 70


print(filter(süz, notlar.values()))  # nesnin adresini
print(type(filter(süz, notlar.values())))  # nesneyin tipini yazar
print(list(filter(süz, notlar.values())))  # nesneyi liste olarak yazar
print(tuple(filter(süz, notlar.values())))  # nesneyi tuple olarak yazar
print(set(filter(süz, notlar.values())))  # nesneyi set olarak yazar
print(*filter(süz, notlar.values()))  # nesneyi unpacking yapıp elemanlarını tek tek yazar
