# our goal
print("meow")
print("meow")
print("meow")

# while loop
i = 3
while i != 0:
    print("meow")
    i = i - 1

# good way is starting from zero
i = 0
while i < 3:
    print("meow")
    i += 1

# for loop
for i in range(3):
    print("meow")

# use end
print("meow\n" * 3, end="")

# Example 1
while True:
    n = int(input("What's n? "))
    if n < 0:
        break

for _ in range(n):
    print("meow")

# Example 2

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        return n
def meow(n):
    for _ in range(n):
        print("meow")