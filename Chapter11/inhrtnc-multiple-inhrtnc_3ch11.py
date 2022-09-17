class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level+1

# class Programmer(Freelancer,Employee):
class Programmer(Employee, Freelancer):
    name = "Manish"

m = Programmer()
print(m.level)
print(m.eCode)
print(m.name)
print(m.company)
m.upgradeLevel()
print(m.level)
