# Python Dict and Files

# Dict Hash Table
# Dictionary is a key/value hash table structrure
# {} = empty dictionary
# keys can only be strings, numbers and tuples whereas values can be anything

## Can build up a dictionary by starting with the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value for that specific key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict) ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(dict['a']) ## Simple lookup, returns 'alpha'
dict['a'] = 6 ## put new key/value into dict
'a' in dict ## True because 'a' is a key in dict
## print(dict['z']) ## will not work because z is not a valid or existing key in dict
if 'z' in dict: print(dict['z']) # checks if 'z' is a character stored in the dict dict, if it does it is then going to print its corresponding value
print(dict.get('z')) # uses the .get function wherein because z is not a valid value, outputs None instead of KeyError from normal dict['z']

## By default, iterating over a dict iterates over its keys.
## Note that the keys are always in a random order.
for key in dict:
    print(key)
## prints a g o

## Exactly the same as above
for key in dict.keys():
    print(key)

## Get the .keys() list:
    print(dict.keys()) ## dict_keys(['a', 'o', 'g'])

## Likewise, there's a .values() list of values
    print(dict.values()) ## dict_values(['alpha', 'omega', 'gamma'])

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items()) ## dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)
# we call on .items() function for dict variable, giving us a list of tuple values
# each tuple value is then iterated whereint he first element is unpacked into k, second element is unpacked into v
# for each iteration, we then print k > v
## a > alpha o > omega g > gamma

## Dict Formatting
# % operator substitutes values from a dict into a string by name:

h = {}
h['word'] = 'garfield'
h['count'] = 42
s = 'I want %(count)d copies of %(word)s' % h # %d for int, %s for string
# 'I want 42 copies of garfield'

# You can also use str.format()
s = 'I want {count:d} copies of {word}'.format(h)

## Del
# handles deletions

var = 6
del var # var no more, does not longer exist

list = ['a', 'b', 'c', 'd']
del list[0] ## Deletes first element
del list[-2:] ## Deletes third and fourth element or the last 2 elements
print(list) ## ['b'] applies changes to the actual original list itself

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b'] ## Deletes 'b' entry, deleting both itself as the key and its corresponding value
print(dict) ## {'a':1, 'c': 3}

## Files
# open() function that opens and returns a file handle
# 'r' for reading (only outputs), 'w' for writing (make modifications), 'a' for appending (only add but not remove), 'rt' for read text

# Echo the contents of a text file
f = open('foo.txt', 'rt', encoding='utf-8')
# opens the foo.txt file in read text mode with utf-8 encoding
# file is then stored into the f variable as its handle
for line in f:
    print(line, end='')

f.close()

# we iterate over each line in the foo.txt file through its f handle
# every line is then printed and with end='' means there is no end of line character as the line itself already contains an end of line (single spacing only prevents double spacing)

## if you use .readlines() method - reads whole file into a list
## .read() reads the whole file into a single string
## f.write(string) - easiest way to write data to an open output file

## Files Unicode
with open('foo.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        # here line is a *unicode* string

with open('write_test', encoding='utf-8', mode='wt') as f:
    f.write('\u20ACunicode\u20AC\n') # unicode
    # AKA prtint 

    