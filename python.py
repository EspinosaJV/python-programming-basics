numbers = [2, 5, 8, 12, 13, 17, 20, 23, 26]
target = 13

# Step 1 - Algorithm will look at index position 4 and see if the value mathces the target which it does (13 for 13) - search stops and returns the index position of the matched value

# What if target is 17?

target = 17

# Step 1 - Algorithm will look at index position 4, determines it is not a match, then also determines that the target is greater than the middle value therefore look at right half and ignore left half
# Step 2 - Now it looks at [17, 20, 23, 26] which is 0, 1, 2, 3, and will look at index position 1 which returns 20 which is still not the target, but determines that it is less than the middle value so new half to look at is just [17,]
# Step 3 - Matches with only value in the last remaining half - returns index position which is 5

def binary_search_recursive(arr, target, left=0, right=None):

    if right is None:
        right = len(arr) - 1
    if left > right:
        return - 1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = binary_search_recursive(numbers, 8)
print(f"Found at index: {result}") # Output: Found at index: 3

# Iterative Binary Search (using a while loop)

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search_iterative(numbers, 13)
print(f"Found at index: {result}") # Output: Found at index: 6

# Using Python's built-in bisect module

import bisect

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Find the insertion point for your value
pos = bisect.bisect_left(numbers, 40)
print(f"Position: {pos}") # Output: Position: 3

# Check if the element exists
target = 40
pos = bisect.bisect_left(numbers, target)
if pos < len(numbers) and numbers[pos] == target:
    print(f"Found {target} at index {pos}")
else:
    print(f"{target} not found")

# Insert while maintaining sorted order
bisect.insort(numbers, 41)
print(numbers)

import bisect

# Streaming service movie library (sorted)

available_movies = ["Abbott elementarty", "Blackish", "Fast and furious", "Game of thrones"]

# Check if a movie is available
movie_to_watch = "Moana"
position = bisect.bisect_left(available_movies, movie_to_watch)

if position < len(available_movies) and available_movies[position] == movie_to_watch:
    print(f"'{movie_to_watch}' is available to stream")
else:
    print(f"'{movie_to_watch}' is not in the catalog")

# Finding insertion positions in ordered data

import bisect
from datetime import datetime

# Events sorted by start time
event_times = [
    datetime(2026, 2, 5, 9, 0), # 9:00 AM
    datetime(2026, 2, 5, 10, 30), # 10:30 AM
    datetime(2026, 2, 5, 14, 0) # 2:00 PM
    datetime(2026, 2, 5, 16, 30) # 4:30 PM
]

# Add a new meeting at 12:00 PM
new_meeting = datetime(2026, 2, 5, 12, 0)
position = bisect.bisect_left(event_times, new_meeting)
event_times.insert(position, new_meeting)

print(f"Meeting inserted at position {position}")
print(f"Total events: {len(event_times)}")

# Searching logs, IDs, or timestamps

import bisect

# User IDs from sorted database query
user_ids = [1001, 1045, 1089, 1123, 1167, 1201, 1245, 1289, 1334, 1378]

# Find user with ID 1200
target_id = 1200
pos = bisect.bisect_left(user_ids, target_id)

if pos < len(user_ids) and user_ids[pos] == target.id:
    print(f"User {target_id} found at index {pos}")
else:
    if pos < len(user_ids):
        print(f"User {target_id} not found. Next highest ID is {user_ids[pos]} at index")
    else:
        print(f"User {target_id} not found. This ID is higher than every ID in the database")

# Errror: wrong answer
unsorted_list = [20, 30, 25, 10, 5, 15]
result = binary_search_iterative(unsorted_list, 5)

# Best5 practice: correct answer

# Method 1: Using sorted()
unsorted_list = [20, 30, 25, 10, 5, 15]
sorted_list = sorted(unsorted_list)
result = binary_search_iterative(sorted_list, 5)
print(unsorted_list) # Still [20, 30, 25, 10, 5, 15]
print(sorted_list) # Now [5, 10, 15, 20, 25, 30]

# Method 2: Using .sort()
unsorted_list = [20, 30, 25, 10, 5, 15]
unsorted_list.sort()
result = binary_search_iterative(unsorted_list, 5)
print(unsorted_list) # Now [5, 10, 15, 20, 25, 30]

# ERROR : binary search on a list with duplicate values
def standard_search(arr, target):
    lefgt, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid # Returns any occurence - unpredictable!
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 2, 2, 2, 2, 3, 4]
result = standard_search(arr, 2)
print(f"Found at index: {result}") # Might return 1, 2, 3, or 4 - unpredictable!

# BEST PRACTICE: Using bisect
import bisect

# Find first occurence using bisect_left
first = bisect.bisect_left(arr, 2)
print(f"First occurence of 2: index {first}") # Always returns index 1

# Find last occurence using bisect_right
last = bisect.bisect_right(arr, 2) - 1
print(f"Last occurence of 2: index {last}") # Always returns index 4

# Write your own first occurence search
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1 # Keep searching left half for earlier occurence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Wrtie your own last occurence search
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1 # Keep searchiong right half for later occurence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(f"First occurence: {find_first(arr, 2)}") # Always returns 1
print(f"Last occurence: {find_last(arr, 2)}") # Always returns 4

# Code with errors
def buggy_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left < right: # error 1: Should be left <= right
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid # error 2: Should be mid + 1
        else:
            right = mid # error 3: Should be mid - 1

    return -1