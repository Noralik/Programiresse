class Product:
  def __init__(self, name: str, price: float, stock: int):
      self.name = name
      self.price = price
      self.stock = stock

class ShoppingCart:
  def __init__(self):
      self.products = []

  def add_product(self, product: Product):
      if product.stock > 0:
          self.products.append(product)
      else:
          print("Product out of stock:", product.name)

  def can_remove_product(self, product: Product) -> bool:
      return product in self.products

  def remove_product(self, product: Product):
      if self.can_remove_product(product):
          self.products.remove(product)
      else:
          print("Cannot delete this product")

  def get_products_with_name(self, name: str) -> list:
      name_lower = name.lower()
      result = [product for product in self.products if product.name.lower() == name_lower]
      return result

  def calculate_total_price(self) -> float:
      total_price = sum(product.price for product in self.products)
      return round(total_price, 2)

  def checkout(self):
      for product in self.products:
          product.stock -= 1
      self.products = []

  def get_products(self):
      return self.products

if __name__ == '__main__':
  # shopping
  product1 = Product("Laptop", 1200.0, 5)
  product2 = Product("Headphones", 80.0, 10)
  product3 = Product("Mouse", 20.0, 3)

  cart = ShoppingCart()

  cart.add_product(product1)
  cart.add_product(product2)
  cart.add_product(product3)

  out_of_stock_product = Product("Out-of-Stock Item", 50.0, 0)
  cart.add_product(out_of_stock_product)

  print("Current Cart:", [product.name for product in cart.get_products()])  # Laptop, Headphones, Mouse

  cart.remove_product(product2)

  print("Current Cart:", [product.name for product in cart.get_products()])  # Laptop, Mouse

  matching_products = cart.get_products_with_name("laptop")
  print("Matching Products:", [product.name for product in matching_products])  # Laptop

  total_price = cart.calculate_total_price()
  print("Total Price:", total_price)  # 1220.0

  cart.checkout()

  print("Current Cart:", [product.name for product in cart.get_products()])  # should be empty
