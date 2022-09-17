try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please Enter a valid value !")
except ZeroDivisionError as e:
    print("Make sure you are note dividing by 0 !")

print("Thankyou for using this code !")
