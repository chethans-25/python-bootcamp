# Methods
# every object has methods, which are functions that belong to the object. You can call a method on an object using the dot notation.

# list methods

mylist = [1, 2, 3]
help(mylist.append)
mylist.append(4)
print(mylist)
# string methods
mystring = "hello"
help(mystring.upper)
print(mystring.upper())

# etc. there are many methods for different types of objects, and you can find them in the documentation or by using the help() function.


# functions
# functions are reusable blocks of code that perform a specific task. You can define your own functions using the def keyword.

# syntax:
'''
def function_name(parameters):
    # code to execute
    return value
'''

def add_numbers(x, y):
    return x + y
result = add_numbers(3, 5)
print(result)

result = add_numbers('10', '20')
print(result)

# you can also have default parameters, which are used if the caller does not provide a value for that parameter.
def greet(name="World"):
    return f"Hello, {name}!"
print(greet()) 


# return even numbers from a list
def get_even_numbers(lst):
    even_num = []
    for num in lst:
      if num % 2 == 0:
        even_num.append(num)
      else:
        continue
    return even_num

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = get_even_numbers(numbers)
print(even_numbers)


# Tuple unpacking with functions

work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]
def employee_check(work_hours):
  current_max = 0
  employee_of_month = ""
  for employee, hours in work_hours:
    if hours > current_max:
      current_max = hours
      employee_of_month = employee
    else:
      continue
  return (employee_of_month, current_max)

name, hours = employee_check(work_hours)
print(f'Employee of the month: {name} with {hours} hours')

name, hours, location = employee_check(work_hours) # this will raise an error because the function returns only 2 values, but we are trying to unpack it into 3 variables.


# interaction bw python functions and methods
from random import shuffle

def shuffle_list(mylist):
  shuffle(mylist)
  return mylist

mylist = ['0','','']
def player_guess(mylist):
  guess = ""
  while guess not in ["0", "1", "2"]:
    guess = input("Pick a number: 0, 1, or 2: ")
  return int(guess)

def check_guess(mylist, guess):
  if mylist[guess] == "0":
    print("Correct!")
    print(mylist)
  else:
    print("Wrong guess!")
    print(mylist)

shuffled_list=shuffle_list(mylist)
guess = player_guess(shuffled_list)
check_guess(shuffled_list, guess)




# *args and **kwargs
# *args allows you to pass a variable number of non-keyword arguments to a function.
def myfunc(*args):#using args is a convention, you can use any name you want, but it is recommended to use args for readability.
  return sum(args) * 0.05
print(myfunc(40, 60, 100))

# **kwargs allows you to pass a variable number of keyword arguments to a function.
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print(f"My favorite fruit is {kwargs['fruit']}")
  else:
    print("I don't like fruit")

myfunc(fruit='apple')
myfunc()


# args return a tuple, while kwargs return a dictionary.
def myfunc(*args, **kwargs):
  print(args)
  print(kwargs)

myfunc(1, 2, 3, name='John', age=30)


# Function practice problems

'''
write a function that returns lesser of two even numbers if both numbers are even, but returns greater if one or both numbers are odd.
'''
def lesser_of_two_evens(a, b):
  if a % 2 == 0 and b % 2 == 0:
    return min(a, b)
  else:
    return max(a, b)
  

'''
write a function that takes in a two word string and returns True if both words begin with the same letter.
'''
def animal_crackers(text):
  wordlist = text.upper().split()
  print(wordlist)
  return wordlist[0][0] == wordlist[1][0]

animal_crackers('Levelheaded Llama')


'''
write a function that capitalizes the first and fourth letters of a name.
'''

def old_macdonald(name):
  if len(name) < 4:
    return "Name must be at least 4 letters long"
  else:
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()
print(old_macdonald('macdonald'))



'''
given a sentence, return a sentence with the words reversed. Like yoda (star wars reference), but the order of the words should be reversed.
'''
def master_yoda(text):
  wordlist = text.split()
  reversed_wordlist = wordlist[::-1]
  return " ".join(reversed_wordlist)

print(master_yoda('we are strong'))



# map, filter, lambda
# map is a built-in function that takes a function and an iterable and returns a new iterable with the function applied to each element of the iterable.
def square(num):
  return num ** 2
my_nums = [1, 2, 3, 4, 5]
print(list(map(square, my_nums))) # this will return a map object, which is an iterator
# notice square does not have parentheses because we are passing the function itself, not the result of the function.

# filter is a built-in function that takes a function and an iterable and returns a new iterable with only the elements of the iterable for which the function returns True.
def check_even(num):
  return num % 2 == 0
print(list(filter(check_even, my_nums))) # this will return a filter object, which is an iterator

# lambda is a way to create anonymous functions, which are functions that are not bound to a name. They are often used in conjunction with map and filter.
print(list(map(lambda num: num ** 2, my_nums))) # this will return a map object, which is an iterator
print(list(filter(lambda num: num % 2 == 0, my_nums))) # this will return a filter object, which is an iterator

# local vs global scope
# variables that are defined inside a function are called local variables, and they are only accessible within that function. Variables that are defined outside of a function are called global variables, and they are accessible throughout the entire program.
x=25
def myfunc():
  x=50
  return x
print(x) # prints 25
print(myfunc()) # prints 50

# LEGB rule
# Local -> Enclosing -> Global -> Built-in
# when you reference a variable, Python looks for it in the following order:
# 1. Local scope: the current function you are in
# 2. Enclosing scope: any enclosing functions (if you are in a nested function)
# 3. Global scope: the top-level of the script or module
# 4. Built-in scope: the built-in functions and variables that are always available in Python

name = "This is a global variable"
def greet():
  # name = "This is an Enclosing variable"
  def hello():
    # name = "This is a Local variable"
    print("Hello " + name)
  hello()

greet()

# local reassignment of global variable
x = 50
def func(x):
  print(f"x is {x}")
  x = 200
  print(f"I just locally changed x to {x}")

func(x)
print(f"x is still {x}")

def func():
  global x
  print(f"x is {x}")
  x = 200
  print(f"I just globally changed x to {x}")

func()
print(f"x is now {x}")




