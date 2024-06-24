import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Won with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You won 😁"
    elif user_score > computer_score:
        return "You won 😃"
    else:
        return "You lose 😤"


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    pick = deal_card()
    if pick == 11 and (sum(cards) + 11) > 21:
        cards.append(1)
    else:
        cards.append(pick)
    return sum(cards)


def blackjack():
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    user_score = sum(user_card)
    computer_score = sum(user_card)

    print(f"Computer's first card: {computer_card[0]}")
    while user_score < 21:
        print(f"Your cards: {user_card}, current score: {user_score}")
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() != 'y':
            break
        user_score = calculate_score(user_card)

    while computer_score <= 17:
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}"
          f"\nComputer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    user_card = []
    computer_card = []

    blackjack()
