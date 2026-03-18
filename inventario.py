inventory= []

def add_product(name, price, quantity):
    
    product= {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)
    print(f"Product '{name}' added successfully to the inventory.") 
    
    
def show_inventory():
    if not inventory:
        print("The inventory is currently empty. No products to show.")
    else:
        for product in inventory:
            print(f"Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")

def calculate_statistics():
        if not inventory:
                print("The inventory is currently empty. No statistics to calculate. \n")
            
        else:
            
            total_value= sum(product['price']*product['quantity'] for product in inventory)
            total_items= sum(product['quantity'] for product in inventory)
                
            print(f"Total Inventory Value: ${total_value:.2f}")
            print(f"Total Number of Items: {total_items}")
            
            
            
to_continue= 1
while to_continue==1:
    
    print(f""" {'-'*20}INVENTORY MENU{'-'*20}
    1. Add Product
    2. Show Inventory
    3. Calculate Statistics
    4. Exit \n""")
    
    
    opt_menu= int(input("Please, enter a menu option (1-4): "))

    
    if 0<opt_menu<5:
        
        if opt_menu == 1:
            
            keep_adding= 1
            while keep_adding==1:
            
                print(f"\n {'-'*20}PRODUCT ADDITION MODULE{'-'*20}")
                
                valid_input= False
                exit_module= False
                while not valid_input:
                    
                    exit_option= input("Return to the main menu? (1: Yes, ENTER TO CONTINUE) ")

                    if exit_option == "1":
                        exit_module= True
                        break
                    
                    product_name= input("Enter the product name: ").capitalize()
                    
                    if product_name.strip() == "" or product_name.isdigit():
                        print("Error: Product name cannot be empty or only digit. Please enter a valid name.")
                        continue

                    price_str = input("Enter the product price: ")
                    
                    try:
                        product_price = float(price_str)
                    except ValueError:
                        print("Error: Please enter a valid number for the product price.")
                        continue
                    
                    if product_price < 0:
                        print("Error: Product price cannot be negative. Please enter a valid price.")
                        continue

                    qty_str = input("Enter the product quantity: ")
                    
                    try:
                        product_quantity = int(qty_str)
                    except ValueError:
                        print("Error: Please enter a valid integer for the product quantity.")
                        continue
                    
                    if product_quantity < 0:
                        print("Error: Product quantity cannot be negative. Please enter a valid quantity.")
                        continue

                    valid_input = True
                    
                if exit_module:
                    print("Returning to main menu...\n")
                    break   

                add_product(product_name, product_price, product_quantity)
                
                keep_adding= int(input("Do you want to continue adding products? (1 for Yes, another number for No): "))
                
                print("You chose continue adding another product \n") if keep_adding==1 else print("Returning to the main menu... \n")
                
            
        elif opt_menu == 2:
            
            print(f"\n {'-'*20}INVENTORY SHOW MODULE{'-'*20}")
            
            show_inventory()
            
        elif opt_menu == 3:
            print(f"\n {'-'*20}STATISTICS MODULE{'-'*20}")
            
            calculate_statistics()
            

        elif opt_menu == 4:
            print("Thank you for using our program! Exiting...")
            to_continue=0
            
    else:
        print("Error: Invalid option, please enter a number between 1 and 4.")