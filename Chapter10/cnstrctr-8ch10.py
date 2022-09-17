class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created..!")
    
    def getDetails(self):
        print(f"The name of the member is {self.name}")
        print(f"The salary of the member is {self.salary}")
        print(f"The subunit of the member is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for workink in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning Sir...")

    @staticmethod
    def time():
        print("The time is 09 AM in the morning..")

# manish = Employee() -->This throws an error

manish = Employee("Manish", 200000, "YouTube")
manish.getDetails()

 