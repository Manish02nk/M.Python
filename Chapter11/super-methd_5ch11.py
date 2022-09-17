class Person:
    country = "INDIA"
    
    def __init__(self):
        print("Initializing Person...!\n")

    def takeBreath(self):
        print("I am breathing...!")

class Employee(Person):
    company = "Mahindra"
    
    def __init__(self):
        super().__init__()
        print("Initializing Employee...!\n")
        
    def getSalary(self):
        print(f"Salary is {self.slary}")

    def takeBreath(self):
        super().takeBreath()
        print("I m an also a human so I m breathing...!")

class Programmer(Employee):
    company = "Fiverr"
    
    def __init__(self):
        super().__init__()
        print("Initializing Programmer..!\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I m a Programmer so I m breathing++..!")

# p = Person()
# p.takeBreath()
# print(p.country)
# print(p.company) # Throw an ERROR

# e = Employee()
# e.takeBreath()
# print(e.company)
# print(e.country)

pr = Programmer()
# pr.takeBreath()
# print(pr.company)
# print(pr.country)
