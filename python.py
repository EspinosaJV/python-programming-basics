# SHOPPING RECEIPT CALCULATOR PROJECT

# 1. Prompt the user for the item name (string) - Done
# 2. Prompt the user for the price of the item (string) - Done
# 3. Prompt the user for the quantity of the item (string) - Done
# 4. Calculate the subtotal - price * quantity and add all - Done
# 5. Add 12% tax - subtotal * 0.12 then add to subtotal - Done
# 6. Prompt the user how much the customer has paid - Done
# 7. Calculate the change - Done
# 8. Print a receipt

receipt_contents = dict()

def prompt_item_name(receipt_contents: dict):
    """
    Prompt the user to input the specific item names in the receipt itself wherein these item names will become the keys of the receipt_contents dictionary

    Args:
        - receipt_contents = dictionary containing the items of the receipt
    Returns:
        - None, only performs the appending of the items as keys to the receipt_contents dictionary
    """

    # This section handles the loop prompting of the user to input all the items that needs to be included in the receipt
    user_input = True

    while(user_input):
        user_input = input("What is the name of the item you want to include in the receipt? Input X to stop adding anymore items. ")

        if user_input == "X":
            print("Stopping the addition of anymore items into the receipt.")
            user_input = False
            break
        else:
            receipt_contents[user_input] = None

    # This section handles the display of the items that are in the receipt_contents dictionary

    print("Here are the items to be contained in the outputted receipt: ")

    for item in receipt_contents.keys():
        print(item)

def prompt_item_price(receipt_contents: dict):
    """
    Prompt the user to input the specific item prices of the items in the receipt itself wherein these item prices will become the individual prices of each item in the receipt_contents dictionary

    Args:
        - receipt_contents = dictionary containing the items of the receipt
    Returns:
        - None, only performs the appending of the individual prices of the items to the receipt_contents dictionary
    """

    # This section handles the loop prompting the user to input the individual prices of the items that needs to be included in the receipt

    for item in receipt_contents.keys():
        user_input = float(input(f"For the item {item}, what is it's individual price? "))

        receipt_contents[item] = {"price": user_input}

    # This section handles the display of the items with their corresponding individual prices

    for item in receipt_contents.keys():
        print(f"For the item {item}, its price is {receipt_contents[item]["price"]}")

def prompt_item_qty(receipt_contents: dict):
    """
    Prompt the user to input the item quantities of the items in the receipt wherein these quantity values will determine how many of each item is to be calculated with the price for the receipt subtotal & total

    Args:
        - receipt_contents = dictionary containing the items of the receipt
    Returns:
        - None, only performs the appending of the quantity values to the items in the receipt_contents dictionary
    """

    # This section handles the loop prompting of the user ot input the respective quantity values of all the items that needs to be included in the receipt

    for item in receipt_contents.keys():
        user_input = int(input(f"For the item {item}, what is the quantity value? "))

        receipt_contents[item]["quantity"] = user_input

    # This section handles the display of the items with their corresponding individual quantity values
    
    for item in receipt_contents.keys():
        print(f"For the item {item}, its quantity value is {receipt_contents[item]["quantity"]}")

def calculate_subtotal(receipt_contents: dict):
    """
    This function handles the calculation of the subtotal given the items in the dictionary.

    Args:
        - receipt_contents = dictionary containing the items of the receipt and their corresponding price & quantity values
    Returns:
        - calculated subtotal value
    """

    # This section handles the calculation of the subtotal for all of the items in the receipt

    calculated_subtotal = 0.0
    item_totals = []
    running_total = 0

    # This section handles the calculation of the total prices of the individual items and adds them to the item totals list for summation

    for item in receipt_contents.keys():
        current_item_price = 0.0
        current_item_qty = 0
        current_item_total = 0.0

        # Acquires the price & quantity of current item in the iteration
        current_item_price = float(receipt_contents[item]["price"])
        current_item_qty = int(receipt_contents[item]["quantity"])

        # Calculates the current item's total given its price & quantity
        current_item_total = current_item_price * current_item_qty

        # Appends the current item total to the item totals list
        item_totals.append(current_item_total)

    # This section handles the summation of the item totals list to then output the subtotal value
    running_total = 0

    for total in item_totals:
        running_total += total

    return running_total

def calculate_total(receipt_contents: dict, subtotal: float):
    """
    This function handles the calculation of the total given the subtotal value and the tax value

    Args:
        - receipt_contents = dictionary containing the items of the receipt and their corresponding price & quantity values
        - subtotal = float value which is the subtotal before tax
    Returns:
        - total = float value which is the subtotal after tax
    """

    # This section handles the calculation of the total for all of the items in the receipt
    calculated_tax = subtotal * 0.12
    calculated_total = subtotal + calculated_tax

    return calculated_total

def prompt_customer_payment():
    """
    This function prompts the user to input how much the customer has paid.

    Args:
        - None
    Returns:
        - customer_payment = float value representing how much the customer has paid
    """

    # This section handles the prompting of the user for how much the customer has paid
    customer_payment = float(input("How much has the customer paid for this receipt? "))

    return customer_payment

def calculate_customer_change(customer_payment: float, receipt_total: float):
    """
    This function handles the calculation of the customer's change.

    Args:
        - customer_payment = float value representing the amount the customer has paid
        - receipt_total = float value representing the total amount of the receipt
    Returns:
        - customer_change = float value representing how much customer should receive as change
    """

    # This section handles the calculation of the change that must be given to the customer after customer payment & receipt total

    customer_change = customer_payment - receipt_total

    return customer_change

def display_customer_receipt(receipt_contents: dict, receipt_subtotal: float, receipt_total: float, customer_payment: float, customer_change: float):
    """
    This function handles the display of the customers entire receipt

    Args:
        - receipt_contents = dictionary containing all of the items with their price & quantities
        - receipt_subtotal = float value representing the total price before tax
        - receipt_total = float value representing the total price after tax
        - customer_payment = float value representing the amount customer has given
        - customer_change = float value representing the amount that must be given back to the customer as change

    Returns:
        - None
    """

    # This section handles the display of the items in the receipt with their price & quantities
    for item in receipt_contents.keys():
        print(f"{item}, {receipt_contents[item]["price"], {receipt_contents[item]["quantity"]}}")

    # This section handles the display of the subtotal
    print(f"Subtotal: {receipt_subtotal}")

    # This section handles the display of the total after tax
    print("Tax of 12%")
    print(f"Total: {receipt_total}")

    # This section handles the display of the customer payment
    print(f"Customer Paid: {customer_payment}")

    # This section handles the display of the customer change
    print(f"Customer Change: {customer_change}")

print("="*60)
print("Welcome to the Shopping Receipt Calculator program")

# This section handles the prompting of the user for items in receipt
prompt_item_name(receipt_contents)

# This section handles the prompting of the user for the individual price of the items in the receipt
print("="*60)
print("Now going to be asking you for the individual price of each of the items in the receipt. ")
prompt_item_price(receipt_contents)

# This section handles the prompting of the user for the quantity of a singular item in the receipt
print("="*60)
print("Now going to be asking you for the quantity of each of the items in the receipt. ")
prompt_item_qty(receipt_contents)

# This section handles the calculation of the subtotal of all of the items
print("="*60)
print("Now the program is going to be calculating the subtotal of all of the items in the receipt. ")
receipt_subtotal = calculate_subtotal(receipt_contents)
print(f"The receipt's subtotal is: ", receipt_subtotal)

# This section handles the calculation & addition of tax to the subtotal
print("="*60)
print("Now the program is going to be calculating the total which includes the tax addition in the receipt. ")
receipt_total = calculate_total(receipt_contents, receipt_subtotal)
print(f"The receipt's total is: ", receipt_total)

# This section now handles prompting the user for how much the customer has paid
print("="*60)
print("Now the program is going to be asking you for how much the customer has paid. ")
customer_payment = prompt_customer_payment()
print(f"The customer has paid {customer_payment}. ")

# This section now handles the calculation of the change that must be given to the customer
print("="*60)
print("Now the program is going to be calculating the change that you must give to the customer.")
customer_change = calculate_customer_change(customer_payment, receipt_total)
print(f"The customer's change is {customer_change}.")

# This section now handles the display of the entire receipt itself
print("="*60)
print("Now the program is going to be displaying the receipt.")
display_customer_receipt(receipt_contents, receipt_subtotal, receipt_total, customer_payment, customer_change)