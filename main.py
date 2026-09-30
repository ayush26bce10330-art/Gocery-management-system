# Grocery Management System

from file_handler import create_files
from products import (
    add_product,
    view_products,
    search_product,
    update_product,
    delete_product
)
from sales import record_sale
from purchases import record_purchase
from reports import view_reports


def main_menu():
    print("\n====================================")
    print("       GROCERY MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Record Sale")
    print("7. Record Purchase")
    print("8. View Reports")
    print("9. Exit")
    print("====================================")


create_files()

while True:

    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        record_sale()

    elif choice == "7":
        record_purchase()

    elif choice == "8":
        view_reports()

    elif choice == "9":
        print("\nThank you for using Grocery Management System.")
        break

    else:
        print("\nInvalid choice. Please try again.")