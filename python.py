# command-line ATM where the user can
# 1. Check their balanca
# 2. Deposit money
# 3. Withdraw money
# 4. Exit

# This section handles the initialization / definition of variables
user_balance = 0.0 # initialized the overall bank balance of the user
deposited = 0.0 # initialized the amount deposited by the user
withdrawn = 0.0 # initialized the amount that can be withdrawn by the user

# This section handles the definition of custom exceptions
class DepositError(Exception):
    pass

class WithdrawalError(Exception):
    pass

# This section handles the function definition of all the actions that the user can take.
def check_balance(user_balance: float):
    """
    This function handles the display of the user's current balance to the terminal.

    Args:
        1. user_balance - float type variable representing the current bank balance of the user
    Returns:
        1. None - performs the displaying of the users balance only - does not return any value.
    """

    print("="*60)
    print("You have opted to check your current balance.")
    print("="*60)

    # This section handles the display of the user balance to the user
    print(f"Your current balance is: {user_balance}")

def deposit_money(user_balance: float):
    """
    This function handles the depositing of money into the user's bank account.

    Args:
        1. user_balance - float type variable representing the current bank balance of the user
    Returns:
        1. deposit - represents the validated deposit amount by the user to be added to user_balance
    """
    print("="*60)
    print("You have opted to deposit money to your bank balance.")
    print("="*60)

    # This section handles the prompting & validation of the users deposit amount
    print("How much would you like to deposit into your bank account?")
    try:
        deposit = float(input())

        if deposit < 0:
            raise DepositError()
        
    except (ValueError, DepositError):
        print("Please input an appropriate deposit amount!")
        exit()
    except Exception:
        print("Something went wrong - please contact support!")
        exit()

    print(f"You have deposited {deposit}.")
    return deposit

def withdraw_money(user_balance: float):
    """
    This function handles the withdrawal of money from the user's bank account.

    Args:
        1. user_balance - float type variable representing the current bank balance of the user
    Returns:
        1. withdrawal - float type variable representing the validated withdrawn amount by the user to be subtracted from user_balance
    """
    print("="*60)
    print("You have opted to withdraw money from your bank balance.")
    print("="*60)

    # This section handles the prompting & validation of the users withdrawal amount
    print("How much would you like to withdraw from your bank account?")
    try:
        withdrawal = float(input())

        if (withdrawal > user_balance) or (withdrawal < 0):
            raise WithdrawalError()

    except (ValueError, WithdrawalError):
        print("Please input an appropriate withdrawal amount!")
        exit()
    except Exception:
        print("Something went wrong - please contact support!")
        exit()

    print(f"You have withdrawn {withdrawal}")
    return withdrawal

print("="*60)
print("Welcome to the Terminal ATM! What would you like to do for today? Please input the appropriate numbers 1, 2, and 3.")
print("="*60)

# This section handles the display of the different possible user actions to the user through the terminal
print("1. Check your current balance")
print("2. Deposit money to your bank account")
print("3. Withdraw money from your bank account")
print("4. Exit")

# This section handles the prompting & validation of the user input for the choices

while(True):
    try:
        user_choice = int(input("What would you like to do? "))
    except ValueError:
        print("Please input an appropriate number!")
        exit()
    except Exception:
        print("Something went wrong - please contact support!")
        exit()

    # This section handles the calling of the appropriate functions depending on user choice
    match user_choice:
        case 1:
            check_balance(user_balance)
        case 2:
            deposited = deposit_money(user_balance)
            user_balance = user_balance + deposited
            print(f"Your new balance is now {user_balance}.")
        case 3:
            withdrawn = withdraw_money(user_balance)
            user_balance = user_balance - withdrawn
            print(f"Your new balance is now {user_balance}.")
        case 4:
            print("Thank you for using the command-line ATM!")
            exit()
        case _:
            print("Please choose an appropriate number!")
            exit()