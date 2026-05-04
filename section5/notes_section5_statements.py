# Statements

# Control flow uses colons and indendations

# if syntax
'''
if condition:
    # code to execute if condition is true
'''


# if-else syntax
'''
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
'''

# if-elif-else syntax
'''
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if none of the conditions are true
'''

if 5 > 3:
  print("5 is greater than 3")
else:
  print("5 is not greater than 3")

age = 18
if age >= 18:
  print("You are an adult.")
else:
  print("You are a minor.")

temperature = 30
if temperature > 30:
  print("It's hot outside.")
elif temperature > 20:
  print("It's warm outside.")
else:
  print("It's cold outside.")



# loops

# for loop syntax
'''
for variable in iterable:
    # code to execute for each item in the iterable
'''
mylist = [1, 2, 3, 4, 5]
for num in mylist:
  print(num)

mylist = [(1, 'one'), (2, 'two'), (3, 'three')]
for num, word in mylist:
  print(f"{num} is {word}")

d1 = {'a': 1, 'b': 2, 'c': 3}
for key in d1:
  print(f"{key}: {d1[key]}")

for key, value in d1.items():
  print(f"{key}: {value}")

for i in range(5):
  print(i)

for i in range(1, 10, 2):
  print(i)

for item in enumerate("mylist"):
  print(item)

list2 = ['a', 'b', 'c', 'd', 'e']
for item in zip(mylist,list2):
  print(item)

# while loop syntax
'''
while condition:
    # code to execute as long as condition is true
else:
    # code to execute when condition becomes false
'''

# break, continue, pass
# break syntax
'''
while True:
    # code to execute
    if condition:
        break  # exit the loop
'''
# continue syntax
'''
while True:
    # code to execute
    if condition:
        continue  # skip the rest of the loop and start the next iteration
'''

# pass syntax
'''
while True:
    # code to execute
    if condition:
        pass  # do nothing and continue with the loop
'''


# in keyword
mylist = [1, 2, 3, 4, 5]
if 3 in mylist:
  print("3 is in the list")


from random import shuffle, randint
mylist = [1, 2, 3, 4, 5]
shuffle(mylist)
print(mylist)


num = randint(1, 10)
print(num)

name = input("Enter your name: ")  # string
print(f"Hello, {name}!")

age = int(input("Enter your age: "))  # integer
print(f"You are {age} years old.")


# List comprehensions
mystring = "hello"
mylist = [letter for letter in mystring]
print(mylist)

squares = [x**2 for x in range(10)]
print(squares)

# if-else in list comprehensions
even_odd = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(even_odd)

mylist = [x*y for x in [1, 2, 3] for y in [4, 5, 6]]
print(mylist)



# practive exercises
st = "Print only the words that start with s in this sentence"
for word in st.split():
  if word.startswith('s'):
    print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11, 2):
  print(num)

# Use a list comprehension to create a list of all the numbers between 1 and 50 that are divisible by 3.
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(divisible_by_3)

# go through the string below and if the length of a word is even print "even!" otherwise print the word 
st = "Print every word in this sentence that has an even number of letters"
for word in st.split():
  if len(word) % 2 == 0:
    print("even!")
  else:
    print(word)


