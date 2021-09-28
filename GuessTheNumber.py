#User will guess the number num
import random
#num=83
num=random.randint(1,100)
#print(num,"Random number")
count=0
while 1:
    user_input = int(input('Enter a number between 1 - 100 to guess :'))
    if num<user_input:
        count+=1
        print('This is the run no',count,'.Try a number smaller than',user_input)
        continue
    elif num>user_input:
        count += 1
        print('This is the run no',count,'.Try a number greater than',user_input)
        continue
    elif num==user_input:
        count += 1
        print('You have guessed the right number',user_input)
        print('You took',count ,'runs to guess')
        break