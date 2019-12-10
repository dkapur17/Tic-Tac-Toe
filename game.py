import click
import shutil
import time
import random
import csv

cols, rows = shutil.get_terminal_size()


def compDecision(compChar, items):

	if compChar == "X":
		playerChar = "O"
	else:
		playerChar = "X"

	# See if comp can win

	# Orthogonally
	for i in range(3):
		if items[i][0] == items[i][1] and items[i][0] == compChar and not items[i][2].isalpha():
			items[i][2] = compChar
			return items
		elif items[i][0] == items[i][2] and items[i][0] == compChar and not items[i][1].isalpha():
			items[i][1] = compChar
			return items
		elif items[i][1] == items[i][2] and items[i][1] == compChar and not items[i][0].isalpha():
			items[i][0] = compChar
			return items

		elif items[0][i] == items[1][i] and items[0][i] == compChar and not items[2][i].isalpha():
			items[2][i] = compChar
			return items
		elif items[0][i] == items[2][i] and items[0][i] == compChar and not items[1][i].isalpha():
			items[1][i] = compChar
			return items
		elif items[1][i] == items[2][i] and items[1][i] == compChar and not items[0][i].isalpha():
			items[0][i] = compChar
			return items

	# Diagonally
	if items[0][0] == items[1][1] and items[0][0] == compChar and not items[2][2].isalpha():
		items[2][2] = compChar
		return items
	elif items[0][0] == items[2][2] and items[0][0] == compChar and not items[1][1].isalpha():
		items[1][1] = compChar
		return items
	elif items[1][1] == items[2][2] and items[1][1] == compChar and not items[0][0].isalpha():
		items[0][0] = compChar
		return items

	# Reverse-Diagonally
	if items[0][2] == items[1][1] and items[0][2] == compChar and not items[2][0].isalpha():
		items[2][0] = compChar
		return items
	elif items[0][2] == items[2][0] and items[0][2] == compChar and not items[1][1].isalpha():
		items[1][1] = compChar
		return items
	elif items[1][1] == items[2][0] and items[1][1] == compChar and not items[0][2].isalpha():
		items[0][2] = compChar
		return items

	# See if player can win

	# Orthogonally
	for i in range(3):
		if items[i][0] == items[i][1] and items[i][0] == playerChar and not items[i][2].isalpha():
			items[i][2] = compChar
			return items
		elif items[i][0] == items[i][2] and items[i][0] == playerChar and not items[i][1].isalpha():
			items[i][1] = compChar
			return items
		elif items[i][1] == items[i][2] and items[i][1] == playerChar and not items[i][0].isalpha():
			items[i][0] = compChar
			return items

		elif items[0][i] == items[1][i] and items[0][i] == playerChar and not items[2][i].isalpha():
			items[2][i] = compChar
			return items
		elif items[0][i] == items[2][i] and items[0][i] == playerChar and not items[1][i].isalpha():
			items[1][i] = compChar
			return items
		elif items[1][i] == items[2][i] and items[1][i] == playerChar and not items[0][i].isalpha():
			items[0][i] = compChar
			return items

	# Diagonally
	if items[0][0] == items[1][1] and items[0][0] == playerChar and not items[2][2].isalpha():
		items[2][2] = compChar
		return items
	elif items[0][0] == items[2][2] and items[0][0] == playerChar and not items[1][1].isalpha():
		items[1][1] = compChar
		return items
	elif items[1][1] == items[2][2] and items[1][1] == playerChar and not items[0][0].isalpha():
		items[0][0] = compChar
		return items

	# Reverse-Diagonally
	if items[0][2] == items[1][1] and items[0][2] == playerChar and not items[2][0].isalpha():
		items[2][0] = compChar
		return items
	elif items[0][2] == items[2][0] and items[0][2] == playerChar and not items[1][1].isalpha():
		items[1][1] = compChar
		return items
	elif items[1][1] == items[2][0] and items[1][1] == playerChar and not items[0][2].isalpha():
		items[0][2] = compChar
		return items

	randX = random.randrange(3)
	randY = random.randrange(3)
	while items[randX][randY].isalpha():
		randX = random.randrange(3)
		randY = random.randrange(3)

	items[randX][randY] = compChar
	return items


def analyseTable(items):

	for i in range(3):
		if items[i][0] == items[i][1] and items[i][1] == items[i][2]:
			if items[i][0] == "X":
				return 1
			else:
				return 2
		if items[0][i] == items[1][i] and items[1][i] == items[2][i]:
			if items[0][i] == "X":
				return 1
			else:
				return 2

	if items[0][0] == items[1][1] and items[1][1] == items[2][2]:
		if items[1][1] == "X":
			return 1
		else:
			return 2
	if items[0][2] == items[1][1] and items[1][1] == items[2][0]:
		if items[1][1] == "X":
			return 1
		else:
			return 2

	return 0


def getInput(playerTurn, items):
	while True:
		choiceLoc = input("\nChoose one of the unfilled boxes by entering the number in it: ")
		while choiceLoc not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			choiceLoc = input("Please only enter a number from 1 to 9: ")

		choiceCoord = parseCoordinate(int(choiceLoc))
		if not items[choiceCoord[0]][choiceCoord[1]].isalpha():
			items[choiceCoord[0]][choiceCoord[1]] = playerTurn
			return items
		else:
			print("That box is already occupied.", end="")


def parseCoordinate(location):
	if location == 1:
		return [0, 0]
	if location == 2:
		return [0, 1]
	if location == 3:
		return [0, 2]
	if location == 4:
		return [1, 0]
	if location == 5:
		return [1, 1]
	if location == 6:
		return [1, 2]
	if location == 7:
		return [2, 0]
	if location == 8:
		return [2, 1]
	if location == 9:
		return [2, 2]


def drawTable(items):
	print()
	for i in range(9):
		for x in range(cols // 2 - 12):
			print(" ", end="")
		for j in range(21):
			if j == 7 or j == 14:
				print("|", end="")
			if i == 2 or i == 5:
				print("_", end="")
			elif i == 1 and j == 3:
				print(items[0][0], end="")
			elif i == 1 and j == 10:
				print(items[0][1], end="")
			elif i == 1 and j == 17:
				print(items[0][2], end="")
			elif i == 4 and j == 3:
				print(items[1][0], end="")
			elif i == 4 and j == 10:
				print(items[1][1], end="")
			elif i == 4 and j == 17:
				print(items[1][2], end="")
			elif i == 7 and j == 3:
				print(items[2][0], end="")
			elif i == 7 and j == 10:
				print(items[2][1], end="")
			elif i == 7 and j == 17:
				print(items[2][2], end="")
			else:
				print(" ", end="")
		print()


def pvc(gameCount, p1Score, p2Score):
	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v COMPUTER".center(cols))

	if gameCount % 2 == 0:
		p1 = "You"
		p2 = "Computer"
	else:
		p1 = "Computer"
		p2 = "You"

	print(p1 + " is X and " + p2 + " is O")
	print("\nHit enter to continue")

	items = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
	result = 0

	for i in range(9):
		click.clear()
		print("TIC TAC TOE".center(cols))
		print("PLAYER v COMPUTER".center(cols))
		print(p1 + " -> X -> " + str(p1Score) + " points")
		print(p2 + " -> O -> " + str(p2Score) + " points")
		drawTable(items)
		print()
		if gameCount % 2 == 0:
			# User is p1
			if i % 2 == 0:
				print(("Your Turn").center(cols))
				items = getInput("X", items)
			else:
				items = compDecision("O", items)
				print((p2 + "'s Turn. Thinking. ").center(cols))
				time.sleep(1)
		else:
			# Comp is p2
			if i % 2 == 0:
				items = compDecision("X", items)
				print((p2 + "'s Turn. Thinking. ").center(cols))
				time.sleep(1)
			else:
				print("Your Turn".center(cols))
				items = getInput("O", items)

		result = analyseTable(items)
		if result != 0:
			break

	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v COMPUTER".center(cols))
	print()
	print()
	drawTable(items)
	print()
	with open("stats.csv", "r") as f:
		reader = csv.reader(f)
		rawList = list(reader)
		statList = rawList[0]
		if result == 0:
			print("It's a DRAW!")
			statList[2] = str(int(statList[2]) + 1)
		elif result == 1:
			if p1 == "You":
				print(p1 + " WIN!")
				statList[0] = str(int(statList[0]) + 1)
			else:
				print(p1 + " WINS!")
				statList[1] = str(int(statList[1]) + 1)
			p1Score += 1
		else:
			if p2 == "You":
				print(p2 + " WIN!")
				statList[0] = str(int(statList[0]) + 1)
			else:
				print(p2 + " WINS!")
				statList[1] = str(int(statList[1]) + 1)
			p2Score += 1

	with open("stats.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerow(statList)

	gameCount += 1
	print("Choose one of the following options:\n")
	print("1. Play another match against the Computer")
	print("2. Play a new game against another player")
	print("3. Return to Main Menu")
	print("4. Quit")

	choice = input("\nChoose one of the options above: ")
	while choice not in ["1", "2", "3", "4"]:
		choice = input("\nPlease choose an option from 1 to 4: ")

	if choice == "1":
		pvc(gameCount, p2Score, p1Score)
	elif choice == "2":
		pvp(True, "", "", 0, 0)
	elif choice == "3":
		main()
	else:
		click.clear()
		print("Goodbye!")
		time.sleep(1)
		click.clear()
		exit()


def pvp(newPlayers, p1Name, p2Name, p1Score, p2Score):
	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v PLAYER".center(cols))

	if newPlayers:
		p1Name = input("Enter Player 1's name: ").upper()
		p2Name = input("Enter Player 2's name: ").upper()

	print("\n" + p1Name + " is X and " + p2Name + " is O\n")
	input("Hit enter to continue")

	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v PLAYER".center(cols))

	items = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
	result = 0
	for i in range(9):
		click.clear()
		print("TIC TAC TOE".center(cols))
		print("PLAYER v PLAYER".center(cols))
		print(p1Name + " -> X -> " + str(p1Score) + " points")
		print(p2Name + " -> O -> " + str(p2Score) + " points")

		drawTable(items)
		print()
		# Player 1's Turn
		if i % 2 == 0:
			print((p1Name + "'s Turn.").center(cols))
			items = getInput("X", items)

		else:
			print((p2Name + "'s Turn.").center(cols))
			items = getInput("O", items)
		result = analyseTable(items)
		if result != 0:
			break

	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v PLAYER".center(cols))
	print()
	print()
	drawTable(items)
	print()
	if result == 0:
		print("It's a DRAW!")
	elif result == 1:
		print(p1Name + " WINS!")
		p1Score += 1
	else:
		print(p2Name + " WINS!")
		p2Score += 1

	print("Choose one of the following options:\n")
	print("1. Play another match: " + p1Name + " v " + p2Name)
	print("2. Play a new game between different players")
	print("3. Play against the computer")
	print("4. Return to Main Menu")
	print("5. Quit")

	choice = input("\nChoose one of the options above: ")
	while choice not in ["1", "2", "3", "4", "5"]:
		choice = input("\nPlease choose an option from 1 to 5: ")

	if choice == "1":
		pvp(False, p2Name, p1Name, p2Score, p1Score)
	elif choice == "2":
		pvp(True, "", "", 0, 0)
	elif choice == "3":
		pvc()
	elif choice == "4":
		main()
	else:
		click.clear()
		print("Goodbye!")
		time.sleep(1)
		click.clear()
		exit()


def stats():
	click.clear()
	print("TIC TAC TOE".center(cols))
	print("PLAYER v COMPUTER STATISTICS".center(cols))
	with open("stats.csv", "r") as f:
		reader = csv.reader(f)
		rawList = list(reader)

	statList = rawList[0]
	gamesPlayed = int(statList[0]) + int(statList[1]) + int(statList[2])

	if gamesPlayed == 0:
		print("You have played no games against the computer yet!")

	else:
		print("Total games played: " + str(gamesPlayed))
		print("\nWins:")
		print("Player: " + statList[0] + "\tComputer: " + statList[1] + "\tDraws: " + statList[2])
		print()
		print("Win percentage: " + str(int(statList[0])/gamesPlayed*100) + "%")
		print("Draw percentage: " + str(int(statList[2])/gamesPlayed*100) + "%")
		print("Lose Percentage: " + str(int(statList[1])/gamesPlayed*100) + "%")
		print()

	print("Choose one of the following: ")
	print("1. Reset Stats")
	print("2. Return to Main Menu")

	choice = input("\nChoose one of the above options: ")

	while choice not in ["1", "2"]:
		choice = input("Please enter a valid option: ")

	if choice == "1":
		blankStatList = ["0", "0", "0"]
		with open("stats.csv", "w") as f:
			writer = csv.writer(f)
			writer.writerow(blankStatList)

		input("The Stats have been reset! Hit enter to return to main menu.")
		main()
	else:
		main()


def main():
	click.clear()
	print("TIC TAC TOE".center(cols))

	print("Choose one of the following:\n")
	print("1. Play against the Computer")
	print("2. Play against another Player")
	print("3. Statistics (Player v Computer)")
	print("4. Quit")

	choice = input("\nChoose one of the above options: ")

	while choice not in ["1", "2", "3", "4"]:
		choice = input("\nPlease enter a valid choice: ")

	if choice == "1":
		pvc(0, 0, 0)
	elif choice == "2":
		pvp(True, "", "", 0, 0)
	elif choice == "3":
		stats()
	else:
		click.clear()
		print("Goodbye!")
		time.sleep(1)
		click.clear()
		exit()


if __name__ == "__main__":
	main()
