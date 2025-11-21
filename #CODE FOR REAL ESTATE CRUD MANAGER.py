  #CODE FOR REAL ESTATE CRUD MANAGER
#list to store properties
properties = []

def add_property():
    property_id=input("Enter property ID: ")
    address = input("Enter property address: ")
    price = input("Enter property price: ")
    owner = input("Enter owner's name: ")
    property_type = input("Enter property type (e.g., apartment, house): ")
    property_data = {
        "address": address,
        "price": price,
        "type": property_type,
        "owner": owner,
        "id": property_id,

    }
    properties.append(property_data)
    print("Property added successfully!\n")
def view_properties():
    if not properties:
        print("No properties available.\n")
        return
    for prop in properties:
        print(f"ID: {prop['id']}, Address: {prop['address']}, Price: {prop['price']}, Type: {prop['type']}, Owner: {prop['owner']}")
    print()
def update_property():
    property_id = input("Enter the property ID to update: ")
    for prop in properties:
        if prop['ID'] == property_id:
            print("Leave field blank to keep current value.")
            address = input(f"Enter new address (current: {prop['address']}): ") or prop['address']
            price = input(f"Enter new price (current: {prop['price']}): ") or prop['price']
            owner = input(f"Enter new owner's name (current: {prop['owner']}): ") or prop['owner']
            property_type = input(f"Enter new property type (current: {prop['type']}): ") or prop['type']
            prop.update({
                "address": address,
                "price": price,
                "type": property_type,
                "owner": owner
            })
            print("Property updated successfully!\n")
            return
    print("Property ID not found.\n")
def delete_property():
    property_id = input("Enter the property ID to delete: ")
    for i, prop in enumerate(properties):
        if prop['ID'] == property_id:
            del properties[i]
            print("Property deleted successfully!\n")
            return
    print("Property ID not found.\n")
def main():
    while True:
        print("Real Estate CRUD Manager")
        print("1. Add Property")
        print("2. View Properties")
        print("3. Update Property")
        print("4. Delete Property")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_property()
        elif choice == '2':
            view_properties()
        elif choice == '3':
            update_property()
        elif choice == '4':
            delete_property()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
