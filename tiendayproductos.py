class Product:
    def __init__(self, item_name, price, weight, brand):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "para la venta"
    
    def sell(self):
        self.status = "vendido"
        return self

    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self
    
    def return_item(self, reason_for_return):
        if reason_for_return == "defectuoso":
            self.status = "defectuoso"
            self.price = 0
        if reason_for_return == "como nuevo":
            self.status = "para la venta"
        if reason_for_return == "abierto":
            self.status = "usado"
            self.price = self.price - (self.price * 0.20)
        return self

    def display_info(self):
        print("Item Name: " + str(self.item_name))
        print("Price: " + str(self.price))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Status: " + str(self.status))
        return self

product_one = Product("Vasos", 3.99, 0.16, "El románttico Viajero")
product_one.display_info() .return_item("abierto") .display_info()

product_two = Product("Tenedores", 7.99, 0.75, "Wonderful Kitchen")
product_two.display_info() .return_item("como nuevo") .display_info()

product_three = Product("Cafetera", 33.99, 4.25, "Melitta")
product_three.display_info() .return_item("defectuoso") .display_info()

product_four = Product("Plumones", 4.99, 0.25, "Faber Castell")
product_four.display_info() .add_tax(0.12) .display_info()

product_five = Product("Plumones", 4.99, 0.25, "Faber Castell")
product_five.display_info() .sell() .display_info()