class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            year = input("Enter the year of publication: ")
            library.add_book(title, author, year)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()