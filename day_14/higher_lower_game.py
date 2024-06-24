import random

vs_logo = """
   ________   ________ 
  /    /   \ /        \
 /         //        _/
 \        //-        / 
  \\_____/ \_______//  
  
"""

famous_people = [
    {
        "name": "Priyanka Chopra",
        "description": "Індійська акторка, співачка та модель.",
        "followers": 90000000
    },
    {
        "name": "Nike",
        "description": "Офіційний аккаунт бренду спортивного одягу та взуття.",
        "followers": 190000000
    },
    {
        "name": "Kylie Jenner",
        "description": "Американська модель, бізнесвумен, засновниця Kylie Cosmetics.",
        "followers": 380000000
    },
    {
        "name": "Selena Gomez",
        "description": "Американська співачка, акторка та продюсер.",
        "followers": 420000000
    },
    {
        "name": "Dwayne Johnson",
        "description": "Американський актор і колишній реслер.",
        "followers": 390000000
    },
    {
        "name": "Ariana Grande",
        "description": "Американська співачка та акторка.",
        "followers": 370000000
    },
    {
        "name": "Kim Kardashian",
        "description": "Американська телевізійна персона, бізнесвумен та модель.",
        "followers": 360000000
    },
    {
        "name": "Beyoncé",
        "description": "Американська співачка, акторка та продюсер.",
        "followers": 320000000
    },
    {
        "name": "Justin Bieber",
        "description": "Канадський співак та автор пісень.",
        "followers": 310000000
    },
    {
        "name": "Kendall Jenner",
        "description": "Американська модель та телевізійна персона.",
        "followers": 280000000
    },
    {
        "name": "Taylor Swift",
        "description": "Американська співачка та авторка пісень.",
        "followers": 270000000
    },
    {
        "name": "Lionel Messi",
        "description": "Аргентинський футболіст, відомий гравець у клубі Inter Miami.",
        "followers": 450000000
    },
    {
        "name": "Neymar Jr.",
        "description": "Бразильський футболіст, гравець клубу Paris Saint-Germain.",
        "followers": 200000000
    },
    {
        "name": "Khloe Kardashian",
        "description": "Американська телевізійна персона та бізнесвумен.",
        "followers": 180000000
    },
    {
        "name": "Jennifer Lopez",
        "description": "Американська співачка, акторка та продюсер.",
        "followers": 240000000
    },
    {
        "name": "Real Madrid",
        "description": "Офіційний аккаунт футбольного клубу Real Madrid.",
        "followers": 140000000
    },
    {
        "name": "Virat Kohli",
        "description": "Індійський крикетист, колишній капітан національної збірної Індії з крикету.",
        "followers": 240000000
    },
    {
        "name": "Cristiano Ronaldo",
        "description": "Португальський футболіст, один з найкращих гравців світу.",
        "followers": 580000000
    },
    {
        "name": "Nicki Minaj",
        "description": "Американська реперка, співачка та акторка.",
        "followers": 200000000
    },
    {
        "name": "Katy Perry",
        "description": "Американська співачка та авторка пісень.",
        "followers": 190000000
    },
    {
        "name": "UEFA Champions League",
        "description": "Офіційний аккаунт Ліги чемпіонів УЄФА.",
        "followers": 110000000
    },
    {
        "name": "Miley Cyrus",
        "description": "Американська співачка, авторка пісень та акторка.",
        "followers": 210000000
    },
]
indexes = [i for i in range(len(famous_people))]
random.shuffle(indexes)


def is_answer_right(a, b, user_guess):
    if user_guess == 'A' and a["followers"] > b["followers"]:
        print("Good")
        return True
    elif user_guess == 'B' and a["followers"] < b["followers"]:
        print("Good")
        return True
    else:
        print("You lose")
        return False


def game():
    points = 0
    for i in range(len(indexes) - 1):
        a = famous_people[indexes[i]]
        b = famous_people[indexes[i+1]]

        print("Compare A: ", a["name"], a["description"])
        print(vs_logo)
        print("Against B: ", b["name"], b["description"])

        user_guess = input("Who has more followers? Type 'A' or 'B': ")

        if is_answer_right(a, b, user_guess):
            points += 1
        else:
            return points
    return points

points = game()
print(points)
