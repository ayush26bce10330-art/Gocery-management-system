# Validation Functions


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_non_negative_integer(message):
    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value

            print("Please enter 0 or a positive number.")

        except ValueError:
            print("Please enter a valid whole number.")