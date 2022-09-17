###   Using While Loop #####

# n=int(input("Enter the number N limit :  "))
# Sum=0
# i=1
# while i<=n:
#     Sum+=i
#     i+=1
# print("Sum = ",Sum)

###   Using Recuirsen ###

a=eval(input("Enter the value of a : "))
def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n
b=sum(a)
print(b)
