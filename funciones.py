# This module contains the functions for the inventory management program.


# Function to add a product to the inventory, it receives the inventory list and the product details as parameters, 
# creates a dictionary with the product details and appends it to the inventory list, 
# then returns the updated inventory list
def add_product(inventory, name, price, quantity):
    
    
    product= {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)
    
    return inventory

# Function to show the inventory, it receives the inventory list as a parameter, 
# if the inventory is empty, it returns a message indicating that,
def show_inventory(inventory):
    if not inventory:
        return "The inventory is currently empty. No products to show. \n"
    else:
        for product in inventory:
            return f"Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}" 

# Function to calculate the total value of the inventory and the total number of items, 
# it receives the inventory list as a parameter


def calculate_statistics(inventory):
    #if the inventory is empty, it returns 0 for both total value and total items,
        if not inventory:
                return 0, 0
            
        else:
            
            # else, it calculates the total value by summing the product of price and quantity for each
            # product in the inventory, and calculates the total items by summing the quantity of each product,
            total_value= sum(product['price']*product['quantity'] for product in inventory)
            total_items= sum(product['quantity'] for product in inventory)
            
            return total_value, total_items
  
  
# Function to validate user input, it receives a prompt message, a type function to convert the input,
# an optional condition function to check the validity of the input, and an error message to show
# if the input is valid, it returns the converted value,
# otherwise it shows the error message and asks for input again      
def validate_input(prompt, type_func, condition=None, error_msg="Entrada inválida."):
    valid= False
    while not valid:
        user_input = input(prompt)
        try:
            value = type_func(user_input)
            if condition and not condition(value):
                print(error_msg)
                continue
            valid= True
            return value
        except ValueError:
            print(error_msg)