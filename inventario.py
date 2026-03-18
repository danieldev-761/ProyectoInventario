inventory= [] 

to_continue= 1
while to_continue==1:
    
    print(f""" {'-'*20}MENÚ INVENTARIO{'-'*20}
    1. Add Product
    2. Show Inventory
    3. Calculate Statistics
    4. Exit \n""")
    
    
    opt_menu= int(input("Please, enter a menu option (1-4): "))

    
    if 0<opt_menu<5:
        
        if opt_menu == 1:
            
            print(f" {'-'*20}PRODUCT ADDITION MODULE{'-'*20}")
            
        elif opt_menu == 2:
            print()
            
        elif opt_menu == 3: 
            print()

        elif opt_menu == 4:
            print("Exiting the program...")
            to_continue=0
            
    else:
        print("Error: Invalid option, please enter a number between 1 and 4.")