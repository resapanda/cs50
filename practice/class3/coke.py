"""Suppose that a machine sells bottles of Coca-Cola (Coke)
for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py,
implement a program that prompts the user to insert a coin,
one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents,
output how many cents in change the user is owed.
Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination."""


# def main():
#     print("Amount Due: 50")
#     calculate()
#
#
# def calculate():
#     coke = 50
#
#     while coke > 0:
#         # input integers(insert coin) from the user and save it into paid
#         paid = int(input("Insert Coin: "))
#
#         if paid == 25 or paid == 10 or paid == 5:  # only accept 25, 10, 5
#             result = coke - paid  # calculate how much the user has to pay more
#
#             if result > 0:  # when we get less than 50 in total from the user
#                 print("Amount Due: ", result)
#                 coke = result
#             else:  # when we get more than 50 in total from the user
#                 print("Change Owed: ", abs(result))
#                 break
#                 # return False
#
#         else:
#             print("Amount Due: ", coke)
#
#
# main()


def main():
    buy_coke()

def buy_coke():
    coke = 50
    print("Amount Due: ", coke)

    while coke > 0:
        # input integers(insert coin) from the user and save it into paid
        paid = int(input("Insert Coin: "))

        if paid == 25 or paid == 10 or paid == 5:  # only accept 25, 10, 5
            diff = coke - paid  # calculate how much the user has to pay more

            if diff > 0:  # when we get less than 50 in total from the user
                print("Amount Due: ", diff)
                coke = diff
            else:  # when we get more than 50 in total from the user
                print("Change Owed: ", abs(diff))
                break
        else:
            print("Amount Due: ", coke)


main()