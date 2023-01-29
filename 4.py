"""
4.define a book class with the following attributes Title,Author(fullname),Price
1.Define a constructor used to initialize the attributes of the method with values entered by the user
2.set the view()method to display information for current book.
write a programme to  testing the bookclass
"""

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def view(self):
        print("title of the book:",self.title)
        print("author of the book:",self.author)
        print("price of the book",self.price)


b=Book("harrypotter","j.krowling",500)
b.view()