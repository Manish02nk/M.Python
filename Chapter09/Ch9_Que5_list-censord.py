words = ["donkey", "kaddu", "pagal", "mottey"]

with open("Ch9_Que5.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "@#$#^&^@*%$%..")
    with open("Ch9_Que5.txt", "w") as f:
        f.write(content)
