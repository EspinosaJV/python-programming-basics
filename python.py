# Make a personal expense tracker where:
# This tracker allows you to add an expense
# This tracker allows you to view your expenses
# This tracker allows you to calculate the total expenses
# This tracker allows you to show expenses by category
# Allows you to exit the tracker

# This section displays the greeting message to the user
print("Welcome to your Personal Expense Tracker!")
print("="*60)
print("1. Add Expense")
print("2. View Expenses")
print("3. Calculate Total Expenses")
print("4. Show Expenses by Category")
print("5. Exit Tracker")

expenses = {}

def add_expense(expenses: dict):
    """
    This function handles the addition of a new expense to existing expense list.

    Args:
        1. expenses - dict type parameter representing the dictionary variable expenses.
    Returns:
        1. None - only performs the appending of a new expense into the expenses dictionary.
    """
    print("You have chosen to add an expense!")

    # This section handles the inputting of the description of the new expense
    expense_description = input("What is the description of this expense? ")
    print(f"Description: {expense_description}")

    # This section handles the inputting of the category of the new expense
    expense_category = input("What is the category of this expense? ")
    print(f"Category: {expense_category}")

    # This section handles the inputting of the amount of the new expense
    expense_amount = input("What is the amount of this expense? ")
    print(f"Amount: {expense_amount}")

    # This section handles the inputting of the new expense to the expenses dictionary & its display
    expenses[expense_description] = {"Category": expense_category, "Amount": expense_amount}

    print(f"The expense for {expense_description} has just been added!")

def view_expenses(expenses: dict):
    """
    This function handles the display of current expenses from the expense list.

    Args:
        1. expenses - dict type variable containing all of the expenses inputted by the user.
    Returns:
        1. None - function only performs the displaying of the expenses to the user - does not return anything.
    """
    print("You have chosen to view your current expenses!")

    # This section handles the display of all of the expenses and its corresponding category & amounts from the expenses dictionary
    for expense in expenses:
        print(f"Description: {expense}")
        print(f"Category: {expenses[expense]["Category"]}")
        print(f"Amount: {expenses[expense]["Amount"]}")
        print("-"*30)

def calculate_expenses(expenses: dict):
    """
    This function calculates the total expenses using the price from the expense list.
    
    Args:
        1. expenses - dict type variable containing all of the expenses inputted by the user.
    Returns:
        1. None - function only performs the calculation of the total expense and its display to the user - does not return anything.
    """
    print("You have chosen to calculate the total expenses!")

    running_expense_total = 0

    # This section handles the calculation of the total expenses given the added expenses from the expenses dictionary
    for expense in expenses:
        current_expense_amount = int(expenses[expense]["Amount"])
        running_expense_total += current_expense_amount

    print(f"Your total expense so far is {running_expense_total}!")


def show_expenses_category(expenses: dict):
    """
    This function handles the display of expenses given a category.

    Args:
        1. expenses - dict type variable containing all of the expenses inputted by the user.
    Returns:
        1. None - function only performs the display of all of the different expense categories & the expenses under the chosen expense category
    """
    print("You have chosen to show the expenses by category")

    # This section handles the display of all of the different categories of expenses
    print("Here are the current categories of your expenses so far:")

    expense_counter = 1
    expense_categories = []

    for expense in expenses:
        category_to_display = expenses[expense]["Category"]

        if category_to_display not in expense_categories:
            print(f"{expense_counter}. {category_to_display}")
            expense_categories.append(category_to_display)
            expense_counter += 1

    # This section handles prompting the user of what categories' expenses needs to be displayed
    user_choice = input("Please input the name of the category you would like to see the expenses of ")

    for expense in expenses:
        if user_choice not in expense_categories:
            print("Please input a proper category.")
            break
        else:
            if (expenses[expense]["Category"] in expense_categories) and (expenses[expense]["Category"] == user_choice):
                print(f"Description: {expense}")
                print(f"Category: {expenses[expense]["Category"]}")
                print(f"Amount: {expenses[expense]["Amount"]}")
                print("-"*30)        

# This section handles the prompting of user's choice for action
while(True):
    user_choice = int(input("What action would you like to do right now? "))

    match user_choice:
        case 1:
            add_expense(expenses)
        case 2:
            view_expenses(expenses)
        case 3:
            calculate_expenses(expenses)
        case 4:
            show_expenses_category(expenses)
        case 5:
            print("You have chosen to exit your personal expenses tracker, goodbye!")
            exit()

