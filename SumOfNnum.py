a=eval(input("Enter value a : "))
def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n
ans=sum(a)
print(ans)

