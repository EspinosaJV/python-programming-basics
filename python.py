# Python Lists

colors = ['red', 'blue', 'green']
print(colors[0]) ## red
print(colors[2]) ## green
print(len(colors)) ## 3

# FOR and IN
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum) ## 30

list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay') ## yay

## print the numbers from 0 through 99
for i in range(100):
    print(i)

# While Loop
## Access every 3rd element in a list
i = 0
while i < len(a):
    print(a[i])
    i = i + 3

list = ['larry', 'curly', 'moe']
list.append('shemp') ## append elem at end
list.insert(0, 'xxx') ## insert elem at index 0
list.extend(['yyy', 'zzz']) ## add list of elems at end
print(list) ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly')) ## 2

list.remove('curly') ## search and remove that element
list.pop(1) ## removes and returns ('larry')
print(list) ## ['xxx', 'moe'. 'shemp', 'yyy', 'zzz']

list = [1, 2, 3]
print(list.append(4)) ## NO, does not work, append() returns None
## Correct pattern:
list.append(4)
print(list)

list = [] ## Start as the empty list
list.append('a') ## Use append() to add elements
list.append('b') # Use append() to add another element

# List Slices
list = ['a', 'b', 'c', 'd']
print(list[1:-1]) ## ['b', 'c']
list[0:2] = 'z' ## replace ['a', 'b'] with ['z']
print(list) ## ['z', 'c', 'd']