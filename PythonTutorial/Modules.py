####################################################
# 6. Modules
####################################################

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries

# You can import modules
import math
# You can import all functions from a module.
# Warning: this is not recommended
from math import *
# You can shorten module names
import math as m
# you can also test that the functions are equivalent
from math import sqrt

print(math.sqrt(16))  # => 4

# You can get specific functions from a module
from math import ceil, floor

print(ceil(3.7))  # => 4.0
print(floor(3.7)  # => 3.0