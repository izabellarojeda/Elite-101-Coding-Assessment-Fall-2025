from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def print_available_books(books_data): 
   # printing details of books in system
   if not books_data:
      print("No books available in system")
      return

   print('Available Books:')
   for book in books_data:
      # data uses the key 'available' in `library_books.py`
      if book.get('available', False):
         book_id = book.get('id', 'N/A')
         title = book.get('title', 'Untitled')
         author = book.get('author', 'Unknown')
         print(f"{book_id}: {title} — {author}")

if not any(book.get('available', False) for book in library_books):
   print("No books are currently avalaible.")

    #example for looking for available books
if __name__ == "__main__":
        library_books: [ 
        {{'id': 'B3', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'available': True},
        {'id': 'B4', 'title': '1984', 'author': 'George Orwell', 'available': False},
        {'id': 'B2', 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': True},
        {'id': 'B5', 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'available': True},
        {'id': 'B8', 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'available': False},
        ]



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
   # demo: print currently available books from the catalog
   print_available_books(library_books)

