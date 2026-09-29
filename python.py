## CHAPTER 9 - LISTS
# A list is just a list of items

# Assignment
# Let's work on Fantasy Quest's inventory! We can store items the player is carrying in a list!
# Fix our get_inventory function by adding Shortsword to the end of the list.

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]

# Lists continued
# You can put list items in their own lines so that the list can be more readable
player_inventory = [
    "200 Gold",
    "Iron Breastplate",
    "Potion of Healing",
    "Shield"
]

# We can store multiple types of values in a list
# If you use an array however and put different values - this cannot be possible.
# Counting in Programming

player_inventory = ["200 Gold", "Iron Breastplate", "Potion of Healing", "Shield"]
player_gold = player_inventory[0]

print(f"Inventory: {player_inventory}")
print(f"Gold: {player_gold}")

# Assignment
# We need to allow our players to access items in their inventories! Fix our get_leather_scraps function by changing the value of item_index to the index in inventory that holds the value "Leather Scraps"

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmt",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]

# Assignment
# Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.
# Complete the get_last_index function so that it returns the length of the inventory list minus 1

def get_last_index(inventory):
    length = len(inventory) # returns the number of items in the inventory list
    longsword = inventory[length - 1]
    print(f"Length: {length}")
    print(f"Index 3: {longsword}")

# when it comes to updating a value in a list:
player_inventory[0] = "150 Gold" # updates the value at position 0 of the player_inventory list to instead be 150 Gold

# Assignment
# We need to update the items in our players' inventory whenever they smelt Iron Ore into an Iron Bar!
# On line 7, update the Iron Ore element in the list to be an Iron Bar.

def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Breastplate", "Shortsword"]
    print(f"Inventory: {inventory}")

    inventory[1] = "Iron Bar"

# Append method
player_inventory.append("Ring of Power") # method - a function that is attached to the list data structure type - append methods adds Ring of Power to player inventory list

# Assignment
# We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.
# Let's finish the generate_user_list function. In the body of the loop, use the incrementing value i as unique IDs and append them to the player_ids list.

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# Pop Method
# Built-in in python but instead of adding a value to the end of the list - it pops a value off the list (last value in the list)
player_inventory = ["200 Gold", "Iron Breastplate", "Potion of Healing", "Shield"]

last_item = player_inventory.pop()

print(f"Inventory: {player_inventory}")
print(f"Popped value: {last_item}")

# Assignment
# Our player is selling the items in their inventory to the shopkeep!
# Pop the last element from the inventory list until there is nothing left. Pop the elements into an item variable so that each prints in turn on line 19.


for i in range(0, len(inventory)):
    item = inventory.pop()

# Counting the items in a list
# Assignment
# Our players need a way to see how many copies of a specific item they have within thbeir inventory!
# Let's finish the get_item_counts function. Within the loop, check if the items are a Potion, Bread, or SHortsword, then add up how many there are of each by incrementing the potion-count, bread_Count, and shortsword_count variables respectively

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    for i in range(0, len(items)):
        current_item = items[1]

        if current_item == "Potion":
            potion_count += 1
        elif current_item == "Bread":
            bread_count += 1
        elif current_item == "Shortsword":
            shortsword_count += 1
        else:
            print("This item is not something we care about")

    return potion_count, bread_count, shortsword_count

player_inventory = ["200 Gold", "Iron Breastplate", "Potion of Healing", "Shield"]

for i in range(0, len(player_inventory)):
    print(f"Current item: {player_inventory[i]}")

# other way

for item in player_inventory:
    print(f"Current item: {item}")

# No-Index Syntax
# We can use the no index syntax if we dont need to know the syntax itself

# Assignment
# Find an Item in a List
# We need to check if a player has a specific item under in their inventory. In thee contians_leather_scraps function, use the no index syntax to itrrerate over each item in items. If you find an item colled Leeahter scraps, set the found variable to True

 def contains_leather_scraps(items):
    found = False

    for item in items:
        if item == "Leather scraps":
            found = True

# Assignment

for i in range(0, len(old_character_levels)):
    old_level = old_character_levels[i]
    new_level = new_characteer_levels[i]

    if old_level < new_level:
        print(i)
    else:
        print("The player did not level up")

# Assignment
# Our players want a way to see their strongest attack from their last combat. Let's add another function to analyze data from our combat log.
# Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found, it just returns negative infinity

def find_max(nums):
    max_so_far = float("-inf")

    for num in nums:
        if num > max_so_far:
            max_so_far = num

    return max_so_far

# Modulo operator
numbers = [54, 21, 2, 5, 117, 298, 299, 10, 43, 11, 8]
total = 0

print(6 % 2) # modulo is kinda like dividing but gives us the remainder of te division

for num in numbers:
    remainder = num % 2

    if remainder != 0:
        total += num
    else:
        print(f"{num} is even")

# Assignment
# Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        remainder = i % 2
        if remainder != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers

## SLICING LISTS
# We take a list and make a new list which creates a new list from the specific values from the old list

def get_champion_slices(champions):
    # my_list[ start : stop : step ]
    sublist_1 = champions[3:] # starts from the 3rd element and goes all the way to the end of the list
    sublist_2 = champions[:-2] # starts at the beginning of the list and ends with the third champion from the end
    sublist_3 = champions[::2]

    return sublist_1, sublist_2, sublist_3

## LIST OPERATIONS
# CONCATENATION

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    s1 = 'Trash '
    s2 = 'Puppy'

    print(s1 + s2)

    # taking 2 strings and combining them together

# ASSIGNMENT
# Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different parameters - the player's favorite_weapons, favorite_armor, and favorite_items.
# Create a new list that combines favorite_weapons, favorite_armor, and favorite_items in this order.
# Return the list containing the combined favorites.

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    mega_list = favorite_weapons + favorite_armor + favorite_items # items in both lists are in new lists

    return mega_list

## LIST DELETION

# ASSIGNMENT
# In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:
# Delete the first stronghold from the list
# Delete the last two strongholds from the list
# Return the new trimmed-down list

def trim_strongholds(strongholds):
    del strongholds[0] # deletes the first stronghold
    del strongholds[-2:] # deletes the last two items in the strongholds list
    del strongholds[0:5] # deletes the first 4 items in the strongholds list
    del strongholds[0:5:2] # deletes items from 1 to 4 items but in steps of 2
    return strongholds

## TUPLES
# Another data struct in python similar to list but have important differences
# Lists are mutable, Tuples are immutable
# Mutable - can be changed, Immutable - cannot be changed
# Tuples are used for small collections of items and we know they are going to be staying the same
# We want to keep same types of data in lists (although we can put different types of data ina  lsit)
# Tuples can store different types of data

tup = (2, "Puppies", True, 11.6)

for i in range(0, len(tup)):
    # Try to change item
    current_item = tup[i]

    print(f"Current Item: {current_item}")

tup.append("add_me!") # tuples do not have the built in append method because tuples are immutable - this will not work
del tup[1] # tuples cannot also be deleted from - this will not work
tup[1] = 'Kitties' # tuples cannot also be changed even in the element-level

# Tuples Assignment
# The "Fantasy Quest" character system needs a list of "heroes" to be able to run the game properly. Someone wrote some pretty nasty code, and the code in question creates a "heroes" list where every 3rd index defines a new hero. First their name, then their age, then whether or not they're an "elf".
# Change the heroes list declaration from its current state to a list of tuples. Use the same data for each hero, and order it in the same way

def get_heroes():
    heroes = [("Glorfindel", 2093, True), ("Gandalf", 1054, False), ("Gimli", 389, False), ("Aragorn", 87, False)]

    return heroes

# Assignment
# Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then retuirn the string ERROR instead

def get_first_item(items):
    if len(items) > 0:
        return items[0]
    else:
        return 'ERROR'

# Assignment
# Some of our players would like to view their inventories in reverse order.
# Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

# Method #1: Ranged for loop method
def reverse_array(items):
    reversed = []
    for i in range(len(items) - 1, -1, -1): # start at the last index into our list, ending value is -1 because it is exclusive so we want element at index 0 so -1, and then -1 step so that it goes downwards or backwards
        item = items[i]
        reversed.append(item)

    return reversed

# Method #2: Slicing method
def reverse_array(items):
    reversed = items[len(items) - 1::-1]

    return reversed

# Assignment
# We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:
# 1. A list of the same messages but with all instances of the word "dang" removed
# 2. A list containing the number of "dang" words

messages = ["dang it bobby!", "look at it go"]

first_msg = messages[0]
print(f" First msg: {first_msg}")

split = first_msg.split() # turns the message into a list of individaul elements (the words)
print(f"Split: {split}")

first_word = split[0]
print(f"First Word {first_word}")

def filter_messages(messages):
    dang_occurrences = []
    filtered_msgs = []
    dang_counter = 0

    # Loop through each messages in the messages list:
    for current_msg in messages:
        filtered_words = []
        dang_counter = 0
        # print(f"Current Msg: {current_msg}")

        # Loop through each word in the current_msg
        for word in current_msg.split():
            # print(f"Current Word: {word}")
            if word == 'dang':
                dang_counter += 1
            else:
                filtered_words.append(word)

        filtered_msgs.append(" ".join(filtered_words))
        dang_occurrences.append(dang_counter)

    return filtered_msgs, dang_occurences