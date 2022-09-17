try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
    exit()  # With out this (-exit()-) program run with Error

finally:
    print("We are done !")

print("Thanks for using the program")
