class PrintedMaterial:
    def __init__(self, title, page_count, publication_year):
        self.title = title
        self.page_count = page_count
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Page Count:", self.page_count)
        print("Publication Year:", self.publication_year)


class Book(PrintedMaterial):
    def __init__(self, title, page_count, publication_year, author, genre):
        super().__init__(title, page_count, publication_year)
        self.author = author
        self.genre = genre

    def display_info(self):
        super().display_info()
        print("Author:", self.author)
        print("Genre:", self.genre)


class Magazine(PrintedMaterial):
    def __init__(self, title, page_count, publication_year, issue_number, frequency):
        super().__init__(title, page_count, publication_year)
        self.issue_number = issue_number
        self.frequency = frequency

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)
        print("Frequency:", self.frequency)


class Newspaper(PrintedMaterial):
    def __init__(self, title, page_count, publication_year, issue_date):
        super().__init__(title, page_count, publication_year)
        self.issue_date = issue_date

    def display_info(self):
        super().display_info()
        print("Issue Date:", self.issue_date)


class Library:
    def __init__(self):
        self.collection = []

    def add_material(self, material):
        self.collection.append(material)

    def remove_material(self, title):
        removed = False
        for material in self.collection:
            if material.title == title:
                self.collection.remove(material)
                print(f"{material.title} removed from the library.")
                removed = True
                break

    def display_all_books(self):
        print("All books:")
        for material in self.collection:
            material.display_info()


# Создаем экземпляр библиотеки
test_library = Library()

# Добавляем материалы
test_library.add_material(Book("1984", 328, 1949, "George Orwell", "Düstoopia"))
test_library.add_material(Magazine("Science", 123, 2021, "482", "Kuukiri"))
test_library.add_material(Newspaper("The New York Times", 40, 2022, "2022-05-15"))
x = Newspaper("lkfdkdlkfp", 234324, 203422, "2022-05-15")
test_library.add_material(x)
# Отображается информация обо всех материалах в библиотеке
print("Algne raamatukogu sisu:")
for material in test_library.collection:
    material.display_info()

# Удаление материала
print()
print("Net v nalichii")
test_library.remove_material("Science")
print()

# Показать все книги в библиотеке
print("Ostalis Knigi")
print("\nKõigi raamatukogus olevate raamatute kuvamine:")
test_library.display_all_books()


