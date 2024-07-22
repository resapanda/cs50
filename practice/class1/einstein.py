"""In a file called einstein.py, implement a program in Python
that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer."""

# input kg from users
m = int(input("m: "))

# convert kg to joule
e = int(m*300000000**2)

# print result
print("E: " + f"{e}")


# m = float(input("m: "))
#
# # convert kg to joule
# e = float(m*8.98755178780128E+16)
#
# result = round(e)
#
# # print result
# print("E: " + f"{result}")