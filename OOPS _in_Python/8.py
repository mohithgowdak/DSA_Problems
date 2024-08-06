class Mobile:
    def __init__(self, price=None, brand=None, ios_version=None):
        self.price = price
        self.brand = brand
        self.ios_version = ios_version

# Creating instances of Mobile class with attributes initialized
mob1 = Mobile(20000, "Apple", 11)
mob2 = Mobile(3000, "Samsung", 10)

# Accessing and printing attributes of mob1 and mob2
print(mob1.price, mob1.brand, mob1.ios_version)
print(mob2.price, mob2.brand, mob2.ios_version)