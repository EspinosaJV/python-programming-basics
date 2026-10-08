# LINKED LISTS
# linear data structure that is an approach to data organization using a sequence of items called nodes
# each node has a specific data value as well as a reference or pointer to the next node in the chain

# LINKED LISTS VS LISTS
# Regular lists use contiguous array in memory (slots are side by side) providing fast & simple access to elements through an index position
# but because of this, there needs to be a block of continuous memory for the list - in the case of modifications, list resizing happens which affects performance
# This only happens occassioanlly however as Python overallocates memory for lists for this reason

# Linked Lists use nodes linked with pointers making them unsuitable for random access

# INDIVIDUAL NODES
# single element in the linked list containing its own data and a reference to the next node in the sequence

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # reference to the next node in the chain, initialized as None until a link is established to another Node

head = Node(100) # head is the first node in the linked list
second_node = Node(200) # the next node after the head

head.next = second_node # making it so that the address pointer stored in the head points to the second node address

# INITIALIZING AN EMPTY LIST

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        # Set as head if empty list
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        # Traverse linked list looking for the tail node
        while current.next is not None:
            current = current.next

        # Append new_node at the end of the list
        current.next = new_node

linked_list = LinkedList() # starts an empty linmked list
print(linked_list.head)
# Expected result is None

# ADDING NEW NODES
# create a method called append() to add nodes to the end of the linked list
# accept a new value, create a new node, and add to the end of the list

linked_list.append(100)
linked_list.append(200)
linked_list.append(300)

# TRAVERSING THE LINKED LIST
# the traverse() method prints each list value starting from the head and continually moving to the next node until it reaches the end of the list

def traverse(self):
    current = self.head

    while current is not None: # Continue through the tail node
        print(current.data)
        current = current.next

linked_list.traverse()

# Expected result
# 100
# 200
# 300

# SEARCHING FOR A NODE
# search() method begins at the head of the list and compares each nodes value to the input - returning the first node where the data matches or None if it cannot find a value

def search(self, value):
    current = self.head

    while current is not None:
        if current.data == value:
            return current

        current = current.next

    return None

my_node = linked_list.search(200)

print(my_node.data)

# Expected result:
# 200

# REMOVING NODES
# this skips over the targett node and connects the previous node to the next node - eliminates the first node matching the input value and if no nodes match, it instead raises a ValueError

def remove(self, value):
    # Raise error if list is empty
    if self.head is None:
        raise ValueError(f"{value} not found in linked list")

    # Handle removing the head as a special case
    if self.head.data == value:
        self.head = self.head.next
        return

    current = self.head

    # Lookf or value, connect around it if found
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            return

        current = current.next # Move on if value doesn't match

    # Raise error if value not found
    raise ValueError(f"{value} not found in linked list")

linked_list.remove(200)
linked_list.traverse()

# Expected result:
# 100
# 300

# DOUBLY LINKED LISTS
# two references per node - the next node and the previous node is referenced in the current node
# linked list can be progressed in a forward and backward direction

# here is how Python class Node changes for a doubly linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None #  points to the previous node in the linked list, helping move through the list backwards
        self.next = None

head = Node(100)
second = Node(200)

head.next = second # the next pointed node for the head is the 2nd node
second.prev = head # the previously pointed node for the second node is the head node

# LinkedList class also changes - in addition to tracking the head, it now also has a tail reference serving as a starting point for backwrd traversal starting with the tail

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# append() - set next for the old tail and prev for the new node at the tail
# traverse() adds an option to follow the list forward or backward
# search() adds an option to search starting from the front or back of the list
# remove() update the next and prev references of the neighboring nodes

# CIRCULAR LINKED LISTS
# tail of the list points back to the head instead of pointing to None
# can think of the linked list variation as a loop - can be singly or doubly linked as well

# Node class follows the same structure as singly or doubly - just make sure that the tail node points backt o the head node of the linked list

head = Node(100)
second = Node(200)
third = Node(300)

head.next = second
second.next = third
third.next = head # tail points back to head, forming the circular linked list

# LinkedList constructor stays the same but traversal changes because nthere is no None anymore - meaning stopping condition neds to be changed

def traverse(self):
    # Detect empty list
    if self.head is None:
        return

    current = self.head

    while True:
        print(current.data)
        current = current.next

        # Stop when reaching head once more
        if current == self.head:
            break

circular_linked_list = LinkedList()
circular_linked_list.head = head

circular_linked_list.traverse()
# Expected resukt:
# 100
# 200
# 300

# append() should look for a node that points back to herad rather than pointing to none

# INTERVIEW QUESTIONS
# HOW DO YOU REVERSE A LINKED LIST?
# make it so that the next address pointed to by a node is the one before or the previous node instead
def reverse(self):
    previous = None
    current = self.head

    while current is not None: # continue through tail node
        next_node = current.next
        current.next = previous # switch reference to previous
        previous = current
        current = next_node

    self.head = previous

# HOW DO YOU DETECT A CYCLE IN A LINKED LIST
# the key to this question is Floy'd cycle detection algorithm
# you can detect a cycle using two pointers, slow which advances only one node per iteration, and fast which advances two nodes per iteration
# is fast reaches the end of the list, your linked list does not have a cycle but if both the slow and the fast eventually reference the same node, there is a cycle

def has_cycle(self):
    slow = self.head
    fast = self.head

    # Continue while fast can advance
    while fast is not None and fast.next is not None:
        slow = slow.next # Advance one node
        fast = fast.next.next # Advance two nodes

        # Cycle detected is slow and fast meet
        if slow == fast:
            return True

    return False # no cycle if fast reaches the end of thbe list

# HOW DO YOU FIND THE MIDDLE OF A LINKED LIST?
# you can still leverage the same slow & fast pointers technique where slow advances one node per iteration, and fast advances two nodes per iteration,
# when fast reaches end of the list, slow is already in the middle

def find_middle(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow gives you the midpoint when fast reaches the end
    return slow

