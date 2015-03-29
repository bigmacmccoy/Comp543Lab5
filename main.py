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
            elif middleCard < right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle
        else:
            if middleCard < left:
                self.hand = (middleCard, middle, right)
                return left
            elif middleCard > right:
                self.hand = (left, middle, middleCard)
                return right
            else:
                self.hand = (left, middleCard, right)
                return middle

    def isInOrder(self):
        left, middle, right = self.hand

        ascending = (left < middle) and (middle < right)
        descending = (left > middle) and (middle > right)
        return ascending or descending

def deal():
    cardList = [x for x in range(1, 8)]
    print(cardList)
    cards = []

    while len(cardList) > 0:
        index = random.randint(0, len(cardList) - 1)
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
        print ("%s: (%d, %d, %d)" % (currentPlayer.name, left, middle, right))
        print ("middleCard: %d" % (middleCard))

        playerOrder = (nextPlayer, currentPlayer)

    print ("%s won the game!" % (winningPlayer.name))
