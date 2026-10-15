# Capstone-Project - The Kiosk Management System
# Lazarus Kiosk Management System

A Python-based, command-line kiosk management application designed to simplify stock management, sales recording, revenue tracking, and data storage for small retail businesses.

## Project Overview

The **Lazarus Kiosk Management System** helps kiosk owners and attendants manage daily business operations through a simple, interactive terminal menu.

The application allows users to maintain product inventory, record customer purchases, monitor available stock, generate sales reports, and save business data locally using Python file handling.

The project demonstrates fundamental Python programming concepts and modular software development by separating application functionality into individual Python files.

## Features

### 1. Kiosk Setup
- Enter the kiosk name.
- Enter the manager's name.
- Display a personalized welcome message.

### 2. Inventory Management
- View all available products, their selling prices, and stock quantities.
- Add new products to the inventory.
- Restock existing products.
- Search for products by name.
- Automatically update inventory after successful sales.

### 3. Sales Management
- Record sales transactions.
- Validate product availability and requested quantities.
- Calculate the total selling price of each transaction.
- Deduct sold quantities from available stock.
- Maintain a sales log during the current program session.

### 4. Sales Reporting
- Display individual sales transactions.
- Calculate total revenue from recorded transactions.
- Identify unique products sold using Python sets.
- Save sales reports to a text file.
- Read previously saved sales reports.

### 5. Data Persistence
- Save product names, prices, and quantities to a local text file.
- Load previously saved inventory when the application starts.
- Store sales reports locally for future reference.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Dictionaries | Store product prices and quantities |
| Lists | Maintain sales transactions |
| Sets | Identify unique products sold |
| Functions | Organize reusable operations |
| Conditional statements | Validate input and control application logic |
| Loops | Handle repeated operations and menu navigation |
| File handling | Save and retrieve inventory and sales reports |
| Modules and packages | Separate application functionality into multiple files |
| `pathlib` | Manage file paths |

## Project Structure

```text
lazarus_kiosk/
|
|-- main.py
|-- README.md
|
|-- kiosk/
|   |-- __init__.py
|   |-- setup.py
|   |-- data.py
|   |-- inventory.py
|   |-- sales.py
|   |-- reports.py
|   |-- storage.py
|   |-- menu.py
|
|-- data/
    |-- stock.txt
    |-- sales.txt
```

**Note:** The `data/` directory and its text files are created as needed by the storage functions. They may not exist before the first save operation.

### Module Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Entry point that initializes and runs the application |
| `setup.py` | Collects the kiosk name and manager's name |
| `data.py` | Holds the shared inventory dictionary and sales log |
| `inventory.py` | Handles viewing, adding, restocking, and searching products |
| `sales.py` | Records transactions and displays sales summaries |
| `reports.py` | Identifies unique products sold |
| `storage.py` | Saves and loads inventory and sales reports |
| `menu.py` | Displays
