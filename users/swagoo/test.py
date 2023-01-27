#player choices are just the strings "rock", "paper", or "scissors"
def winner(p1_choice, p2_choice):
  if not a_valid_choice:
    # prompt user to try again
elif p1_choice == p2_choice:
    # it's a draw
else:
    # check if player 1 wins else player 2 wins
    # using a list ["rock", "paper", "scissors"] note the order of the list is such that the next item defeats the previous
    winner = "Player 1" if weapons.index(p1_choice) == (weapons.index(p2_choice) + 1) % 3 else "Player 2"
    
    # or using a dictionary
    winner = "Player 1" if choices[p1_choice] == p2_choice else "Player 2"

  print(f"{winner} wins")