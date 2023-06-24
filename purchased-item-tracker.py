# Initialize an empty list to store purchased items
purchased_items = []

# Function to add an item to the purchased_items list
def add_item():
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the quantity purchased: "))
    purchased_items.append({'Name': name, 'Price': price, 'Quantity': quantity})
    print("Item added successfully!")
  
# Function to display the summary of all purchased items
def display_summary():
    print("\n--- Purchased Items Summary ---")
    total_cost = 0
    for item in purchased_items:
        print("Name:", item['Name'])
        print("Price:", item['Price'])
        print("Quantity:", item['Quantity'])
        print("------------------------")
        total_cost += item['Price'] * item['Quantity']
    print("Total Cost: ", total_cost)
    print("------------------------")
  
# Main program loop
while True:
    print("1. Add an item")
    print("2. Display purchased items summary")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        add_item()
    elif choice == '2':
        display_summary()
    elif choice == '3':
        print("Thank you for using the travel item tracker. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.\n")
