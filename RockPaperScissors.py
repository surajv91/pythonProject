import random

rps = ['Rock', 'Paper', 'Scissors']
c = random.choice(rps)
# print(c)

choice=int(input("""Please enter the below selection:
1. Rock
2. Paper
3. Scissors\n"""))

if choice==1:
    guess="Rock"
elif choice==2:
    guess="Paper"
elif choice==3:
    guess="Scissors"
else:
    print("Invalid Input!!!")

if (c.upper()=='ROCK' and guess.upper()=="SCISSORS") or (c.upper()=='SCISSORS' and guess.upper()=='PAPER') or (c.upper()=='PAPER' and guess.upper()=="ROCK") :
    print("Computer Wins")
elif (guess.upper()=='ROCK' and c.upper()=="SCISSORS") or (guess.upper()=='SCISSORS' and c.upper()=='PAPER') or (guess.upper()=='PAPER' and c.upper()=="ROCK") :
    print("You Win")
else:
    print('Its a Tie!!!')

print(f'Computer selected {c}')
print(f'You selected {guess}')