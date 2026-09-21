## CHAPTER 5 - TESTING & DEBUGGING

# tests the functionality of the code we write - unit tests
# we write inputs to the code that we write expecting outputs - unit tests

def total_xp(level, xp_to_add):
    pass

# unit tests rpovide run cases that provide different sets of inputs
# unit tests also provide submit cases that provide different sets of input swhen we decide to submit a code

# we want to test our code bit by bit - methodical with how we test things

# output testing - just checking the outputs of our code
# unit testing - inputting different values into our code to see how they are processed

## Assignment
# complete the total_xp function. It accepts two integers as input:
# level and xp_to_add
# There are 100 xp per level and total_xp should convert the current level to xp, then add this current xp to the xp_to_add argument and return the player's total xp. For example:
# If a player is level 1 and gains 100 xp, they have 200 total xp.
# If a player is level 2 and gains 250 xp, they have 450 total xp.
# If a player is level 170 and gains 590 xp, they have 17590 total xp.

def total_xp(level, xp_to_add):
    base_xp = level * 100
    total = base_xp + xp_to_add

    return total

# Debugging
# it's best practice to debug code before making it go live

def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    actual_damage_dealt = total_damage - resist
    new_health = health - actual_damage_dealt

    return new_health

# Assignment
# Complete the take_magic_damage function. It should return the new_health after calculating how much magic-type damage the player takes. Here is a description of the arguments:
# health: the player's starting health
# resist: the player's magic resistance. This reduces the damage they take by a static amount
# amp: the attacker's magic amplification. This increases the damage they deal by a damage multiplier
# spell_power: the base damage of the spell
# first, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.

# Learning effectively
# First read through the whole lesson & understand the lesson
# For each assignment - read through whole assignment & understand the assignment
# Add print statements to code to help debug

# Debugging Practice

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    print(f"After XP = {after_xp}")

    alert = f"Achievement Unlocked: {ach_name}"
    print(f"Alert string = {alert}")
    return after_xp, alert

# Assignment
# Let's complete the unlock_achievement function. It accepts 3 arguments:
    # before_xp - int
    # ach_xp - int
    # ach_name - str

# It should return 2 values:
    # The player's xp after the achievement is unlocked (The sum of before_xp and ach_xp)
    # An alert message that says "Achievement Unlocked: ACHIEVEMENT_NAME", WHERE ACHIEVEMENT_NAME is the name of the achievement

# Stack Trace
# Also known as Traceback
# Tells us that there are errors in our different files
# Python treats whitespace as meaningful - indents needs to be 4 spaces long
# 

def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} stength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg