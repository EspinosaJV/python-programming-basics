## CHAPTER 12 - ERRORS
# Syntax errors and exceptions

player_inventory = []

print("Look I'm running!")

first_item = player_inventory[0} # this is a syntax error - something about how we write the code is breaking the rules of the language

# corrected but still wrong
first_item = player_inventory[0] # this is a runtime logic error - empty list but we are trying to call the first item from the list

print(f"First Item: {first_item}")

# Try and Except block

try:
    first_item = player_inventory[0]
    print(f"First Item: {first_item}")
except Exception as e:
    print(f"There was an error getting the first item: {e}")

print("Also made it this far!")

## Assignment
def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    except Exception as e:
        print(f"The Error is {e}")

## Raising your own Exceptions
# we can use raise Exception to raise our own exceptions

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    else:
        raise Exception('player id not found')

# Using try except block

def shoot_arrow():
    player_arrows = player_inventory[1]
    total_arrows = player_arrows['arrow count']

    print("Shooting arrow...")
    try:
        total_arrows -= 1
        print(f"Arrows remaining in the inventory: {total_arrows}")
    except Exception as e:
        print(e)
    except TypeError:
        print('Error: There are not enough arrows in the inventory')


shoot_arrow()

## ASSIGNMENT

def handle_get_player_record(player_id):
    try:
        get_player_record(player_id)
    except IndexError: 
        return 'index is too high'
    except Exception as e:
        return e