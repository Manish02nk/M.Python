class Person:
    country = "INDIA"

    def takeBreath(self):
        print("I am breathing...!")


class Employee(Person):
    company = "Mahindra"

    def getSalary(self):
        print(f"Salary is {self.slary}")

    def takeBreath(self):
        print("I m an also a human so I m breathing...!")


class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print(f"No salary to programmers")


p = Person()
p.takeBreath()
print(p.country)
# print(p.company) # Throw an ERROR

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
