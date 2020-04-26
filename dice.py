import random

print("---ROLL DICE---")

rolls = 0
userList = []
userDicelist = []

userDice = int(input("How many dice?\n-->"))
userDicelist.append(userDice)
y = userDicelist[0]

userRolls = int(input("How many rolls?\n-->"))

userSides = int(input("How many sides?\n-->"))

userPrompt = input("\nPress \'r' to roll the dice\nPress \'q' to quit\n -->")

while rolls < userRolls:

	if userPrompt == "r":
		for x in range(0, y):
			userNum = random.randint(1, userSides)
			userList.append(userNum)
		print("\nYou rolled:\n----{}----".format(userNum))
		rolls += 1
		print("\n({} rolls)\n".format(rolls))
		print("Your rolls: {}".format(userList))
		userPrompt = input("Press \'r' to roll the dice -->")
	elif userPrompt == 'q':
		break
	else:
		userPrompt = input("\nPress \'r' to roll the dice\nPress \'q' to quit\n -->")

