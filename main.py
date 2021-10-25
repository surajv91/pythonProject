# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# #if __name__ == '__main__':
#  #   print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# import requests
# from bs4 import BeautifulSoup
#
# #URL = "https://realpython.github.io/fake-jobs/"
# #page = requests.get(URL)
#
# #print(page.text)
#
# URL = "https://fast.com/"
# r = requests.get(URL)
# print(r.text)
# soup = BeautifulSoup(r.content,'html5lib')
# # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())

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


# x=100
#
# def func1():
#     global x
#     x=x+1
#     print(x)
#
# func1()
# print(x)

# # Enumerate
# y=['A','B','C','D']
#
# for i,j in enumerate(y):
#     if i%2==0:
#         print(f"{i} is assigned to {j}")

# import sys
# print(sys.path) #PATH variable like linux

#Enumerate
lst=['Kawasaki','Honda','Royal Enfield']
#
# for index,bike in enumerate(lst,start=1):
#     print(index,bike)
# a=",".join(lst)
# for item in lst:
#     print(item, "and ")
#
# print(f"The bikes we have are {a}")

gro=["Harpic","Vim","Deodorant","Lollypop",56]
# print(gro[4])
num=[1,7,9,11,3]
num.sort()

print(num)
