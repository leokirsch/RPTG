class Unit:
	def __init__(self, x, y, name, symbol, isKillable):
		self.x = x
		self.y = y
		self.name = name
		self.symbol = symbol
		self.isAlive = True
		self.isKillable = isKillable

	def take_damage(self,damage):
		pass

	def check_alive(self):
		pass

	def kill(self):
		if self.isKillable:
			self.isAlive = False