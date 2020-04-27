import random
import sys
import click

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
		print("<><><>ROLL DICE<><><>")

		self.userNumDice = click.prompt("How many dice?", type=click.IntRange(1,100))
		self.userSides = click.prompt("How many sides?", type=click.IntRange(1,100))
		self.userRolls = click.prompt("How many rolls?", type=click.IntRange(1,100))

		self.user_inputs = (self.userNumDice, self.userSides, self.userRolls)
		return self.user_inputs

	def user_prompt(self):
		valid_response = ('r','q')
		self.userPrompt = click.prompt("\nShaking dice...", type=click.Choice(['r','q'], case_sensitive=False))
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
		keep_on_playing = click.prompt(f"\nPlay again?", type=click.Choice(['y','n'], case_sensitive=False))
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


























