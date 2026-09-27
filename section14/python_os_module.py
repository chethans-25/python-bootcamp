import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# f = open("test.txt", "w+")
# f.write("Hello, World!")
# f.close()
# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory+"\section14")
print("Files and Directories in Current Directory:")
print(files_and_directories)
print("\n")

import shutil
# Move the file to a new location
# shutil.move("test.txt", current_directory + "\section14\\test.txt")

'''
# delete a file
os.remove(current_directory + "\section14\\test.txt")
os.unlink(current_directory + "\section14\\test.txt")

# delete a directory
os.rmdir(current_directory + "\section14\\test_directory")

# rmtree is used to delete a directory and all its contents
it is in the shutil module
'''

# use send2trash to move a file to the recycle bin instead of permanently deleting it
# import send2trash
# send2trash.send2trash(current_directory + "\section14\\test.txt")

print("OS walk:")
print(list(os.walk(current_directory + "\section14")))