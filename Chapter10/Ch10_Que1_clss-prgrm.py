class Programmer:
    company = "Microsoft Company"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


manish = Programmer("Manish", "Skype")
rohan = Programmer("Rohan", "GitHub")
manish.getInfo()
rohan.getInfo()
