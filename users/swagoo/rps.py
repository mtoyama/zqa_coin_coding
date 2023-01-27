import random
choices = {"rock": "scissors", "paper": "rock", "scissors" : "paper"}

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
            import random
            player2 = random.randrange(1, 4)

        if player1 == player2:
            print("draw")
            draw += 1
            scoreboard(win, loss, draw)
        elif player1 == 1 and player2 == 2:
            print("lose")
            loss += 1
            scoreboard(win, loss, draw)
        elif player1 == 1 and player2 == 3:
            print("win")
            win += 1
            scoreboard(win, loss, draw)

        elif player1 == 2 and player2 == 1:
            print("win")
            win += 1
            scoreboard(win, loss, draw)
        elif player1 == 2 and player2 == 3:
            print("lose")
            loss += 1
            scoreboard(win, loss, draw)

        elif player1 == 3 and player2 == 1:
            print("lose")
            loss += 1
            scoreboard(win, loss, draw)
        elif player1 == 3 and player2 == 2:
            print("win")
            win += 1
            scoreboard(win, loss, draw)

        elif player1 == 4:
            print("restart")
            win = 0
            loss = 0
            draw = 0
            player_select = input("Single player or multiplayer? ").lower()

        elif player1 == 5:
            print("I knew you were soft...")
            break

        else:
            print("That is not a valid option. Please enter the number of your choice.")

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
