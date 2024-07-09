# a=10
# b=20
# c=a+b
# print("global",c)
# def add():
#     c=a+b
#     print("local",c)
# add()

a=10
b=20
def add():
    c=a+b
    print("sum of two numbers:",c)
add()
def sub():
    c=a-b
    print("sub of two numbers:",c)
sub()
def mul():
        c = a * b
        print("mul of two numbers:", c)
mul()
def div():
            c = a / b
            print("div of two numbers:", c)
div()