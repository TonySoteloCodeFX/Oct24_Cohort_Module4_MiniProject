from art import welcome, goodbye
from helpers import clr, hr

def run_program():
    '''Runs the main program.'''
    clr()
    print(welcome)

    run_operation = True
    while run_operation:
        try:
            print('''
                Main Menu:
                        1. Book Operations
                        2. User Operations
                        3. Author Operations
                        4. Quit
                ''')
            operation = int(input("Enter Number: "))

            if operation == 1:
                pass
            elif operation == 2:
                pass
            elif operation == 3:
                pass
            elif operation == 4:
                clr()
                hr(50)
                print(goodbye)
                run_operation = False
            else:
                clr()
                hr(50)
                print(f"{operation} is not an option. Try again.")
        except ValueError:
            clr()
            hr(50)
            print(f"Input must be a number between 1-4.")

run_program()