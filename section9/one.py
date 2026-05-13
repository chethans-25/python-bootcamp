# this is one.py
# when run directly, __name__ is set to "__main__"

def func():
  print("func() in one.py")

print("Top level code in one.py")

if __name__ == "__main__":
  print("one.py is being run directly")
else:
  print("one.py is being imported")