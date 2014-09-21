
suit = ["heart", "diamond", "spade", "club"]

class Cards:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Blackjack(Cards):
	def __init__(self, suit, value):
		Cards.__init__(self ,suit, value)
		if value == 1:
			self.value = 11
		elif value <= 10:
			self.value = value

bj = Blackjack(suit[1], 6)
print "bj : " + str(bj.suit) + ", " + str(bj.value)


bj = Blackjack(suit[1], 1)
print "bj : " + str(bj.suit) + ", " + str(bj.value)