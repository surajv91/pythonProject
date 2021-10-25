class Employee:
    """Has global Employee details"""
    no_of_leaves=20
    location="Mumbai"
    pass

A=Employee()
B=Employee()

A.name="A"
A.salary=10000
A.role="Manager"

B.name="B"
B.salary=2000
B.role="Employee"

# print(A.salary,A.no_of_leaves)
# print(B.salary,B.no_of_leaves)
# print(Employee.__dict__)

# print(A.no_of_leaves)
# print(Employee.no_of_leaves)
# Employee.no_of_leaves=33
# print(A.no_of_leaves)
# print(Employee.no_of_leaves)
# B.no_of_leaves=20
# print(B.no_of_leaves)
# print(B.location)
# print(Employee.__dict__)
# print(A.__dict__)
# print(Employee.__class__(A))

print(A.__dict__)
A.no_of_leaves=40
print(A.__dict__)
print(Employee.no_of_leaves)
