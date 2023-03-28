import random

def random_number():
    random_choice = random.randint(1, 100)
    return random_choice

def game():
    lives = 0
    continue_playing = True
    computer_number = random_number()
    chosen_difficulty = input('Would you like "easy" or "hard"? ')
    if chosen_difficulty.lower() == 'easy':
        lives = 10
        print(f'You have chosen easy. You have {lives} lives left.')
    else:
        lives = 4
        print(f'You have chosen hard. You have {lives} lives left.')
    
    while continue_playing:
        guess = int(input('Guess a number between 1 and 100: '))
        if guess == computer_number:
            print('Congratulations, you guessed the number!')
            continue_playing = False
        elif guess > computer_number:
            print('Too high!')
            lives -= 1
        else:
            print('Too low!')
            lives -= 1
        
        if lives == 0:
            print('Sorry, you ran out of lives.')
            continue_playing = False

while True:
    answer = input('Would you like to play a game? (y/n) ')
    if answer.lower() == "y":
        print("Great! Let's play.")
        game()
        break
    elif answer.lower() == "n":
        print('Okay, maybe another time.')
        break
    else:
        print("Sorry, I didn't understand your response.")