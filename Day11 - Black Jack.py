import random

cards = {
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 10,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 10,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 10,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 10,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def deal():
    card = random.choice(list(cards.keys()))
    value = cards[card]
    del cards[card]  # Remove the dealt card from the deck
    return card, value

def full_deal():
    dealers_card1, dealers_card1_value = deal()
    dealers_card2, dealers_card2_value = deal()
    players_card1, players_card1_value = deal()
    players_card2, players_card2_value = deal()
    print(f"Dealer's cards are {dealers_card1} + ???  ({dealers_card1_value})")
    players_count = int(players_card1_value) + int(players_card2_value)  # Value of both cards from the player
    print(f"Your cards are {players_card1}  + {players_card2}  ({players_count})")
    return players_count, dealers_card1_value + dealers_card2_value

def play_game():
    players_count, dealers_count = full_deal()
    while True:
        action = input("Do you want to hit or stand? ")
        if action == 'hit':
            card, value = deal()
            players_count += value
            print(f"You drew a {card} ({value})")
            print(f"Your hand value is now {players_count}")
            if players_count > 21:
                print("You have gone bust!")
                break
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'")
    print("Dealer's turn...")
    while dealers_count < 17:
        card, value = deal()
        dealers_count += value
        print(f"Dealer drew a {card} ({value})")
        print(f"Dealer's hand value is now {dealers_count}")
    if dealers_count > 21:
        print("Dealer has gone bust!")
    else:
        print(f"Dealer stands at {dealers_count}")
    # Compare hand values to determine the winner

play_game()