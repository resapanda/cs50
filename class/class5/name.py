# sys
# sys.argv

import sys

print("hello, my name is", sys.argv[1])

# input -> python name.py David
# output -> hello, my name is David

# if there is no input
# -> IndexError: list index out of range

# use exception to handle this error?
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# use condition
# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# if you put quotation mark it counts as one argument
# ex -> "David Black"

# still get some errors
# to avoid errors, exit from the program earlier
# sys.exit()

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# slices
# using [1:] can get subsets of the list
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
