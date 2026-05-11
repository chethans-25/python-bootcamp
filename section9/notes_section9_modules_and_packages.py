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