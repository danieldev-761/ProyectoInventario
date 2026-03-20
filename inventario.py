#import functions from funciones.py
from funciones import *

#initialize inventory list 
inventory= []            
            
            
#main menu loop: while to continue is 1, the menu will keep showing, if the user chooses to exit, it will change to 0 and the loop will end           
to_continue= 1
while to_continue==1:
    
    print(f""" {'-'*20}INVENTORY MENU{'-'*20}
    1. Add Product
    2. Show Inventory
    3. Calculate Statistics
    4. Exit \n""")
    
    
    opt_menu= (input("Please, enter a menu option (1-4): "))

    #validate that the input is not empty and is a number between 1 and 4, if not, show an error message and ask for input again
    if opt_menu.strip() == "":
        print("Error: Input cannot be empty. Please enter a valid option.")
        continue
    
    if 0< int(opt_menu)<5:
        
        #OPTION 1: Add Product
        if opt_menu == "1":
            
            #second loop to keep adding products until the user chooses to stop, if the user chooses to stop, it will return to the main menu
            keep_adding= 1
            while keep_adding==1:
            
                print(f"\n {'-'*20}PRODUCT ADDITION MODULE{'-'*20} \n")
                
                #third loop to validate the input for product name, price and quantity, if the user chooses to exit, it will return to the main menu, 
                # if the input is invalid, it will show an error message and ask for input again
                valid_input= False
                exit_module= False
                while not valid_input:
                    
                    exit_option= input("Return to the main menu? (1: Yes, ENTER TO CONTINUE) ")
                    
                    #validate that the input is either 1 or empty, if not, show an error message and ask for input again
                    if exit_option == "1":
                        exit_module= True
                        break
                    
                    
                    
                    #validate product name: not empty, not only digits, if invalid show error message and ask for input again
                    product_name = validate_input("Enter the product name: ", str, lambda x: x.strip() != "" and not x.isdigit(), "Error: Product name cannot be empty or only digit. Please enter a valid name.").capitalize()
                    
                    #validate product price: not empty, must be a number, must be greater than or equal to 0, if invalid show error message and ask for input again
                    product_price = validate_input("Enter the product price: ", float, lambda x: x >= 0, "Error: Product price cannot be negative or empty. Please enter a valid price.")
                    
                    #validate product quantity: not empty, must be a number, must be greater than or equal to 0, if invalid show error message and ask for input again
                    product_quantity = validate_input("Enter the product quantity: ", int, lambda x: x >= 0, "Error: Product quantity cannot be negative or empty. Please enter a valid quantity.")
                    
                    
                #if the user chose to exit the module, break the loop and return to the main menu
                if exit_module:
                    print("\n Returning to main menu...\n")
                    break   
                
                #add the product to the inventory if is all valid and show a success message
                add_product(inventory, product_name, product_price, product_quantity)
                
                print(f"Product '{product_name}' added successfully to the inventory. \n") 
                
                # ask the user if they want to keep adding products, if they choose to continue
                keep_adding= (input("Do you want to continue adding products? (1 for Yes, another number or char for No): "))
                keep_adding= int(keep_adding) if keep_adding.isdigit() else 0
                
                print("You chose continue adding another product \n") if keep_adding==1 else print("Returning to the main menu... \n")
                
        #OPTION 2: Show Inventory
        elif opt_menu == "2":
            
            print(f"\n {'-'*20}INVENTORY SHOW MODULE{'-'*20} \n")
            
            #call the function to show the inventory and show a message personlized depending on the result
            print(show_inventory(inventory))
        
        #OPTION 3: Calculate Statistics
        elif opt_menu == "3":
            print(f"\n {'-'*20}STATISTICS MODULE{'-'*20} \n")
            
            #call the function and store the results in variables
            total_value, total_items = calculate_statistics(inventory)
            
            #if the inventory is empty, show this message
            if total_value == 0 and total_items == 0:
                print("No statistics to display due to empty inventory. \n")
                
            #else, show the total value and total items in the inventory with a message
            else:
                print(f"Total Inventory Value: ${total_value:.2f}")
                print(f"Total Number of Items: {total_items}")

        #OPTION 4: Exit
        elif opt_menu == "4":
            print("Thank you for using our program! Exiting...")
            to_continue=0
            
    #if the user input is not a number between 1 and 4, show an error message and ask for input again      
    else:
        print("Error: Invalid option, please enter a number between 1 and 4.")
        
        
'''
Objetivo de la semana 2: Crear un programa de inventario que permita al usuario agregar productos, 
mostrar el inventario y calcular estadísticas básicas como el valor total del inventario 
y la cantidad total de productos. El programa debe ser fácil de usar y manejar entradas inválidas de manera adecuada, 
además de incluir código modularizado con funciones.


'''