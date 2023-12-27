"""
 * map sınıfı
 * map(function, iterable1, iterable2, ...)

 * Çıktısı map sınıfıdır.
 * List,tuple, set olarak dönüştürülebilir.
 * iterable bir nesne üzerinde tek tek işlemler yapar

"""

liste = [1, 2, 3, 4, 5]
kareleri = map(lambda x: x ** 2, liste)
print(list(kareleri))


######################################################################
# Another example
######################################################################

# girilen karakteri büyük harf yapan bir fonksiyon
def UpperCase(string):
    return string.upper()


sample_list = ("Ali", "Hasan", "Mert")

print(type(map(UpperCase, sample_list)))
print(*map(UpperCase, sample_list)) # unpacking yap. yani
print([*map(UpperCase, sample_list)]) # liste yap


######################################################################
# Another example
######################################################################
def karesini_al(x):
    return x ** 2


sayilar = range(1, 21)
print([*map(karesini_al, sayilar)])


