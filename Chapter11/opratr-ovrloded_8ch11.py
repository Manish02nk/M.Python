class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets Add")
        return self.num + num2.num

    def __sub__(self, num2):
        print("Lets Substract")
        return self.num - num2.num

    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num

    def __truediv__(self, num2):
        print("Lets Divide")
        return self.num / num2.num

    def __floordiv__(self, num2):
        print("Lets Floordive")
        return self.num // num2.num


n1 = Number(int(input("Enter First number : ")))
n2 = Number(int(input("Enter Second number : ")))

# # # Or # # #

# n1 = Number(50)
# n2 = Number(5)

sum = n1+n2
print(sum)

sub = n1-n2
print(sub)

mul = n1*n2
print(mul)

div = n1/n2
print(div)

floordiv = n1//n2
print(floordiv)
