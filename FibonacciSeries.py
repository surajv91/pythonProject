# 0 1 1 2 3 5 8 13 21 34

#
# n=int(input("Enter a range : "))
# a,b=0,1
# print(a)
# print(b)
# for num in range(n-2):
#     c=a + b
#     a,b=b,c
#     print(b)

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number=int(input("Enter the number"))
print(fibonacci(number))