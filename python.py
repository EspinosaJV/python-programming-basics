# ARRAYS IN PYTHON
# An array is basically a data structure that can hold more than one value at a time - collection or ordered series of elements of the same type
# Indexing starts at 0
# Length of array = n, index of array is n - 1
# Ordered series of elements - all elements are present in its particular address and is specified by its index value

# IS PYTHON LIST THE SAME AS AN ARRAY
# Python Arrays & Lists have the same way of storing data
# Arrays can only take a single data type elements
# Lists can have many types of data

# HOW TO CREATE ARRAYS IN PYTHON
# Arrays in python can b4e created after importing the array module

# WITHOUT ALIAS
import array

# USING ALIAS
import array as arr

# USING *
from array import * # imports all that is present in the array module

a = array.array('i', [1, 2, 3, 4, 5, 6]) # creates an array of integer values

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6]) # creates an array of integer values

from array import *
a = array('i', [1, 2, 3, 4, 5, 6]) # creates an array of integer values

# ACCESSING ARRAY ELEMENTS
# make use of index values
# each index value holds a unique element
# indexing starts at 0 - not from 1
# negative indexing also exists - starts from right hand side to left hand side (a[-1] represents the last value)
a[2] # outputs the 3rd element in the array
a[-2] # outputs the 2nd to the last element in the array going from right to left

# BASIC ARRAY OPERATIONS
# ARRAYS ARE MUTABLE - WHICH MEANS THEY CAN BE MODIFIED
# 1. Finding the length of an array
# 2. Adding / Changing element of an array
# 3. Removing / Deleting elements of an array
# 4. Array Concatenation
# 5. Slicing
# 6. Looping through an array

# FINDING THJE LENGTH OF AN ARRAY
# len() - returns the number of elements present in the array
import array as arr
a = arr.array('d', [1.1, 2.1, 3.1])
len(a) # this outputs 3

# ADDING ELEMENTS TO AN ARRAY
# append() - add an element to end of an array
# extend() - add more than one elements to the end of the array
# insert() - add an element to a specific position in the array

import array as arr
a = arr.array('d', [1.1, 2.1, 3.1])
a.append(3.4) # added to end of the array
print("Array a=", a)

b = arr.array('d', [2.1, 3.2, 4.6])
b.extend([4.5, 3.6, 7.2]) # added these elements to the end of the array
print("Array b=", b)

c = arr.array('d', [1.1, 2.1, 3.1])
c.insert(2, 3.4) # index position 2 - value inserted at the position is 3.4
print("Array c=", c)

a = array('i', [1, 2, 3, 4, 5])
a.append(8)
print(a)
a.append(1.2) # this outputs an error because the array is integer but we are trying to add a float value - arrays are not allowed to do this
a.extend([9, 8, 6, 5, 6, 8, 9, 8, 6, 5, 4])
print(a)
a.insert(2, 6)
print(a)

# REMOVING ELEMENTS FROM AN ARRAY
# pop() - removes the element and returns it - removes last element by default
# remove() - removes the element but does not return it

# EXAMPLE
import array as arr
a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7])
print("Popping last element", a.pop()) # removes the last element and then returns it back to the array
print("Popping 4th element", a.pop(3)) # removes the element at index position 3 and then returns it back to the array
a.remove(1.1) # completely removes element 1.1 from the array
print(a)

print(a.pop()) # removes last element present in the array
print(a.pop(-2)) # pops 2nd to the last element in the array
print(a.pop(2)) # pops element at index position 2
print(a.pop(-1)) # pops last element in the array
a.remove(8) # removes the element 8 from the array - remove() function needs specific element

# ARRAY CONCATENATION
import array as arr
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
b = arr.array('d', [3.7, 8.6])
c = arr.array('d')

c = a + b # concatenates or adds the 2 arrays together and then stores it in the empty initialized array c

print("Array c=", c)

b = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
c = arr.array('i', [3, 5, 7, 5, 3, 2, 1])
d = arr.array('i')
d = b + c
print(d)

e = arr.array('d', [3.1, 5.1, 7.1, 5.1, 3.1, 2.1, 1.1])
d = b + e # this outputs an error because the types of both arrays are different and arrays need to have the same type

# SLICING AN ARRAY
# array can be sliced using the : symbol - returns a range of elements that we have specified using index numbers
import array as arr
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
print(a[0:3]) # this outputs the first index to the value at index position 2 - the last parameter is EXCLUSIVE

d = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 3, 4, 2, 1, 3, 5, 6, 7, 8])
print(d[0:5]) # outputs elements from array d wherein the elements are from index position 0 to 4
print(d[0:-2]) # outputs elements from array d wherein the elements are from index position 0 to 3rd to last element in the array
print(d[::-1]) # outputs a reversed copy of the array

# LOOPING THROUGH AN ARRAY
# we can loop through an array using for & while loops
# for iterates over the items of an array specified number of times
# while iterates over the elements until a certain condition is met - stopping the loop

# EXAMPLE
import array as arr
a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7])
print("All values")
for x in a:
    print(x)

d = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 3, 4, 2, 1, 3, 5, 6, 7, 8])

for x in d:
    print(x)

for x in d[0:-3]: #outputs only the vcalues at index position 0 to index position 4th to the last element
    print(x)

# While Loop implementation
import array as arr
a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7])
b = 0

while b < len(a):
    print(a[b])
    b = b + 1

temp = 0
while temp < d[2]: # condition is that the value for iterator temp needs to be less than value at d[2]
    print(d[temp])
    temp = temp + 1

temp = 0
while temp < len(a): # runs through all elements in the array
    print(a[temp])
    temp = temp + 1

# An array is basically a data structure which can hold more than one value at a time