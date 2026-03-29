class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} kitobi olindi.")
        else:
            print("Kitob mavjud emas.")

    def return_book(self):
        self.available = True
        print(f"{self.title} qaytarildi.")

    def get_info(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} qo'shildi.")

    def show_books(self):
        print("\nKitoblar:")
        for book in self.books:
            print(book.get_info())

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


def run_library():
    lib = Library()

    b1 = Book("Python Basics", "John Smith")
    b2 = Book("AI Guide", "Sara Lee")
    b3 = Book("Data Science", "Mike Ross")

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    lib.show_books()

    book = lib.find_book("Python Basics")

    if book:
        book.borrow()

    lib.show_books()

    if book:
        book.return_book()

    lib.show_books()


run_library()
