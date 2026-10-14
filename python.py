# HOW TO IMPLEMENT A PYTHON STACK

# Stack is a data structure storing items in a Last-In / First-Out manner LIFO
# POPPING IS WHEN YOU UNDO FOR EXAMPLE ANM ADDITION INTO THE STACK - IN THIS CASE - THE ITEM IS REMOVED FROPM THE STACK

# USING A LIST TO CREATE A PYTHON STACK

myStack = []
myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

myStack.pop()
# this outputs c
myStack.pop()
# this outputs b
myStack.pop()
# this outputs a

# it can run into speed issues as it grows
# if you use .insert() to add an element to the stack at a position other than the end, it can take much longer
# if the stack grows bigger than the block of memory currently holding it - Python will have to do some memory allocations which can lead to .append() calls taking much longer than other ones 

# USING collections.deque TO CREATE A PYTHON STACK
# deque is pronounced deck and stands for double-ended queue

from collections import deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

myStack.pop() # this outputs c
myStack.pop() # this outputs b
myStack.pop() # this outputs a

# this is identical to using the list to make this data structure

# difference between a deque and a list is that the list is a contiguous memory block - meaning slots have to be side by side and if the stack has to grow, there needs to be a memory reallocation - compared to deque which is a doubly linked list where each slot contains a reference to the next slot but does not have to be contiguous
# problem is however, indexing is longer for a deque because we have to traverse to the different references whereas for a list - they are side by side and the python function already knows that directly, the 3rd index contains its corresponding value for example

# PYTHON STACKS AND THREADING

# LIST IS NOT THREAD SAFE
# For Deques however, the .append() and the .pop() operations are atomic meaning they wont be interrupted by a different thread - so only limiting yourself to these functions, you will be thread safe

# so if we cannot use lists & deques for stacks in a thread program, what do we use? we use the queue.LifoQueue from the Queue module

from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')
myStack.put('b')
myStack.put('c')

print(myStack) # this will output a reference to the memory address of the LifoQueue object

myStack.get() # this outputs c
myStack.get() # this outputs b
myStack.get() # this outputs a

# LifoQueue is designed to be fully thread safe - all of its methods are safe to use in a threaded environment
# LifoQueue however, for the sake of it being thread safe, its operations will take a little longer

# PYTHON STACKS WHICH IMPLEMENTATION SHOULD YOU USE
# Deque - if not threading
# LifoQueue - if threading, but if the performance is confirmed to REALLY be the issue, swap to Deque

# lists are familiar - but can cause memory reallocation issues

# CONCLUSION
