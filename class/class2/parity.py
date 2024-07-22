# +
# -
# *
# /
# %

# x = int(input("What's x? "))
#
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(print("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):

# version 1
    if n % 2 == 0:
        return True
    else:
        return False

# version 2
    # return True if n % 2 == 0 else False

# version 3
    # return n % 2 == 0

main()