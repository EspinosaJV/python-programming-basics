## CHAPTER 10 - DICTIONARIES
# another data structure for Python
# saves data in a key-value pair instead of it just being a single item

# POTIONS DICTIONARY
# dictionaries are a good way to save data with varying properties
# dictionary values can be of any data type
potion = {
    "name" : "Potion of Spell Power", # "name" is a key which is mapped to its value of "Potion of Spell Power"
    "stat buff" : "Spell Critical",
    "multiplier" : 0.25,
    "resource pool" : ("magika",),
    "resource increase" : [500],
    "other effects" : None,
    "zone drop": "Vvardenfell"
}

stat_buff = potion['staff buff'] # access a dictionary and get a specific value out of it
print(f"Stat buff: {stat_buff}")


# CHANGE ME:
# potion = potion

print(f"You've taken a {potion['name']}...")

print(f"Your {potion['stat buff']} has increased by {100 * potion['multiplier']}% !")

def get_character_record(name, server, level, rank):
    record = {
        'name' : name,
        'server' : server,
        'level' : level,
        'rank' : rank,
        'id' : f"{name}#{server}",
    }

    return record

## SETTING DICTIONARY VALUES
potion['zone drop'] = 'Northern Elsweyr' # zone drop does not exist - what it does is make a new key which is zopne drop and its value which is Northern Elsweyr

print(f"This potion only drops in {potion['zone_drop']}")

# syntax for dictionary is dict[key] = value # creates a new key value pair in dict
# if you assign a new value to an existing key - the value updates for that specific key

## DELETING DICTIONARY VALUES
del potion['zone drop']

print(potion) # zone drop key value pair is now dropped as it has been deleted

# If you try to del a key that doesn't exist in the dictionary - it will cause an error

## CHECKING IF A SPECIFIC KEY EXISTS IN THE DICTIONARY
is_in = 'stat buff' in potion # this will result to a True or False stored in the is_in variable
print(is_in)

# if using the in keyword - wwe can only check if the key exists in the dictionary

# Assignment
def count_enemies(enemy_names):
    counts = {}

    for enemy in enemy_names:
        if enemy in counts:
            counts[enemy] += 1
        else:
            counts[enemy] = 1

    return counts

## ITERATING OVER A DICTIONARY
# List
player_inventory = ["200 Gold", "Iron Breastplate", "Potion of Healing"]

# Iteration syntax:
for item in player_inventory:
    print(f"Item: {item}")

# Dictionary
# Iteration syntax:
for key in potion:
    print(f"Key: {key}")

## Assignment
# Iterating over a dictionary in Python

def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return 
    
    most_common_enemy = float('-inf') # this is going to create the value negative infinity and saves it to the variable

    for enemy in enemies_dict:
        enemy_occurences = enemies_dict[enemy]

        if enemy_occurences > most_common_enemy:
            most_common_enemy = enemy_occurences
            name = enemy


    return name

## ORDERED AND UNORDERED
# Before Python 3.7 - dictionaries were unordered - which meant that you could initialize a dictionary with a specific order but if you iterate over it, the order of the key value pairs would be different
# After Python 3.7 - dictionaries are now ordered - whatever ordered they are declared in - it will retain that order

