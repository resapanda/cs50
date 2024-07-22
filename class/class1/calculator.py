# It treats x and y as string
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)

# Integer version
x1 = input("What's x1? ")
y1 = input("What's y1? ")

z1 = int(x1) + int(y1)

# Combine version (z doesn't exist)
x2 = int(input("What's x? "))
y2 = int(input("What's x? "))

print(x2 + y2)

# Technically we can combine everything but it's too complicated
print(int(input("What's x3? ")) + int(input("What's y3? ")))

# float (decimal number) floating point value
x4 = float(input("What's x4? "))
y4 = float(input("What's y4? "))

print(x4 + y4)

# Return rounded decimal number
# round(number[, ndigits])
# and put , every three digits

x5 = float(input("What's x5? "))
y5 = float(input("What's y5? "))

z = round(x5 + y5)

print(f"{z:,}")

# division
x4 = float(input("What's x4? "))
y4 = float(input("What's y4? "))

z = round(x4/y4, 2)

print(z)

# Another way
z = x4/y4

print(f"{z:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)


