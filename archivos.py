import csv

DEFAULTPATH= 'inventory.csv'

def save_csv(inventory, path= DEFAULTPATH, include_header= True):
    #Validate that inventory is not empty
    if not inventory:
        print("Error: inventory is empty, cannot save.")
        return

    try:
        path = input("Enter file path (PRESS ENTER to use default: inventory.csv): ").strip()
        path = path if path else DEFAULTPATH
        
        file_type = path.split('.')
        
        if 'csv' in file_type:
            
            #Open file in write mode
            with open(path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["name", "price", "quantity"]
                )

                # Write header if required
                if include_header:
                    writer.writeheader()

                # Write data
                writer.writerows(inventory)

            # Success message
            print(f"Inventory saved to: {path}")
        else:
            print("Changes not saved. Only .csv files are allowed. ")

    except PermissionError:
        print("Error: you do not have permission to write to this file.")
    except IOError:
        print("Error: an issue occurred while saving the file.")
        



def load_csv(current_inventory, path= DEFAULTPATH):
    """
    Loads inventory data from a CSV file and returns the updated inventory.
    Applies validation rules and allows user to choose between overwrite or merge.
    """

    loaded_inventory = []
    invalid_rows = 0
    products_loaded= 0

    try:
        
        path = input("Enter file path (PRESS ENTER to use default: inventory.csv): ").strip()
        path = path if path else DEFAULTPATH
        
        file_type = path.split('.')
        
        if 'csv' in file_type:
        
            with open(path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                # Validate header
                try:
                    header = next(reader)
                except StopIteration:
                    print("Error: the file is empty.")
                    return current_inventory

                expected_header = ["name", "price", "quantity"]
                if header != expected_header:
                    print("Error: invalid header. Expected: name,price,quantity")
                    return current_inventory

                # Process rows
                for row in reader:
                    if len(row) != 3:
                        invalid_rows += 1
                        continue

                    name, price, quantity = row

                    try:
                        price = float(price)
                        quantity = int(quantity)

                        if (name.strip()== "") or (price <= 0) or (quantity < 0):
                            raise ValueError

                        loaded_inventory.append({
                            "name": name,
                            "price": price,
                            "quantity": quantity
                        })

                    except ValueError:
                        invalid_rows += 1

            # Ask user action
            option = input("Overwrite current inventory? (Y/N): ").strip().upper()

            if option == "Y":
                final_inventory = loaded_inventory
                action = "overwrite"
                products_loaded= len(loaded_inventory)

            else:
                # Merge policy:
                # - If product exists: sum quantity
                # - If price differs: update to new price
                # - If quantity and price are the same: omit duplicate
                final_inventory = {item["name"]: item for item in current_inventory}
                
                if current_inventory == loaded_inventory:
                    merge_option= input("The loaded inventory is identical to the current inventory. Do you want to proceed with the merge? (Y/N or any other char): ").strip().upper()

                    if merge_option != "Y":
                        print("Merge cancelled. Returning current inventory. \n")
                        return current_inventory
            
                for item in loaded_inventory:
                    name = item["name"]

                    if name in final_inventory:
                        
                        if item["quantity"] == 0:
                            continue
                        
                        final_inventory[name]["quantity"] += item["quantity"]
                        products_loaded+= 1

                        if final_inventory[name]["price"] != item["price"]:
                            final_inventory[name]["price"] = item["price"]
                            products_loaded+= 1
                    else:
                        final_inventory[name] = item
                        products_loaded+= 1

                final_inventory = list(final_inventory.values())
                action = "merge"

            #Summary
            print("\nLoad summary:")
            print(f"Products loaded: {products_loaded}")
            print(f"Invalid rows skipped: {invalid_rows}")
            print(f"Action performed: {action}")

            return final_inventory
        
        else:
            print("Invalid upload. Only .csv files are allowed. ")

    except FileNotFoundError:
        print("Error: file not found.")
    except UnicodeDecodeError:
        print("Error: file encoding is not supported.")
    except ValueError:
        print("Error: invalid data format in file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return current_inventory

