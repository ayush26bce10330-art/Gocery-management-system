# Sales Management

from file_handler import load_products, save_products, add_sale
from validation import get_non_empty_input, get_positive_integer


def record_sale():
    print("\n---------- RECORD SALE ----------")

    products = load_products()

    if len(products) == 0:
        print("No products available.")
        return

    product_id = get_non_empty_input("Enter product ID: ")

    selected_product = None

    for product in products:
        if product["id"] == product_id:
            selected_product = product
            break

    if selected_product is None:
        print("Product not found.")
        return

    print("Product:", selected_product["name"])
    print("Price:", selected_product["price"])
    print("Available quantity:", selected_product["quantity"])

    quantity = get_positive_integer("Enter quantity to sell: ")

    if quantity > selected_product["quantity"]:
        print("Not enough stock available.")
        return

    total = selected_product["price"] * quantity

    selected_product["quantity"] -= quantity

    save_products(products)

    add_sale(
        selected_product["id"],
        selected_product["name"],
        quantity,
        total
    )

    print("\nSale recorded successfully.")
    print("Total amount:", total)
    print("Remaining quantity:", selected_product["quantity"])