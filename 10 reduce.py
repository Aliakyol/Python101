"""
 * reduce() fonksiyonu, Python'un functools modülünde bulunan bir fonksiyondur ve bir dizi değer üzerinde bir işlem yaparak tek bir sonuca ulaşmayı sağlar.
 * Bu fonksiyon, soldan sağa doğru bir diziye (örneğin, bir liste veya başka bir veri yapısı) bir işlev uygular ve ardışık olarak bu işlevi kullanarak tek bir sonuca ulaşır.
 * reduce() fonksiyonu Python 2.x sürümlerinde yerleşik bir fonksiyondu, ancak Python 3.x sürümlerinde functools modülünde bulunmaktadır.
 * Bu nedenle, Python 3.x sürümlerinde kullanabilmek için öncelikle bu modülü içe aktarmalısınız:
 * reduce() fonksiyonunun genel sözdizimi şu şekildedir:
        reduce(function, sequence[, initial])

"""

from functools import reduce

#########################################################################
# SAMPLE 1
#########################################################################

"""
 * 1 den 10 a kadar rakamların olduğu bir listemiz var.
 * ilk elemanı x e ata, ikinci elemanı y ye ata. Bunları topla ve tekrar x e ata.
 * üçüncü elemanı y ye ata ve böyle devam et.

"""

liste = [x for x in range(1, 11)]
toplam = reduce(lambda x, y: x + y, liste)
print(toplam)

#########################################################################
# SAMPLE 2
#########################################################################
liste = [x for x in range(1, 11)]
toplam = reduce(lambda x, y: x + y, liste, 100) # sondaki 100 ü sonuca ekle.
print(toplam)



#########################################################################
# SAMPLE 3
#########################################################################

def add(x, y): # Örnek bir işlev: İki sayıyı toplama
    return x + y


# Bir liste üzerinde reduce kullanımı
numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)
print(result)

######################################################################
# SAMPLE 4
######################################################################

sample_list = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a * b, sample_list))


######################################################################
# SAMPLE 5
######################################################################

num_list = np.arange(10)
filter_list = list(filter(lambda x: x %3 ==0, num_list))
final_list = reduce(lambda x, y: x * x, filter_list)


