letter = '''Dear <|NAME|>,
Greeting from AB Coding house , We are happy to tell you about your selection
You are selected !
Have a great day ahead !
Thanks and Regards ,
Billow
Date : <|DATE|>'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
