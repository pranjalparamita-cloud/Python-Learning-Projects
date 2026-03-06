while True:
    print("---------Contact Book Management---------")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter contact name: ")
        if name.isalpha()==True:
            while True:
                phone = input("Enter contact phone number: ")
                if phone.isdigit() and len(phone) == 10:
                    with open("contacts.txt", "a") as file:
                        file.write(f"{name},{phone}\n")
                    print("Contact added successfully.")
                else:
                    print("Invalid phone number. Please enter a 10-digit number or press enter to select other option.")
                    if phone == "":
                        break
        else:
            print("Invalid name. Please enter a valid name.")
    elif choice == '2':
        while True: 
            name = input("Enter contact name to edit: ")
            new_phone = input("Enter new phone number: ")
            if new_phone.isdigit() or len(new_phone) == 10:
                with open("contacts.txt", "r") as file:
                    contacts = file.readlines()
                with open("contacts.txt", "w") as file:
                    for contact in contacts:
                        if contact.startswith(name + ","):
                            file.write(f"{name},{new_phone}\n")
                        else:
                            file.write(contact)
                print("Contact edited successfully.")
            else:
                print("Invalid phone number. Please enter a 10-digit number or press enter to select other options.")
                if new_phone == "":
                    break
    elif choice == '3':
        name = input("Enter contact name to search: ")
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        found = False
        for contact in contacts:
            if name in contact:
                print(f"Contact found: {contact.strip()}")
                found = True
        if not found:
            print("Contact not found.")
    elif choice == '4':
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        if contacts:
            print("All Contacts:")
            for contact in contacts:
                print(contact.strip())
        else:
            print("No contacts found.") 
    elif choice == '5':
        name = input("Enter contact name to delete: ")
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        with open("contacts.txt", "w") as file:
            for contact in contacts:
                if not contact.startswith(name + ","):
                    file.write(contact)
        print("Contact deleted successfully.")    
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")