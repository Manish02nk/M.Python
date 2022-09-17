num = int(input("Enter the starting number : "))

l1 = int(input("Enter the ending number : "))

for i in range(l1, 0, -1):

    # print(str(num) + " X " + str(i) + " = " + str(i*num))

    # or (both method are equily worked)

    print(f" {num} X {i} = {num*i} ")
