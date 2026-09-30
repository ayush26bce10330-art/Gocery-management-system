# Product Management

from file_handler import load_products, save_products
from validation import (
    get_non_empty_input,
    get_positive_number,
    get_non_negative_integer
)


def add_product():
    print("\n---------- ADD PRODUCT ----------")

    products = load_products()

    product_id = get_non_empty_input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("A product with this ID already exists.")
            return

    product_name = get_non_empty_input("Enter product name: ")
    price = get_positive_number("Enter product price: ")
    quantity = get_non_negative_integer("Enter product quantity: ")

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    save_products(products)

    print("Product added successfully.")


def view_products():
    print("\n---------- ALL PRODUCTS ----------")

    products = load_products()

    if len(products) == 0:
        print("No products available.")
        return

    print("-" * 65)
    print(f"{'ID':<10}{'Name':<20}{'Price':<15}{'Quantity':<10}")
    print("-" * 65)

    for product in products:
        print(
            f"{product['id']:<10}"
            f"{product['name']:<20}"
            f"{product['price']:<15.2f}"
            f"{product['quantity']:<10}"
        )

    print("-" * 65)


def search_product():
    print("\n---------- SEARCH PRODUCT ----------")

    products = load_products()

    search = get_non_empty_input("Enter product ID or name: ").lower()

    found = False

    for product in products:
        if (
            product["id"].lower() == search
            or product["name"].lower() == search
        ):
            print("\nProduct Found")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            found = True

    if not found:
        print("Product not found.")


def update_product():
    print("\n---------- UPDATE PRODUCT ----------")

    products = load_products()

    product_id = get_non_empty_input("Enter product ID to update: ")

    found = False

    for product in products:
        if product["id"] == product_id:
            found = True

            print("Current product details:")
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])

            new_name = get_non_empty_input("Enter new product name: ")
            new_price = get_positive_number("Enter new price: ")
            new_quantity = get_non_negative_integer(
                "Enter new quantity: "
            )

            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity

            save_products(products)

            print("Product updated successfully.")
            break

    if not found:
        print("Product not found.")


def delete_product():
    print("\n---------- DELETE PRODUCT ----------")

    products = load_products()

    product_id = get_non_empty_input("Enter product ID to delete: ")

    found = False

    for product in products:
        if product["id"] == product_id:
            products.remove(product)

            save_products(products)

            print("Product deleted successfully.")
            found = True
            break

    if not found:
        print("Product not found.")