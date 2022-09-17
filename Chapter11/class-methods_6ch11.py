class Employee:
    company = "TATA"
    salary = 500
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.salary = sal

       #### Or ###

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal  # This is underscore-underscore class called ***Dunder***

       ### Or ###

    @classmethod
    def changeSalary(cls, sal):  # This is class method 
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(598)
print(e.salary)
print(Employee.salary)
