# This is two.py
import one #top level code in one.py will be executed when one.py is imported
print("Top level code in two.py")

one.func()

if __name__ == "__main__":
  print("two.py is being run directly")
else:
  print("two.py is being imported")