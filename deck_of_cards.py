class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	def __repr__(self):
		#return "{} of {}".format(self.value, self.suit)
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(value, suit) for suit in suits for value in values]
		print(self.cards)
	def count(self):
		return len(self.cards)

d = Deck()
print(d.count())