import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|/  |
 / /  |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|/  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|/  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ['apple', 'banana', 'cherry', 'elephant', 'aggregate', 'alien', 'multiworld', 'hangman']
chosen_word = random.choice(words)

result_word = []
for i in range(len(chosen_word)):
    result_word += '_'

hearts = 6

while hearts > 0 and ''.join(result_word) != chosen_word:
    print(stages[hearts])
    print(''.join(result_word))
    user_input = input('Guess a letter: ').lower()
    if user_input in ''.join(result_word):
        hearts -= 1
        print('Already been there')
    elif user_input in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == user_input:
                result_word[i] = user_input
    else:
        hearts -= 1
        print('You lost one heart')

if hearts == 0:
    print(stages[hearts])
    print('You are dead!')
else:
    print('You won!')
