
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


M = "Manish is a boy good....!"
n = remove_and_split(M, "boy")

print(n)

# print(M)
# print(M.strip())


# Strip is used for remove an extra spaces.

# this = "    Manis is a good boy..    "
# print(this)
# print(this.strip())
