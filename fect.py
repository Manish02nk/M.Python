### Using Recuirsen ###

# a=eval(input("Enter value of a : "))
# def fect(n):
#     if n==0:
#         return 1
#     return fect(n-1)*n
# b=fect(a)
# print(b)


a=eval(input("Enter value of a : "))
def fect(n):
    a=1
    while n>1:
        a=a*n
        n=n-1
    return a
b=fect(a)
print(b)


        
        
