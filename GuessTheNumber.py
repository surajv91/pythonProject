#User will guess the number num
import random
#num=83
num=random.randint(1,100)
#print(num,"Random number")
total_count,count=5,5
while 1:
    if count==0:
        print('\nYou are out of tries. Hard luck!!!!!!!!')
        print('The number was',num,'.')
        break
    else:
        user_input = int(input('Enter a number between 1 - 100 to guess :'))
        if num<user_input:
            count-=1
            print('Try a number smaller than',user_input,'.      (Tries left :',count, ')')
            continue
        elif num>user_input:
            count -= 1
            print('Try a number greater than',user_input,'.      (Tries left :',count, ')')
            continue
        elif num==user_input:
            count -= 1
            print('You have guessed the right number',num)
            print('You took',total_count-count ,'tries to guess')
            break