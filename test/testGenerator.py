def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"

f = fib(6)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

f = fib(10)
for n in f:
    print(n)

f = fib(3)
try:
    while True:
        print(next(f))
# need to catch the StopIteration exception in order to get the return value of the generator
except StopIteration as e:
    print(e.value)
