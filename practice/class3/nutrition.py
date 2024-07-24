"""In a file called nutrition.py,
implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit,
per the FDA’s poster for fruits, which is also available as text.
Capitalization aside, assume that users will input fruits exactly
as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn’t a fruit."""


# fruits = [
#     {"fruits": "apple", "calories": "130"},
#     {"fruits": "avocado", "calories": "50"},
#     {"fruits": "banana", "calories": "110"},
#     {"fruits": "cantaloupe", "calories": "50"},
#     {"fruits": "grapefruit", "calories": "60"},
#     {"fruits": "grapes", "calories": "90"},
#     {"fruits": "honeydew melon", "calories": "50"},
#     {"fruits": "kiwifruit", "calories": "90"},
#     {"fruits": "lemon", "calories": "15"},
#     {"fruits": "lime", "calories": "20"},
#     {"fruits": "nectarine", "calories": "60"},
#     {"fruits": "orange", "calories": "80"},
#     {"fruits": "peach", "calories": "60"},
#     {"fruits": "pear", "calories": "100"},
#     {"fruits": "pineapple", "calories": "50"},
#     {"fruits": "plums", "calories": "70"},
#     {"fruits": "strawberries", "calories": "50"},
#     {"fruits": "sweet cherries", "calories": "100"},
#     {"fruits": "tangerine", "calories": "50"},
#     {"fruits": "watermelon", "calories": "80"}
#     ]

fruit = {"apple": "130",
         "avocado": "50",
         "banana": "110",
         "grapefruit": "60",
         "grapes": "90",
         "honeydew melon": "50",
         "kiwifruit": "90",
         "lemon": "15",
         "lime": "20",
         "nectarine": "60",
         "orange": "80",
         "peach": "60",
         "pear": "100",
         "pineapple": "50",
         "plums": "70",
         "strawberries": "50",
         "sweet cherries": "100",
         "tangerine": "50",
         "watermelon": "80"
         }

item = (input("Item: ")).lower()

if item in fruit:
    print("Calories: ", fruit[item])
