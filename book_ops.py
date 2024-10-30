from helpers import clr, hr
from art import main_book_menu

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
                pass
            elif book_operation == 2:
                pass
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