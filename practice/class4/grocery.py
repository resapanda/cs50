"""In a file called grocery.py, implement a program
that prompts the user for items, one per line,
until the user inputs control-d
(which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times
the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively."""

item = []
while True:
    try:
        item.append(input().upper())
    except EOFError:
        break


result = {}
for f in range(len(item)):
    if item[f] not in result:
        result.update({item[f]: 1})
    else:
        num = result.get(item[f])
        num += 1
        result.update({item[f]: num})



for k, v in result.items():
    print(v, " ", k)
