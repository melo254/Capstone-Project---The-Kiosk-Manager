
# kiosk/storage.py

from pathlib import Path

from kiosk.data import stock, sales_log


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
STOCK_FILE = DATA_DIR / "stock.txt"
SALES_FILE = DATA_DIR / "sales.txt"


def save_stock():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(STOCK_FILE, "w", encoding="utf-8") as file:
        for goods, details in stock.items():
            file.write(
                f"{goods}|"
                f"{details['price']}|"
                f"{details['quantity']}\n"
            )

    print("Stock saved successfully.")


def load_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as file:
            loaded_stock = {}

            for line in file:
                goods, price, quantity = line.strip().split("|")

                price = int(price)
                quantity = int(quantity)

                if price <= 0 or quantity < 0:
                    raise ValueError("Invalid price or quantity.")

                loaded_stock[goods] = {
                    "price": price,
                    "quantity": quantity
                }

            stock.update(loaded_stock)

        print("Stock loaded successfully.")

    except FileNotFoundError:
        print("No saved stock found. Using default stock.")

    except (ValueError, OSError) as error:
        print(f"Could not load stock: {error}")


def save_sales():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    total_revenue = sum(total for _, _, total in sales_log)

    with open(SALES_FILE, "w", encoding="utf-8") as file:
        file.write("LAZARUS KIOSK SALES REPORT\n")
        file.write("=" * 35 + "\n")

        for goods, quantity, total in sales_log:
            file.write(
                f"{goods} - {quantity} units - KES {total}\n"
            )

        file.write("-" * 35 + "\n")
        file.write(f"Total Revenue: KES {total_revenue}\n")

    print("Sales report saved successfully.")


def read_sales():
    try:
        with open(SALES_FILE, "r", encoding="utf-8") as file:
            print()
            print(file.read())

    except FileNotFoundError:
        print("No saved sales report found.")
