
# kiosk/sales.py

from kiosk.data import stock, sales_log


def record_sale():
    while True:
        goods = input("Enter goods sold: ").strip().title()

        if goods in stock:
            print(f"{goods} is available.")

            quantity = input("How many units were sold? ")

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)

                if quantity <= stock[goods]["quantity"]:
                    price = stock[goods]["price"]
                    total = price * quantity

                    stock[goods]["quantity"] -= quantity

                    sales_log.append((goods, quantity, total))

                    print("Sale recorded successfully.")
                    print(
                        f"Remaining {goods}: "
                        f"{stock[goods]['quantity']} units"
                    )
                    print(f"Total sale: KES {total}")

                else:
                    print("Not enough stock available.")

            else:
                print("Please enter a valid positive quantity.")

        else:
            print(f"{goods} is not in stock.")

        choice = input(
            "Do you want to record another sale? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            break


def view_sales():
    print()
    print("=" * 30)
    print("SALES REPORT")
    print("=" * 30)

    total_revenue = 0

    if not sales_log:
        print("No sales have been recorded.")

    for goods, quantity, total in sales_log:
        print(f"{goods:<15} {quantity} units   KES {total}")
        total_revenue += total

    print("-" * 30)
    print(f"Total Revenue: KES {total_revenue}")