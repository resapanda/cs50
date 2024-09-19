# random.choice(seq)

# import module
import random

coin = random.choice(["heads", "tails"])
print(coin)

# from
# random.choice
from random import choice

coin = random.choice(["heads", "tails"])
print(coin)


# random.randint(a, b)
number = random.randint(1, 10)
print(number)


# random.shuffle(x)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
