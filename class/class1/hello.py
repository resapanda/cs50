# Ask user for your name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name but only first word
name = name.capitalize()
# Every single words can be capitalized
name = name.title()

# We can combine the function
name = name.strip().title()
name = input("What's your name? ").strip().title()

# Sprit user's name into first name and last name
first, last = name.split("")

# Say hello to user
# 1
print("Hello, " + name)
# 2
print("Hello,", name)
# 3
print("Hello, ", end="")
print(name)
# 4
print(f"Hello, {name}")

# The ways to put quotation marks inside the arguments
print('Hello, "friend"')
print("Hello, \"friend\"")

# def definition make a new function by yourself
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
name = "haruka"
hello(name)

# scope
