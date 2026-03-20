# Inventory Management Program

This repository contains a Python program called `inventario.py` that allows the user to:

- Register products by entering name, price, and quantity.
- Calculate the total number of registered units.
- Estimate the total cost of the inventory.
- Execute multiple data entries in an optional loop.

The code is intentionally simple and is designed as a fundamentals of programming exercise that includes:

- Reading data from the console
- Use of variables and basic types
- Arithmetic operations
- Output of results on screen

## Usage

To run the program, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Ensure Python 3 is installed (`python3 --version`).
3. Run the script with: `python3 inventario.py`
4. When prompted, enter the product name, price, and quantity.
5. The program will display the total cost and inventory summary.
6. When asked if you want to register another product, enter 1 to continue or any other key to exit.

The rest of the operation is done by following the on-screen instructions.

## Example Execution/Output

```
--------------------INVENTORY MENU--------------------
    1. Add Product
    2. Show Inventory
    3. Calculate Statistics
    4. Exit

Please, enter a menu option (1-4): 1

--------------------PRODUCT ADDITION MODULE--------------------
Return to the main menu? (1: Yes, ENTER TO CONTINUE)
Enter the product name: Bread
Enter the product price: 2.5
Enter the product quantity: 10
Product 'Bread' added successfully to the inventory.
Do you want to continue adding products? (1 for Yes, another number or char for No): 2
Returning to the main menu...

--------------------INVENTORY MENU--------------------
    1. Add Product
    2. Show Inventory
    3. Calculate Statistics
    4. Exit

Please, enter a menu option (1-4): 3

--------------------STATISTICS MODULE--------------------
Total Inventory Value: $25.00
Total Number of Items: 10
```

## Author

- Daniel Echeverría, Coder Riwi

## License

This project is distributed under the GNU General Public License (GPL). See the LICENSE file for more details.
