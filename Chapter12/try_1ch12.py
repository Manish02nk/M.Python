while(True):
    print("Press m to quite ")
    a = input("Enter a number :")
    if a == 'm':
        break
    try:
        a = int(a)
        if a > 6:
            print(f"You Entered {a} number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error : {e}")
print("Thanks for playing this game.")
