"""When texting or tweeting,
it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py,
implement a program that prompts the user for a str of text
and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase."""

# make a list in char
name = [char for char in input("Input: ")]
stop_letters = ["A", "E", "I", "O", "U", "a", "e", "u", "i", "o"]
new_list = []

for s in range(len(name)):
    if name[s] not in stop_letters:
        new_list.append(name[s])

print("".join(new_list))