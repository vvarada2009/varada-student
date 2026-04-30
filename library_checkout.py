# =====================================
# Library Checkout System
# This program lets librarians log in and manage many things with books in the system. 
# They can add, view, edit, remove, check out, and return books.
# =====================================

# Each account has a password and username and its own library data.


sample_books = {
    "The Hobbit": {"author": "J.R.R. Tolkien", "status": "Available"},
    "1984": {"author": "George Orwell", "status": "Checked Out"},
    "Atomic Habits": {"author": "James Clear", "status": "Available"},
    "The Alchemist": {"author": "Paulo Coelho", "status": "Available"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "status": "Checked Out"}
}


# All librarian accounts have a username, password and their personal library data. 
librarian_accounts = {
    "testlibrarian": {
        "password": "library123",
        "library_data": sample_books
    }
}


# list_books
# Shows all books or only books with a chosen status.
# book_dict: the books to show
def list_books(book_dict, filter_status=None):

    if filter_status:
        print(f"\nBooks with status '{filter_status}':")
    else:
       
     print("\nAll Library Books:")
    if not book_dict:
        print("No books are currently in the system.")
        return

    found_any = False 

    
    for title, info in book_dict.items():

        
        if filter_status is None or info["status"] == filter_status:
            print(f"  {title} by {info['author']} - {info['status']}")
            found_any = True

    
    if not found_any:
        print(f"  No books found with status '{filter_status}'.")



# Here users can add a book into the system 
# System asks for the title of the book and author so that it can be dded to the library collection. 
# book_dict: current library collection
def add_book(book_dict):
    # Ask for the new book title.
    book_title = input("\nEnter book title: ")

    # Stops if the book is already there so there are not two copies of the same book. 
    if book_title in book_dict:
        print("\nThat book is already in the library system.")
        return

    # Ask for the rest of the details such as the author and if it is avilable or checked out. 
    author = input(f"Enter author for '{book_title}': ")
    status = input("Enter status (Available / Checked Out): ").strip().title()

    # he default option is Available if the user does not enter a valid status 
    if status not in ["Available", "Checked Out"]:
        print("Unrecognized status. Defaulting to 'Available'.")
        status = "Available"

    # Saves the book and a confirmation message is shown 
    book_dict[book_title] = {"author": author, "status": status}
    print(f"\n'{book_title}' has been added to the system.")


# Booke can be removed from the system if it is no longer needed 
# Removes a book if it exists.
# book_dict: current library collection
def remove_book(book_dict):
    book_title = input("\nEnter the title of the book to remove: ")

    # Remove only if the title exists in the system. Otherwise it shows a message saying that the book was not found
    if book_title in book_dict:
        del book_dict[book_title]
        print(f"'{book_title}' has been removed.")
    else:
        print("Book not found.")


# edit_book
# Updates author and status for a book.
# book_dict: current library collection
def edit_book(book_dict):
    book_title = input("\nEnter the title of the book to edit: ")

    # Edit only if the title exists.
    if book_title in book_dict:
        new_author = input(f"Enter new author for '{book_title}': ")
        new_status = input("Enter new status (Available / Checked Out): ").strip().title()

        # Keep the old status if input is invalid
        if new_status not in ["Available", "Checked Out"]:
            print("Invalid status. Keeping previous status.")
            new_status = book_dict[book_title]["status"]

        # Save the new values
        book_dict[book_title] = {"author": new_author, "status": new_status}
        print(f"\n'{book_title}' has been updated.")
    else:
        print("Book not found.")


# view_book
# Shows details for one book such as title, author, and status 
# book_dict: current library collection
def view_book(book_dict):
    book_title = input("\nEnter book title: ")

    # Show info only if the book is found
    if book_title in book_dict:
        info = book_dict[book_title]
        print(f"\nTitle:  {book_title}")
        print(f"Author: {info['author']}")
        print(f"Status: {info['status']}")
    else:
        print("Book not found. Check spelling and try again.")


# checkout_return_book
# Switches a book from Available to Checked Out and the other way around too
# book_dict: current library collection
def checkout_return_book(book_dict):
    book_title = input("\nEnter the title of the book: ")

    # Continue only if the book exists.
    if book_title in book_dict:
        current_status = book_dict[book_title]["status"]
 # If available, check it out. Otherwise, return it.
        if current_status == "Available":
            book_dict[book_title]["status"] = "Checked Out"
            print(f"\n'{book_title}' has been checked out.")
        else:
            book_dict[book_title]["status"] = "Available"
            print(f"\n'{book_title}' has been returned and is now available.")
    else:
        print("Book not found.")


# I used modified code from Copilot to help me with the login and logout system.
# login system allows users to create accounts and login with a username and password. 
# Creates a new account or signs in to an existing one.
# Returns the username and password entered.
def login():
    print("\n===== Library Checkout System =====")
    create_account = input("\nDo you need to create a new librarian account? (y/n): ").lower()

    if create_account == 'y':
        username = input("\nChoose a username: ")
        password = input("Choose a password: ")

        # Creates account then confirm it was created by showing a message 
        librarian_accounts[username] = {"password": password, "library_data": {}}
        print("\nAccount created! You can now log in.")
        return username, password
    else:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        return username, password


# verify_login
# Checks if username and password are correct.
# Returns True if valid, otherwise False.
def verify_login(username, password):
    # Check that username exists and password matches.
    if username in librarian_accounts and librarian_accounts[username]["password"] == password:
        return True
    else:
        print("\nWrong username or password. Please try again.")
        return False


# logout
# Prints a goodbye message.
def logout():
    print("\nYou have been logged out. Goodbye!")


# =====================================
# Main loop:
# Keep asking for login until it works,
# then show the menu until logout or exit.
# =====================================

while True:
    # Ask for login info.
    username, password = login()

    if verify_login(username, password):
        # Confirm login success.
        print("\nLogin successful! Welcome,", username)
        # Use this user's book data for all menu actions.
        current_library_data = librarian_accounts[username]["library_data"]

# Keep showing the menu until the user logs out or exits
    while True:
            print("\n---------- MENU ----------")
            print("1. Add a book")
            print("2. View a book")
            print("3. List ALL books")
            print("4. List AVAILABLE books only")
            print("5. List CHECKED OUT books only")
            print("6. Edit a book")
            print("7. Remove a book")
            print("8. Check out / Return a book")
            print("9. Log out")
            print("10. Exit")

            
            choice = input("\nEnter your choice: ")


        
            if choice == '1':
                add_book(current_library_data)
            elif choice == '2':
                                view_book(current_library_data)
            elif choice == '3':
                                list_books(current_library_data)
            elif choice == '4':
                                list_books(current_library_data, filter_status="Available")
            elif choice == '5':
                                list_books(current_library_data, filter_status="Checked Out")
            elif choice == '6':
                edit_book(current_library_data)
            elif choice == '7':
                remove_book(current_library_data)
            elif choice == '8':
                checkout_return_book(current_library_data)
            elif choice == '9':
                logout()
                break  # Goes back to the login
            elif choice == '10':
                print("\nExiting the system. Goodbye!")
                exit()
            else:
                # Show message for invalid input.
                print("Invalid choice. Please enter a number from 1 to 10.")