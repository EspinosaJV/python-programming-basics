# HEAP
# tree-based data structure in which the value of a parent node is ordered in a certain way in respect to the value of its child node, if its a min heap - the value of the parent node is less than or equal to the value of its children, whereas for max heap the value of the parent node is greater than or equal to the value of its children

# STACK
# operations are performed LIFO (last in first out) - last element in is the first one removed, stack can also be implemented using an array or a linked list - if a stack runs out of memory, it is called a stack overflow

# QUEUE
# operations are performed in FIFO (first in first out) - queue can be implemented using an array

# WHAT ARE HEAPS
# min heap is for storing objects with a partial order - fast method for removing the minimum object from the heap and are useful for calculations where you have multiple minimum computations to perform
# heaps can only be either min heap or max heap
# heaps are known also as priority queues and are technically one implementation of priority queues

# In heaps, keys are the values that determine the order - if storing numbers these can be the keys and if storing more complicated objects, key is the data field we are comparing by, keys in heaps do not have to be unique
# extract_min is the method of quickly being able to extract the minimum element from the min heap

# min heap is able to quickly extract the minimum value in a heap and repeated extractions from a min heap into an array can result into a sorted array

# its weakness however is that there is no convenient way of searching for a particular key value ikn a heap

# HEAPS ARE FOR MINIMUM OR MAXIMUM EXTRACTIONS 
    # - Finding the minimum distance between 2 nodes in a graph
    # - Getting the next event that is scheduled to occur
    # - Keep track of the median value while streaming
    # - Find the first k non-repeating characters in a string in a single traversal

# COMMON HEAP OPERATIONS
# insert(key) operation - inserts key into a heap and can modify to have a key / value pair, time complexity is O(log n) and can mutate the structure
# extract_min() - returns and removes item with minimum key from the heap, time complexity is O(log n) and can also mutate the structure
# peek_min() - can view the minimum key but does not remove it from the heap, time complexity is O(1) and does not mutate the structure
# heapify(list) - creates a new heap from a list of n items - functionally equivalent to starting with an empty heap and inserting elements one at a time - has a better run time than the O(n log n) of this approach - time complexity is O(n) and it creates a new heap

# STACKS & QUEUES
# both designed to hold elements and return in a specific order - only difference is the order in which items are retrieved

# STACKS ARE FIRST IN, LAST OUT AND LAST IN, FIRST OUT
# QUEUES ARE FIRST IN, FIRST OUT

# BOTH ARE ABSTRACT DATA TYPES - guaranteed to be able to put elements in and remove them in the specified order

# BOTH HAVE AN ADD OPERATION (push / enqueue) and a remove operation (pop / dequeue)

# push is adding object to top of stack
# pop is removing object from top of stack
# enqueue is adding object to the back of the queue
# dequeue is removing object from the front of the queue

# COMMON OPERATIONS CHEAT SHEET
# push(item) - pushes item on the top of the stack, time complexity of O(1) and mutates the structure
# pop() - removes the most recently added item from the stack with a time complexity of O(1) and also mutates the structure
# peek() - accesses the most recently added item in the stack without removing it - O(1) time complexity and does not mutate the structure
# isEmpty() - returns True if there are no items in the stack, False otherwise, time complexity of O(1) and does not mutate the structure

# COMMON OPERATIONS BUT FOR QUEUES CHEAT SHEET
# enqueue(item) - puts item at the end of the queue
# dequeue() - removes the item at the front of the queue which mutates the structure of the dict
# peek() - accesses the item at the front of the queue without removing it - does not mutate the structure of the dict
# isEmpty() - returns true if no item in the queue, false otherwise - does not mutate the structure

# all of the common operations for queue have a time complexity of O(1)
