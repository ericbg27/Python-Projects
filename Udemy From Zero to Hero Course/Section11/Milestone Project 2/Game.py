from Player import Player
from Dealer import Dealer

player_1 = Player()
dealer = Dealer()
end = False

def initialize():
	player_1.initializeCards()
	dealer.initializeCards()

	print(dealer)

def gamePlay():
	global end
	print("Distributing cards...\n")
	initialize()
	print("It's player's turn! \n")
	print("One of the House's card is: " + dealer.cards[0][0] + "\n")

	print("Player's current sum: " + str(player_1.sum_of_cards))
	decision = askForDecision()
	while decision == "hit" and end == False:
		player_1.play()

		if player_1.sum_of_cards == 21:
			print("Congratulations! Player won!")
			end = True
		elif player_1.sum_of_cards > 21:
			print("Player blew! The House won!")
			end = True
		if end == False:
			print("Player's current sum: " + str(player_1.sum_of_cards))
			decision = askForDecision()

	while end == False:
		dealer.play()

		if dealer.sum_of_cards >= player_1.sum_of_cards:
			print("The House won!")
			end = True
		elif dealer.sum_of_cards > 21:
			print("The House blew! Player won!")
			end = True

def askForDecision():
	decision = input("Want to hit or pass?: ")

	if decision == "hit" or decision == "pass":
		return decision
	else:
		print("Invalid decision. Try again.\n")
		decision = askForDecision()

if __name__ == "__main__":
	gamePlay()