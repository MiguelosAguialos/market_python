class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class CartProduct:
    def __init__(self, product, qty):
        self.code = product.code
        self.name = product.name
        self.price = product.price
        self.qty = qty

    def obj(self):
        return [self.code, self.name, self.price, self.qty]
