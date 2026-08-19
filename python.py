# build a contact list - DONE
# make a way to add new contacts to the list - DONE
# make a way to remove contacts in the list - DONE
# make a way to update contacts in the list
# make a way to view all of the contacts in a list - DONE
# make a way to view specific contacts in a list - DONE

# This is the contacts dictionary containing all of the different contacts and their metadata (phone, email, and age)
contacts = {
    "JV": {"phone": "123-456-7890", "email": "jvtestemail@gmail.com", "age": 23},
    "Jem": {"phone": "234-567-8901", "email": "jemtestemail@gmail.com", "age": 24},
    "Snow": {"phone": "345-678-9012", "email": "snowtestemail@gmail.com", "age": 1},
    "Dalmy": {"phone": "456-789-0123", "email": "dalmytestemail@gmail.com", "age": 7}
}


def add_contact(contacts: dict):
    """
    This method handles the addition of a new contact in the contact book dictionary

    Args:
        1. contacts - variable that contains the contact book dictionary
    Returns:
        Nothing - only performs the addition operation into the contact book dictionary
    """
    print("You have chosen to add a new contact.")

    # This section contains the initialized while loop variables for user input & validation
    adding_contact = True
    contact_name_input = ""
    contact_phone_number_input = ""
    contact_email_address_input = ""
    contact_age_input = 0

    # This section handles the prompting of the user to input new contact name & validation
    while(adding_contact):
        user_input = input("What is the name of the contact you'd like to add? ")

        # This section handles the instance that the contact name already exists in the contact book dictionary
        if user_input in contacts.keys():
            user_input = input("This name already exists in the contact book - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of adding a contact")
                adding_contact = False
                break
            else:
                continue

        print(f"Adding {user_input} as new contact name to the contact book.")
        contact_name_input = user_input
        break


    # This section handles the prompt of the user to input new phone number & validation
    while(adding_contact):
        user_input = input("What is the phone number of the contact you'd like to add? ")

        # This section handles the instance that the phone number already exists in the contact book dictionary
        for contact in contacts.values():
            if contact["phone"] == user_input:
                user_input = input("This phone number already exists in the contact book - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

                if user_input == "Y":
                    print("Exiting out of adding a contact")
                    adding_contact = False
                    break
                else:
                    user_input = False
                    continue

        if not user_input: continue

        print(f"Adding {user_input} as the new phone number to the contact {contact_name_input}")
        contact_phone_number_input = user_input
        break

    # This section handles the prompt of the user to input new email address & validation
    while(adding_contact):
        user_input = input("What is the email address of the contact you'd like to add? ")

        # This section handles the instance that the email address already exists in the contact book dictionary
        for contact in contacts.values():
            if contact["email"] == user_input:
                user_input = input("This email address already exists in the contact book - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

                if user_input == "Y":
                    print("Exiting out of adding a contact")
                    adding_contact = False
                    break
                else:
                    user_input = False
                    continue

        if not user_input: continue

        print(f"Adding {user_input} as the new email address to the contact {contact_name_input}")
        contact_email_address_input = user_input
        break

    # This section handles the prompting of the user to input age & validation
    while(adding_contact):

        # This section handles the instance that the age input is invalid
        try:
            user_input = int(input("What is the age of the contact you'd like to add? "))
        except:
            user_input = input("The age value that you entered is invalid - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of adding a contact")
                adding_contact = False
                break
            else:
                continue

        print(f"Adding {user_input} as the age for the new contact {contact_name_input}")
        contact_age_input = user_input
        break

    print(f"So the contact you are going to be adding is {contact_name_input} wherein this contacts phone number is {contact_phone_number_input}, this contacts email address is {contact_email_address_input}, and this contacts age is {contact_age_input}")

def remove_contact(contacts: dict):
    """
    This method handles the removal of an existent contact in the contact book dictionary

    Args:
        1. contacts - variable that contains the contact book dictionary
    Returns:
        Nothing - only performs the removal operation from the contact book dictionary
    """
    print("You have chosen to remove a contact")

    # This section displays the current dictionary to the user
    print("="*60)
    print("Your current contacts are:")

    counter = 1
    removing_contact = True
    contact_remove_input = ""

    for contact_name in contacts.keys():
        print(f"{counter}. {contact_name}")
        counter += 1

    # This section handles the prompting of the user to remove an existing contact & validation
    while(removing_contact):
        user_input = input("What is the name of the existing contact you'd like to remove from your contacts? ")

        if user_input not in contacts.keys():
            user_input = input("This contact name does not exist in the contact book - would you like to re-input or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of removing a contact")
                removing_contact = False
                break
            else:
                continue

        print(f"Removing {user_input} as the contact to remove from the contact book.")
        contact_remove_input = user_input
        break

    # This section handles the actual contact removal logic
    del contacts[contact_remove_input]

    print(f"Contact {contact_remove_input} has just been removed from your contacts list.")

    print(f"Your new contacts list is: ")

    counter = 1
    for contact_name in contacts.keys():
        print(f"{counter}. {contact_name}")
        counter += 1

def update_contact(contacts: dict):
    """
    This method handles the updating of an existing contact in the contact book dictionary

    Args:
        1. contacts - variable that contains the contact book dictionary
    Returns:
        Nothing - only performs updating a specific contact operation from the contact book dictionary
    """

    # This section displays the entire contacts dictionary to the user
    print("="*60)
    print("You have chosen to update a contact")

    counter = 1
    for contact_name in contacts.keys():
        print(f"{counter}. {contact_name}")
        counter += 1

    # This section contains the initialized variables for user input & validation
    updating_contact = True
    contact_name_input = ""
    contact_detail_input = ""

    # This section handles the prompting of the user to update the contact information of a specific contact & validation
    while(updating_contact):
        user_input = input("What is the name of the contact you'd like to update? ")

        # This section handles the instance that the contact name does not exist in the contact book dictionary
        if user_input not in contacts.keys():
            user_input = input("This contact name does not exist in the contact book - would you like to re-input or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of updating a contact")
                updating_contact = False
                break
            else:
                continue

        print(f"Updating the details of {user_input} from your contacts.")
        contact_name_input = user_input
        break

    # This section handles the prompting of the user as to which contact detail to update & validation
    while(updating_contact):
        user_input = input("Which contact detail would you like to update? (phone, email, age) ")

        # This section handles the instance that the chosen detail to update does not exist in the contact book dictionary
        if user_input not in contacts[contact_name_input].keys():
            user_input = input("This contact detail does not exist in the contact book - would you like to re-input or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of updating a contact")
                updating_contact = False
                break
            else:
                continue

        print(f"Updating the {user_input} of {contact_name_input}")
        contact_detail_input = user_input
        break

    # This section handles the actual contact updating logic
    
    # This section handles the prompting of the user to input the new phone number & validation
    while(updating_contact and contact_detail_input == "phone"):
        user_input = input("What is the phone number of the contact you'd like to add? ")

        # This section handles the instance that the phone number already exists in the contact book dictionary
        for contact in contacts.values():
            if contact["phone"] == user_input:
                user_input = input("This phone number already exists in the contact book - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

                if user_input == "Y":
                    print("Exiting out of adding a contact")
                    adding_contact = False
                    break
                else:
                    user_input = False
                    continue

        if not user_input: continue

        print(f"Updating {user_input} as the new phone number to the contact {contact_name_input}")
        contacts[contact_name_input][contact_detail_input] = user_input
        break

    # This section handles the prompting of the user to input the new email address & validation
    while(updating_contact and contact_detail_input == "email"):
        user_input = input("What is the email address of the contact you'd like to add? ")

        # This section handles the instance that the email address already exists in the contact book dictionary
        for contact in contacts[contact_name_input].values():
            if contact["email"] == user_input:
                user_input = input("This email address already exists in the contact book - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

                if user_input == "Y":
                    print("Exiting out of updating a contact")
                    updating_contact = False
                    break
                else:
                    user_input = False
                    continue

        if not user_input: continue

        print(f"Updating {user_input} as the new email address to the contact {contact_name_input}")
        contacts[contact_name_input][contact_detail_input] = user_input
        break

    # This section handles the prompting of the user to input the new age & validation
    while(updating_contact and contact_detail_input == "age"):

        # This section handles the instance that the age input is invalid
        try:
            user_input = int(input("What is the age of the contact you'd like to update it to? "))
        except:
            user_input = input("The age value that you entered is invalid - would you like to re-add or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of updating a contact")
                updating_contact = False
                break
            else:
                continue

        print(f"Updating {user_input} as the new age to the contact {contact_name_input}")
        contacts[contact_name_input][contact_detail_input] = user_input
        break

def view_all_contacts(contacts: dict):
    """
    This method handles the viewing of all of the contacts in the contact book dictionary

    Args:
        1. contacts - variable that contains the contact book dictionary
    Returns:
        Nothing - only performs the view all contacts in the contact book dictionary operation
    """

    # This section handles the displaying of all the current contacts in the contact book dictionary

    print("="*60)
    print("You have chosen to view all of the contacts in your contact book.")

    counter = 1

    for contact_name in contacts.keys():
        print(f"{counter}. {contact_name}")
        counter += 1

def view_contact(contacts:dict):
    """
    This method handles the viewing of only a specific contact in the contact book dictionary

    Args:
        1. contacts - variable that contains the contact book dictionary
    Returns:
        Nothing - only performs the view specific contact in the contact book dictionary operations
    """

    print("="*60)
    print("You have chosen to view the details of a specific contact in your contact book.")

    counter = 1
    for contact_name in contacts.keys():
        print(f"{counter}. {contact_name}")
        counter += 1

    # This section contains the initialized variables for user input & validation
    viewing_contact = True
    contact_name_input = ""
    
    # This section handles the prompting of the user to display the contact information of a specific contact & validation
    while(viewing_contact):
        user_input = input("What is the name of the contact you'd like to view? ")

        # This section handles the instance that the contact name does not exist in the contact book dictionary
        if user_input not in contacts.keys():
            user_input = input("This contact name does not exist in the contact book - would you like to re-input or exit? Input Y to exit, otherwise, enter any key ")

            if user_input == "Y":
                print("Exiting out of viewing a contact")
                viewing_contact = False
                break
            else:
                continue

        print(f"Viewing the details of {user_input} from your contacts.")
        contact_name_input = user_input
        break

    # This section handles the actual contact viewing logic

    print(f"The contact name is {contact_name_input}")
    print(f"The contact phone number is {contacts[contact_name_input]["phone"]}")
    print(f"The contact email address is {contacts[contact_name_input]["email"]}")
    print(f"The contact age is {contacts[contact_name_input]["age"]}")

is_continue = True

# This is the start of the program itself which prompts the user to choose from existing options
print("="*60)
print("CONTACT BOOK PROGRAM")
print("="*60)
print("\n")
print("What would you like to do for today in the Contact Book Program?")
print("1. Add a New Contact to the Contact Book")
print("2. Remove an Existing Contact from the Contact Book")
print("3. Update an Existing Contact in the Contact Book")
print("4. View All Contacts in the Contact Book")
print("5. View a Specific Contact in the Contact Book")

# This section takes in user input and ensures that the user input is from what are only the possible options
while(is_continue):
    user_input = int(input("Please enter your chosen action: "))

    if user_input not in range(1, 6):
        print("Please only choose the listed possible actions to choose from")
        exit()

    # This section handles the calling of the specific methods for each of the action based on provided user input
    match user_input:
        case 1:
            add_contact(contacts)
        case 2:
            remove_contact(contacts)
        case 3:
            update_contact(contacts)
        case 4:
            view_all_contacts(contacts)
        case 5:
            view_contact(contacts)

    # This section handles the prompting of the user if they wish to continue using the program
    user_input = input("Do you wish to exit the program? If yes, please input Y ")

    if user_input == "Y":
        is_continue = False
        print("Thank you for using the program!")
        exit()
    else:
        print("User did not input Y, therefore continuing program")
        is_continue = True