from product import product_details

def test_product_details():
    expected = (
        "Product ID:P101\n"
        "Product Name:Laptop\n"
        "Quantity:5\n"
        "Price:45000\n"
    )
    assert product_details("P101","Laptop",5,45000) == expected
