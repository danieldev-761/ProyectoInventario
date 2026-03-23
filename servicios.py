# This module contains the functions for the inventory management program.

# Function to add a product to the inventory
def add_product(inventory, name, price, quantity):
    """
    Adds a new product to the inventory.

    Parameters:
    inventory (list): The list of products in the inventory.
    name (str): The name of the product.
    price (float): The price of the product.
    quantity (int): The quantity of the product.

    Returns:
    list: The updated inventory list with the new product added.
    """
    # Create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    # Append to inventory
    inventory.append(product)
    return inventory

# Function to display the inventory
def show_inventory(inventory):
    """
    Displays the inventory.

    Parameters:
    inventory (list): The list of products in the inventory.

    Returns:
    str: A string representation of the inventory.
    """
    if not inventory:
        return "The inventory is currently empty. No products to show.\n"
    result = ""
    for product in inventory:
        result += f"Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}\n"
    return result

# Function to search for a product by name
def search_product(inventory, name):
    """
    Searches for a product by name in the inventory.

    Parameters:
    inventory (list): The list of products in the inventory.
    name (str): The name of the product to search for.

    Returns:
    dict or None: The product dictionary if found, None otherwise.
    """
    for product in inventory:
        if product['name'] == name:
            return product
    return None

# Function to update a product's price and/or quantity
def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Updates the price and/or quantity of a product in the inventory.

    Parameters:
    inventory (list): The list of products in the inventory.
    name (str): The name of the product to update.
    new_price (float, optional): The new price for the product.
    new_quantity (int, optional): The new quantity for the product.

    Returns:
    bool: True if the product was updated, False if not found.
    """
    for product in inventory:
        if product['name'] == name:
            if new_price is not None:
                product['price'] = new_price
            if new_quantity is not None:
                product['quantity'] = new_quantity
            return True
    return False

# Function to delete a product by name
def delete_product(inventory, name):
    """
    Removes a product from the inventory by name.

    Parameters:
    inventory (list): The list of products in the inventory.
    name (str): The name of the product to remove.

    Returns:
    bool: True if the product was removed, False if not found.
    """
    for i, product in enumerate(inventory):
        if product['name'] == name:
            del inventory[i]
            return True
    return False

# Function to calculate inventory statistics
def calculate_statistics(inventory):
    """
    Calculates statistics for the inventory.

    Parameters:
    inventory (list): The list of products in the inventory.

    Returns:
    tuple: A tuple containing (total_value, total_items).
    """
    if not inventory:
        return 0, 0
    total_value = sum(product['price'] * product['quantity'] for product in inventory)
    total_items = sum(product['quantity'] for product in inventory)
    return total_value, total_items

# Function to validate user input
def validate_input(prompt, type_func, condition=None, error_msg="Invalid Input."):
    """
    Validates user input.

    Parameters:
    prompt (str): The prompt message to display.
    type_func (function): The function to convert the input (e.g., int, float).
    condition (function, optional): A condition function to check validity.
    error_msg (str): The error message to display on invalid input.

    Returns:
    The converted and validated value.
    """
    valid = False
    while not valid:
        user_input = input(prompt)
        try:
            value = type_func(user_input)
            if condition and not condition(value):
                print(error_msg)
                continue
            valid = True
            return value
        except ValueError:
            print(error_msg)