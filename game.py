import sys

from character import Character
from monster import Goblin
from monster import Troll
from monster import Dragon

class Game:


# setup game, what the user sees at the start of the game

	def setup(self):
		print('='*60)
		print("Hack 'n Slash: The ultimate battle between human and monster!")
		print('='*60)
		self.player = Character()  
		self.monsters = [Goblin(),
						Troll(),
						Dragon()]
		self.monster = self.get_next_monster() 


# get next monster using this method

	def get_next_monster(self):  # whenever getNextMonster is called it will 'grab' a monster from the list

		try:
			return self.monsters.pop() # try popping a monster from the monsters list
		except IndexError: # if there is an error due to index error i.e. list is empty
			return None		

# monsters turn

	def monsters_turn(self):
		print('='*30)
		print("It is now the Monster's turn")
		print('='*30)
		
		# if the monster attacks it either hits the character or it misses
		if self.monster.attack():
			print('The {} is attacking you now!'.format(self.monster))
			#if input('Dodge? Y/N ').lower() == 'y':			
			if self.player.dodge():
				print('You dodged their attack, phew!')
			else:
				self.player.hit_points -= 1
				print('Bad luck, you got hit.')
			#else:
				#print('{} hit you for 1 HP'.format(self.monster))
				#self.player.hit_points -= 1
		# if the monster doesn't attack
		else:
			print('The {} is not attacking you this turn. Hooray!'.format(self.monster))

# characters turn

	def users_turn(self):
		print('='*30)
		print("It's now your turn")
		print('='*30)
		# give the user an option to attack, rest or quit
		action = input('What would you like to do? [A]ttack, [R]est or [Q]uit: ').lower()

		# if user chooses to attack

		if action == 'a':
			print('You are attacking the {}'.format(self.monster))	
			if self.player.attack():
				if self.monster.dodge():
					print('The {} dodged your attack. Bummer!'.format(self.monster))
				else:
					print('The {} tried to dodge but you hit it!'.format(self.monster))
					if self.player.level_up():
						# reduce monster hit point by weapon max damage selected by user
						self.monster.hit_points -= self.player.weapon['damage'] + 0.5  
					else:
						self.monster.hit_points -= self.player.weapon['damage']
					print('You hit the {} with your {}!'.format(self.monster, self.player.weapon['type']))	
			else:
				print('You missed')
			
		elif action == 'r':
			self.player.rest()
			print('You decided to rest and gained +1 HP!')
			
		elif action == 'q':
			sys.exit()	# standard python way to exit program

		else:
			self.player.turn()
	
			
# end game scenario

	def clean_up(self):
	# if the monsters hit point equals 0 or less i.e. it is 'dead' then add exp to character
		if self.monster.hit_points <= 0:
			self.player.experience += self.monster.experience 
			print('You successfully eliminated the {}!'.format(self.monster))

			self.monster = self.get_next_monster()
		
# define __init__ condition

	def __init__(self):
		self.setup()
		
		# Create counter to track number of turns taken during the game
		turns = 1
		# Do this while loop as long as player has hit points and there is at least one monster
		while self.player.hit_points and (self.monster or self.monsters): 
			print('='*60)
			print('Turns taken: #{}'.format(turns))
			print('='*60)
			print('You: {}'.format(self.player))
			print('Monster: {}'.format(self.monster))
			self.monsters_turn()
			self.users_turn()
			self.clean_up()
			continue_on = input('Continue to next turn? [Y]es or [N]o: ').lower()
			if continue_on == 'n':
				sys.exit()
			turns += 1
    
		# if there are no more monsters left and player still has hit points   
		if self.player.hit_points:
			print('*'*60)
			print("You win!")
			print('*'*60)
		# if player has not more hit points and there is at least one monster left i.e. with HP
		elif self.monsters or self.monsters: 
			print('*'*60)
			print("You lose!")
			print('*'*60)
		sys.exit()

Game() # call Game class to initiate game module