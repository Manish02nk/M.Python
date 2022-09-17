class Employee:
    pass
    
    def printDetails(self):
        return f"Name is {self.name}.Salary is  {self.salary} & roll number is {self.roll}"


ravi=Employee()
rahul=Employee()

ravi.name="Ravi"
ravi.salary=345
ravi.roll=34

rahul.name="rahul"
rahul.salary=348
rahul.roll=31

print(rahul.printDetails())
