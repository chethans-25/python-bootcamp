
# try, except, else and finally

# try: this is the block of code that we want to execute
# except: this is the block of code that will be executed if an error occurs in the try block
# else: this is the block of code that will be executed if no error occurs in the try block
# finally: this is the block of code that will be executed regardless of whether an error occurs or not 

try:
  f = open("C:\\Local Disk D\\GIT_REPOS\\python_bootcamp\\section3\\myfile.txt", "r")
  print(f.read())
except FileNotFoundError:
  print("The file was not found.")
except OSError:
  print("An OS error occurred.")
else:
  print("The file was read successfully.")
finally:
  print("This block will always be executed.")

def ask_for_int():
  while True:
    try:
      num = int(input("Please enter an integer: "))
    except ValueError:
      print("That's not an integer. Please try again.")
    else:
      print("Thank you for entering an integer.")
      return num

ask_for_int()