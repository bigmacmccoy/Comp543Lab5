# Joe Moraal and Braedon McCoy

import random

global playerOneHand = {"one": None, "two": None, "Three": None }
global playerTwoHand = {"one": None, "two": None, "Three": None }
middleCard = None
someoneWins = false
winningHand = None
winningPlayer = None

def deal():
	cards = []
	while len(cards) < 7:
		num = random.randrange(1,8)
		if num not in cards:
			cards.append(num)

	global playerOneHand["one"] = cards[0]
	global playerTwoHand["one"] = cards[1]
	global playerOneHand["two"] = cards[2]
	global playerTwoHand["two"] = cards[3]
	global playerOneHand["three"] = cards[4]
	global playerTwoHand["three"] = cards[5]
	global middleCard = cards[6]

def play_state():
	deal()
	global playerOneHand = orderCards(global playerOneHand)
	global playerTwoHand = orderCards(global playerTwoHand)
	while global someoneWins == false:
		playerOneTurn(global playerOneHand)
		if global someoneWins is True:
			global winningHand = global playerOneHand
			global winningPlayer = "One"
		playerTwoTurnglobal playerTwoHand)
	if global someoneWins is True and global winningHand is None:
		global winningHand = global playerTwoHand
		global winningPlayer = "Two"
	endGame()

def playerOneTurn(playerHand):
	print "Player One's Turn : ({0}, {1}, {2})".format(playerHand["one"], playerHand["two"], playerHand["three"])
	if checkWinState(global playerHand) is True:
		someoneWins = True
		return
	else:
		playerHand = replaceWorstCard(playerHand)
		global playerOneHand = playerHand
	print "Player One Result : ({0}, {1}, {2})".format(playerHand["one"], playerHand["two"], playerHand["three"])

def playerTwoTurn(playerHand):
	print "Player Two's Turn : ({0}, {1}, {2})".format(playerHand["one"], playerHand["two"], playerHand["three"])
	if checkWinState(global playerHand) is True:
		someoneWins = True
		return
	else:
		playerHand = replaceWorstCard(playerHand)
		global playerTwoHand = playerHand
	print "Player Two Result : ({0}, {1}, {2})".format(playerHand["one"], playerHand["two"], playerHand["three"])


def checkWinState(playerHand):
	if playerHand["three"] - playerHand["two"] == 1 and playerHand["two"] - playerHand["one"] == 1 and playerHand["three"] - playerHand["one"] == 2:
		return True
	else
		return False

def replaceWorstCard(playerHand):
	if playerHand["three"] - playerHand["one"] == 2:
		playerHand["two"] = swapForMiddle(playerHand["two"])
	elif abs(playerHand["one"] - global middleCard) == 1:
		playerHand["one"] = swapForMiddle(playerHand["one"])
	elif abs(playerHand["two"] - global middleCard) == 1:
		playerHand["two"] = swapForMiddle(playerHand["two"])
	elif abs(playerHand["three"] - global middleCard) == 1:
		playerHand["three"] = swapForMiddle(playerHand["three"])
	else:
		if global middleCard < playerHand["one"]:
			playerHand["one"] = swapForMiddle(playerHand["one"])
		elif global middleCard > playerHand["three"]:
			playerHand["three"] = swapForMiddle(playerHand["three"])
		else:
			playerHand["two"] = swapForMiddle(playerHand["two"])
	return playerHand

def swapForMiddle(worstCard):
	temp = global middleCard
	global middleCard = worstCard
	return temp

def orderCards(playerHand):
	lowest = 0
	middle = 0
	highest = 0

	if playerHand["one"] < playerHand["two"] and playerHand["two"] < playerHand["three"]:
		lowest = playerHand["one"]
		playerHand["one"] = None
	elif playerHand["two"] < playerHand["one"] and playerHand["two"] < playerHand["three"]:
		lowest = playerHand["two"]
		playerHand["two"] = None
	elif playerhand["three"] < playerHand["two"] and playerHand["three"] < playerHand["one"]:
		lowest = playerHand["three"]
		playerHand["three"] = None

	if playerHand["one"] > playerHand["two"] and playerHand["two"] > playerHand["three"]:
		lowest = playerHand["one"]
		playerHand["one"] = None
	elif playerHand["two"] > playerHand["one"] and playerHand["two"] > playerHand["three"]:
		lowest = playerHand["two"]
		playerHand["two"] = None
	elif playerhand["three"] > playerHand["two"] and playerHand["three"] > playerHand["one"]:
		lowest = playerHand["three"]
		playerHand["three"] = None

	if playerHand["one"] is None and playerHand["two"] is None:
		middle = playerHand["three"]
		playerHand["three"] = None
	elif playerHand["one"] is None and playerHand["three"] is None:
		middle = playerHand["two"]
		playerHand["two"] = None
	elif playerHand["two"] is None and playerHand["three"] is None:
		middle = playerHand["one"]
		playerHand["one"] = None

	playerHand["one"] = lowest
	playerHand["two"] = middle
	playerHand["three"] = highest

	return playerHand
def endGame():
	print "Player {0} Wins!".format(global winningPlayer)
	print "Table Layout: \n[{0}] [{1}] [{2}]\n    [{3}]\n[{4}] [{5}] [{6}]".format(global playerOneHand["one"], global playerOneHand["two"], global playerOneHand["three"], global middleCard, global playerTwoHand["one"], global playerTwoHand["one"], global playerTwoHand["one"], )