class Employee:
    company = "Google"
    salary = 500000


manish = Employee()
rohan = Employee()
rajinder = Employee()
shubham = Employee()


# Creatinng instance attribute salary for both the objects
# manish.salary = 190000
# rohan.salary=180000
# rajinder.salary=170000
# shubham.salary=165000
print(manish.salary)
print(rohan.salary)
print(rajinder.salary)
print(shubham.salary)


print(manish.address) # throw attribute error 'address' is not present in instent/class

 