## Chapter 4 - Scope
# Scope is the context that a variable or a function belongs to
# everything that is defined or created in thbe program has its own scope

# example code from the lesson

# THIS IS THE PARENT SCOPE
movie = "Reservoir Dogs"
color = "blonde"

def start_movie():
    # This is the start_movie scope
    a = get_actor()
    message = f"The movie {movie} is starting... Starring {a}"

    return message

def get_actor():
    # This is the get_actor scope
    if cn == "Mr. Blonde":
        actor = "Michael Madsen"

    if cn == "Mr. Pink":
        actor = "Steve Buscemi"

    return actor

def get_codename():
    if color == "blonde":
        codename = "Mr. Blonde"

    if color == "pink":
        codename = "Mr. Pink"

    return codename

cn = get_codename()
m = start_movie()
print(m)

# Another Exercise
# Find the bug in the code on line 10. We're using variable names from the wrong scope. Fix it!

def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

# Global Scope
# the parent or the entire program - the scope of it - available everywhere throughout the program

# ?
player_level = 4

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

# Don't touch below this line

print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

# functions can always access variables defined in the global scope
# code cannot access variables from outside of a function when they are defined inside of it