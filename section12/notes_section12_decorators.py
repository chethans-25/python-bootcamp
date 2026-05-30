# Decorators are a powerful tool in Python that allow you to modify the behavior of functions or classes without changing their source code. 
# They are often used for logging, access control, memoization, and more.
# A decorator is a function that takes another function as an argument and returns a new function that typically extends the behavior of the original function.

# def hello():
#     return "Hello, World!"
# # A simple decorator that adds a greeting before the original function's output

# greet = hello
# print(greet())  # Output: Hello, World!

# del hello  # Deleting the original function
# print(greet())  # Output: Hello, World! (greet still works because it references the original function)



def hello(name = "john"):
  print("hello function called ")

  def greet():
     return "\tthis is the greet function inside the hello function"
  def welcome():
     return "\tthis is the welcome function inside the hello function"
  
  # scope of the greet and welcome functions is limited to the hello function, they cannot be accessed outside of it
  if name == "john":
    return greet
  else:
    return welcome

my_new_func = hello("john")
print(my_new_func())  # Output: this is the greet function inside the hello function

def cool():
  def super_cool():
    return "this is the super cool function inside the cool function"
  return super_cool

my_cool_func = cool()
print(my_cool_func())  # Output: this is the super cool function inside the cool function

def other_function(func):
  print("other function is called")
  print(func())  # Calling the passed function

other_function(my_cool_func)  # Output: other function is called
# Output: this is the super cool function inside the cool function

other_function(hello("john"))  # Output: other function is called
# Output: this is the greet function inside the hello function

