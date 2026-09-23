## CHAPTER 7 COMPARISONS

# Comparison Operators
# Boolean logic & Comparison operators
# Comparing logic that results in either True or False

# <, >, <=, >=, ==, !=

# Assignment
# Complete the player_1_wins function. It should return True if player 1 has a high score and False otherwise

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

# Sample Code

user_username = 'nate_codes'
user_password = 'password12345'

def check_login_credentials(login_username, login_password):
    usernames_match = login_username == user_username

    passwords_match = login_password == user_password

    both_match = usernames_match & passwords_match
    return both_match

login_username = 'nate_codes'
login_password = 'WoWisALameGame!'

login_successful = check_login_credentials(login_username, login_password)
print(f"Login Successful: {login_successful}")

# Assignment
# Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

# 1. is_mustang_edward_same
# 2. is_alphonse_edward_same
# 3. is_winry_alphonse_same

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# Assignment
# Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.

def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

# If Statements
def print_status(player_health):
    # ?

# Don't edit below this line

def test(health):
    print(f"Player Health: {health}")

# The condition should result to a truthy value 
# empty string (''), 0 - Falsy, 1 - Truthy

# Assignment
# Complete the print_status function
# If player_health is 0, print the text dead to the console
# Afterwards, whether or not the player is dead, print the text status check complete to the console

def print_status(player_health):

    if player_health == 0:
        print("dead")

    print("status check complete")

# Don't edit below this line

def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("========================")

def main():
    test(0)
    test(5)

# Assignment
# Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string correct amount, otherwise, return the string incorrect amount

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"

    return "incorrect amount"

# Another assignment
# Complete the player_status function. If the player health is less than or equal to 0, return the string dead, otherwise, if it's less than or equal to 5, return the string injured, otherwise, return the string healthy

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"

# Another assignment
# There is a bug in the check_high_score function! Add the proper conditional statement to fix the bug. If the names match, "You are the highest scoring player!" should be returned. Otherwise, "You are not the highest scoring player!" should be returned.

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

# Another assignment
# Complete the check_high_score function. If the player_name matches the high score name, return the string high, otherwise if it's the low scorer, return the string low, otherwise return the string neither

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name)
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"

# Boolean Logic

# Another assignment
# We need a way for our game to track whether a character's attack hits or misses
# Complete the does_attack_hit function. The function should return True if either of the following conditions are met:
    # The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
    # The attack roll is a 20
# Otherwise, it should return False

def does_attack_hit(attack_roll, armor_class):
    if attack_roll != 1 and attack_roll >= armor_class or attack_roll == 20:
        return True
    else:
        return False

    # or you can do
    condition_1 = attack_roll != 1
    condition_2 = attack_roll >= armor_class
    condition_3 = attack_roll == 20

    result = (condition_1 and condition_2) or condition_3
    return result

# Another assignment
# In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!
# Complete the function that determines if a bartender should server drinks to a customer. Only return True if all of these conditions apply:
    # The customer's age is 21 or older
    # The bartender is working
    # The time is at least 5 but no later than 10

def should_serve_customer(customer_age, on_break, time):
    condition_1 = customer_age >= 21
    condition_2 = on_break == False
    condition_3 = 5 >= time <= 10

    if condition_1 and condition_2 and condition_3:
        return True

    # or

    condition_1 = customer_age >= 21
    # condition_2 = on_break
    condition_3 = 5 <= time <= 10

    return condition_1 and not on_break and condition_3

