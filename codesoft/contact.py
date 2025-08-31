contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("No matching contact found.\n")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave field empty to keep old value.")
            name = input(f"Enter new name ({contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"Enter new phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"Enter new email ({contacts[index]['email']}): ") or contacts[index]['email']
            address = input(f"Enter new address ({contacts[index]['address']}): ") or contacts[index]['address']

            contacts[index].update({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact updated successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Contact '{removed['name']}' deleted successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-6.\n")

if __name__ == "__main__":
    main()
