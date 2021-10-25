
# x=100
# def func1():
#     x=20
#     def func2():
#         global x
#         x=99
#     print('Before calling func2',x)
#     func2()
#     print('After calling func2',x)
#
# func1()
# print(x)


x=100

def func1():
    global x
    x=x+1
    print(x)

func1()
print(x)

