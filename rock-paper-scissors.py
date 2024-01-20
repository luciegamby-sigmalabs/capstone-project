import random


def make_choice():
    options = ['Rock', 'Paper', 'Scissors']
    choice = random.choice(options)
    return choice


def check_winner(bot_choice, player_choice):
    if bot_choice == player_choice:
        print('Tie')
        return 0
    elif bot_choice == 'Rock':
        if player_choice == 'Paper':
            print('Paper covers Rock! Player wins!')
            return 1
        else:
            print('Rock smashes Scissors! I win!')
            return 2
    elif bot_choice == 'Paper':
        if player_choice == 'Scissors':
            print('Scissors cuts Paper! Player wins!')
            return 1
        else:
            print('Paper covers Rock! I win!')
            return 2
    elif bot_choice == 'Scissors':
        if player_choice == 'Rock':
            print('Rock smashes Scissors! Player Wins')
            return 1
        else:
            print('Scissors cuts Paper! I win')
            return 2


print('Welcome to Rock, Paper, Scissors!')
bot_score = 0
player_score = 0
while True:
    player_choice = input(
        'Please type either \'Rock\', \'Paper\', or \'Scissors\': ').title()
    if player_choice == 'Rock' or player_choice == 'Paper' or player_choice == 'Scissors':
        pass
    else:
        print('Invalid Input. Please try again')
        continue

    bot_choice = make_choice()
    print(f'I chose {bot_choice}!')
    winner = check_winner(bot_choice, player_choice)

    if winner == 1:
        player_score += 1
    elif winner == 2:
        bot_score += 1

    play_again = input('Would you like to play again? Y/N: ').upper()
    if play_again == 'Y':
        print('Let\'s go!')
        continue
    elif play_again == 'N':
        print('Ending game...')
        break
    else:
        print('Invalid response - we\'ll play one more just to be sure...')
        continue

print(f'Final Scores! You: {player_score}, Me: {bot_score}')
if player_score == bot_score:
    print('We tied! Great Game!')
elif player_score > bot_score:
    print('You won! Well Done!')
else:
    print('You lost! Better luck next time!')
print('Thanks for playing!')
