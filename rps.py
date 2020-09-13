import random
print("""!!ROCK!!  !!PAPER!!  !!SCISSORS!!""")
print("""r ----> Rock
p ----> Paper
S ----> Scissors """)
moves = ["r", "p", "s"]
player_wins = ["pr", "sp", "rs"]
while True:
    print("""
     ROCK
     PAPER
     SCISSORS!!!
    """)
    player_move = input("Your Move :")
    computer_move = random.choice(moves)
    print("You :", player_move)
    print("Me :", computer_move)
    if player_move == computer_move:
        print("""
        TIE!
        """)
        break
    elif player_move + computer_move in player_wins:
        print("""
        You WIN!!
        """)
        break
    else:
        print("""
        You lose!
        """)
        break
print("break")