####################################################
#  3. Control Flow
####################################################

# Let's just make a variable
some_var = 5

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else: # This is optional too.
    print("some_var is indeed 10.")

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use {0} to interpolate formatted strings. (See above.)
    print("{0} is a mammal".format(animal))

"""
"range(number)" returns a list of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns a list of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1


# Handle exceptions with a try/except block

# Works on Python 2.6 and up:
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass  # Multiple exceptions can be handled together, if required.
else:  # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")  # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)
