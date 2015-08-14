import random

from combat import Combat # enable monster class to use attack and defend behaviours

COLORS = ['red', 'blue', 'green', 'gold']


class Monster(Combat):

#attributes common to all monsters, min and max hit points are related to attack
	
	min_hit_points = 1
	max_hit_points = 1 
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

# create init method

	def __init__(self, **kwargs): # **kwargs allow you to define an arbitrary number of keyword arguments
		# initialise Monster attributes of hit points, exp and color using random
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)
		
		for key, value in kwargs.items():
			setattr(self, key, value)
		
# create __str__ to return summary of monster to user

	def __str__(self):
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(), # title() capitalises each word
												self.__class__.__name__,
												self.hit_points,
												self.experience)

# define battlecry for each monster

	def battleCry(self):
		return self.sound.upper()

#create class for each monster which inherits attributes of Monster class

class Goblin(Monster):
	max_hit_points = 3
	max_experience = 2
	sound = 'Eorrrk'

	
class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 6
	min_experience = 2
	max_experience = 6
	sound = 'Nagghhr'
	

class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 12
	sound = 'Hwroaaagggh'