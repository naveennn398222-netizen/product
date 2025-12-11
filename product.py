def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


if name == "main":
    product_id = "P101"
    name = "Laptop"
    quantity = 5
    price = 45000

    print(product_details(product_id, name, quantity, price))
