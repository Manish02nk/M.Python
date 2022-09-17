# convert celsius to fahrenheit

# def farh(cel):
#     return (cel*(9/5)) + 32
# # c = 45
# c = int(input("Entr The Number : "))
# f = farh(c)
# print("The Fahrenheit Temperature is " + str(f))


# convert  fahrenheit to celsius

def celsius(farh):
    return(farh-(32)) * 5/9


f = 6
# f = int(input("Enter the Number : "))
c = celsius(f)

print("The Celsius Temperature is " + str(c))
