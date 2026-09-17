### Python Regular Expressions
# matching text patterns
# re module provides regular expression support
match = re.search(pat, str)
# the re.search() function takes a pattern and a string and searches for the pattern within the string

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group()) ## 'found word:cat'
else:
    print('did not find')

## Basic Patterns
# a, X, 9 < ordinary characters that match themselves excactly
# . (period) - matches any single character except newline formatting \n
# \w (lowercase w) - matches a "word" character
# \W (uppercase W) - matches any non-word character
# \b - boundary between word and non-word
# \s (lowercase s) - matches a single whitespace characters
# \S (uppercase S) - matches any non-whitespace character.
# \t, \n, \r  - matches tab, newline, and return
# \d - matches any decimal digit [0-9]
# ^ - start, $ - end = matches the start or end of a string
# \ - inhibits the "specialness" of a chartacter 

# the match finds from start to end - stops at the first match found
# the entire pattern must match, not the string
# if re.search() is found, match is going not be None and match.group() returns the matching text

## Search for pattern 'iii' in string 'piiig'
## Entire pattern must match, but it may appear anywhere in the string
## On success, match.group() returns or is the matched text
match = re.search(r'iii', 'piiig') # found, match.group() = 'iii'
match = re.search(r'igs', 'piiig') # not foujnd, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == '123'
match = re.search(r'\w\w\w', '@@abcd') # found, match.group() == 'abc'

## Repetition
# + = 1 or more occurences of the pattern to its left, e.g. 'i+' one or more i's
# * = 0 or more occurences of the pattern to its left
# ? = match 0 or 1 occurences of the pattern to its left

## Repetition Examples
## i+ = one or more i's, as much or as many as possilbe
match = re.search(r'pi+', 'piiig') # found, match.group() = "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

## \s* = zero or more whitespace characters
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of the string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match.group() == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"

## Emails Example
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group()) ## 'b@google'

## Square Brackets
# [abc] matches a or b or c
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group()) ## 'alice-b@google.com'

# [a-z] matches all lowercase letters in square brackets
# [abc-] matches a or b or c or a -
# [^ab] matches all characters except for a or b

## Group Extraction
# pick out parts of the matching text
# match.group(1) - match text corresponding to the 1st left parenthesis
# match.group(2) - match text corresponding to the 2nd left parenthesis

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-])+@([\w.-]+)', str)
if match:
    print(match.group()) ## 'alice-b@google.com' (the whole match)
    print(match.group(1)) ## 'alice-b (the username, group 1)
    print(match.group(2)) ## 'google.com' (the host, group 2)

## findall
# findall() - function from re that finds all of the matching patterns in a string and returns a list of all of the patterns matched - one matching pattern is one element in the list

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)

## findall with files
# Open file
f = open('test.txt', encoding='utf-8')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())

## findall and groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.\-]+)@([\w\.-]+)', str)
print(tuples) ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0]) ## username
    print(tuple[1]) ## host

## Options
# IGNORECASE - ignore upper/lower case differences
# DOTALL - allow dot to match newline
# MULTILINE - allows ^/$ to match the start and end of each line

## Greedy vs. Non-Greedy (optional)

## Substitution
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replace, str) -- returns a new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

