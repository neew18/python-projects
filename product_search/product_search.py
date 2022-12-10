def search(products: list, criterion= lambda x: True):
    return [p for p in products if criterion(p)]
def price_under_4_euros(product):
    return product[0].startswith('P')
if __name__ == "__main__":
    products = [('Apple', 4.0, 3), ('Orange', 5.95, 5), ('Banana', 2.95, 10), ('Pineapple', 5.5, 3), ('Pear', 6.95, 2), ('Grapefruit', 3.95, 4)]
    for product in search(products, price_under_4_euros):
        print(product)