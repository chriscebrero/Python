print("Rock...")
print("Paper...")
print("Scissors!!")

player1 = input("Player 1, make your move: ")
print("***NO CHEATING***" * 20)
player2 = input("Player 2, make your move: ")

if player1 == player2:
	print("It's a tie...Unbelievable!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player 1 Wins")
	elif player2 == "paper":
		print("Player 2 Wins")
elif player1 == "paper":
	if player2 == "rock":
		print("Player 1 Wins")
	elif player2 == "scissors":
		print("Player 2 Wins")
elif player1 == "scissors":
	if player2 == "paper":
		print("Player 1 Wins")
	elif player2 == "rock":
		print("Player 2 Wins")
else:
	print("Start over!")

