class Employee:
    """Has global Employee details"""
    no_of_leaves = 20
    location = "Mumbai"

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, role is {self.role}"


A = Employee("A", 10000, "Manager")
B = Employee("B",2000,"Employee")

# A.name="A"
# A.salary=10000
# A.role="Manager"
#
# B.name="B"
# B.salary=2000
# B.role="Employee"

print(A.printdetails())
print(A.name)