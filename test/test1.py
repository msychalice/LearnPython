import sys

for i in range(5, -1, -1):
    print("i is " + str(i))

def Func():
    msg = "local msg"
    print(msg)

msg = "123"
Func()

sys.exit()

print("after exit")
