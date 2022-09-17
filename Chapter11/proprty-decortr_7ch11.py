class Employee:
    company = "Bharat Gas"
    salary = 5800
    salarybonus = 4200
    # totalSalary=10,000

    #  This is @.getter Method ### Getter Method ###
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus


    # This is @.setter Method  ### Setter Method ### 
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val-self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary =6300
print(e.salary)
print(e.salarybonus)
