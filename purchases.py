# Purchase Management

from file_handler import load_products, save_products, add_purchase
from validation import get_non_empty_input, get_positive_integer


def record_purchase():
    print("\n---------- RECORD PURCHASE ----------")

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
    print("Current quantity:", selected_product["quantity"])

    quantity = get_positive_integer("Enter quantity purchased: ")

    total = selected_product["price"] * quantity

    selected_product["quantity"] += quantity

    save_products(products)

    add_purchase(
        selected_product["id"],
        selected_product["name"],
        quantity,
        total
    )

    print("\nPurchase recorded successfully.")
    print("Total purchase amount:", total)
    print("Updated quantity:", selected_product["quantity"])