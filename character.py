import unit
import attack

class Character(unit.Unit):
	def __init__(self, x, y, name, symbol, health, units, attacks):
		unit.Unit.__init__(self, x, y, name, symbol, True)
		self.health = health
		self.units = units
		self.attacks = attacks

	def move_up(self):
		self.symbol = '^'
		for unit in self.units:
			if self.x == unit.x and self.y - 1 == unit.y:
				break
		else:
			self.y = self.y - 1

	def move_down(self):
		self.symbol = 'v'
		for unit in self.units:
			if self.x == unit.x and self.y + 1 == unit.y:
				break
		else:
			self.y = self.y + 1		

	def move_left(self):
		self.symbol = '<'
		for unit in self.units:
			if self.x - 1 == unit.x and self.y == unit.y:
				break
		else:
			self.x = self.x - 1

	def move_right(self):
		self.symbol = '>'
		for unit in self.units:
			if self.x + 1 == unit.x and self.y == unit.y:
				break
		else:
			self.x = self.x + 1		

	def get_melee_attack_location(self):
		ax = self.x
		ay = self.y
		if self.symbol == '>': ax = ax + 1
		if self.symbol == '<': ax = ax - 1
		if self.symbol == '^': ay = ay - 1
		if self.symbol == 'v': ay = ay + 1
		if self.symbol == '0': ax, ay = 0, 0
		return ax, ay

	def melee_attack(self):
		damage = 1
		ax, ay = self.get_melee_attack_location()
		att = attack.Attack(ax, ay, '/')
		self.attacks.append(att)

		for unit in self.units:
			if ax == unit.x and ay == unit.y:
				if unit.isKillable:
					unit.take_damage(damage)

	def take_damage(self,damage):
		if self.isKillable == True:
			self.health = self.health - damage
			self.check_alive()

	def check_alive(self):
		if self.health <= 0:
			self.health = 0
			self.kill()			