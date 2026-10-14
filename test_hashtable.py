# In Python, Hash Tables are implemented through the built in data type dictionaries

# A Hash Table or a Hashmap is a type of data structure that maps keys to its value pairs (implement abstract array data types)
# makes use of a function that computes an index value that in turn holds the elements to be searched, inserted, removed, etc...
# in general, hash tables store key-value pairs where a key is generated using a hash function

# ELEMENTS OF A DICTIONARY ARE NOT ORDERED AND THEY CAN BE CHANGED

# DIFFERENCE BETWEEN HASH TABLE AND A HASH MAP IN PYTHON
# Hash Table is synchronized, fast, and allows one null key and more than one null values
# Hash Map is a non-synchronized, slow, and also does not allow null keys or values

# DICTIONARIES CAN BE CREATED IN 2 WAYS - CURLY BRACES OR THE DICT() FUNCTION

# USING CURLY BRACES
my_dict = {'Dave' : '001', 'Ava'  : '002', 'Joe' : '003'}
print(my_dict)
type(my_dict)

# USING DICT() FUNCTION
new_dict = dict() # this initializes an empty dictionary with no key-value pairs
print(new_dict)
type(new_dict)

# USING DICT() FUNCTION (BUT WITH KEY VALUE PAIRS THIS TIME)
new_dict = dict(Dave = '001', Ava = '002', Joe = '003')
print(new_dict)
type(new_dict)

# CREATING NESTED DICTIONARIES
emp_details = {'Employee' : {'Dave': {'ID': '001',
                                      'Salary': 2000,
                                      'Designation': 'Python Developer'},
                             'Ava': {'ID': '002',
                                     'Salary': 2300,
                                     'Designation': 'Java Developer'},
                             'Joe': {'ID': '003',
                                     'Salary': 1843,
                                     'Designation': 'Hadoop Developer'}}}

# PERFORMING OPERATIONS ON HASH TABLES USING DICTIONARIES

# Accessing values, Updating values, Deleting element

# ACCESSING VALUES
# to access values, we can do it so through using key values, using functions, implementing the for loop

# USING KEY VALUES
my_dict={'Dave', '001', 'Ava': '002', 'Joe': '003'}
print(my_dict['Dave']) # prints out 001

# USING FUNCTIONS
# We can use a number of built-in functions such as get(), keys(), values(), etc...
my_dict={'Dave': '001'; 'Ava': '002', 'Joe': '003'}
print(my_dict.keys()) # outputs the values
print(my_dict.values()) # outputs the values of the dictionary
print(my_dict.get('Dave')) # outputs the value of the key Dave

# THROUGH THE IMPLEMENTATION OF THE FOR LOOP
# allows you to access over the items through iteration
my_dict = {'Dave' : '001', 'Ava' : '002', 'Joe' : '003'}
print("All keys")
for x in my_dict:
    print(x) # only outputs the keys

print("All values")
for x in my_dict.values():
    print(x) # only outputs the values

print("All keys & values")
for x, y in my_dict.items():
    print(x, ":", y) # prints keys and values
    