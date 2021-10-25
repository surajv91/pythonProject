class Student:
    pass

A=Student()
B=Student()

print(A)
print(B)

Student.name="STU"
A.name="A"
A.std=12
A.section=1
B.std=11
B.sub=["Eng","Maths"]
print(A.name,B.name)
