import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
your_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
print(game_list[your_chose])

computer_chose = random.randint(0,2)
print(game_list[computer_chose])

if your_chose == computer_chose:
    print("Draw")
elif your_chose == 2 and computer_chose == 0:
    print("You lose")
elif your_chose == 0 and computer_chose == 2:
    print("You win")
elif your_chose < computer_chose:
    print("You lose")
else:
    print("You win")

