

# simple arithmetic operators

'''
+ (addition)
- (subtraction)
* (multiplication)
/ (true division)
// (floor division)
% (modulo)
** (exponentiation)


'''

# Variable names
'''
- Can contain letters, numbers, and underscores
- Cannot start with a number
- Cannot be a reserved keyword (e.g., 'if', 'for', 'while', etc.)
- Cannot contain special characters (e.g., '@', '#', '$', ' ', etc.)
- Should be descriptive of the value they hold (e.g., 'age', 'height', 'name', etc.)
'''

# Python is dynamically typed, which means that you don't need to declare the type of a variable when you create it.
# The type is inferred from the value you assign to it.
# Same variable can hold different types of values at different times.

from pyexpat.errors import codes


age =25
type(age) # provides the type of the variable 'age'


# Strings
# Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Triple quotes are often used for multi-line strings or docstrings.

# use indexing and slicing to access parts of a string
# Indexing starts at 0, so the first character of a string is at index 0, the second character is at index 1, and so on.
# Negative indexing allows you to access characters from the end of the string, with -1 being the last character, -2 being the second to last character, and so on.
name = "Alice"
print(name[0])  # Output: 'A'
print(name[-1]) # Output: 'e'
# Slicing allows you to extract a substring from a string using the syntax: string[start:end:step]
# 'start' is the index of the first character to include (default is 0)

# slicing syntax: string[start:end:step]
# 'end' is the index of the first character to exclude (default is the length of the string)

# slicing example
greeting = "Hello, World!"
print(greeting[0:5])  # Output: 'Hello'
print(greeting[::-1])  # Output: '!dlroW ,olleH'



# more on indexing and slicing
greeting = "Hello, World!"
print(greeting[7:12])  # Output: 'World'
print(greeting[::2])  # Output: 'Hlo ol!'


greeting = "Hello World"
print(greeting[-3])

# String Properties and Methods
# Strings are immutable, which means that you cannot change a string after it has been created. However, you can create a new string based on an existing string using various string methods.

name = "Sam"
name[0] = 'P'  # This will raise a TypeError because strings are immutable

# concatenation and repetition
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print(full_name)  # Output: 'John Doe'
repeated_name = first_name * 3  # Repetition
print(repeated_name)  # Output: 'JohnJohnJohn'

print(first_name.upper())  # Output: 'JOHN'
print(last_name.lower())  # Output: 'doe'

# common string methods
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.split())  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
print(sentence.replace("fox", "cat"))  # Output: 'The quick brown cat jumps over the lazy dog.'
print(sentence.find("lazy"))  # Output: 35 (index of the first occurrence of 'lazy')
print(sentence.count("o"))  # Output: 4 (number of occurrences of 'o')
print(sentence.startswith("The"))  # Output: True
print(sentence.endswith("dog."))  # Output: True  
print(sentence.strip())  # Output: 'The quick brown fox jumps over the lazy dog.' (removes leading and trailing whitespace)
print(sentence.isalpha())  # Output: False (returns True if all characters in the string are alphabetic)
print(sentence.isdigit())  # Output: False (returns True if all characters in the string are digits)
print(sentence.islower())  # Output: False (returns True if all characters in the string are lowercase)
print(sentence.isupper())  # Output: False (returns True if all characters in the string are uppercase)
print(sentence.isspace())  # Output: False (returns True if all characters in the string are whitespace)
print(sentence.title())  # Output: 'The Quick Brown Fox Jumps Over The Lazy Dog.' (capitalizes the first letter of each word) 
print(sentence.capitalize())  # Output: 'The quick brown fox jumps over the lazy dog.' (capitalizes the first letter of the string)


# string formatting
first_name = "Chethan"

print(f"Hello, {first_name}!")  # Output: 'Hello, Chethan!' (using f-strings) fstrings requires Python 3.6 or later
print("Hello, {}!".format(first_name))  # Output: 'Hello, Chethan!' (using str.format())
print("Hello, %s!" % first_name)  # Output: 'Hello, Chethan!' (using old-style string formatting)


print("{} {} {}".format("brown", "fox", "quick"))  # Output: 'brown fox quick'
print("{2} {0} {1}".format("brown", "fox", "quick"))  # Output: 'quick fox brown'
print("{2:<10} {0:<10} {1:<10}".format("brown", "fox", "quick"))  # Output: 'quick      brown     fox       ' (using field width and alignment)
# the '<' character indicates left alignment, and the number '10' specifies a minimum width of 10 characters for each field. If the string is shorter than 10 characters, it will be padded with spaces on the right to meet the minimum width requirement.


result = 10 / 3
print(result)  # Output: 3.3333333333333335 (true division)

# precision
print(f"{result:.2f}")  # Output: '3.33' (formatting to 2 decimal places)
print("{:.2f}".format(result))  # Output: '3.33' (using str.format() to format to 2 decimal places)


print("{} rules".format('Python'))


# Lists
# Lists are ordered, mutable collections of items that can hold elements of different types. They are defined using square brackets [] and can contain any number of items, including other lists.

my_list = [1, 2, 3, "four", [5, 6], True]
print(my_list)  # Output: [1, 2, 3, 'four

len(my_list)  # Output: 6 (returns the number of items in the list)

# indexing and slicing
print(my_list[0])  # Output: 1 (first item)
print(my_list[-1])  # Output: True (last item)
print(my_list[3:5])  # Output: ['four', [5, 6]] (slicing from index 3 to 4)

# concatenation and repetition
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = list1 + list2  # Concatenation
print(combined_list)  # Output: [1, 2, 3, 'a', 'b', 'c']
repeated_list = list1 * 2  # Repetition
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]

list1.append(4)  # Adds 4 to the end of list1
print(list1)  # Output: [1, 2, 3, 4

list1.insert(0, 0)  # Inserts 0 at index 0 of list1
print(list1)  # Output: [0, 1, 2, 3

list1.remove(2)  # Removes the first occurrence of 2 from list1
print(list1)  # Output: [0, 1, 3, 4 
list1.pop()  # Removes and returns the last item from list1
print(list1)  # Output: [0, 1, 3]
list1.pop(1)  # Removes and returns the item at index 1 from list1
print(list1)  # Output: [0, 3]
list1.clear()  # Removes all items from list1
print(list1)  # Output: []

list1.sort()  # Sorts the items of list1 in place
print(list1)  # Output: [0, 3] (sorted list)

list1.reverse()  # Reverses the items of list1 in place
print(list1)  # Output: [3, 0] (reversed list)

# Dictionaries
# Dictionaries are unordered, mutable collections of key-value pairs. They are defined using curly braces {}

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict["name"])  # Output: 'Alice' (accessing value by key)
my_dict["age"] = 31  # Updating the value associated with the key 'age'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
my_dict["country"] = "USA"  # Adding a new key-value pair to the dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
del my_dict["city"]  # Removing the key-value pair with the key 'city' from the dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
my_dict.clear()  # Removing all key-value pairs from the dictionary
print(my_dict)  # Output: {}
my_dict.values()  # Returns a view object containing the values of the dictionary
my_dict.keys()  # Returns a view object containing the keys of the dictionary
my_dict.items()  # Returns a view object containing the key-value pairs of the dictionary as tuples
my_dict.get("name")  # Returns the value associated with the key 'name' (or None if the key is not found)
my_dict.get("name", "Unknown")  # Returns the value associated with the key 'name' (or 'Unknown' if the key is not found)
my_dict.pop("age")  # Removes and returns the value associated with the key 'age' (or raises a KeyError if the key is not found)
my_dict.pop("age", None)  # Removes and returns the value associated with the key 'age' (or returns None if the key is not found)


# Tuples
# Tuples are ordered, immutable collections of items that can hold elements of different types. They are defined using parentheses ().

# immutable, which means that you cannot change a tuple after it has been created. However, you can create a new tuple based on an existing tuple using various tuple methods.

tuple1 = (1, 2, 3, "four", [5, 6], True)
print(tuple1)  # Output: (1, 2, 3, 'four
len(tuple1)  # Output: 6 (returns the number of items in the tuple)
print(tuple1[0])  # Output: 1 (first item)
print(tuple1[-1])  # Output: True (last item)
print(tuple1[3:5])  # Output: ('four', [5, 6]) (slicing from index 3 to 4)

tuple1.index(3)  # Returns the index of the first occurrence of 3 in tuple1
tuple1.count(3)  # Returns the number of occurrences of 3 in tuple1


# Sets
# Sets are unordered, mutable collections of unique items. They are defined using curly braces {} or the set() constructor.

new_set = set([1, 2, 3, 3, 3, 4, 5])  # Creating a set from a list
print(new_set)  # Output: {1, 2, 3, 4, 5} (duplicates are removed in a set)

my_set = {1, 2, 3, "four", (5, 6), True}
print(my_set)  # Output: {1, 2, 3, 'four, (5, 6), True} (note that the order of items in a set is not guaranteed)
len(my_set)  # Output: 6 (returns the number of unique items in the set)
my_set.add(7)  # Adds 7 to the set
print(my_set)  # Output: {1, 2, 3, 'four, (5, 6), True, 7}
my_set.remove(2)  # Removes 2 from the set (raises a KeyError if 2 is not found)
print(my_set)  # Output: {1, 3, 'four, (5 6), True, 7}
my_set.discard(2)  # Removes 2 from the set (does nothing if 2 is not found)
print(my_set)  # Output: {1, 3, 'four, (5 6), True, 7}
my_set.pop()  # Removes and returns an arbitrary item from the set (raises a KeyError if the set is empty)
print(my_set)  # Output: {3, 'four, (5 6), True, 7} (the item that was removed may vary)
my_set.clear()  # Removes all items from the set
print(my_set)  # Output: set()



# Booleans
# Booleans are a data type that can only take on two values: True and False

print(1>2)  # Output: False
print(2>1)  # Output: True

myfile = open("myfile.txt", "r")  # Opens a file named 'myfile.txt' in read mode
# mention full path if the file is not in the same directory as the script
content = myfile.read()  # Reads the entire content of the file and stores it in the variable 'content'
print(content)  # Output: (prints the content of the file)

print(myfile.read())  # Output: '' (returns an empty string because the file pointer is at the end of the file after the first read operation)

myfile.seek(0)  # Moves the file pointer back to the beginning of the file
print(myfile.read())  # Output: (prints the content of the file again)

myfile.seek(0) 
myfile.readlines()  # Reads the file line by line and returns a list of lines

myfile.close()  # Closes the file to free up system resources


# best practice: use with open statement to handle files, as it ensures that the file is properly closed after its suite finishes, even if an exception is raised.
with open( "myfile.txt", "r") as myfile:
  content = myfile.read()
  print(content)  # Output: (prints the content of the file)


# access modes
# 'r': Read mode (default) 
# 'w': Write mode (creates a new file or overwrites an existing file)
# 'a': Append mode (creates a new file or appends to an existing file)
# 'x': Exclusive creation mode (creates a new file and raises an error if the file already exists)
# 'b': Binary mode (used for non-text files, such as images or PDFs)
# 't': Text mode (default, used for text files)
# 'r+': Read and write mode (allows both reading and writing to the file)
# 'w+': Write and read mode (creates a new file or overwrites an existing file, and allows both writing and reading to the file)

