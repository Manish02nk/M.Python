MyDictionary = {
    "M": "Manish is a Coder",
    "Fast": "In a Quick Manner",
    "Marks": [97, 99, 98, 95, 96],
    "AnotherDict": {'Coder': 'Player'},
    1: 5
}
print("The Value of MyDicyionary is : ")
print(MyDictionary.values())

print("The Keys of MyDictionary is : ")
print(list(MyDictionary.keys()))

print("The type of Keys of MyDictionary is : ")
print(type(MyDictionary.keys()))

print("The items of MyDictionary is : ")
print(MyDictionary.items())

print("MyDictionary is : ")
print(MyDictionary)

print("My update Dictionary is : ")
updateDictionary = {
    "Gabru": "mittra",
    "Sakt Munda": "friend",
    "Sigma Male": "friend",
}
MyDictionary.update(updateDictionary)

print(MyDictionary)

print(MyDictionary.get("M"))

print(MyDictionary.get("M1"))

print(MyDictionary["M"])

print(MyDictionary["M1"])
