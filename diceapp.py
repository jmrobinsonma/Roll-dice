import random
import sys
import click

class RollDice:
	def __init__(self, user_num_dice=0, user_sides=0, user_rolls=0):
		self.user_num_dice = user_num_dice
		self.user_sides = user_sides
		self.user_rolls = user_rolls
		self.rolled = 0
		self.user_list = []
		self.user_inputs = ()
		self.user_prompt = ""
		self.rolled_num = 0
		self.play_again = False
		self.quit = False

	def get_user_inputs(self):
		print("<><><>ROLL DICE<><><>")

		self.user_num_dice = click.prompt("How many dice?", type=click.IntRange(1,100))
		self.user_sides = click.prompt("How many sides?", type=click.IntRange(1,100))
		self.user_rolls = click.prompt("How many rolls?", type=click.IntRange(1,100))

		self.user_inputs = (self.user_num_dice, self.user_sides, self.user_rolls)
		return self.user_inputs

	def prompt_user(self):
		valid_response = ('r','q')
		self.user_prompt = click.prompt("\nShaking dice...", type=click.Choice(['r','q'], case_sensitive=False))
		return self.user_prompt

	def roll_dice(self, user_inputs):
		user_num_dice, user_sides, user_rolls = self.user_inputs
		roll_nums = []

		for x in range(0, user_num_dice):
			self.rolled_num = random.randint(1, user_sides)
			self.user_list.append(self.rolled_num)
			roll_nums.append(self.rolled_num)
		self.rolled += 1
		results = f"\nRoll {self.rolled}\nYou rolled:----{roll_nums}----\
					\n({user_rolls - self.rolled} rolls remain)\nYour rolls: {self.user_list}"
		return print(results)


	def play_again_prompt(self):
		keep_on_playing = click.prompt(f"\nPlay again?", type=click.Choice(['y','n'], case_sensitive=False))
		if keep_on_playing == 'y':
			self.play_again = True
			return self.play_again
		else:
			return self.play_again

	def quit_game(self):
		return print("Thanks for Playing!")


def main():
	rolled = 0
	user1 = RollDice()
	user1.get_user_inputs()
	while rolled < user1.user_rolls:
		user1.prompt_user()
		if user1.user_prompt == 'r':
			user1.roll_dice(user1.user_inputs)
			rolled += 1
		elif user1.user_prompt == 'q':
			user1.quit_game()
			sys.exit()
	user1.play_again_prompt()
	if user1.play_again:
		main()
	else:
		user1.quit_game()


if __name__ == '__main__':
	main()
