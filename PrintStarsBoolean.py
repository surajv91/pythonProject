starrows=int(input("Please enter number of rows :"))
b=int(input("Please enter 0 or 1 : "))
bo=bool(b)
star="*"

if bo==True:
    a=0
    while a!=starrows:
        a += 1
        print(star*a)

elif bo==False:
    a=starrows
    while a!=0:
        print(star*a)
        a -= 1
