from helpers import clr, hr
from art import main_book_menu

class Book:
    book_library = []

    def __init__(self, title, author, genre, publication_date):
        '''Creates new book and adds it to book library.'''
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
        Book.book_library.append(self)

    def get_book(self):
        print(self.title) 
    
    def switch_availability(self):
        availability = self.availability
        if availability == True:
            self.availability = False
        else:
            self.availability = True

    def borrow_book(self):
        pass

# ==================== ***** Functions ***** ====================

def add_book():
    '''Creates new book and prints confirmation.'''
    try:
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        genre = input("Enter Book Genre: ")
        publication_date = input("Enter Book Publication Date: ")

        new_book = Book(title, author, genre, publication_date)
        print(f'{new_book.title}: by {new_book.author},\nhas been added to the library.')
    except ValueError:
        print("Input is invalid. Try again.")

def book_menu():
    clr()
    hr(50)
    book_ops_menu = True
    while book_ops_menu:
        try:
            print(main_book_menu)
            print('''
Main Book Menu:
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books
            6. Return to main menu
                  ''')
            book_operation = int(input("Enter Number: "))

            if book_operation == 1:
                add_book()
            elif book_operation == 2:
                Book.borrow_book()
            elif book_operation == 3:
                pass
            elif book_operation == 4:
                pass
            elif book_operation == 5:
                pass
            elif book_operation == 6:
                clr()
                hr(50)
                book_ops_menu = False
            else:
                clr()
                hr(50)
                print(f"{book_operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print("Input must be a number between 1-6")