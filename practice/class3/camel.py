"""In a file called camel.py,
implement a program that prompts the user for the name of a variable
in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case."""

# camel case = firstName
# snake case = first_case


def main():   # input the name of variable in camel case from the user
    camel_case = input("camelCase: ")
    snake_case = translate(camel_case)
    print(snake_case)

def translate(input):
    # make a list by each string
    letters = [char for char in input]
    # detect Uppercase and split them and make a new list
    result = []
    for i in range(len(letters)):
        if letters[i].isupper():
            result.append("_" + letters[i].lower())
        else:
            result.append(letters[i])

    # convert list to str and replace blank to underscore (everything should be lowercase)
    return ''.join(result)


main()
