'''
Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.
'''

def myfunc(*args):
  even_numbers = []
  for num in args:
    if num % 2 == 0:
      even_numbers.append(num)
  return even_numbers