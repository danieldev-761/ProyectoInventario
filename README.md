# Advanced inventory with collections and file persistence

This repository contains a Python program that allows users to manage an inventory through a console-based menu system.

The system includes:

* Add, show, search, update, and delete products
* Calculate inventory statistics (total value, total items, etc.)
* Save and load data using CSV files
* Input validation and error handling
* Menu-based interaction with continuous execution

The project is designed as a programming fundamentals exercise, covering:

* Console input/output handling
* Data structures (lists and dictionaries)
* Control flow (loops and conditionals)
* File handling (CSV persistence)
* Basic validation and error handling


## Features

- CRUD operations (Add, Search, Update, Delete)
- CSV persistence (Save/Load)
- Input validation with error handling
- Inventory statistics calculation


## Usage

To run the program:

1. Open a terminal and navigate to the project directory
2. Ensure Python 3 is installed (`python3 --version`)
3. Run the script: `python3 app.py`
4. Use the menu to interact with the system:

   * Add products
   * View inventory
   * Search, update, or delete products
   * View statistics
   * Save or load inventory from CSV files
   * Exit the program

Follow the on-screen instructions for each option.

## Example Execution

```
--------------------INVENTORY MENU--------------------
1. Add Product
2. Show Inventory
3. Search Product
4. Update Product
5. Delete Product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit

Enter an option: 1

--------------------ADD PRODUCT--------------------
Enter product name: Bread
Enter product price: 2.5
Enter product quantity: 10

Product added successfully.

↩ Return to menu
```

## Project Structure

Core files:

- app.py           - Main program
- servicios.py     - Business logic
- archivos.py      - File handling

Other:

- README.md
- LICENSE
- .gitignore

## Author

* Daniel Echeverría, Coder Riwi

## License

This project is distributed under the GNU General Public License (GPL). See the LICENSE file for more details.
