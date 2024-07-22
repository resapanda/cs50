print("#")
print("#")
print("#")

# efficient way
for _ in range(3):
    print("#")

def main():
    print_column(3)
def print_column(height):
    # for _ in range(height):
    #     print("#")

    # efficient way
    print("#\n" * height, end="")

main()


def main():
    print_row(4)
def print_row(width):
    print("?" * width)

main()


def main():
    print_square(3)
def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        # make a new line
        print()

main()



# Final idea
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print_row(size)
def print_row(width):
    print("#" * width)

main()