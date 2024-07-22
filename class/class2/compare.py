x = int(input("What's x? "))
y = int(input("What's y? "))
# elif is else if
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# 1
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# 2
if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")

# 3
if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")

