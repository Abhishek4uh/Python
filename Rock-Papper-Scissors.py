#This is the Game Rock-Papper-Scissors in Python

import random
def Play():
    print("'r' for Rock")
    print("'p' for Papper")
    print("'s' for Scissors")
    user=input("Enter Your choice")
    computer=random.choice(['r','p','s'])
    print("You select ",user)
    print("Computer Select",computer)

    if user==computer:
        return 'It\'s a tie'

    if is_win(user,computer):
        return 'You Won The Game! '

    print("You select ",user)
    print("Computer Select",computer)
    return "You Lost"
def is_win(player,opponent):
    if (player=='r' and opponent=='s') or(player=='s' and opponent=='p') or (player=='p' and opponent== 'r'):
        return True
print(Play())
