import random


def horror_game():
        
    characters = [
        'Freddy Krueger', 'Jason Voorhees', 'Michael Myers', 'Leatherface', 'Ghostface', 'Chucky', 'Pinhead', 'Jigsaw', 
        'Hannibal Lecter', 'Norman Bates', 'Samara', 'Pennywise', 'Nun'
    ]

    random_character = random.choice(characters)
    random_character = random_character.lower()

    print('--- HORROR GAME ---')
    print('GUESS THE CHARACTER, BEFORE IT FINDS YOU...')
    print("Good Luck, you'll need it.\n")

    turns = 12
    guesses = ''

    while turns > 0:

        failed = 0

        for char in random_character:
            if char in guesses:
                print(char)
            else:
                print('_')
                failed += 1
        
        if failed == 0:
            print('\nUnfortunatelly, you win...')
            print('If you dare, play again.')
            print(f'The character that almost got you was {random_character}.\n')
            break

        guess = input('\nGuess the character: ')
        guesses += guess

        if guess not in random_character:

            turns -= 1
            print(f'Wrong... You are {turns} steps away from your killer.')

            if turns == 0:
                print(f'Huuuuugh, you just died... The one that killed you was {random_character}.\n')

if __name__ == '__main__':
    horror_game()






