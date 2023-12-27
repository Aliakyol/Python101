"""
zip sınıfı

Çıktısı zip sınıfıdır.
Eleman sayıları aynı olan bir den çok listeyi eşleştirir.
Default olarak tuple çıktıs verilir ama list, set ve dict olarak dönüştürülebilir.
"""

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

print(zipped)
print(type(zipped))
print(list(zipped))

for item in zipped:
    print(item)

######################################################################
# Another example
######################################################################

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
liste3 = ['x', 'y', 'z']

birlestirilmis = zip(liste1, liste2, liste3)
for eleman in birlestirilmis:
    print(eleman)
