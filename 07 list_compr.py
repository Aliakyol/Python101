# list comprehensions (liste ifadeleri)
"""
if else sol tarafa yazılır; sdece if sağ tarafa yazılır

"""
salaries = [1000, 2000, 3000, 4000, 5000]

abc = [int(item * 1.2) for item in salaries if item > 3000]
print(abc)
print(type(abc))
print("/-"*50)
numbers = [x for x in range(1, 11)]
print(numbers)

print([x ** 2 for x in numbers])
print([x ** 2 for x in numbers if x ** 2 % 2 == 0])
print([x ** 2 for x in numbers if x ** 2 % 2 != 0])
print([x ** 2 if x % 2 != 0 else x * 100 for x in numbers])
