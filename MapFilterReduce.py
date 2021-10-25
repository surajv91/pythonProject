numbers=["4","5","2"]

# for item in range(len(numbers)):
#     numbers[item]=int(numbers[item])
#
# print(numbers[1]+2)
#
# numbers[2]=numbers[2]+1
# print(numbers)

# numbers2=list(map(int,numbers))
# print(numbers2)
# def sq(x):
#     return x*x
#
# def cu(x):
#     return x*x*x
#
# square=list(map(sq,numbers2))
# print(square)
# square=list(map(cu,numbers2))
# print(square)
#
# square=list(map(lambda x:x*x,numbers2))
# print(square)
# square=list(map(lambda x:x*x*x,numbers2))
# print(square)
#
# fun=[sq,cu]
# for i in range(5):
#     val=list(map(lambda x:x(i),fun))
#     print(val)

#### Filter
# lst=[1,2,3,4,5,6,7,8,9]
# def is_grt_5(x):
#     return x>5
#
# grt_than_5=list(filter(is_grt_5,lst))
# print(grt_than_5)


#### Reduce
from functools import reduce

list1=[1,2,3]
num=0
for i in list1:
    num=num+i
print(num)

y=reduce(lambda x,y:x+y,list1)
print(num)


# list1=[1,2,3]
# a=len(list1)
# print(a)
# for i in range(a):
#     print(list1[i])
