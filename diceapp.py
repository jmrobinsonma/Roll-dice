import random
import sys

class RollDice:
	def __init__(self, userNumDice=0, userSides=0, userRolls=0):
		self.userNumDice = userNumDice
		self.userSides = userSides
		self.userRolls = userRolls
		self.rolled = 0
		self.userList = []
		self.user_inputs = ()
		self.userPrompt = ""
		self.rolledNum = 0
		self.playAgain = False
		self.quit = False

	def get_user_inputs(self):
		print("---ROLL DICE---")
		self.userNumDice = int(input("How many dice?\n-->"))
		self.userSides = int(input("How many sides?\n-->"))
		self.userRolls = int(input("How many rolls?\n-->"))
		self.user_inputs = (self.userNumDice, self.userSides, self.userRolls)
		return self.user_inputs

	def user_prompt(self):
		valid_response = ('r','q')
		self.userPrompt = input("\nPress 'r' to roll the dice 'q' to quit\n --> ")
		while self.userPrompt not in valid_response:
			self.userPrompt = input("\nPress \'r' to roll the dice\nPress \'q' to quit\n --> ")
		return self.userPrompt

	def roll_dice(self, user_inputs):
		userNumDice, userSides, userRolls = self.user_inputs
		roll_nums = [] 

		for x in range(0, userNumDice):  
			self.rolledNum = random.randint(1, userSides)
			self.userList.append(self.rolledNum)
			roll_nums.append(self.rolledNum)
		self.rolled += 1
		results = f"\nRoll {self.rolled}\nYou rolled:----{roll_nums}----\
					\n({userRolls - self.rolled} rolls remain)\nYour rolls: {self.userList}"
		return print(results)

	
	def play_again(self):
		valid_response = ('y','n')
		keep_on_playing = input(f"\nGame over. Play again? 'y' or 'n': ")
		if keep_on_playing not in valid_response:
			keep_on_playing = input(f"\nGame over. Play again? 'y' or 'n': ")
		else:
			if keep_on_playing == 'y':
				self.playAgain = True
				return self.playAgain
			else:
				return self.playAgain
			
	def quit_game(self):
		return print("Thanks for Playing!")


def main():
	rolled = 0
	user1 = RollDice()
	user1.get_user_inputs()
	while rolled < user1.userRolls:
		user1.user_prompt()
		if user1.userPrompt == 'r':
			user1.roll_dice(user1.user_inputs)
			rolled += 1
		
		elif user1.userPrompt == 'q':
			user1.quit_game()
			sys.exit()
	user1.play_again()
	if user1.playAgain:
		main()
	else:
		user1.quit_game()


if __name__ == '__main__':
	main()


























