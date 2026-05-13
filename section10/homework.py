# qn1
try:
  for i in ['a', 'b', 'c']:
    print(i**2)
except TypeError as e:
  print("A TypeError occurred:", e)

# qn2
x=5
y=0
try:
  z = x/y
except ZeroDivisionError as e:
  print("\nA ZeroDivisionError occurred:", e)


def ask_for_int():
  while True:
    try:
      num = int(input("\nPlease enter an integer: "))
    except ValueError as e:
      print("That's not an integer. Please try again.", e)
    else:
      print("Thank you for entering an integer.")
      return num**2
num_squared = ask_for_int()
print(f"\nThe square of the number you entered is: {num_squared}")
