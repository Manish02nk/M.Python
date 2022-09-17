# Use open function toread the content of a file !

# f = open('files_ch09.txt', 'r')

# By default the mode is r !

f = open('files_ch09.txt')
# data = f.read()

data = f.read(10)  # reads first 10 charecters from the file !
print(data)
f.close()
