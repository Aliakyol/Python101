# dict comprehensions

######################################################################
# Another example
######################################################################

sample_list = [1, 2, 3, 4, 5]
result_dict = {k: k ** 2 for k in sample_list}
result_dict


######################################################################
# Another example
######################################################################
sample_list = [1, 2, 3, 4, 5]
result_dict = {k: k ** 2 for k in sample_list if k < 4}


######################################################################
# Another example
######################################################################


sample_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

print(sample_dictionary.items())
print(sample_dictionary.keys())
print(sample_dictionary.values())

print("///////////////")

x = {k: v ** 2 for (k, v) in sample_dictionary.items()}  # value ile işlem yapalaım
print(x)

print("///////////////")

x = {k.upper(): v for (k, v) in sample_dictionary.items()}  # key ile işlem yapalım
print(x)

print("///////////////")

x = {k + " python":
         (v * 5) ** 2 for (k, v) in sample_dictionary.items()}
# hem key hem de value ile işlem yapalım
print(x)

print("///////////////")

data = {
    "Ali": 1000,
    "Veli": 2000,
    "Hasan": 3000,
    "Mert": 4000
}

print({"Pyton " + k: v * 1.5 for (k, v) in data.items()})
