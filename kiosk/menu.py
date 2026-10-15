
# kiosk/menu.py

from kiosk.inventory import (
    view_stock,
    add_or_restock,
    search_goods
)

from kiosk.sales import (
    record_sale,
    view_sales
)

from kiosk.reports import unique_goods_sold

from kiosk.storage import (
    save_stock,
    save_sales,
    read_sales
)


def main_menu():
    while True:
        print()
        print("=" * 30)
        print("LAZARUS KIOSK")
        print("=" * 30)

        print("1. View Stock")
        print("2. Add/Restock Goods")
        print("3. Record Sale")
        print("4. View Sales")
        print("5. Search Goods")
        print("6. Unique Goods Sold")
        print("7. Save Data")
        print("8. Read Saved Sales")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_stock()

        elif choice == "2":
            add_or_restock()

        elif choice == "3":
            record_sale()

        elif choice == "4":
            view_sales()

        elif choice == "5":
            search_goods()

        elif choice == "6":
            unique_goods_sold()

        elif choice == "7":
            save_stock()
            save_sales()

        elif choice == "8":
            read_sales()

        elif choice == "9":
            save_stock()
            save_sales()

            print("Thank you for using Lazarus Kiosk System.")
            break

        else:
            print("Invalid choice. Please try again.")