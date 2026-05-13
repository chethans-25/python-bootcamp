# pip
# pip is a package manager for Python. It allows you to install and manage additional libraries and dependencies that are not included in the standard library.
# pip install package_name
# pip install requests
# pip install numpy
# pip list
# pip show package_name

# Pypi
# PyPI (Python Package Index) is a repository of software for the Python programming language. It is the default package index used by pip. PyPI hosts thousands of third-party packages that can be easily installed and used in Python projects.


# Modules
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py. Modules can define functions, classes, and variables. They can also include runnable code.
# import module_name

# colorama is a module that allows you to print colored text in the terminal.
from colorama import init,Fore
init()
print(Fore.CYAN + 'This text is CYAN')


# creating custom module
# my_main_package/
#     create __init__.py
# create some_main_script.py
# write some code in some_main_script.py

# importing custom module
# from my_main_package import some_main_script
# use some_main_script.my_func() to call the function defined in some_main_script.py

from my_main_package import some_main_script
some_main_script.my_func()

from my_main_package.sub_package import my_sub_script
my_sub_script.my_func()

# __name__ and __main__
# When a Python file is run directly, the __name__ variable is set to "__main__". When it is imported as a module, __name__ is set to the name of the module. This allows you to write code that can be used both as a script and as a module.
# if __name__ == "__main__":
#     # code to be executed when the file is run directly 

