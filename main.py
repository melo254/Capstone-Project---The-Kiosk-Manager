
# main.py

from kiosk.setup import setup_kiosk
from kiosk.storage import load_stock
from kiosk.menu import main_menu


def main():
    setup_kiosk()
    load_stock()
    main_menu()


if __name__ == "__main__":
    main()
