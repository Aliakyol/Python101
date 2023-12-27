"""
 * Python'da genellikle bir döngüde döngü değişkeni kullanmak gerekmiyorsa, bu değişken yerine alt çizgi karakteri (_) kullanılır.
 * Yani, _ aslında bir geçici değişken adı olarak kullanılır, ancak döngü içinde kullanılmayacak anlamına gelir.
 * Örneğin, for _ in range(20): döngüsünde, _ ismi döngüdeki her iterasyonda 0 ile 19 arasındaki değerleri almaktadır.
 * Ancak bu durumda döngü içinde bu _ değişkeni kullanılmadığı için genellikle Python'da bu tarz durumlarda kullanılır.
 * Bu, döngüde bir değişkenin tutulması gerektiği, ancak döngü içinde kullanılmayacağı durumlar için tercih edilen bir yaklaşımdır.
"""

#########################################################################
# EXAMPLE 1
#########################################################################
sample_string = "Python"
for _ in range(11):
    print(f"The {_} sample_string is {sample_string}")

#########################################################################
# EXAMPLE 2
#########################################################################
a, b = 0, 1

for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
