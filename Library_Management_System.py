class Library:
    def __init__(self, listOfBooks, listOfIssuedBooks):
        self.books = listOfBooks
        self.listofIssuedBooks = listOfIssuedBooks

    def listofAvailableBooks(self):
        print("Available books in the Library are :")
        for book in self.books:
            print(f" * {book}")
    
    def issueBook(self, bookName):
        if bookName in self.books:
            print(f"\nYou have issued {bookName} book. Please keep it safe and return it within 30 days.\nHave a great day!")
            self.books.remove(bookName)
            self.listofIssuedBooks.append(bookName)
            return True
        else:
            print("\nSorry! either the book is not available or issued to someone else.\nSorry for the inconvenience")
            return False

    def returnBook(self, bookName):
        if bookName in listOfIssuedBooks:
            print("Thanks! For returning the book to the library. Hope this book was helpful.")
            self.books.append(bookName)
            self.listofIssuedBooks.remove(bookName)
        else:
            print("Sorry, this book is not issued from here.")

    def addBook(self, bookName):
        print("Thanks for adding the book to library! Have a good day.")
        self.books.append(bookName)
    
class Student:
    def borrowBook(self):
        self.book = input("Enter the book you want to borrow from Library : ")
        return self.book.capitalize()
    
    def returnBook(self):
        self.book = input("Enter the book you want to return to Library : ")
        return self.book.capitalize()
    
    def addBook(self):
        self.book = input("Enter the book you want to add in the Library : ")
        return self.book.capitalize()

listOfBooks = ['Python', 'Django', 'Flask', 'Data Structures', 'Maths']
listOfIssuedBooks = []
centralLibrary = Library(listOfBooks, listOfIssuedBooks)
student = Student()
if __name__ == "__main__":
    while True:
        welcomeMsg = '''\nWELCOME TO CENTRAL LIBRARY
        CHOOSE FROM THE FOLLOWING CHOICES :
            1. AVAILABLE BOOKS IN THE LIBRARY.
            2. ISSUE A BOOK FROM THE LIBRARY.
            3. RETURN A BOOK TO THE LIBRARY.
            4. ADD A BOOK TO THE LIBRARY.
            5. EXIT THE LIBRARY.
        '''
        print(welcomeMsg)
        choice = int(input("Choose from the following choices : "))
        if choice == 1:
            centralLibrary.listofAvailableBooks()
        elif choice == 2:
            centralLibrary.issueBook(student.borrowBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            centralLibrary.addBook(student.addBook())
        elif choice == 5:
            print("Thanks for using central library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Input! Please enter a valid choice.")