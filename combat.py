import random


class Combat:
# define attributes common for attack and dodge
	max_attack = 6
	max_dodge = 6

# define dodge behaviour
	def dodge(self):
		roll = random.randint(1, self.max_dodge)
		print('Dodge roll: {}'.format(roll))
		return roll > 4

# define attack behaviour

	def attack(self):
		roll = random.randint(1, self.max_attack)
		print('Attack roll: {}'.format(roll))
		return roll > 4 # only return output if value of roll is greater than 4
	

