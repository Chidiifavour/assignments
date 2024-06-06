library = {
"978-0132350884": {"title": "Clean Code", "author": "Robert C. Martin"},
"978-0201485677": {"title": "Refactoring", "author": "Martin Fowler"},
}

users = {
"Alice": [],
"Bob": [],
}

class Library:

    def __init__(self, library, users) -> None:
        self.library = library
        self.users = users

    def add_new_book(self,ISBN,title,author):
        book = {
            "title": title,
            "author": author
        }
        self.library[ISBN] = book
        return "New book added"
    
    def remove_book(self,ISBN):
        name = self.library[ISBN]["title"]
        del self.library[ISBN]
        return f"\"{name}\" has been removed from the library!"
    
    def register_user(self,name):
        self.users[name] = []
        return f"New user registered"
    
    def borrow_book(self,name,ISBN):
        self.users[name].append(ISBN)
        return f"{name} borrowed book \"{ISBN}\""
    
    def return_book(self,name,ISBN):
        self.users[name].remove(ISBN)
        return f"{name} retured book {ISBN}"
    
    def borrowed_books(self,name):
        return self.users[name]

maxiLibrary = Library(library,users)

print(maxiLibrary.add_new_book("978-6677787","Bullied to Love","Favour"))
print(maxiLibrary.register_user("Favour"))
print(maxiLibrary.borrow_book("Bob","978-0201485677"))
print(maxiLibrary.return_book("Bob","978-0201485677"))
print(maxiLibrary.borrowed_books("Bob"))
print(maxiLibrary.remove_book("978-0132350884"))
print(maxiLibrary.library)