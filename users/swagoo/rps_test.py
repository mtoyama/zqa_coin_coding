import random

outcomes = [
    (1, 1, "draw"),
    (1, 2, "Player 2 wins"),
    (1, 3, "Player 1 wins"),
    (2, 1, "Player 1 wins"),
    (2, 2, "draw"),
    (2, 3, "Player 2 wins"),
    (3, 1, "Player 2 wins"),
    (3, 2, "Player 1 wins"),
    (3, 3, "draw"),
]

def determine_outcome(player1, player2):
    for outcome in outcomes:
        if player1 == outcome[0] and player2 == outcome[1]:
            return outcome[2]
    return "Invalid input"

def scoreboard(win, loss, draw):
    print(f"Player 1 wins: {win}\nPlayer 2 wins: {loss}\ndraws: {draw}")

def player1_input():
    return int(input("""Player 1: please select a number: (1) rock, (2) paper, (3) scissors, (4) restart, (5) quit. 
    >"""))

def player2_input():
    return int(input("""Player 2: please select a number: (1) rock, (2) paper, (3) scissors, (4) restart, (5) quit. 
    >"""))

def rock_paper_scissors(win, loss, draw, player_select):

    while True:

        if player_select == "multiplayer":
            player1 = player1_input()
            player2 = player2_input()
        else:
            player1 = player1_input()
            player2 = random.randrange(1, 4)

        outcome = determine_outcome(player1, player2)
        print(outcome)

        if outcome == "Player 1 wins":
            win += 1
        elif outcome == "Player 2 wins":
            loss += 1
        elif outcome == "draw":
            draw += 1
        elif outcome == "Invalid input":
            print("Invalid input. Please enter a valid number.")

        scoreboard(win, loss, draw)
        
        if player1 == 4:
            print("restart")
            win = 0
            loss = 0
            draw = 0
            player_select = input("Single player or multiplayer? ").lower()

        elif player1 == 5:
            print("I knew you were soft...")
            break
        
#################################################################################################################

win = 0
loss = 0
draw = 0

play = input("Do you want to play a game you sicko? ").lower()

if play == "yes":
    player_select = input("Single player or multiplayer? ").lower()
    rock_paper_scissors(win, loss, draw, player_select)
else:
    print("I didn't want to play either.")
