# you are task with creating a basic libryry management system using inheritance.
# Implement the following classes 
#   Base class - LibraryItem ( attr - title,author,publication_year)(func - display_info[print the details of the item])
#   Derive class - Book It inherite from libriryItem. (additional attri  - genri, isbn ) override display_info
#   Derive class  - Magazine It also inherite from LibraryItem (additional attr - issue number or date of the magazine ) override display info

# Task
# Create instance of each class ( Book, Magazine) withe values to their attributes
# Call the display_info func for each instance to test inheritance and method overidden

class LibrabryItem:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def display_inf(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Publication Year : {self.publication_year}")

class Book(LibrabryItem):
    def __init__(self, title, author, publication_year,genri,isbn):
        super().__init__(title, author, publication_year)
        self.genri = genri
        self.isbn = isbn
    
    def display_inf(self):
        super().display_inf()
        print(f"Genri : {self.genri}")
        print(f"ISBN : {self.isbn}")

class Magazine(LibrabryItem):
    def __init__(self, title, author, publication_year,issu_number_or_date):
        super().__init__(title, author, publication_year)
        self.issu_number_or_date = issu_number_or_date
    
    def display_inf(self): 
        super().display_inf()
        print(f"Issu Number Or Date : {self.issu_number_or_date}")


book_1 = Book("ABC","XYZ",2024,"Novel",923723)
magazine_1 = Magazine("PQR","XYZ",2022,"Feb25")

print("\nBOOK INFO\n")
book_1.display_inf()

print("\nMAGAZINE INFO\n")
magazine_1.display_inf()
         