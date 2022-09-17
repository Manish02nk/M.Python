with open("Ch9_Que8_txtfile.txt") as f:
    content = f.read()

with open("Ch9_Que8Copyfile.txt", 'w') as f:
    f.write(content)
