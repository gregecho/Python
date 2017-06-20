# Note that we can also import division module
# to carry out normal division with just on '/'
from __future__ import division

# Single line comments start with a number symbol.

""" Multiline strings can be writtern
    using three "s, and are often used
    as comments
"""

##############################################
# 1. Primitive Datatypes and Operators
##############################################

# You have numbers
3   #=>3

# Math is what you would expect
1 + 1   # => 2

# Division is a bit tricky. It is integer division and floor the result
# automatically
5 / 2 # => 2


# Python has a print statement
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

print(5 / 2);


print(11 / 4)
print(11 // 4)

# Strings are created with " or '
"This is a string."
'This is also a string.'

# ... or multiplied
print("Hello" * 3)  # => "HelloHelloHello"

# A string can be treated like a list of characters
print("This is a string"[0])  # => 'T'

# You can find the length of a string
print(len("This is a string"))  # => 16

# A newer way to format strings is the format method.
# This method is the preferred way
"{} is a {}".format("This", "placeholder")
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
print("etc" is None)  # => False
print(None is None)  # => True