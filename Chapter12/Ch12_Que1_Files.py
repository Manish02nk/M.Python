# def readFile(filename):
#     with open(filename, "r") as f:
#         print(f.read())

# readFile("Ch12_Que1_Files1.txt")
# readFile("Ch12_Que1_Files2.txt")
# readFile("Ch12_Que1_Files3.txt")
# readFile("Ch12_Que1_Files4.txt")

def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is Not Found")


readFile("Ch12_Que1_Files1.txt")
readFile("Ch12_Que1_Files2.txt")
readFile("Ch12_Que1_Files3.txt")
readFile("Ch12_Que1_Files4.txt")
