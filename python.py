# Chapter 3 - Functions
# allows us to reuse & organize code

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")

## Multiple Parameters
# Functions can have multiple parameters
# order matters for multiple parameters
# we don't need to name parameters when passing them to function calls

# Another exercise
damage_one = 2
damage_two = 4
damage_three = 3
damage_four = -1
damage_five = 10
damage_siz = 5

# Don't touch above this line

def triple_attack(slash_one, slash_two, slash_three):
    total_dmg = slash_one + slash_two + slash_three
    return total_dmg

# Don't touch below this line

print("Getting damage for", damage_one, damage_two, "and", damage_three, "...")
print(triple_attack(damage_one, damage_two, damage_three), "points of damage dealt!")
print("============================================================================")

print("Getting damage for", damage_four, damage_five, "and", damage_siz, "...")
print(triple_attack(damage_four, damage_five, damage_six), "points of damage dealt!")
print("============================================================================")

# We need to calculate the total damage from a triple attack combo. Complete the triple_attack function that takes three numbers as its parameters and returns the sum

## Where to declare functions

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()

# functions need to be defined before they are called
# functions do not need to be defined in the same order that they are called - as long as they are defined before they are called
# best practice when it comes to function ordering is to have an entry point function defined which is then only placed at the bottom

## Another Exercise
# In Fantasy Quest as characters are running around the map they can lose health due to heat exhaustion. The game tracks the temperature in Fahrenheit, but we need to display the temperature in Celsius for players outside the US.

# Write a function called to_celsius that returns the temperature converted from Fahrenheit to Celsius

def to_celsius(f):
    temp = (f - 32) * 5 / 9
    # celsius = (5 / 9) * (f - 32)
    return temp
    # return celsius

## Don't touch below this line

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")

test(100)
test(88)
test(104)
test(112)

# def is the keyword used to create functions in Python
# functions only need to be defined once

# Another exercise

def hours_to_seconds(hours):
    minutes = hours * 60
    seconds = minutes * 60

    return seconds

# Don't touch below this line

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

test(10)
test(1)
test(25)
test(100)
test(33)

# a function without a return - it will always return None by default (an example of a NoneType)

## Multiple Return Values

# Another Exercise
# Complete the become_warrior function. It accepts 3 inputs:
# first_name: string type
# last_name: string type
# power: integer

# It should return 2 values:

# 1. The warrior's "title", which is a string in this format:
# first_name last_name the warrior
# Where first_name and last_name are the actual values of the first_name and last_name inputs. Note: make sure the format is exact, do not add capitalization or punctuation.

# 2. A new "power" value that is one greater than the input power
# For example
# title, power = become_warrior("Aang", "Airbender", 100)
# print(title)
# "Aang Airbender the warrior"
# print(power)
# 101

def become_warrior(first_name, last_name, power):
    title = f"{first_name} {last_name} the warrior"
    new_power = power + 1

    return title, new_power

# Don't edit below this line

def main():
    test("Frodo", "Baggings", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)

def test(first_name, last_name, power):
    title, new_power = become_warrior(first_name, last_name, power)
    print(title, "has a power level of:", new_power)

main()

# Parameters vs Arguments
# parameters - what is being given to the function IN the function definition - placeholders or containers for the arguments
# arguments - when function is called - the values provided withnt he function call are the arguments - actual values

# Default Values for Function Arguments

def get_punched(health, armor=0):
    new_health = health + armor
    dmg = 50
    new_health = new_health - dmg
    return new_health

def get_slashed(health, armor=0):
    new_health = health + armor
    dmg = 100
    new_health = new_health - dmg
    return new_health

# Don't touch below this line

def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=================================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=================================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=================================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=================================================")

# printing vs returning

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title

# if no return line, function just returns None

# Don't touch below this line

def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job) # title just gets None
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=========================================")

test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")