def display_menu():

    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    print("-------------------------")


def add_contact(contact_book):

    print("Enter Name to Add:")
    name = input().strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in contact_book:
        print("Contact already exists!")
        return

    print("Enter Phone:")
    phone = input().strip()
    print("Enter Email:")
    email = input().strip()
    print("Enter Address:")
    address = input().strip()

    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully! ✅")


def view_contact(contact_book):
    """Displays details for a specific contact."""
    print("Enter Name to View:")
    name = input().strip()
    if name in contact_book:
        contact = contact_book[name]
        print(f"\n--- Contact Details: {name} ---")
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("---------------------------------")
    else:
        print("Contact not found! ❌")


def edit_contact(contact_book):
    """Updates an existing contact’s information."""
    print("Enter Name to Edit:")
    name = input().strip()
    if name in contact_book:
        print(f"Editing contact: {name}")

        # Display current info and prompt for new info
        current_phone = contact_book[name]['phone']
        print(f"Current Phone: {current_phone}. Enter new Phone (or leave blank to keep current):")
        phone = input().strip() or current_phone

        current_email = contact_book[name]['email']
        print(f"Current Email: {current_email}. Enter new Email (or leave blank to keep current):")
        email = input().strip() or current_email

        current_address = contact_book[name]['address']
        print(f"Current Address: {current_address}. Enter new Address (or leave blank to keep current):")
        address = input().strip() or current_address

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully! 📝")
    else:
        print("Contact not found! ❌")


def delete_contact(contact_book):
    """Removes a contact from the Contact Book."""
    print("Enter the name of the contact to delete:")
    name_to_delete = input().strip()

    if name_to_delete in contact_book:
        del contact_book[name_to_delete]
        print("Contact deleted successfully! 🗑️")
    else:
        print("Contact not found! ❌")


def list_all_contacts(contact_book):
    """Displays all the contacts in the Contact Book."""
    if not contact_book:
        print("No contacts available.")
        return

    print("\n--- Listing All Contacts ---")
    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("----------------------------")  # Separator for readability

## Main Program Execution

# Initialize the contact book dictionary
contact_book = {}

# Main loop for the contact book application
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        add_contact(contact_book)
    elif choice == '2':
        view_contact(contact_book)
    elif choice == '3':
        edit_contact(contact_book)
    elif choice == '4':
        delete_contact(contact_book)
    elif choice == '5':
        list_all_contacts(contact_book)
    elif choice == '6':
        print("Exiting Contact Book. Goodbye! 👋")
        break  # Exit the while loop
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")