def Game():
	print("Welcome to the game!")
	currentPlayer = 1
	BoardStatus = []

	for i in range(1, 10):
		BoardStatus.append(i)

	def PlayingGame(BoardStatus, currentPlayer):
		PrintBoard(BoardStatus)

		print("\n")

		playerChoice = int(input("It's player {} turn! Choose a position from the board above: ".format(currentPlayer)))

		if playerChoice > 9 or playerChoice < 1:
			print("Player position must be in range [1,9]!")
			print("\n")
			PlayingGame(BoardStatus, currentPlayer)

		if BoardStatus[playerChoice-1] != playerChoice:
			print("Position already taken, try again!")
			print("\n")
			PlayingGame(BoardStatus, currentPlayer)

		BoardStatus = AlterBoardStatus(playerChoice, currentPlayer, BoardStatus)

		if CheckWin(BoardStatus) == False and EndGame(BoardStatus) == False:
			if currentPlayer == 1:
				currentPlayer = 2
			else:
				currentPlayer = 1
			PlayingGame(BoardStatus, currentPlayer)

	PlayingGame(BoardStatus, currentPlayer)

def PrintBoard(BoardStatus):
	print('\t\t\t{}\t|\t{}\t|\t{}'.format(BoardStatus[0], BoardStatus[1], BoardStatus[2]))
	print("\t\t\t--\t|\t--\t|\t--")
	print("\t\t\t{}\t|\t{}\t|\t{}".format(BoardStatus[3], BoardStatus[4], BoardStatus[5]))
	print("\t\t\t--\t|\t--\t|\t--")
	print("\t\t\t{}\t|\t{}\t|\t{}".format(BoardStatus[6], BoardStatus[7], BoardStatus[8]))

def AlterBoardStatus(playerChoice, currentPlayer, BoardStatus):
	if currentPlayer == 1:
		BoardStatus[playerChoice-1] = 'x'
	else:
		BoardStatus[playerChoice-1] = 'o'

	return BoardStatus

def CheckWin(BoardStatus):
	for i in range(1,8):
		win = True
		symbol = BoardStatus[i-1]
		if i == 1:
			for j in range(4,8,3):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(2,4):
					if BoardStatus[j-1] != symbol:
						win = False
			if win == False:
				win = True
				for j in range(5,10,4):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:
				print("Here")
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("\n")
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 2:
			for j in range(1,4,2):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(5,9,3):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:		
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 1:
			for j in range(1,3,1):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(6,10,3):
					if BoardStatus[j-1] != symbol:
						win = False
			if win == False:
				win = True			
				for j in range(5,8,2):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 4:
			for j in range(1,8,6):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(5,7,1):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 5:
			for j in range(4,7,2):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(2,9,6):
					if BoardStatus[j-1] != symbol:
						win = False
			if win == False:
				win = True
				for j in range(1,10,8):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 6:
			for j in range(3,10,6):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(4,6,1):
					if BoardStatus[j-1] != symbol:
						win = False
			
			if win == True:
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win
		elif i == 7:
			for j in range(1,5,3):
				if BoardStatus[j-1] != symbol:
					win = False
			if win == False:
				win = True
				for j in range(8,10):
					if BoardStatus[j-1] != symbol:
						win = False
			if win == False:
				win = True
				for j in range(3,6,2):
					if BoardStatus[j-1] != symbol:
						win = False

			if win == True:
				if symbol == 'x':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 1! Thank you for playing!")
				elif symbol == 'o':
					print("\n")
					PrintBoard(BoardStatus)
					print("Congratulations player 2! Thank you for playing!")
				return win

	return False


def EndGame(BoardStatus):
	for i in range(1, 10):
		if BoardStatus[i-1] == i:
			return False

	print("\n")
	PrintBoard(BoardStatus)
	print("It's a draw! Thank you for playing!")

Game()