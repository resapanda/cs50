# SyntaxError

# ValueError
x = int(input("What's x?"))
print(f"x is {x}")

# try
# except
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# NameError
# cat can never be int so the code shows ValueError
# But it is already handled by except
# so print(f"x is {x}") is executed instantly and made NameError
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# one way to solve
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# infinity loop until the user input a number
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


while True:
    try:
        x = int(input("What's x?"))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


# efficient way?
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x  # 2 thing at once (get out from the loop and return)


main()


def main():
    x = get_int1("What's x? ")
    print(f"x is {x}")


def get_int1(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass  # pass - just ignore and skip

main()
