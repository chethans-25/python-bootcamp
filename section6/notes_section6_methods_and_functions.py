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


