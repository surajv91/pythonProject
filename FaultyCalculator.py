# 45*3=555 , 56+9=77, 56/6=4

print('Enter a symbol: ')
symbol=input()
print('Enter 1st number: ')
num1=int(input())
print('Enter 2nd number: ')
num2=int(input())

if num1==45 and num2==3 and symbol=="*":
    mul=555
    print("The product is : ",mul)
elif num1==56 and num2==9 and symbol=="+":
    sum=77
    print("The sum is : ",sum)
elif num1==56 and num2==6 and symbol=="/":
    div=4
    print("The div is : ",int(div))
elif symbol=="+":
    sum=num1+num2
    print("The sum is :",sum)
elif symbol=="-":
    diff=num1-num2
    print("The difference is : ",diff)
elif symbol=="*":
    mul=num1*num2
    print("The product is : ",mul)
elif symbol=="/":
    div=num1/num2
    print("The div is : ",int(div))
else:
    print('Unknown symbol.')
