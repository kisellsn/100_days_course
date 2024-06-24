import random

art = """
   ___                     _                ___                   
  / __| _  _  ___  ___ ___(_) _ _   __ _   / __| __ _  _ __   ___ 
 | (_ || || |/ -_)(_-<(_-<| || ' \ / _` | | (_ |/ _` || '  \ / -_)
  \___| \_,_|\___|/__//__/|_||_||_|\__, |  \___|\__,_||_|_|_|\___|
                                   |___/                          
"""


def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
        return 10
    else:
        return 5


def is_correct(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("too low.")
        return False
    else:
        print("Congratulations! You guessed the number")
        return True


def game():
    print(f"{art}\nWelcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 101)
    hearts = set_difficulty()

    while hearts > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if is_correct(guess, answer):
            return
        else:
            hearts -= 1

    print("Sorry. The number was " + str(answer) + ".")
    return


game()
