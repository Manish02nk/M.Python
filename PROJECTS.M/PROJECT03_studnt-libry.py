class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("* " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have issued {bookName}. Please keep it safe and return it with in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry,This book has already been issued to someone else.Please wait until the book is returned.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you injoyed reading it! Have a great day ahead!")

class Student:
    def requestBook(self):
        reqBook = input("Enter the name of the book you want to borrow : ")
        self.books = reqBook
        return reqBook

    def returnBook(self):
        retBook = input("Enter the name of the book you want to return : ")
        self.books = retBook
        return retBook

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student=Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ===== Welcome to Central Library =====
        Please choose an option:
        1.List all the books
        2.Request a book 
        3.Return/Add a book 
        4.Exit a Library'''
        print(welcomeMsg)
        a = int(input("Enter a choice : "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library! Have a great day Ahead..😊.")
            exit()
        else:
            print("!!..😡..YOU ARE ENTRED..INVALID CHOICE.!!")
            