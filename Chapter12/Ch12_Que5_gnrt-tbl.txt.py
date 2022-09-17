num = int(input("Enter Your Number : "))

table = [num*i for i in range(1, 11)]
print(table)
with open("Ch12_Que5_Table.txt", "a") as f:
    f.write(str(table))
    f.write('\n')
