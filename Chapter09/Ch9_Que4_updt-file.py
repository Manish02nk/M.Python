with open("Ch9_Que4_updt-file.txt") as f:
    content = f.read()


content = content.replace("please..", "Altimate..")

with open("Ch9_Que4_updt-file.txt", "w") as f:
    f.write(content)
