

def dollars_to_float(d):

    price = float(d.replace("$", ""))
    result = round(price, 1)

    return result

def percent_to_float(p):
    tip = p.replace("%", "")
    # tip = float(p.replace("%", ""))
    result = float((tip*0.01))

    return result

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()

