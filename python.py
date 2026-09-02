s = 'hi'
print(s[1]) ## i
print(len(s)) ## 2
print(s + ' there') ## hi there

pi = 3.14
## text = 'The value of pi is ' + pi ## NO, does not work
text = 'The value of pi is ' + str(pi)
print(text)

raw = r'this\t\n and that'

# this\t\n and that
print(raw)

multi = """It was the best of times.
It was the worst of times."""

# It was the best of times.
#   It was the worst of times.
print(multi)

# String Slicing
s = "Hello"
print(s[1:4]) # ell
print(s[1:]) # ello
print(s[:]) # Hello
print(s[1:100]) # is 'ello'

print(s[-1]) # 'o'
print(s[-4]) # 'e' - 4th from the end
print(s[:-3]) # 'He' - going up to but not including the last 3 characters
print(s[-3:]) # 'llo' - starting with the 3rd character from the end and extending to the end of the string.

# String Formatting
value = 2.791514
print(f'approximate value = {value:.2f}') # approximate value = 2.79

car = {'tires': 4, 'doors': 2}
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}

address_book = [{'name': 'N.X.', 'addr': '15 Jones St', 'bonus': 70},
                {'name': 'J.P.', 'addr': '1005 5th St', 'bonus': 400},
                {'name': 'A.A.', 'addr': '200001 Bdwy', 'bonus': 5},]

for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

# String %

# % operator
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')

# Add parentheses to make the long line work:
text = (
    "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))

# Split the line into chunks, which are concatenated automatically by Python
# text = (
#     "%d little pigs come out, "
#     "or I'll %s, and I'll %s, "
#     "and I'll blow your %s down."
#     %s (3, 'huff', 'puff', 'house'))

ustring = 'A unicode \u018e string \xf1'
b = ustring.encode('utf-8')
print(b) ## bytes of utf-8 encoding. Note the b prefix.
t = b.decode('utf-8') ## convert bytes back to a unicode string
print(t)    ## it's the same as the original, yay!
print(t == ustring)

# If Statements
if time_hour >= 0 and time_hour <= 24:
    print('Suggesting a drink option...')
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')

if time_hour < 10: print('coffee')
else: print('water')