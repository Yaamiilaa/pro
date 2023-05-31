class Book:
    def __init__(self, title: str, author: str, age_of_publication: int, copies_available: int):
        self.title = title
        self.author = author
        self.age_of_publication = age_of_publication
        self.copies_available = copies_available

    def book_loan(self, orders: int):
        if self.copies_available < orders:
            print('There are not enough stock')
        else:
            self.copies_available -= orders

    def return_book(self):
        self.copies_available += 1

    def __str__(self) -> str:
        return f'''Title: {self.title}
Author: {self.author}
Age of publication: {self.age_of_publication}
Copies available: {self.copies_available}'''


class User:
    def __init__(self, name: str, user_id: int):
        self.name = name 
        self.user_id = user_id
        self.book_loans = []

    def show_active_loans(self):
        return self.book_loans

    def make_loan(self, book):
        if book.copies_available > 0:
            book.book_loan(1)
            self.book_loans.append(book)
        else:
            print("No copies available of the book", book.title)

    def return_book_loan(self, book):
        if book in self.book_loans:
            book.return_book()
            self.book_loans.remove(book)
        else:
            print("The book", book.title, "is not borrowed by the user.")


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books_available = []
        self.users_register = []

    def show_books(self):
        return self.books_available

    def show_users(self):
        return self.users_register

    def register_new_user(self, user):
        self.users_register.append(user)

    def add_book(self, book):
        self.books_available.append(book)

    def make_loan(self, user, book):
        if user in self.users_register:
            user.make_loan(book)
        else:
            print("The user", user.name, "is not registered in the library.")

    def return_book(self, user, book):
        if user in self.users_register:
            user.return_book_loan(book)
        else:
            print("The user", user.name, "is not registered in the library.")
