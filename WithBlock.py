with open("First.txt") as f:
    a=f.readlines()
    print(a)

f=open("First.txt",'rt')
a=f.readlines()
print(a)
f.close()

