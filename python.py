## SETS
# Another data structure in Python a lot like sets
# Sets can only hold 1 of each item - meaning all items in the set needs to be unique
# We use sets to check if a value is in a set - deduplication - and really fast lookup

my_set = {'Potion of Healing', '200 Gold', 'Bronze Sword'}
my_set2 = {} # Python will treat this as an empty dictionary
my_set3 = set() # Proper way to initialize an empty set

my_set.add('500 arrows') # adds the 500 arrows element into the my_set set

print(f"The following items are in your inventory: {my_set}")

# finding a value in a set is a lot faster & more efficient than finding a value in a list in Python

# in a list - finding a value is slow because we have to look into every element individually to see if the element matches what we are looking for
# in a set - finding a value is faster because Python puts the value through an equation and the result tells Python the address in memory already

## Iterating over a set

for item in my_set:
    print(f"Current item: {item}")

## Assignment
# Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this by creating a set, adding all the spells to it, then iterating over the set and adding all the spells back into a list and returning the list.
# It makes no sense to learn a spell twice! Once it's learned, it's learned forever.

def remove_duplicates(spells):
    unique_spells = set(spells)
    new_list = []

    for spell in unique_spells:
        new_list.append(spell)

    return new_list

## Removing Items from a Set

my_set.remove('200 Gold')

print(f"The following items are in your inventory: {my_set}")
