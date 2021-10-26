import sys

dicTest = {1:"msy",
        2:"mmx",
        3:"ahj"}

print(type(dicTest.keys()))

for i in dicTest.keys():
    print("i ", i)

print(type(list(dicTest.keys())))
print(sys.getsizeof((list(dicTest.keys()))))
print(sys.getsizeof(dicTest))
