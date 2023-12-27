# Kendi kendisini çağıran fonksiyondur.
# Döngülere alternatif bir konudur.
"""
Faktoriyel hesabını bu yöntemle yapalım.
"""
import random


def factorial(number):
    if number >= 0:
        if number == 0 or number == 1:
            return 1
        else:
            return number * factorial(number - 1)
    else:
        print("Enter a positive number: ")


print(factorial(5))

"""
Bir listenin elemanlarının toplamı yapalım.
"""


def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])


sample_list = [2, 3, 6, 4, 5, 9, 8]

print(sum(sample_list))






"""
Fibonacci dizisini normal metoda yapalım.

"""

######################################
# en basit  çözümü ChatGPT verdi.
a, b = 0, 1

for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b  # Değiştirme işini yapıyor.

# Değiştirme işinin ilkel hali aşağıdadır.

a = 0
b = 1
for _ in range(20):
    print(a, end=" ")
    c = a
    a = b
    b = a + c

######################################


new_list = [1, 1]


def fibonacci_normal(number):
    for i in range(2, number + 1):
        new_list.append(new_list[i - 1] + new_list[i - 2])
    return new_list


print(fibonacci_normal(5))

"""
Aşağıdaki kod bloğu sonucu doğru veriyor ama çok fazla işlem yapıyor.
"""


def fibo_mit_recursive(n):
    print("Şu an hesaplanan sayı: ", n)
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo_mit_recursive((n - 1)) + fibo_mit_recursive(n - 2)


print("Sonuç", fibo_mit_recursive(5))

"""
Normal method ile gereksiz işlemler yapıyor. 
Aşağıdaki tool ile çok verimli iş  yapıyor
"""

from functools import lru_cache


@lru_cache(None)
def fibo_mit_recursive(n):
    print("Şu an hesaplanan sayı: ", n)
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo_mit_recursive((n - 1)) + fibo_mit_recursive(n - 2)


print("Sonuç", fibo_mit_recursive(10))
