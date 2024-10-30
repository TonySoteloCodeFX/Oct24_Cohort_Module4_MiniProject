<h1>Mini-Project: Library Management System</h1>
<hr>

<h4>Project Requirements</h4>

In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

<h5>Enhanced User Interface (UI) and Menu:</h5>

1. Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.

```
    Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit
```
 - Book Operations:

```
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
```
 - User Operations:

```
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
```
 - Author Operations:

```
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
```

<h4>Class Structure:</h4>
1. Implement a class structure that represents key entities in the library management system, including:

 - Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
<br>
 - User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
<br>
 - Author: A class representing book authors with attributes like name and biography.

<h5>Encapsulation:</h5>

1. Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.


<h5>Modules:</h5>

1. Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

<h5>Menu Actions:</h5>

1. Implement the following actions in response to menu selections using the classes you've created:

 - Adding a new book with all relevant details.
<br>
 - Allowing users to borrow a book, marking it as "Borrowed."
<br>
 - Allowing users to return a book, marking it as "Available."
<br>
 - Searching for a book by its unique identifier (title) and displaying its details.
<br>
 - Displaying a list of all books with their unique identifiers.
<br>
 - Adding a new user with user details.
<br>
 - Viewing user details.
<br>
 - Displaying a list of all users.
<br>
 - Adding a new author with author details.
<br>
 - Viewing author details.
<br>
 - Displaying a list of all authors.
<br>
 - Quitting the application.

<h5>User Interaction:</h5>

1. Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
<br>
2. Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)

<h5>Error Handling:</h5>

1. Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

<h5>GitHub Repository:</h5>

1. Create a GitHub repository for your project and commit code regularly.
<br>
2. Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
<br>
3. Include a link to your GitHub repository in your project documentation.

<h5>Optional Bonus Points</h5>

1. <b>Text File Handling (Bonus):</b> Implement text file handling to load and save data for various entities in the library management system, such as books, users, authors, and genres. Create dedicated text files for each entity type and develop methods to read data from these files during system startup and save data to them when changes occur. Ensure data integrity and error handling during file operations.
<br>
2. <b>Reservation System (Bonus):</b> Enhance the system by implementing a reservation system. Users can reserve books that are currently unavailable, and the system will notify them when the book becomes available. Develop methods to handle reservations, check availability, and notify users of reservation status changes.
<br>
3. <b>Fine Calculation (Bonus):</b> Implement a fine calculation system for overdue books. Assign due dates to borrowed books, and calculate fines for users who exceed the due date. Develop a mechanism for users to pay fines and update their accounts accordingly.

<h5>Submission</h5>
 - Upon completing the project, submit your code, including all source code files, and the README.md file in your GitHub repository to your instructor or designated platform.
<br><br>
<b>NOTE:</b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.
<br><br>

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

View Rubric here: <a href="https://codingtemple.notion.site/Module-4-Mini-Project-0f7f92a54ba148ae8908ce2b5ebc3157">Module 4 Mini-Project Rubric</a>