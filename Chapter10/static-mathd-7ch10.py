class Employee:
    company = "Google"

    def getSalary(self, signature):
        
        print("Manish have got..")
        print(
            f"Salary for workink in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning Sir...")

    @staticmethod
    def time():
        print("The time is 09 AM in the morning..")


manish = Employee()
manish.salary = 200000
manish.getSalary("Thanks...!")  # or # Employee.getSalary(manish)
manish.greet()  # Employee.greet()
manish.time()
 