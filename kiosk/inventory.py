
# kiosk/inventory.py

from kiosk.data import stock


def view_stock():
    print()
    print("=" * 30)
    print("KIOSK STOCK")
    print("=" * 30)

    for goods, details in stock.items():
        price = details["price"]
        quantity = details["quantity"]

        print(f"{goods:<15} KES {price:<10} {quantity} units")


def add_or_restock():
    goods = input("Enter goods name: ").strip().title()

    if not goods:
        print("Goods name cannot be empty.")
        return

    if goods in stock:
        print(f"{goods} already exists!")

        choice = input(
            "Do you want to add more units? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            quantity = input("How many units do you want to add? ")

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                stock[goods]["quantity"] += quantity

                print(f"Added {quantity} units of {goods}.")
                print(f"New quantity: {stock[goods]['quantity']}")

            else:
                print("Please enter a valid positive quantity.")

    else:
        print(f"{goods} is a new product.")

        price = input("Enter price per unit: ")
        quantity = input("Enter initial quantity: ")

        if (
            price.isdigit()
            and quantity.isdigit()
            and int(price) > 0
            and int(quantity) > 0
        ):
            stock[goods] = {
                "price": int(price),
                "quantity": int(quantity)
            }

            print(f"{goods} successfully added.")

        else:
            print("Please enter valid positive numbers.")


def search_goods():
    goods = input("Enter goods name to search: ").strip().title()

    if goods in stock:
        print(f"{goods} is available.")
        print(f"Price: KES {stock[goods]['price']}")
        print(f"Available units: {stock[goods]['quantity']}")

    else:
        print(f"{goods} is not in stock.")
