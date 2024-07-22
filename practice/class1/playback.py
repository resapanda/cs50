"""In a file called playback.py, implement a program in Python
that prompts the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods)."""

# input something from users
message = input()
# put the three periods each space and print
print(message.replace(" ","..."))