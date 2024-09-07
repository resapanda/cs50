"""In a file called fuel.py, implement a program that prompts
the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, 1% or less remains,
output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate
that the tank is essentially full."""


while True:
    try:
        fraction = input("Fraction: ").split('/')
        x = fraction[0]
        y = fraction[1]
        result = int(x)/int(y)
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        if result > 1:
            continue
        elif result >= 0.99 or result == 1:
            print("F")
            break
        elif result <= 0.01 or result == 0:
            print("E")
            break
        else:
            print(f"{int(result*100)}%")
            break
