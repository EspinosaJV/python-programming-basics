## CHAPTER 8 - LOOPS
# Loops are for when we want to do the same job multiple times

# Another Assignment
# Complete the misssing sections of the for loop in the print numbers function so that it prints the numbers 0-99 to the console

def print_numbers():
    for i in range (0, 100):
        print(i)

# Another assignment
# In the print_numbers_from_five_to function, the for-loop starts at 0. It should start at 5. Only change the start

def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

#  it is required to indent the body of a traditional for-loop in Python

## Range Continued
# Assignment
# Fix the for loop in the count_down function so that it prints the numbers counting down from start to (but not including) end in order.

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

# Assignment
# Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of 1 + 1 + 1 + 1 + 1...  we want: 0 + 1 + 2 +3 + 4... the desired output is a single number after the loop has finished executing

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

# Assignment
# Complete the sum_of_odd_numbers function. It should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

