# ============================================================
# Library Checkout System
# AP Computer Science Principles - Create Performance Task
# ============================================================
# This program allows librarians to log in and manage
# a library's book collection. Librarians can add, view,
# edit, remove, check out, and return books.
# ============================================================

# --- Librarian account data (dictionary of dictionaries) ---
# Each account stores a password and a library_data dictionary.
# Using a dictionary makes it easy to look up any account
# instantly without searching through a list manually.

sample_books = {
    "The Hobbit": {"author": "J.R.R. Tolkien", "status": "Available"},
    "1984": {"author": "George Orwell", "status": "Checked Out"},
    "Atomic Habits": {"author": "James Clear", "status": "Available"},
    "The Alchemist": {"author": "Paulo Coelho", "status": "Available"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "status": "Checked Out"}
}

# This stores all librarian accounts.
# Key = username, Value = password + that librarian's personal library data.
librarian_accounts = {
    "testlibrarian": {
        "password": "library123",
        "library_data": sample_books
    }
}


# --- Procedure: list_books ---
# Quick summary: prints all books, or only books with a chosen status.
# Purpose: Displays all books in the library, with optional
#          filtering by status ("Available" or "Checked Out").
# Parameters:
#   book_dict  - the dictionary of books to display
#   filter_status - (str or None) if provided, only books
#                   with that status are shown
# This procedure contains:
#   Sequencing  - steps run top to bottom
#   Selection   - if/elif checks decide what to print
#   Iteration   - for loop goes through every book
def list_books(book_dict, filter_status=None):
    # If a filter is provided, show only books with that status.
    # If no filter is provided, show every book.
    # --- Sequencing: set up the header first ---
    if filter_status:
        print(f"\nBooks with status '{filter_status}':")
    else:
        print("\nAll Library Books:")

    # --- Selection: handle empty library ---
    if not book_dict:
        print("No books are currently in the system.")
        return

    found_any = False  # track whether any books matched the filter

    # --- Iteration: loop through every book in the collection ---
    for title, info in book_dict.items():

        # --- Selection: apply the status filter if one was given ---
        if filter_status is None or info["status"] == filter_status:
            print(f"  {title} by {info['author']} - {info['status']}")
            found_any = True

    # --- Selection: tell the user if the filter matched nothing ---
    if not found_any:
        print(f"  No books found with status '{filter_status}'.")


# --- Procedure: add_book ---
# Quick summary: asks for book details and saves a new book record.
# Asks the user for a title, author, and status, then
# adds the new book to book_dict.
# Parameters: book_dict - the current library collection
def add_book(book_dict):
    # Ask user for the new book's title.
    book_title = input("\nEnter book title: ")

    # Selection: prevent duplicate entries
    if book_title in book_dict:
        print("\nThat book is already in the library system.")
        return

    # Ask for book details.
    author = input(f"Enter author for '{book_title}': ")
    status = input("Enter status (Available / Checked Out): ").strip().title()

    # Selection: default to Available for unrecognized input
    if status not in ["Available", "Checked Out"]:
        print("Unrecognized status. Defaulting to 'Available'.")
        status = "Available"

    # Sequencing: store the new entry, then confirm
    book_dict[book_title] = {"author": author, "status": status}
    print(f"\n'{book_title}' has been added to the system.")


# --- Procedure: remove_book ---
# Quick summary: deletes a book if the title exists in the library.
# Asks the user for a title and removes it from book_dict.
# Parameters: book_dict - the current library collection
def remove_book(book_dict):
    book_title = input("\nEnter the title of the book to remove: ")

    # Selection: only remove if it exists
    if book_title in book_dict:
        del book_dict[book_title]
        print(f"'{book_title}' has been removed.")
    else:
        print("Book not found.")


# --- Procedure: edit_book ---
# Quick summary: updates the author and status for an existing book.
# Lets the user update an existing book's author and status.
# Parameters: book_dict - the current library collection
def edit_book(book_dict):
    book_title = input("\nEnter the title of the book to edit: ")

    # Selection: only edit if it exists
    if book_title in book_dict:
        new_author = input(f"Enter new author for '{book_title}': ")
        new_status = input("Enter new status (Available / Checked Out): ").strip().title()

        # Selection: keep old status if new one is invalid
        if new_status not in ["Available", "Checked Out"]:
            print("Invalid status. Keeping previous status.")
            new_status = book_dict[book_title]["status"]

        # Replace the old author/status with the new values.
        book_dict[book_title] = {"author": new_author, "status": new_status}
        print(f"\n'{book_title}' has been updated.")
    else:
        print("Book not found.")


# --- Procedure: view_book ---
# Quick summary: shows one book's title, author, and status.
# Displays detailed info for one book.
# Parameters: book_dict - the current library collection
def view_book(book_dict):
    book_title = input("\nEnter book title: ")

    # Selection: only display if found
    if book_title in book_dict:
        info = book_dict[book_title]
        print(f"\nTitle:  {book_title}")
        print(f"Author: {info['author']}")
        print(f"Status: {info['status']}")
    else:
        print("Book not found. Check spelling and try again.")


# --- Procedure: checkout_return_book ---
# Quick summary: switches a book between Available and Checked Out.
# Toggles a book's status between Available and Checked Out.
# Parameters: book_dict - the current library collection
def checkout_return_book(book_dict):
    book_title = input("\nEnter the title of the book: ")

    # Selection: only act if it exists
    if book_title in book_dict:
        current_status = book_dict[book_title]["status"]

        # Selection: toggle based on current status
        # If available, check it out. Otherwise, return it.
        if current_status == "Available":
            book_dict[book_title]["status"] = "Checked Out"
            print(f"\n'{book_title}' has been checked out.")
        else:
            book_dict[book_title]["status"] = "Available"
            print(f"\n'{book_title}' has been returned and is now available.")
    else:
        print("Book not found.")


# --- Procedure: login ---
# Quick summary: creates a new account or collects existing login info.
# Handles both new account creation and existing login.
# Returns the username and password entered by the user.
# No parameters needed (uses global librarian_accounts).
def login():
    print("\n===== Library Checkout System =====")
    create_account = input("\nDo you need to create a new librarian account? (y/n): ").lower()

    if create_account == 'y':
        username = input("\nChoose a username: ")
        password = input("Choose a password: ")

        # Sequencing: create account then confirm
        librarian_accounts[username] = {"password": password, "library_data": {}}
        print("\nAccount created! You can now log in.")
        return username, password
    else:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        return username, password


# --- Procedure: verify_login ---
# Quick summary: checks whether login credentials are correct.
# Checks whether the username exists and the password matches.
# Parameters:
#   username - the username entered by the user
#   password - the password entered by the user
# Returns: True if valid, False otherwise
def verify_login(username, password):
    # Selection: check existence then password match
    if username in librarian_accounts and librarian_accounts[username]["password"] == password:
        return True
    else:
        print("\nWrong username or password. Please try again.")
        return False


# --- Procedure: logout ---
# Quick summary: prints a goodbye message when the user logs out.
# Prints a logout message. No parameters needed.
def logout():
    print("\nYou have been logged out. Goodbye!")


# ============================================================
# MAIN PROGRAM LOOP
# Keeps asking for login until credentials are correct,
# then shows the menu until the user logs out or exits.
# ============================================================

while True:
    # --- Input: collect login credentials ---
    username, password = login()

    if verify_login(username, password):
        # Output: confirm successful login
        print("\nLogin successful! Welcome,", username)
        # Grab the current user's book dictionary so menu actions edit their data.
        current_library_data = librarian_accounts[username]["library_data"]

        # Inner loop: keep showing the menu until logout/exit
        while True:
            # Output: display menu options
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

            # Input: get the user's menu choice
            choice = input("\nEnter your choice: ")

            # Selection: route to the correct procedure
            if choice == '1':
                add_book(current_library_data)
            elif choice == '2':
                view_book(current_library_data)
            elif choice == '3':
                # Call list_books with no filter — shows everything
                list_books(current_library_data)
            elif choice == '4':
                # Call list_books with filter_status="Available"
                list_books(current_library_data, filter_status="Available")
            elif choice == '5':
                # Call list_books with filter_status="Checked Out"
                list_books(current_library_data, filter_status="Checked Out")
            elif choice == '6':
                edit_book(current_library_data)
            elif choice == '7':
                remove_book(current_library_data)
            elif choice == '8':
                checkout_return_book(current_library_data)
            elif choice == '9':
                logout()
                break  # break inner loop → go back to login
            elif choice == '10':
                print("\nExiting the system. Goodbye!")
                exit()
            else:
                # Output: invalid input message
                print("Invalid choice. Please enter a number from 1 to 10.")