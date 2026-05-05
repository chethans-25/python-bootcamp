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