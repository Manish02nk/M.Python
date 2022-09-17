with open('this.txt', 'r') as f:
    a = f.read()
with open('this.txt', 'w') as f:
    a = f.write("You know who am I...")
    print(a)
