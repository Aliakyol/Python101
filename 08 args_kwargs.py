"""
Girilecek verilerin ne olduğu ve ne kadar olduğu bilinmediği durumlarda kullanılır,
Sonuç tuple olarak verilir.
"""


def multiply(*numbers):
    """
    Args:
        *numbers:

    Returns: a function that multiplies numeric values.

    """
    result = 1
    for number in numbers:
        if type(number) == int or type(number) == float:
            result *= number
    return result


print(multiply(5, 6, 7, "ali", 1.85, [1, 2, 3], (4, 5, 6)))

sample_input = (5, 6, 7, "ali", 1.85, [1, 2, 3], (4, 5, 6))
print(multiply(*sample_input))


def öğrenci_numaraları(*numaralar):
    tek_numaralar = []
    çift_numaralar = []
    for numara in numaralar:
        if numara % 2 == 0:
            çift_numaralar.append(numara)
        else:
            tek_numaralar.append(numara)
    return tek_numaralar, çift_numaralar


print(öğrenci_numaraları(55, 69, 54, 21, 25, 36, 69, 87, 52, 14, 99))

###############################################################################
"""
Girilecek olan telefon numarasından isme ulaşma
"""


def numaradan_isim_bulma(**rehber):
    x = ""
    for isim, numara in rehber.items():
        if numara == "1781787878":
            x = isim
            break
    return x


örnek_girdi = {"ali": "1781787878", "veli": "55465465465", "deli": "66541", "49elli": "454121"}
print(numaradan_isim_bulma(**örnek_girdi))
