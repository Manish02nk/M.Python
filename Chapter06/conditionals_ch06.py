# This program is dynamic(user entered value)

a = int(input("Enter your age :"))
if(a >= 18):
    print("You can vot for everyone")
elif(a >= 12):
    print("You can vote for teenager")
elif(a >= 5):
    print("You can vote for children")
else:
    print("Jaake Padaai Karr... Samajhaa..")

# This program is strategic(value declayred)

age = 18
if(age > 17):
    print("You can vote for children")
else:
    print("Jaake Padaai Karr....Samajhaa..")
