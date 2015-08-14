import random

from combat import Combat


class Character(Combat):

# standard attributes that a character starts off with each time the game is run

	max_attack = 10
	experience = 0
	base_hit_points = 10
	
# define attack method

	def attack(self):
		roll = random.randint(1, self.max_attack)
		# if user selects sword for weapon, add one to max attack value return by roll
		if self.weapon['type'] == 'sword':
			roll += 2
		if self.weapon['type'] == 'axe':
			roll += 1
		return roll > 4
	
# define select weapon method

	def getWeapon(self):
		weapon_choice = input('Choose your weapon: A [S]word, an [A]xe or a [C]lub? ').lower()
		
		if weapon_choice in 'sac':
			if weapon_choice == 's':
				return {'type':'sword', 'damage':3}
			elif weapon_choice == 'a':
				return {'type':'axe', 'damage':2}
			else:
				return {'type':'club', 'damage':1}
		else:
			return self.getWeapon() # call getWeapon method if user inputs nothing or different selection
	
	
	def __init__(self, **kwargs):
		# user sees this every time the class is initialised i.e. at the start of the 'game'
		self.name = input('What is your name oh brave soul? ')
		self.weapon = self.getWeapon()
		self.hit_points = self.base_hit_points
		
		for key, value in kwargs.items():
			setattr(self, key, value)
	
	def __str__(self):
		return '{}, HP: {}, EXP: {}'.format(self.name, self.hit_points, self.experience)
	
	def rest(self):
		if self.hit_points < self.base_hit_points:  # ensure character can't amase more than base_hit_points
			self.hit_points += 1 # if player decides to rest for their turn, add one additional hit point to base score
			
	def levelUp(self):
		return self.experience >= 5 # when character reaches exp of 5 or more