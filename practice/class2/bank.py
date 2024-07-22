"""In a file called bank.py,
implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”),
output $20. Otherwise, output $100.
Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively."""

greeting = input("Greeting: ").lower()
first_letter = greeting[0]

def hello_detector(term, g):
    term = "hello"
    term2 = "hello,"
    g = greeting.split()

    if term in g or term2 in g:
        return True
    else:
        return False

# if the greeting contains "hello"
if hello_detector("hello",greeting):
    print("$0")
# if the greeting starts with "h"
elif first_letter == "h":
    print("$20")
else:
    print("$100")

