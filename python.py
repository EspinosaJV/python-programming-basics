## CHAPTER 6 - COMPUTING

# basic math operations of addition, subtraction, multiplication, and division
# if done on integers = integer result
# if done on floats = float type results

# Assignment
# Complete the missing sections of the calculate_damage function.
    # Fix the total_damage variable so that it contains the sum of all the different weapons' damage values
    # Fix the average_damage variable so that it contains the average weapon damage

def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword + arrow + spear + dagger + fire
    average_damage = total_damage / 5

    return total_damage, average_damage

# integers and floats are numerical types in Python

## Floor Division = //
# if we give it 2 integers - it will always output an integer type, chopping off decimal points
# 7 // 3
# 2 (an integer)
# Floor of a number is the LARGEST integer which is less than or equal to the number

# 9 / -4 = -2.25
# but with floor division, 9 // -4 = -3 (remember floor is the LARGEST integer which is less than or equal to the number) (-2.25 rounds down to the floor which is -3)

# result of 11 / 2 - actual answer is 5.5 but for 11 / 2 this is 5

## Exponents - **

expo = 9 ** 2

print(f" EXPO: {expo}") # the answer is 81 or 9 * 9

# 2 ** 3 = 8

## Changing in Place
# You can change a variable in place
# Variables can be used in the left & right hand side of the equal sign

def update_player_score(current_score, increment):
    print(f"Current score before changing in place: {current_score}")
    current_score = current_score + 300 # we are resetting the value of the variable current score to the same value + 300
    # we are assigning current_score value + 300 to the current_score variable once again, changing in place
    print(f"Current score after changing in place: {current_score}")

# Assignment
# Complete the update_player_score function. It should add increment to current_score and then return the new current_score

def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score

## Plus Equals = +=
# Also known as in place operators (-=, /=, *=)

def get_hurt(current_health, damage):
    print(f"Current Health: {current_health}")
    current_health += 77
    print(f"Current Health after: {current_health}")
    current_health *= 77
    print(f"Current Health after: {current_health}")
    current_health /= 77
    print(f"Current Health after: {current_health}")

# Assignment
# Complete the get_hurt function. It should use the -= in-place operator to subtract damage from current_health and then return the new current_health.

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

# Binary Notation

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    permission = user_permissions & can_create_guild
    return permission

def get_review_bits(user_permissions):
    return user_permissions & can_review_guild

def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild

def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

## Bitwise | Operator
# Assignment
# Complete the calculate_guild_perms function. It should return a binary number that represents the permissions of all the members of the guild (Glorfindel, Galadriel, Elendil, and Elrond).
# Use a series of bitwise "or" operations to calculate the superset of all the member's permissions

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond): 
    party_permissions = glorfindel | galadriel | elendil | elrond
    return party_permissions