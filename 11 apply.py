"""
apply() fonksiyonu, Python'da Pandas kütüphanesinin bir parçası olarak kullanılan bir DataFrame metodudur.
Bu metod, DataFrame'deki her bir satır veya sütun üzerinde belirli bir fonksiyonu uygulamak için kullanılır.

Genellikle kullanımı şu şekildedir:
    df.apply(func, axis=0) -> sütuna uygular
    df.apply(func, axis=1) -> satıra uygular



"""
import pandas as pd

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)
df

df.apply(max)  # Her bir sütunda maksimum değeri bulma

df.apply(max, axis=1)  # Her bir satırda maksimum değeri bulma

df.apply(min)

df.apply(np.std)  # max ve min normal çalışırken std için niye np.std yapmak gerekiyor.
