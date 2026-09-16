strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len)) # ['d', 'bb', 'ccc', 'aaaa']

## "key" argument specifying str.lower function to use for sorting
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs, key=str.lower)) ## ['aa', 'BB', 'CC', 'zz']

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd', 'wa']

## Write a little function that takes a string, and returns its last letter
## This will be the key function (takes in 1 value, returns 1 value).
def myFn(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=myFn)) ## ['wa', 'zb', 'xc', 'yd']

from operator import itemgetter
# (first name, last name, score) tuples
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
print(sorted(grade, key=itemgetter(1,0)))
# [('Anil', 'Frank', 100), ('Freddy', 'Frank', 3), ('Anil', 'Wang', 24)]

print(sorted(grade, key=itemgetter(0, -1)))
# [('Anil', 'Wang', 24), ('Anil', 'Frank', 100), ('Freddy', 'Frank', 3)]

# sort() method
# alist.sort() ## correct
# alist = blist.sort() ## incorrect - sort() function returns None
# sort() does not work on any enumerable collection but sorted() works on anything

# Tuples
# fixed size grouping of elements
# immutable and do not change size

tuple = (1, 2, 'hi')
print(len(tuple)) ## 3
print(tuple[2]) ## hi
tuple[2] = 'bye' ## NO, tuples are immutable which means they cannot be modified
tuple = (1, 2, 'bye') ## this works

# size 1 tuple
tuple = ('hi',) ##size-1 tuple

(x, y, z) = (42, 13, "hike")
print(z) ## hike
# (err_string, err_code) = Foo() ## Foo() returns a lenth-2 tuple

# List Comprehensions
# Compact way to write an expression that expands to a whole list

nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ] ## [1, 4, 9, 16]
# iterates over the nums variable
# each element in nums is used as the value for n in the iterator
# n is multipled by itself in the expression
# appended into the squares variable list

strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
# for each element in strs
# they get put into iterator variable s 
# the element of iterator variable s is then uppercased and then concatenated with !!!
# element is then appended into the shouting variable inside of a list

## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ] ## [2, 1]
## iterates over the nums variable containing a list
## each element in the list first undergoes the condition check of the if statement
## if element passes condition check, is appended to the list contained within the small variable

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
## iterates over each element of the list contained within the fruits variable
## applies the if condition wherein if the element contains an 'a' character, it is then uppercased and appended into the list contained within the afruits variable
## ['APPLE', 'BANANA']