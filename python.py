# Chapter 2 - Variables
# variables are how we store data in our program for usage later

player_health = 1000
print(player_health)

# variables can hold any type of data - varies by what they are holding

player_health = 1000

# reduce by 100 here
player_health -= 100

print(player_health)

# and here
player_health -= 100

print(player_health)

# and here
player_health -= 100

print(player_health)

# and here
player_health -= 100

print(player_health)

# another exercise
# create a new variable called armored_health and set it equal to player_health * armor_multiplier

player_health = 1000
armor_multiplier = 2

# create armored_health here
armored_health = player_health * armor_multiplier
print(armored_health)

# another exercise
# when our hero walks through poison, their health should be reduced. Right now the hero is gaining 10 health instead of losing 10 health. Change the poison_damage variable to be negative.

player_health = 100
poison_damage = -10

# don't touch below this line

player_poison_health = player_health + poison_damage

print(player_poison_health)

## Comments
# comments are ignored by the computer

# hi I'm a comment!
# comments are good for explaining code sections

# the best_sword variable holds the value of the best sword in the video game (the # sign before a statement makes it a comment)
best_sword = "scimitar"
print(best_sword)

my_name = "Trash Puppy" # conventional way of naming a variable in python
my7_name = "Trash Puppy"
# 7my_name = "Trahs Puppy" # will cause the program to error because number at the start
# !my_name = "Trash Puppy" # will cause the program to error because special symbol at the start

# conventional ways to name variables
variablename = 'TP' # this is not a conventional way of naming a variable

variableName = 'TP' # Camel Case where first word is lowercase and then the next words are uppercase first letters (heroHealth)
variable_name = 'TP' # snake_case - this is python's convention (hero_health)
VARIABLE_NAME = 'TP' # SCREAMING SNAKE_CASE - not necessarily a good idea and indicates a constant variable

# String types are just text - called strings because char are individual elements whereas a string of chars is called a string
# a float is a number withb a decimal (5.2 or -5.2)
# a boolean is a data type that can only have one or two values which is True or False (player_has_magic = True)

# another exercise
# Fix the bugs in the code to move on. player_health should be an integer and player_has_magic should be a boolean

player_health = 100
player_has_magic = True

# don't touch below this line
print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")

# F-strings in python
# these allow us to use our variables within strings

# without using f-strings
name = "Trash Puppy"
height = "6ft"
print("My name is " + name + " and I am " + height + " tall!")

# while using f-strings
print(f"My name {name} and I am {height} tall!")

# another exercise
# fix the bug on line 7 - use an f-string to inject the dynamic values into the string:
# 1. replace NAME with the value of the name variable
# 2. replace RACE with the value of the race variable
# 3. replace AGE with the value of the age variable
# do not hard code the values into the string

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line
print("NAME is a RACE who is AGE years old.")
print(f"{name} is a {race} who is {age} years old.") # this is the solution

# Nonetype Variables
# variable holds literally nothing
# if we have a variable that is set early in the code but is only used in specific situations - we sometimes want to check if this variable holds a value or not where nonetype is useful

# Another exercise
# Declare a variable named enemy and set it to None. Don't change the print() function.

# create the "enemey" variable here
enemy = None

# don't touch below this line
print(enemy is None)

# Dynamic Typing
# Python is dynamically typed - the type of the variables can change entirely dependent on what value the variables currently hold
speed = 5 # speed here is a variable of integer type
speed = "five" # speed here then becomes a variable of string type

# in general it is not advisable to change variable types constantly - keep variables to be the same type throughout the code
# Python employs Dynamic Typing - variable type can change throughout the code

# Math With Strings
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line
print(sentence_start + player1_health) # You have 1200
print(sentence_start * 6) # You have You have You have You have You have You have

# Another exercise
# We have a second player in our game!
# We need to tell each of our players how much health they have left.
# Edit line 9 to print Player 1's health: You have 1200 health using string concatenation and the variables provided
# Edit line 10 to print Player 2's health: You have 1100 health in the same way

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

# Multi-Variable Declaration
# More than 1 variable on the left hand side of the assignment sign - values separated by commas
# sword_name, sword_damage, sword_length = "Excalibur", 10, 200
# this is the same as
# sword_name = "Excalibur"
# sword_damage = 10
# sword_length = 200

# clean code is code that is easy for developers to read and understand

