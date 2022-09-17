# creating empaty set
a = set()
print(type(a))

# Adding values to an empty set
a.add(4)
a.add(4)
a.add(5)
a.add(5)  # adding a value repeatedly does not change a set
a.add((4, 5, 6))

# a.add({4: 5}) # Can't add list or dictionary to sets
print(a)

print(len(a))  # Prints the lenth of this set

# Removel of an Item
a.remove(5)  # Remove 5 from set a
# print(a)
# throw an error while trying to remove 15(which is not present in this set)
# a.remove(15)
print(a)

print(a.pop())
print(a)
