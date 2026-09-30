# Reports Management

from file_handler import load_products, load_sales, load_purchases


def view_reports():
    print("\n========== REPORTS ==========")

    products = load_products()
    sales = load_sales()
    purchases = load_purchases()

    print("\n----- STOCK REPORT -----")

    if len(products) == 0:
        print("No products available.")
    else:
        for product in products:
            print(
                product["id"],
                "-",
                product["name"],
                "- Quantity:",
                product["quantity"]
            )

    total_sales = 0
    sales_quantity = 0

    for sale in sales:
        total_sales += sale["total"]
        sales_quantity += sale["quantity"]

    total_purchases = 0
    purchase_quantity = 0

    for purchase in purchases:
        total_purchases += purchase["total"]
        purchase_quantity += purchase["quantity"]

    print("\n----- SALES REPORT -----")
    print("Total items sold:", sales_quantity)
    print("Total sales amount:", total_sales)

    print("\n----- PURCHASE REPORT -----")
    print("Total items purchased:", purchase_quantity)
    print("Total purchase amount:", total_purchases)

    print("\n============================")