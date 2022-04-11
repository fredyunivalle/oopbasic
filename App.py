class Book:

    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getPrice(self):
        return self.price

book1 = Book("Las aventuras","Charles",50,568)
book2 = Book("Odisea","Juan",41,412)

print(book1.getPrice())
print(book2.getPrice())
