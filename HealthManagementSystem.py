def getdate():
    import datetime
    return datetime.datetime.now()

# def retrieveData():

print('1. A')
print('2. B')
print('3. C')
opt=int(input('Please select your option : '))

if opt==1 or opt==2 or opt==3:
    print('1. Food')
    print('2. Gym')
    h=int(input('Please select food or gym from above : '))
    if h==1:
        with open(f'{opt}Food.txt','a') as f:
            dt=getdate()
            a=f.write(f'[{dt}]    {opt} had Food.\n')
    elif h==2:
        with open(f'{opt}Gym.txt', 'a') as f:
            dt=getdate()
            a=f.write(f'[{dt}]    {opt} went to Gym.\n')
    else:
        print('Invalid option!!!')
else:
    print('Invalid option!!!')
