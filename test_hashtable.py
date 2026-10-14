# test_hashtable.py

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test" # solution to fixing this set assertion error

    # the assert statement takes a Boolean expression as an argument followed by an error message, if the expression evaluates to true, nothing happens otherwise the error message is displayed

# DEFINE A CUSTOM HASHTABLE CLASS

from hashtable import HashTable, BLANK

def test_should_create_hashtable():
    assert HashTable() is not None

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(size=100) is not None

# ADDING ANOTHER TEST CASE

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

# A NEW HASH TABLE SHOULD PROBABLY START WITH EMPTY SLOTS FOR THE STORED VALUES:

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

# it's normal to have verbose test function names because they will appear in the report - the more readable & descriptive the names the better

# as much as possible, test cases need to be as independent & atomic as possible - meaning using only one assertion per function

# GIVEN-WHEN-THEN CONVENTION:
# GIVEN defines what the conditions are to be / the requirements - initial state & preconditions
# WHEN defines the actual input for the given test - represents the action of your code under the test
# THEN defines the rule that needs to be set wherein the GIVEN and the WHEN matches otherwise an assertion error is returned - responsible for asserting the resulting outcome
def test_should_create_empty_value_slots():
    # GIVEN STATE
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)

    # WHEN STATE
    actual_values = hash_table.values

    # THEN
    assert actual_values == expected_values

# A Python Dictionary has a length corresponding to the actual number of key-value pairs stored instead of its internal capacity

# INSERTING A KEY-VALUE PAIR
# traditional hash table is backed by an array capable of storing only one data type
# this is why in many other languages - they require you to declare the type for their keys and values up front
# Python has an efficient array collection but it is intended for numeric values only

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100) # intiialize a hash table with 100 empty slots

    hash_table["hola"] = "hello" # we populate the hash table with 3 pairs of keys & values of string, floating point, and boolean types
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 100

# in the real world - you want to create separate test cases with descriptive names dedicated to testing only specific behaviors

# you want to write a test case to express the desired behavior - an edge case that would handle an instance where None is in the hash table, creating conflict between a legitimate value and a designated sentinel value

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values


# FIND A VALUE BY KEY

import pytest_lazyfixture

@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    saample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True

# test fixture - function annotated with the @pytest.fixture decorator

# to find values by key - you can implement element lookup through another special method called .__getitem__() in your HashTable class

# in instances where a missing key is a possibility - you want to be able to raise a KeyError exception instead

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

# you create an empty hash table and try to access one of its values through a missing key
# pytest.raises allows you to expect a specific kind of exception within its given code block

# dict.get() method allows us to specify a default value which can replicate the same behavior in custom hash table
def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"

# DELETE A KEY-VALUE PAIR
# using the built-in del keyword - removes info about both the key and the value

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 100 # ensure that although we deleted key-value pairs, we are still not losing their memory slots

    del hash_table["hola"] # then we delete both the key and the value

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.pairs
    assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

# UPDATE THE VALUE OF AN EXISTING PAIR

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100

# GET THE KEY VALUE PAIRS

# This attribute in our HashTable class will hold the key-value pairs themselves

def test_should_return_pairs(hash_table):
    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

# This verifies that an empty hash table has no None values when created - you can use a list comprehension:

def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values

# USE DEFENSIVE COPYING

def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs

# the leading underscore when naming variables suich as ._pairs indicates internal implementation

def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._pairs == [None, None, None]

def test_should_insert_none_value():
    hash_table = HashTable(100)
    hash_table["key"] = None
    assert("key", None) in hash_table.pairs

# GET THE KEYS AND VALUES
def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values

# WHEN USING SET COMPREHENSION TO COMMUNICATE LACK OF GUARANTEES FOR THE ORDER OF VALUES WITHOUT LOSING INFORMATION ABOUT DUPLICATE VALUES IN THE HASH TABLE

def test_should_return_duplicate_values():
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)

    # here, we have a hash table of names and values and obviously the values are ages which can be duplicated - so .values should keep all repeated age values

# To reliably check if 2 lists have exactly the same elements of arbitrary types with potential duplicates while ignoring their order:

def have_same_elements(list1, list2):
    return all(element in list1 for element in list2)

# Same method but using the pytest-unordered plugin

# We import the unordered() function into the test suite and use it to wrap the hash table's values:

import pytest
from pytest_unordered import unordered

from hashtable import HashTable

def test_should_get_values(hash_table):
    assert unordered(hash_table.values) == ["hello", 37, True]