"""
 * lambda ifadesi, Python'da anonim (isimsiz) işlevler oluşturmak için kullanılan bir araçtır.
 *Fonksiyon tanımlamak için def ifadesi kullanılırken, lambda ifadesi kısa ve tek satırlık işlevlerin oluşturulmasını sağlar.

"""

kare = lambda x: x ** 2
print(kare(5))


######################################################################
# Another example
######################################################################

def multiply(x):
    return (x * x)


def addition(x):
    return (x + x)


funcs = [multiply, addition]
for i in range(5):
    result = list(map(lambda x: x(i), funcs))
    print(result)
