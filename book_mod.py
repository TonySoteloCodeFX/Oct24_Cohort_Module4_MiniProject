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

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_publication_date(self):
        return self.publication_date

    def get_availability(self):
        return self.availability
    
    def switch_availability(self):
        if self.availability == True:
            self.availability = False
        else:
            self.availability = True

    @classmethod
    def display_all_books(cls):
        clr()
        print("Books In Library")
        for book in cls.book_library:
            hr(50)
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author()}")

# ==================== ***** Functions ***** ====================

def add_book():
    '''Creates new book and prints confirmation.'''
    clr()
    hr(50)
    try:
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        publication_date = input("Enter Publication Date: ")

        new_book = Book(title, author, genre, publication_date)
        clr()
        hr(50)
        print(f'{new_book.title}: by {new_book.author},\nhas been added to your library.')
    except ValueError:
        clr()
        hr(50)
        print("Input is invalid. Try again.")

def display_books():
    Book.display_all_books()

def borrow_book():
    clr()
    hr(50)
    borrow_title = input("Enter Title: ")

    book_to_borrow = None
    for book in Book.book_library:
        if book.get_title() == borrow_title:
            book_to_borrow = book
            break

    if book_to_borrow:
        if book_to_borrow.get_availability() == True:
            print(f"You've borrowed: {book_to_borrow.get_title()}.")
            book_to_borrow.switch_availability()
        else:
            print(f"Sorry, {borrow_title} is currently unavailable.")
    else:
        print(f"{borrow_title} not found in the library.")

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
                borrow_book()
            elif book_operation == 3:
                pass
            elif book_operation == 4:
                pass
            elif book_operation == 5:
                display_books()
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

