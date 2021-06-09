import random

# def winner(x,y):
#     if x == 'rock':
#         if y == 'paper':
#             print("You lose!")
#         else:
#             print("You win!")
#     else:
#         if x == 'paper':
#             if y == ''
    


def main():
    roshambo = ['rock', 'paper', 'scissors']
    pc_choice = random.choice(roshambo)
    i = int(input("""Choose 1, 2 or 3
    1. Rock
    2. Paper
    3. Scissors\n"""))
    player_choice = roshambo[i-1]

    print(f"You chose {player_choice}")
    print(f"The computer chose {pc_choice}")

    #winner(player_choice, pc_choice)
main()