import random

class Actor():

	possible_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	cards_values = [(1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	def __init__(self):
		self.sum_of_cards = 0
		self.cards = []
		self.tag = ""

	def initializeCards(self):
		for i in range(2):
			index = random.randint(0,12)
			if(self.possible_cards[index] != 'A'):
				self.sum_of_cards += self.cards_values[index]
				self.cards.append((self.possible_cards[index], self.cards_values[index]))
			else:
				if(self.tag == "player"):
					a_value = self.assertValueOfA()
					self.sum_of_cards += a_value
				else:
					a_value = self.cards_values[0][1]
					self.sum_of_cards += a_value
				self.cards.append((self.possible_cards[index], a_value))

	def hit(self):
		index = random.randint(0,12)
		if(self.possible_cards[index] != 'A'):
				self.sum_of_cards += self.cards_values[index]
				self.cards.append((self.possible_cards[index], self.cards_values[index]))
		else:
			if(self.tag == "player"):
				a_value = self.assertValueOfA()
				self.sum_of_cards += a_value
			else:
				if(self.sum_of_cards < 11):
					a_value = self.cards_values[0][1]
					self.sum_of_cards += a_value
				else:
					a_value = self.cards_values[0][0]
					self.sum_of_cards += a_value
			self.cards.append((self.possible_cards[index], a_value))

	def checkForACard(self):
		for card, value in self.cards:
			if card == 'A':
				if value == self.cards_values[0][1]:
					value = self.cards_values[0][0]
					return True

		return False

	def assertValueOfA(self):
		a_value = 0

		if self.sum_of_cards < 11:
			while(a_value != 11 and a_value != 1):
				a_value = int(input("Want your 'A' card to have value 1 or 11?: "))
			
				if(a_value != 11 and a_value != 1):
					print("Invalid value, try again!\n")
		else:
			a_value = 1
			#print("'A' card assigned value 1.\n")

		return a_value

	def play(self):
		self.hit()

		while(self.sum_of_cards > 21):
			a_card_present = self.checkForACard()

			if(a_card_present == False):
				break