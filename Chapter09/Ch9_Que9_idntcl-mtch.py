file1 = "Ch9_Que9m1.txt"
file2 = "Ch9_Que9m2.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical(same)...")
else:
    print("Files are not identical(same)...")
   