from art import welcome, goodbye
from helpers import clr, hr
import book_ops

clr()

def run_program():
    '''Runs the main program.'''
    run_main_menu = True
    while run_main_menu:
        try:
            print(welcome)
            print('''
Main Menu:
        1. Book Main Operations
        2. User Main Operations
        3. Author Main Operations
        4. Quit
                ''')
            main_operation = int(input("Enter Number: "))

            if main_operation == 1:
                book_ops.book_menu()
            elif main_operation == 2:
                pass
            elif main_operation == 3:
                pass
            elif main_operation == 4:
                clr()
                hr(50)
                print(goodbye)
                run_main_menu = False
            else:
                clr()
                hr(50)
                print(f"{main_operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print(f"Input must be a number between 1-4.")

run_program()