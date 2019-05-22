from Actor import Actor

class Player(Actor):

	def __init__(self):
		Actor.__init__(self)
		self.tag = "player"