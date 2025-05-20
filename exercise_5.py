class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_info(self):
        return f"Ім'я: {self.name}, Рік народження: {self.birth_year}"

class Book:
    def __init__(self, title, author, year, annotation=""):
        self.title = title
        self.author = author
        self.year = year
        self.annotation = annotation

    def get_info(self):
        info = f"Назва: {self.title}, Рік видання: {self.year}, Автор: {self.author.name}"
        if self.annotation:
            info += f"\n{self.annotation}"
        return info

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def add_book(self, book):
        if any(existing_book.title == book.title and existing_book.author.name == book.author.name for existing_book in self.books):
            print(f"Книга '{book.title}' вже є у бібліотеці.")
        else:
            self.books.append(book)

    def list_books(self):
        return [book.get_info() for book in self.books]

    def find_books_by_author(self, author_name):
        books_by_author = [book.get_info() for book in self.books if book.author.name == author_name]
        return books_by_author if books_by_author else f"Книги автора {author_name} не знайдено."

    def find_books_by_year(self, year):
        books_by_year = [book.get_info() for book in self.books if book.year == year]
        return books_by_year if books_by_year else f"Книги року {year} не знайдено."

    def remove_book(self, title, author_name):
        self.books = [book for book in self.books if not (book.title == title and book.author.name == author_name)]
        print(f"Книга '{title}' була видалена з бібліотеки.")

class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def register(self):
        print(f"Читач {self.name} зареєстрований.")

    def borrow_book(self, book, library):
        if book in library.books:
            self.borrowed_books.append(book)
            library.remove_book(book.title, book.author.name)
            print(f"Читач {self.name} орендував книгу '{book.title}'.")
        else:
            print(f"Книга '{book.title}' не доступна для оренди.")

author1 = Author("Джордж Орвелл", 1903)
author2 = Author("Френсіс Скотт Фіцджеральд", 1896)

book1 = Book("1984", author1, 1949, "Дистопічний роман про тоталітарне суспільство.")
book2 = Book("Великий Гетсбі", author2, 1925, "Історія про трагедію американської мрії.")
book3 = Book("Колгосп тварин", author1, 1945)

library = Library("Міська бібліотека")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

reader = Reader("Іван")
reader.register()

reader.borrow_book(book1, library)

print("\nСписок книг у бібліотеці:")
for book_info in library.list_books():
    print(book_info)

print("\nПошук книг Джорджа Орвелла:")
for book_info in library.find_books_by_author("Джордж Орвелл"):
    print(book_info)

print("\nПошук книг 1925 року:")
for book_info in library.find_books_by_year(1925):
    print(book_info)