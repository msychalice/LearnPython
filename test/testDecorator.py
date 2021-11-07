def dec1(func):
    def inner(*args, **kwargs):
        print("dec1 start")
        func(*args, **kwargs)
        print("dec1 end")
    return inner


def dec2(func):
    def inner(*args, **kwargs):
        print("dec2 start")
        func(*args, **kwargs)
        print("dec2 end")
    return inner


@dec1
@dec2
def func(a, b):
    print(f"func {a} and {b}")


@dec2
@dec1
def func1(*args, **kwargs):
    for i in range(len(args)):
        print(f"func1 args {i} is {args[i]}")
    for k, v in kwargs.items():
        print(f"func1 kwargs {k}:{v}")


func(1, 2)
func1(1, 2, 3, "4", "done", last="last")
