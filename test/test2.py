import sys

def main():
    ls = [0, 1, 2, "msy"]
    for i in range(len(ls)):
        print("type " + str(type(ls[i])) + " value " + str(ls[i]))

    ls1 = [3, 4, 5, "mmx"]
    lsls = [ls, ls1]

    lsls_copy = lsls[:]
    print("lsls[0][0]", lsls[0][0])
    #print("lsls[1][0]", lsls[1][0])
    print("lsls_copy[0][0]", lsls_copy[0][0])
    #print("lsls_copy[1][0]", lsls_copy[1][0])

    lsls_copy[0][0] = 2
    print("lsls[0][0]", lsls[0][0])
    print("lsls_copy[0][0]", lsls_copy[0][0])

    gen = [i for i in range(10000)]
    print(gen)
    print(sys.getsizeof(gen), "bytes")

    gen = (i for i in range(10000))
    print(gen)
    print(next(gen))
    print(next(gen))
    print(sys.getsizeof(gen), "bytes")

    return "exit"


print(main())

