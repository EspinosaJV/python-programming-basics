# HASH TABKE
# a dictionary is an abstract data type made up of keys and values arranged in pairs (add a key value pair, delete a key value pair, update a key value pair, find a value associated with the given key)
# dictionaries are also known as maps or associative arrays - you're mapping or associating a value to a key
# dictionaries need to have key-value pairs where a key is mapped to a value and vice versa
# dictionaries can have arbitrary keys and values where these can belong to two disjoint sets of the same or separate types
# dictionaries have unordered key-value pairs
# dictionaries can only have unique keys and cannot contain duplicate keys
# in dictionaries, the same value can be associated with many keys but it doesn't have to.

# EXAMPLE
glossary = {"BDFL": "Benevolent Dictator for Life"}
glossary["GIL"] = "Global Interpreter Lock" # Add
glossary["BDFL"] = "Guido Van Rossum" # Update
del glossary["GIL"] # Delete
glossary["BDFL"] # Search
print(glossary)

# HASH TABLE IOS AN ARRAY WITH A HASH FUNCTION

import string
text = string.ascii_uppercase * 100_000_000

text[:50] # Show the first 50 characters
# outputs the firsst 50 characters

print(len(text)) # prints the length of the text itself
print(text[0]) # the first element
print(text[len(text) // 2]) # the middle element
print(text[-1]) # the last element

# sequences in Python are backed by an array which is a random-access data structure - follows 2 principles
# The array occupies a contiguous block of memory
# Every element in the array has a fixed size known up front

# formula is element_address = offset + (element_size x element_index)
# this is the formula to calculate the memory address of a sequence element

# hashing is the process of translating an arbitrary key into an integer number that can work as an index in a regular array
# hash function performs hashing by turning any data into a fixed size sequence of bytes called the hash value or the hash code - acts as a digital fingerprint or a digest that is much smaller than the original data - verifying its integrity
# hash functions also help in security and crptography
# crptographic hash function is another type of hash function that must meet a few additional requirements 

hash(3.14)
hash(3.1415179)
hash("Lorem")

# the hash function always returns the same hash value for a given input, so if you were to hash lorem multipel times - the output of the hashf unction is always the same
# hash values are immutable and do not change throughout an object's lifetime
# the hash function in Python is deterministic - one of the most fundamental features of the hash function
# the hash function takes values of various types and sizes
# When it comes to Python, instances of built-in mutable types like lists, sets, and dicts - are NOT hashable'
# Most data types however should work with a hash function in general
# The hash function always produces a fixed size output no matter how big the input is
# Pigeonhole principle - if m represents the number of items whereas n represents the number of containers, if there are more items than containers then there is bound to be an event where a container can contain more than one item

# hash_distribution.py sample code
from collections import Counter

def distribute(items, num_containers, hash_function = hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'x' * count}{padding} ({count})")


# the uniform distribution of hash values is typically pseudo-random - especially important for cryptographic hash functions
    # this prevents potential attackers from using statistical analysis to try & predict correlation between input and output of hash function

# CPython - when hash values of small integers are hashed - they are equal to themselves which is implemented for simplicity and efficiency
# Hash value calculation is very fast even if the size of the input is very big 
    # For example, calling the hash() on a string with 100 million characters still returns instantaneously

# A regular hash function is deterministic with a universal input, fixed size output, fast to compute, and uniformly distributed
# A cryptographic hash function not only provides the features of a regular hash function but is also randomly distributed, randomized seed, a one way function that also implements the avalanche effect (a small input change can still amplify the hash value output)

# when you use the id() call on a value, it tells you the object's identity which is basically the same as the object's memory address expressed as an integer

def hash_function(text):
    return sum(ord(character) for character in text)

def hash_function(key):
    return sum(ord(character) for character in str(key))

