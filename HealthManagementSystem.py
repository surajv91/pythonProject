def getdate():
    import datetime
    return datetime.datetime.now()

# def retrieveData():



print('1. log')
print('2. retrieve')
choice=int(input('What do you want to do or to exit press 0 :'))

if choice==1:
    print('1. A')
    print('2. B')
    print('3. C')
    opt1=input('Please select your option from above or 0 to exit : ')

    if opt1=='1':
        opt='A'
    elif opt1=='2':
        opt='B'
    elif opt1=='3':
        opt='C'
    elif opt1=='0':
        exit('Successful')
    else:
        print('Wrong option!!!')

    if opt.lower()=='a' or opt.lower()=='b' or opt.lower()=='c':
        print('1. Food')
        print('2. Gym')
        h1=input('Please select food or gym from above or 0 to exit : ')

        if h1=='1':
            h='Food'
        elif h1=='2':
            h='Gym'
        elif h1=='0':
            exit('exit')
        else:
            print('Wrong option!!!')

        if h.lower()=='food':
            with open(f'{opt.capitalize()}Food.txt','a') as f:
                dt=getdate()
                a=f.write(f'[{dt}]    {opt.upper()} had Food.\n')
        elif h.lower()=='gym':
            with open(f'{opt.capitalize()}Gym.txt', 'a') as f:
                dt=getdate()
                a=f.write(f'[{dt}]    {opt.upper()} went to Gym.\n')
        else:
            print('Invalid option!!!')
    else:
        print('Invalid option!!!')
elif choice==2:
    print('code to be done')
    print('1. A')
    print('2. B')
    print('3. C')
    opt1=input('Please select your option from above or 0 to exit : ')

    if opt1=='1':
        opt='A'
    elif opt1=='2':
        opt='B'
    elif opt1=='3':
        opt='C'
    elif opt1=='0':
        exit('Successful')
    else:
        print('Wrong option!!!')

    if opt.lower()=='a' or opt.lower()=='b' or opt.lower()=='c':
        print('1. Food')
        print('2. Gym')
        opt2 = input('Please select your option from above or 0 to exit : ')
        if opt2=='1':
            ch='Food'
        elif opt2=='2':
            ch='Gym'
        else:
            print('Wrong option!!!')

        with open(f'{opt.upper()}{ch.capitalize()}.txt','r') as f:
            a=f.read()
            print(a)
elif choice==0:
    exit('exit successful')
else:
    print('Invalid option!!!')
