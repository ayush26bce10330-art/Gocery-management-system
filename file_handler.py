# File Handling Functions

PRODUCT_FILE = "products.txt"
SALES_FILE = "sales.txt"
PURCHASE_FILE = "purchases.txt"


def create_files():
    files = [PRODUCT_FILE, SALES_FILE, PURCHASE_FILE]

    for file_name in files:
        try:
            open(file_name, "a").close()
        except Exception:
            print("Error creating file:", file_name)


def load_products():
    products = []

    try:
        file = open(PRODUCT_FILE, "r")

        for line in file:
            line = line.strip()

            if line != "":
                data = line.split("|")

                if len(data) == 4:
                    product = {
                        "id": data[0],
                        "name": data[1],
                        "price": float(data[2]),
                        "quantity": int(data[3])
                    }

                    products.append(product)

        file.close()

    except Exception:
        print("Error reading products.")

    return products


def save_products(products):
    try:
        file = open(PRODUCT_FILE, "w")

        for product in products:
            line = (
                product["id"] + "|" +
                product["name"] + "|" +
                str(product["price"]) + "|" +
                str(product["quantity"]) + "\n"
            )

            file.write(line)

        file.close()

    except Exception:
        print("Error saving products.")


def add_sale(product_id, product_name, quantity, total):
    try:
        file = open(SALES_FILE, "a")

        line = (
            product_id + "|" +
            product_name + "|" +
            str(quantity) + "|" +
            str(total) + "\n"
        )

        file.write(line)
        file.close()

    except Exception:
        print("Error saving sale.")


def add_purchase(product_id, product_name, quantity, total):
    try:
        file = open(PURCHASE_FILE, "a")

        line = (
            product_id + "|" +
            product_name + "|" +
            str(quantity) + "|" +
            str(total) + "\n"
        )

        file.write(line)
        file.close()

    except Exception:
        print("Error saving purchase.")


def load_sales():
    sales = []

    try:
        file = open(SALES_FILE, "r")

        for line in file:
            line = line.strip()

            if line != "":
                data = line.split("|")

                if len(data) == 4:
                    sale = {
                        "id": data[0],
                        "name": data[1],
                        "quantity": int(data[2]),
                        "total": float(data[3])
                    }

                    sales.append(sale)

        file.close()

    except Exception:
        print("Error reading sales.")

    return sales


def load_purchases():
    purchases = []

    try:
        file = open(PURCHASE_FILE, "r")

        for line in file:
            line = line.strip()

            if line != "":
                data = line.split("|")

                if len(data) == 4:
                    purchase = {
                        "id": data[0],
                        "name": data[1],
                        "quantity": int(data[2]),
                        "total": float(data[3])
                    }

                    purchases.append(purchase)

        file.close()

    except Exception:
        print("Error reading purchases.")

    return purchases