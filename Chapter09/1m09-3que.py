# for i in range(int(input("Enter which num table you want : ")), int(input("Enter 1st main limit of table : "))):

for i in range(14, 11):
    with open("1m09table.txt", "w") as f:
        # for j in range(int(input("Enter num , you wants table starting from : ")), int(input("Table kahaa tak likhani hai : "))):
        for j in range(1, 11):
            f.write(f"{i}*{j}={i*j}\n")
    break

# # num = int(input("Enter the number : "))
# # print("Multiplication Table Of", num)

# for i in range(1, 11):
# for i in range(1, int(input("enter ending num :"))):

#     with open("Ch9_Que3_tables.txt", "w") as f:
#         print(num, "*", i, "=", num*i)
#         for j in range(int(input("enter ending num :"))):
#             f.write(f"{i}*{j}={i*j}\n")
#         break
