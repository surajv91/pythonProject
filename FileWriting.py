f = open('First.txt', 'r')
# f.write('\nThis is the first line')
# a=f.read(3)
# print(a)
#
# a=f.read(3)
# print(a)
# for line in f:
#     print(line)
# b=f.readline()
# print(b)
# t=f.tell()
# print(t)
# f.seek(0)
# c=f.readline()
# print(c)

c=f.readlines()
print(c)
for line in c:
    print(line,end="")

f.close()