class Employee:
    company = "Google"

    def getSalary(self):
        print(
            f"Salary for employee workink in {self.company} is {self.salary}")

        # print("Manish ")
        # print("Salary is 200K")


manish = Employee()
manish.salary = 200000

manish.getSalary()  # or
# Employee.getSalary(manish)
