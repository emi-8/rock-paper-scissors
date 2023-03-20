import random


def play():
    player = input("Pick your choice: 'r' for rocks, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose: {computer}')

    if player == computer:
        return print("It's a tie!")
    
    if isWin(player, computer):
        return print('Congrats! You win!')
    
    return print('Sorry, you lost!')


def isWin(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True


play()
