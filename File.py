# Use open function to read the content of a file 
f=open('File.txt','r')
# data=f.read()
data=f.read(5) # read first 5 charecters from the file.
print(data)
f.close()
