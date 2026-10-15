
# kiosk/setup.py

def setup_kiosk():
    print("=" * 30)

    kiosk = input("Enter kiosk name: ").strip().title()
    manager = input("Enter manager's name: ").strip().title()

    print(f"Welcome to {kiosk} Kiosk")
    print(f"Manager: {manager}")

    print("=" * 30)
