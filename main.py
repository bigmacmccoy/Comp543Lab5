# Joe Moraal and Braedon McCoy

from enum import Enum
import random

class CardPosition(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2

class Player:
    def __init__(self, inName, inHand):
        left, middle, right = inHand

        self.name = inName
        self.reversed = (left > right)
        self.hand = (left, middle, right)

    def chooseMove(self, middleCard):
        left, middle, right = self.hand

        if reversed:
            if middleCard > left:
                self.hand = (middleCard, middle, right)
                return left
            else if middleCard < right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle
        else:
            if middleCard < left:
                self.hand = (middleCard, middle, right)
                return left
            else if middleCard > right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle

    def isInOrder():
        pass

def deal():
    cardList = [1:7]
    cards = []

    while len(cardList) > 0:
        index = Random.randint(0, len(cardList) - 1)
        cards.append(cardList.pop(index))

    playerOne = Player("playerOne", (cards[0], cards[1], cards[2]))
    playerTwo = Player("playerTwo", (cards[3], cards[4], cards[5]))
    return (playerOne, playerTwo, cards[6])

if __name__ == "__main__":
    gameOver = False
    winningPlayer = None
    playerOne, playerTwo, middleCard = deal()
    playerOrder = (playerOne, playerTwo)

    while not gameOver:
        currentPlayer, nextPlayer = playerOrder
        middleCard = currentPlayer.chooseMove(middleCard)

        if currentPlayer.isInOrder():
            gameOver = True
            winningPlayer = currentPlayer

        left, middle, right = currentPlayer.hand
        print "{0}: ({1}, {2}, {3})".format(currentPlayer.name, left, middle, right)
        print "middleCard: {0}".format(middleCard)

        playerOrder = (nextPlayer, currentPlayer)

    print "{0} won the game!".format(winningPlayer.name)
