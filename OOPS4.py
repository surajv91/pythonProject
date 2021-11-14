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

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

A = Employee("A", 10000, "Manager")
B = Employee("B",2000,"Employee")

print(A.salary)
print(A.printdetails())
# Employee.no_of_leaves=40
A.change_leaves(34)
print(A.no_of_leaves)