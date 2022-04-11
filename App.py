class Book:

    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getPrice(self):
        if hasattr(self,"_discount"):
           return self.price - (self.price * self._discount)
        else:
           return self.price

    def setDiscount(self, amount):
        self._discount= amount    

book1 = Book("Las aventuras","Charles",50,568)
book2 = Book("Odisea","Juan",41,412)

print(book1.getPrice())
print(book2.getPrice())

book2.setDiscount(0.5)
print(book2.getPrice())
