class Book:
    def __init__(self,name , price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Book {self.name} has ${self.price} price"

    def __repr__(self):
        return f"Book('{self.name}' , {self.price})"


b1 = Book('Java','500')

print(b1)       # calls __str__ if not available then execute __repr__
print([b1])     # calls __repr__