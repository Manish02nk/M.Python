class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee.")

class Programmer(Employee):
    language = "Python"
    # company = "YouTube"

    def getLanguage(self):
        print(f"The langusge is {self.language}")

    def showDetails(self):
        print("This ia a Progarmmer.")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
